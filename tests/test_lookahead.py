"""Quotes at period t must use information through t-1 only (no look-ahead)."""
import numpy as np
import yaml

from simulation import general_rare_event as g


def _cell(Y: np.ndarray) -> dict:
    T = Y.shape[1]
    return {
        "M": np.zeros((1, T), dtype=np.int8),
        "p": np.full((1, T), 0.1),
        "Y": Y.astype(bool),
        "O": np.ones((1, T), dtype=bool),
        "provider": np.zeros((1, T), dtype=int),
        "selectivity": np.zeros(int(yaml.safe_load(open(g.CONFIG))["providers"])),
    }


def _states(arrs: dict) -> dict:
    out = {f"learner_{k}": v for k, v in arrs["learners"].items()}
    out["reputation"] = arrs["reputation"]
    out.update({f"price_{k}": v for k, v in arrs["prices"].items()})
    return out


def test_flipping_current_outcome_only_affects_future_quotes():
    cfg = yaml.safe_load(open(g.CONFIG))
    rng = np.random.default_rng(0)
    T, k = 40, 17
    Y = (rng.random((1, T)) < 0.3)
    Y_flip = Y.copy()
    Y_flip[0, k] = ~Y_flip[0, k]
    base = 0.1
    a = _states(g.cell_arrays(_cell(Y), cfg, base))
    b = _states(g.cell_arrays(_cell(Y_flip), cfg, base))
    for name in a:
        if name == "price_A_objective":
            np.testing.assert_array_equal(a[name], b[name])
            continue
        np.testing.assert_array_equal(a[name][0, : k + 1], b[name][0, : k + 1],
                                      err_msg=f"{name} changed at or before t")
        assert not np.allclose(a[name][0, k + 1], b[name][0, k + 1]), (
            f"{name} did not respond at t+1"
        )


def test_first_period_quote_uses_prior_only():
    cfg = yaml.safe_load(open(g.CONFIG))
    base = 0.1
    learn = cfg["learning"]
    s = float(learn["prior_strength"])
    a0 = base * float(learn["prior_mean_scale"]) * s
    for y0 in (0, 1):
        Y = np.zeros((1, 5), dtype=bool)
        Y[0, 0] = bool(y0)
        arrs = g.cell_arrays(_cell(Y), cfg, base)
        assert np.isclose(arrs["learners"]["bayesian"][0, 0], a0 / s, atol=1e-5)
        assert np.isclose(arrs["reputation"][0, 0], 0.5)


def test_naive_and_model_b_use_raw_lagged_experienced_frequency():
    cfg = yaml.safe_load(open(g.CONFIG))
    base = 0.1
    rng = np.random.default_rng(3)
    T = 30
    Y = rng.random((1, T)) < 0.4
    cell = _cell(Y)
    cell["O"][0, :4] = False
    arrs = g.cell_arrays(cell, cfg, base)
    O = cell["O"][0]
    Yo = (Y[0] & O)
    p_init = base * float(cfg["learning"]["prior_mean_scale"])
    alpha = float(cfg["pricing"]["alpha"])
    for t in range(T):
        n = O[:t].sum()
        expected = Yo[:t].sum() / n if n else p_init
        assert np.isclose(arrs["learners"]["naive"][0, t], expected)
        assert np.isclose(arrs["prices"]["B_experienced"][0, t],
                          alpha * expected * arrs["V"][0, t])
