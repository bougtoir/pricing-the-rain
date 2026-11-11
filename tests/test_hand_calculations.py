"""Independent loop-based re-implementation of the generic-simulation layers.

Each quantity is recomputed period by period with explicit t-1 information
and compared with the vectorized code in simulation/general_rare_event.py.
"""
import copy
import math
from pathlib import Path

import numpy as np
import yaml

from simulation import general_rare_event as gre

ROOT = Path(__file__).resolve().parents[1]
CFG = yaml.safe_load((ROOT / "config" / "general_simulation.yml").read_text())


def tiny_cell(seed: int = 3, T: int = 40, J: int = 3, base: float = 0.05):
    rng = np.random.default_rng(seed)
    M = (rng.random((1, T)) < 0.4).astype(int)
    p = base * np.where(M == 1, 3.0, 0.5)
    O = rng.random((1, T)) < 0.6
    Y = rng.random((1, T)) < 0.3
    provider = rng.integers(0, J, size=(1, T))
    cfg = copy.deepcopy(CFG)
    cfg["providers"] = J
    cell = {"M": M, "p": p, "Y": Y, "O": O, "provider": provider,
            "selectivity": np.linspace(-1, 1, J)}
    return cell, cfg, base


def loop_reference(cell, cfg, base):
    learn, pr = cfg["learning"], cfg["pricing"]
    s, a = float(learn["prior_strength"]), float(learn["prior_mean_scale"])
    d, rd = float(learn["recency_decay"]), float(pr["reputation_decay"])
    ws, wf = float(learn["selective_success_weight"]), float(learn["selective_failure_weight"])
    O, Y = cell["O"][0], cell["Y"][0]
    T, J = O.size, int(cfg["providers"])
    out = {k: np.zeros(T) for k in ("naive", "bayesian", "recency", "selective", "rep")}
    n = k = ey = eo = sy = so = 0.0
    ry, ro = np.zeros(J), np.zeros(J)
    for t in range(T):
        out["naive"][t] = k / n if n > 0 else base * a
        out["bayesian"][t] = (base * a * s + k) / (s + n + 1e-6)
        out["recency"][t] = (0.05 + ey) / (0.10 + eo + 1e-6)
        out["selective"][t] = (0.05 + sy) / (0.10 + so + 1e-6)
        j = cell["provider"][0, t]
        if O[t]:
            out["rep"][t] = (0.05 + ry[j]) / (0.10 + ro[j])
        o, y = float(O[t]), float(O[t] and Y[t])
        n, k = n + o, k + y
        ey, eo = d * ey + (1 - d) * y, d * eo + (1 - d) * o
        sy = d * sy + (1 - d) * y * ws
        so = d * so + (1 - d) * (y * ws + o * (1 - float(Y[t])) * wf)
        for jj in range(J):
            m = float(O[t] and cell["provider"][0, t] == jj)
            ry[jj] = rd * ry[jj] + (1 - rd) * m * float(Y[t])
            ro[jj] = rd * ro[jj] + (1 - rd) * m
    return out


def test_learners_and_reputation_match_loop_reference() -> None:
    cell, cfg, base = tiny_cell()
    arrs = gre.cell_arrays(cell, cfg, base)
    ref = loop_reference(cell, cfg, base)
    for name in ("naive", "bayesian", "recency", "selective"):
        np.testing.assert_allclose(arrs["learners"][name][0], ref[name], rtol=1e-10, atol=1e-12)
    np.testing.assert_allclose(arrs["reputation"][0], ref["rep"], rtol=1e-10, atol=1e-12)


def test_quotes_match_hand_formulas() -> None:
    cell, cfg, base = tiny_cell()
    arrs = gre.cell_arrays(cell, cfg, base)
    ref = loop_reference(cell, cfg, base)
    pr = cfg["pricing"]
    al, g = float(pr["alpha"]), float(pr["reputation_gamma"])
    V = float(pr["value_base"]) * (1 + float(pr["value_state_multiplier"]) * cell["M"][0])
    a = float(cfg["weighting"]["prelec_alpha"])
    w = np.array([math.exp(-((-math.log(x)) ** a)) for x in ref["bayesian"]])
    P = arrs["prices"]
    np.testing.assert_allclose(P["A_objective"][0], al * cell["p"][0] * V)
    np.testing.assert_allclose(P["B_experienced"][0], al * ref["naive"] * V)
    np.testing.assert_allclose(P["C_weighted"][0], al * w * V, rtol=1e-9)
    np.testing.assert_allclose(P["D_reputation"][0], al * w * V + g * ref["rep"], rtol=1e-9)


def test_prelec_hand_values_and_lemma2_divergence() -> None:
    assert math.isclose(float(gre.prelec(np.array([0.1]), 0.65)[0]),
                        math.exp(-(math.log(10.0) ** 0.65)), rel_tol=1e-12)
    assert math.isclose(float(gre.prelec(np.array([math.exp(-1)]), 0.65)[0]), math.exp(-1), rel_tol=1e-9)
    rel = [(float(gre.prelec(np.array([p]), 0.65)[0]) - p) / p for p in (1e-2, 1e-3, 1e-4, 1e-5)]
    assert all(b > 4 * a for a, b in zip(rel, rel[1:]))


def test_selection_ratio_and_covariance_identity_by_hand() -> None:
    p = np.array([[0.01, 0.03, 0.01, 0.03, 0.01, 0.03]])
    O = np.array([[False, True, True, True, False, True]])
    Y = np.array([[False, True, False, False, False, True]])
    cell = {"M": (p > 0.02).astype(int), "p": p, "Y": Y, "O": O,
            "provider": np.zeros((1, 6), dtype=int), "selectivity": np.linspace(-1, 1, 3)}
    cfg = copy.deepcopy(CFG)
    cfg["providers"] = 3
    arrs = gre.cell_arrays(cell, cfg, 0.02)
    m = gre.rep_metrics({"base_prob": 0.02}, cell, arrs, cfg, 0)
    p_ref = (0.03 * 3 + 0.01) / 4
    assert math.isclose(m["p_ref_observed"], p_ref)
    assert math.isclose(m["selection_ratio"], p_ref / 0.02)
    o = O[0].astype(float)
    cov = np.mean(o * p[0]) - o.mean() * p[0].mean()
    assert math.isclose(m["selection_ratio"], 1 + cov / (o.mean() * p[0].mean()))
    assert math.isclose(m["p_experienced"], 2 / 4)
    assert math.isclose(m["B_price_A_objective"], 0.0, abs_tol=1e-15)
    assert math.isclose(m["B_subj_naive"], float(np.mean(arrs["learners"]["naive"][0] - p[0])))
    assert math.isclose(m["B_price_B_experienced"], m["B_subj_naive"], rel_tol=1e-12)


def test_distortion_parts_sum_exactly() -> None:
    cell, cfg, base = tiny_cell(T=60)
    arrs = gre.cell_arrays(cell, cfg, base)
    m = gre.rep_metrics({"base_prob": base}, cell, arrs, cfg, 0)
    assert math.isclose(m["D_EV_D_reputation"], m["D_prob_abs_D_reputation"] + m["D_rep_abs_D_reputation"], rel_tol=1e-10)
    assert math.isclose(m["D_rel_D_reputation"], m["D_rel_prob_D_reputation"] + m["D_rel_rep_D_reputation"], rel_tol=1e-10)
    assert math.isclose(m["D_EV_A_objective"], 0.0, abs_tol=1e-15)
