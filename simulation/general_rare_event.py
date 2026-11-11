"""Domain-agnostic rare-event pricing simulation (generalization layer).

Separates four probability objects per the generalized framework:
  p_t           objective event probability
  p_hat_exp     experienced frequency under endogenous observation
  p_hat_subj    subjective probability after learning/weighting
  p_hat_price   price-implied probability

Everything here is generated data (layer C in the claim taxonomy): the module
produces theoretical/simulation evidence only. Rainfall validation lives in
simulation/run_simulation.py and is unchanged.

Outputs (results/):
  general_replications.csv.gz      per-replication metric rows
  general_summary.csv              means + 2.5/97.5 percentiles + MCSE
  general_convergence.csv          Monte Carlo SE by sample size
  general_observational_equivalence.csv
  figures/figure4_four_probabilities.{pdf,png}
  figures/figure6_observational_equivalence.{pdf,png}
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
from scipy.signal import lfilter
from scipy.stats import spearmanr


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "general_simulation.yml"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"

REGIME_ORDER = ["common", "moderately_rare", "rare", "very_rare"]
REGIME_LABELS = {
    "common": "Common",
    "moderately_rare": "Moderately rare",
    "rare": "Rare",
    "very_rare": "Very rare",
}
OBS_RULES = ["exogenous", "endogenous"]
PRICE_MODELS = ["A_objective", "B_experienced", "C_weighted", "D_reputation"]


# Prior stocks of the EWMA learners and of provider reputation: equivalent to
# PRIOR_OBS_STOCK / (1 - decay) attributed outcomes at mean
# PRIOR_SUCCESS_STOCK / PRIOR_OBS_STOCK.
PRIOR_SUCCESS_STOCK = 0.05
PRIOR_OBS_STOCK = 0.10


def expit(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def ewma(values: np.ndarray, decay: float) -> np.ndarray:
    """Exponentially weighted moving sum along axis 1."""
    return lfilter([1.0 - decay], [1.0, -decay], values, axis=1)


def lag1(values: np.ndarray) -> np.ndarray:
    """State before period t's update: column t holds the value at t-1 (zero at t=0)."""
    out = np.zeros_like(values)
    out[:, 1:] = values[:, :-1]
    return out


def prelec(p: np.ndarray, alpha: float) -> np.ndarray:
    p = np.clip(p, 1e-9, 1.0 - 1e-9)
    return np.exp(-((-np.log(p)) ** alpha))


def markov_state(rng: np.random.Generator, shape: tuple[int, int],
                 persistence: float, high_share: float) -> np.ndarray:
    """Two-state chain in {0,1} with stay-probability `persistence`."""
    rows, cols = shape
    p01 = (1.0 - persistence) * high_share / (1.0 - high_share)
    p10 = 1.0 - persistence
    state = np.zeros(shape, dtype=np.int8)
    state[:, 0] = rng.random(rows) < high_share
    for t in range(1, cols):
        prev = state[:, t - 1]
        flip_in = (prev == 0) & (rng.random(rows) < p01)
        flip_out = (prev == 1) & (rng.random(rows) < p10)
        state[:, t] = np.where(flip_in, 1, np.where(flip_out, 0, prev))
    return state


def simulate_cell(regime: dict, obs_rule: str, cfg: dict,
                  rng: np.random.Generator, efficacy: float = 0.0
                  ) -> dict[str, np.ndarray]:
    """Simulate one regime x observation-rule cell. Returns (R, T) matrices."""
    R = int(cfg["_replications"])
    T = int(cfg["horizon"]) + int(cfg["burn_in"])
    J = int(cfg["providers"])
    base = float(regime["base_prob"])

    hs = cfg["hazard_state"]
    M = markov_state(rng, (R, T), float(hs["persistence"]),
                     float(hs["high_share"]))
    p = np.clip(
        base * ((1 - M) * float(hs["low_multiplier"])
                + M * float(hs["high_multiplier"])),
        1e-6, 1.0 - 1e-6,
    )

    dem = cfg["demand"]
    if obs_rule == "endogenous":
        request_prob = expit(float(dem["intercept"]) + float(dem["slope"]) * M)
    else:
        # Exogenous rule: constant rate equal to the endogenous marginal
        # request probability (comparability decision, see decision log).
        hi = float(hs["high_share"])
        marginal = (
            hi * expit(float(dem["intercept"]) + float(dem["slope"]))
            + (1 - hi) * expit(float(dem["intercept"]))
        )
        request_prob = np.full((R, T), marginal)
    D = rng.random((R, T)) < request_prob

    acc = cfg["acceptance"]
    selectivity = np.linspace(
        -float(acc["selectivity_spread"]),
        float(acc["selectivity_spread"]),
        J,
    )
    provider = rng.integers(0, J, size=(R, T))
    if obs_rule == "endogenous":
        # Providers respond to relative hazard (p/base - 1), not absolute
        # p - base, so selective acceptance operates at every rarity regime.
        accept_prob = expit(
            float(acc["intercept"])
            + float(acc["slope"]) * (p / base - 1.0)
            + selectivity[provider]
        )
    else:
        # Exogenous observation: demand AND acceptance are independent of the
        # risk state, so O is independent of p_t and the observed support is
        # representative. Selective acceptance under this rule would silently
        # reintroduce selection (see docs/EXOGENOUS_BENCHMARK_AUDIT.md).
        accept_prob = np.full((R, T), expit(np.array(float(acc["intercept"]))))
    A = rng.random((R, T)) < accept_prob
    O = D & A

    Y = rng.random((R, T)) < np.clip(p + efficacy * O, 0.0, 1.0)

    keep = np.zeros(T, dtype=bool)
    keep[int(cfg["burn_in"]):] = True
    return {
        "M": M[:, keep], "p": p[:, keep], "Y": Y[:, keep],
        "O": O[:, keep], "provider": provider[:, keep],
        "selectivity": selectivity,
    }


def cell_arrays(cell: dict[str, np.ndarray], cfg: dict,
                base: float) -> dict[str, np.ndarray]:
    """Compute learner, reputation, and price arrays once per cell."""
    O = cell["O"].astype(float)
    OY = cell["Y"].astype(float) * O
    # Quotes at t use information through t-1 only: every learner, reputation,
    # and price array at column t excludes the period-t outcome.
    cumO = np.cumsum(O, axis=1) - O
    cumY = np.cumsum(OY, axis=1) - OY

    learn = cfg["learning"]
    a0 = base * float(learn["prior_mean_scale"]) * float(learn["prior_strength"])
    b0 = float(learn["prior_strength"]) - a0
    decay = float(learn["recency_decay"])
    eps = 1e-6

    # Raw experienced frequency through t-1. Before the first observation it
    # is undefined; it is initialized at the pre-specified prior mean
    # (base_prob * prior_mean_scale), an initialization, not smoothing.
    p_init = base * float(learn["prior_mean_scale"])
    naive = np.where(cumO > 0, cumY / np.maximum(cumO, 1.0), p_init)
    bayesian = (a0 + cumY) / (a0 + b0 + cumO + eps)
    recency = (PRIOR_SUCCESS_STOCK + lag1(ewma(OY, decay))) / (
        PRIOR_OBS_STOCK + lag1(ewma(O, decay)) + eps
    )

    ws = float(learn["selective_success_weight"])
    wf = float(learn["selective_failure_weight"])
    sel_y = lag1(ewma(OY * ws, decay))
    sel_o = lag1(ewma(OY * ws + O * (1 - cell["Y"]) * wf, decay))
    selective = (PRIOR_SUCCESS_STOCK + sel_y) / (PRIOR_OBS_STOCK + sel_o + eps)

    # Per-provider reputation evaluated at that provider's observed events.
    J = int(cfg["providers"])
    rep_decay = float(cfg["pricing"]["reputation_decay"])
    rep = np.zeros(O.shape)
    Yf = cell["Y"].astype(float)
    for j in range(J):
        mask = cell["O"] & (cell["provider"] == j)
        rep_j = (PRIOR_SUCCESS_STOCK + lag1(ewma(mask * Yf, rep_decay))) / (
            PRIOR_OBS_STOCK + lag1(ewma(mask.astype(float), rep_decay))
        )
        rep[mask] = rep_j[mask]

    price_cfg = cfg["pricing"]
    V = float(price_cfg["value_base"]) * (
        1.0 + float(price_cfg["value_state_multiplier"]) * cell["M"]
    )
    alpha = float(price_cfg["alpha"])
    wsubj = prelec(bayesian, float(cfg["weighting"]["prelec_alpha"]))
    prices = {
        "A_objective": alpha * cell["p"] * V,
        "B_experienced": alpha * naive * V,
        "C_weighted": alpha * wsubj * V,
        "D_reputation": (
            alpha * wsubj * V
            + float(price_cfg["reputation_gamma"]) * rep
        ),
    }
    return {
        "learners": {
            "naive": naive,
            "bayesian": bayesian,
            "recency": recency,
            "selective": selective,
        },
        "reputation": rep,
        "V": V,
        "prices": prices,
    }


def rep_metrics(regime: dict, cell: dict, arrs: dict,
                cfg: dict, r: int) -> dict[str, float]:
    """Metric row for replication r of a simulated cell."""
    p = cell["p"][r]
    Y = cell["Y"][r]
    O = cell["O"][r]
    M = cell["M"][r]
    eps = 1e-9

    p_bar = float(p.mean())
    n_obs = int(O.sum())
    p_exp = float((Y & O).sum() / max(n_obs, 1))

    # Matched objective benchmark: the true event probability on the same
    # observation support, E[p | O = 1]. Under exogenous observation this
    # equals p_bar; under endogenous observation it is the selection-shifted
    # composition benchmark. Comparing p_exp to p_bar conflates selection
    # (composition) with record bias; only p_exp - p_ref is estimand bias.
    p_ref = float(p[O].mean()) if n_obs else np.nan
    metrics: dict[str, float] = {
        "n_observed": float(n_obs),
        "observation_rate": float(O.mean()),
        "p_objective": p_bar,
        "p_ref_observed": p_ref,
        "p_experienced": p_exp,
        "selection_gap": p_ref - p_bar,
        "selection_ratio": p_ref / p_bar if p_bar > eps else np.nan,
        "B_composition": p_exp - p_bar,
        "B_abs": p_exp - p_ref,
        "B_rel": (p_exp - p_ref) / p_ref if p_ref and p_ref > eps else np.nan,
        "B_exp": p_exp - p_bar,
    }
    for name, est in arrs["learners"].items():
        e = est[r]
        metrics[f"B_subj_{name}"] = float(np.mean(e - p))
        metrics[f"p_subj_{name}"] = float(np.mean(e))

    alpha = float(cfg["pricing"]["alpha"])
    V = arrs["V"][r]
    succ = O & Y
    fail = O & ~Y
    wsubj = prelec(arrs["learners"]["bayesian"], float(cfg["weighting"]["prelec_alpha"]))[r]
    rep_r = arrs["reputation"][r]
    gamma = float(cfg["pricing"]["reputation_gamma"])
    denom = np.maximum(alpha * p * V, eps)
    for name, P_all in arrs["prices"].items():
        P = P_all[r]
        p_impl = P / (alpha * V)
        metrics[f"B_price_{name}"] = float(np.mean(p_impl - p))
        metrics[f"D_EV_{name}"] = float(np.mean(P - alpha * p * V))
        metrics[f"D_rel_{name}"] = float(np.mean((P - alpha * p * V) / denom))
        ps, pf = P[succ], P[fail]
        metrics[f"price_success_diff_{name}"] = (
            float(ps.mean() - pf.mean()) if ps.size and pf.size else np.nan
        )
    # Analytic decomposition for model D, P = alpha*wsubj*V + gamma*R:
    #   D_rel = mean[(wsubj - p)/p] + mean[gamma*R/(alpha*p*V)] + cross term.
    # Both relative parts can diverge as objective EV -> 0: the transformed
    # term under Prelec weighting (Lemma 2) and the reputation term because
    # R does not scale with p. Reported parts sum exactly to D_rel only if the cross term
    # (wsubj-p)*(V-term) correlation is included; we report the exact split
    # P - alpha*p*V = alpha*V*(wsubj-p) + gamma*R applied pointwise, so
    # D_EV = D_prob_abs + D_rep_abs and D_rel = D_rel_prob + D_rel_rep.
    d_prob = alpha * V * (wsubj - p)
    d_rep = gamma * rep_r
    metrics["D_prob_abs_D_reputation"] = float(np.mean(d_prob))
    metrics["D_rep_abs_D_reputation"] = float(np.mean(d_rep))
    metrics["D_rel_prob_D_reputation"] = float(np.mean(d_prob / denom))
    metrics["D_rel_rep_D_reputation"] = float(np.mean(d_rep / denom))

    rep_events = arrs["reputation"][r][O]
    if rep_events.size > 10 and np.std(rep_events) > 0:
        metrics["reputation_hazard_corr"] = float(
            np.corrcoef(rep_events, M[O])[0, 1]
        )
        metrics["reputation_price_corr"] = float(
            np.corrcoef(rep_events, arrs["prices"]["D_reputation"][r][O])[0, 1]
        )
    else:
        metrics["reputation_hazard_corr"] = np.nan
        metrics["reputation_price_corr"] = np.nan

    sel = cell["selectivity"]
    J = int(cfg["providers"])
    provider_success = np.full(J, np.nan)
    for j in range(J):
        m = O & (cell["provider"][r] == j)
        if m.sum() > 0:
            provider_success[j] = Y[m].mean()
    ok = ~np.isnan(provider_success)
    metrics["provider_rank_distortion"] = (
        float(spearmanr(sel[ok], provider_success[ok]).statistic)
        if ok.sum() >= 3
        else np.nan
    )
    return metrics


def summarize(rows: pd.DataFrame, metric_cols: list[str]) -> pd.DataFrame:
    out = []
    for (regime, rule), g in rows.groupby(["regime", "obs_rule"], sort=False):
        for m in metric_cols:
            v = g[m].dropna()
            if len(v) == 0:
                continue
            out.append({
                "regime": regime,
                "obs_rule": rule,
                "metric": m,
                "mean": v.mean(),
                "sd": v.std(),
                "ci_low": v.quantile(0.025),
                "ci_high": v.quantile(0.975),
                "mcse": v.std() / np.sqrt(len(v)),
                "n": len(v),
            })
    return pd.DataFrame(out)


def make_figure6(summary: pd.DataFrame) -> None:
    def get(regime, rule, metric, field="mean"):
        row = summary.loc[
            (summary["regime"] == regime)
            & (summary["obs_rule"] == rule)
            & (summary["metric"] == metric)
        ]
        return float(row[field].iloc[0]) if len(row) else np.nan

    x = np.arange(len(REGIME_ORDER))
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 7.0))

    ax = axes[0, 0]
    for label, metric, color in [
        ("Experienced", "p_experienced", "#0072B2"),
        ("Subjective (Bayesian)", "p_subj_bayesian", "#009E73"),
        ("Subjective (selective)", "p_subj_selective", "#56B4E9"),
        ("Price-implied (Model D)", "_price_D", "#D55E00"),
    ]:
        if metric == "_price_D":
            vals = [
                get(r, "endogenous", "p_objective")
                + get(r, "endogenous", "B_price_D_reputation")
                for r in REGIME_ORDER
            ]
        else:
            vals = [get(r, "endogenous", metric) for r in REGIME_ORDER]
        ax.plot(x, vals, "o-", label=label, color=color, markersize=4,
                linewidth=1.2)
    ax.plot(x, [get(r, "endogenous", "p_objective") for r in REGIME_ORDER],
            "k--", label="Objective (all periods)", linewidth=1.2)
    ax.plot(
        x,
        [get(r, "endogenous", "p_ref_observed") for r in REGIME_ORDER],
        "k:", label="Objective on observed support (p_ref)", linewidth=1.4,
    )
    ax.set_xticks(x)
    ax.set_xticklabels([REGIME_LABELS[r] for r in REGIME_ORDER], fontsize=8)
    ax.set_ylabel("Probability", fontsize=8.5)
    ax.set_title("A. Four probability layers (endogenous observation)",
                 loc="left", fontsize=9.5)
    ax.legend(frameon=False, fontsize=7)
    ax.grid(axis="y", alpha=0.25)

    ax = axes[0, 1]
    ax2 = ax.twinx()
    for rule, color, marker in [
        ("endogenous", "#D55E00", "o"),
        ("exogenous", "#0072B2", "s"),
    ]:
        vals = [get(r, rule, "selection_gap") for r in REGIME_ORDER]
        ax.plot(x, vals, marker + "-", label=f"{rule.capitalize()} abs. gap",
                color=color, markersize=4, linewidth=1.2)
        ratio = [get(r, rule, "selection_ratio") for r in REGIME_ORDER]
        ax2.plot(x, ratio, marker + "--", label=f"{rule.capitalize()} ratio",
                 color=color, markersize=3.5, linewidth=1.0, alpha=0.65)
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([REGIME_LABELS[r] for r in REGIME_ORDER], fontsize=8)
    ax.set_ylabel("Selection gap p_ref − p_obj (absolute)", fontsize=8.5)
    ax2.set_ylabel("Selection ratio p_ref / p_obj", fontsize=8.5)
    ax.set_title("B. Selection distortion: absolute gap shrinks, ratio stable",
                 loc="left", fontsize=9.5)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=6.5, loc="center right")
    ax.grid(axis="y", alpha=0.25)

    ax = axes[1, 0]
    for name, label, color in [
        ("B_experienced", "B: experienced-EV", "#0072B2"),
        ("C_weighted", "C: weighted subjective", "#009E73"),
        ("D_reputation", "D: reputation-mediated", "#D55E00"),
    ]:
        vals = [get(r, "endogenous", f"D_rel_{name}") for r in REGIME_ORDER]
        ax.plot(x, vals, "o-", label=label, color=color, markersize=4,
                linewidth=1.2)
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([REGIME_LABELS[r] for r in REGIME_ORDER], fontsize=8)
    ax.set_ylabel("Relative distortion vs objective-EV price", fontsize=8.5)
    ax.set_title("C. Pricing distortion (endogenous observation)",
                 loc="left", fontsize=9.5)
    ax.legend(frameon=False, fontsize=7)
    ax.grid(axis="y", alpha=0.25)

    ax = axes[1, 1]
    width = 0.35
    for i, (rule, color) in enumerate(
        [("endogenous", "#D55E00"), ("exogenous", "#0072B2")]
    ):
        vals = [
            get(r, rule, "price_success_diff_D_reputation")
            for r in REGIME_ORDER
        ]
        ax.bar(x + (i - 0.5) * width, vals, width=width,
               label=rule.capitalize(), color=color, alpha=0.85)
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([REGIME_LABELS[r] for r in REGIME_ORDER], fontsize=8)
    ax.set_ylabel("Mean price(success) − price(failure)", fontsize=8.5)
    ax.set_title("D. Contemporaneous price–outcome association (Model D)",
                 loc="left", fontsize=9.5)
    ax.legend(frameon=False, fontsize=7)
    ax.grid(axis="y", alpha=0.25)

    fig.suptitle(
        "Four-layer probability separation under endogenous observation",
        fontsize=11.5,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.97), h_pad=1.6, w_pad=1.4)
    fig.savefig(FIGURES / "figure4_four_probabilities.pdf", bbox_inches="tight")
    fig.savefig(
        FIGURES / "figure4_four_probabilities.png", dpi=600, bbox_inches="tight"
    )
    plt.close(fig)


def make_figure8(summary: pd.DataFrame) -> None:
    """Frequency distortion vs price distortion decomposition."""
    def get(regime, rule, metric, field="mean"):
        row = summary.loc[
            (summary["regime"] == regime)
            & (summary["obs_rule"] == rule)
            & (summary["metric"] == metric)
        ]
        return float(row[field].iloc[0]) if len(row) else np.nan

    x = np.arange(len(REGIME_ORDER))
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.9))

    ax = axes[0]
    ax2 = ax.twinx()
    width = 0.35
    for i, (rule, color) in enumerate(
        [("endogenous", "#D55E00"), ("exogenous", "#0072B2")]
    ):
        gaps = [get(r, rule, "selection_gap") for r in REGIME_ORDER]
        ax.bar(x + (i - 0.5) * width, gaps, width=width, color=color,
               alpha=0.45, label=f"{rule.capitalize()} abs. gap")
        ratios = [get(r, rule, "selection_ratio") for r in REGIME_ORDER]
        ax2.plot(x + (i - 0.5) * width, ratios, "o--", color=color,
                 linewidth=1.2, markersize=4,
                 label=f"{rule.capitalize()} ratio")
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([REGIME_LABELS[r] for r in REGIME_ORDER], fontsize=8)
    ax.set_ylabel("Absolute selection gap (p_ref − p_obj)", fontsize=8.5)
    ax2.set_ylabel("Selection ratio (p_ref / p_obj)", fontsize=8.5)
    ax.set_title("A. Frequency distortion: gap shrinks, ratio stable",
                 loc="left", fontsize=9.5)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=6.5, loc="center right")

    ax = axes[1]
    width = 0.35
    for i, (rule, color) in enumerate(
        [("endogenous", "#D55E00"), ("exogenous", "#0072B2")]
    ):
        prob_part = [
            get(r, rule, "D_rel_prob_D_reputation") for r in REGIME_ORDER
        ]
        rep_part = [
            get(r, rule, "D_rel_rep_D_reputation") for r in REGIME_ORDER
        ]
        pos = x + (i - 0.5) * width
        ax.bar(pos, prob_part, width=width, color=color, alpha=0.45,
               label=f"{rule.capitalize()}: transformed-frequency part")
        ax.bar(pos, rep_part, width=width, bottom=prob_part, color=color,
               alpha=0.9, hatch="//", edgecolor="white",
               label=f"{rule.capitalize()}: additive reputation part")
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([REGIME_LABELS[r] for r in REGIME_ORDER], fontsize=8)
    ax.set_ylabel("Relative price distortion (Model D)", fontsize=8.5)
    ax.set_title("B. Price distortion: transformed-frequency and reputation "
                 "parts (both can diverge)", loc="left", fontsize=9)
    ax.legend(frameon=False, fontsize=6)

    fig.suptitle(
        "Frequency vs price distortion across rarity regimes", fontsize=11
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96), w_pad=2.2)
    fig.savefig(
        FIGURES / "figure5_distortion_decomposition.pdf", bbox_inches="tight"
    )
    fig.savefig(
        FIGURES / "figure5_distortion_decomposition.png",
        dpi=600, bbox_inches="tight",
    )
    plt.close(fig)


def make_figure7(equiv: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.9))
    for ax, rule, letter in [
        (axes[0], "endogenous", "A"),
        (axes[1], "exogenous", "B"),
    ]:
        sub = equiv[equiv["obs_rule"] == rule]
        for regime in REGIME_ORDER:
            g = sub[sub["regime"] == regime].sort_values("efficacy")
            ax.plot(
                g["efficacy"], g["apparent_success_mean"], "o-",
                label=REGIME_LABELS[regime], markersize=3.5, linewidth=1.2,
            )
            ax.fill_between(
                g["efficacy"], g["apparent_success_low"],
                g["apparent_success_high"], alpha=0.10,
            )
        ax.set_xlabel("True efficacy added on intervened periods",
                      fontsize=8.5)
        ax.set_title(f"{letter}. {rule.capitalize()} observation",
                     loc="left", fontsize=9.5)
        ax.grid(axis="y", alpha=0.25)
    axes[0].set_ylabel("Apparent success among observed events", fontsize=8.5)
    axes[1].legend(frameon=False, fontsize=7, loc="upper left")
    fig.suptitle(
        "Observational equivalence: endogenous selection with zero efficacy "
        "reproduces apparent efficacy",
        fontsize=10.5,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.95), w_pad=1.4)
    fig.savefig(
        FIGURES / "figure6_observational_equivalence.pdf", bbox_inches="tight"
    )
    fig.savefig(
        FIGURES / "figure6_observational_equivalence.png",
        dpi=600, bbox_inches="tight",
    )
    plt.close(fig)


def convergence_scan(replication_rows: pd.DataFrame,
                     cfg: dict) -> pd.DataFrame:
    out = []
    for size in cfg["convergence_sample_sizes"]:
        sub = replication_rows.groupby(
            ["regime", "obs_rule"], sort=False
        ).head(size)
        for (regime, rule), g in sub.groupby(["regime", "obs_rule"],
                                            sort=False):
            for metric in [
                "selection_gap", "selection_ratio", "B_abs", "B_rel",
                "D_rel_D_reputation", "D_rel_rep_D_reputation",
            ]:
                v = g[metric].dropna()
                out.append({
                    "regime": regime,
                    "obs_rule": rule,
                    "metric": metric,
                    "sample_size": size,
                    "mean": v.mean(),
                    "monte_carlo_se": v.std() / np.sqrt(len(v)),
                })
    return pd.DataFrame(out)


def main() -> None:
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)

    seed_seq = np.random.SeedSequence(int(cfg["seed"]))

    rows = []
    cells = [(regime, rule) for regime in cfg["regimes"] for rule in OBS_RULES]
    sim_seeds = seed_seq.spawn(len(cells))
    for (regime, rule), seed in zip(cells, sim_seeds):
        local = dict(cfg)
        local["_replications"] = cfg["replications"]
        rng = np.random.default_rng(seed)
        cell = simulate_cell(regime, rule, local, rng)
        arrs = cell_arrays(cell, cfg, float(regime["base_prob"]))
        for r in range(int(cfg["replications"])):
            m = rep_metrics(regime, cell, arrs, cfg, r)
            m["regime"] = regime["name"]
            m["obs_rule"] = rule
            m["replication"] = r
            rows.append(m)
        print(f"[cell] {regime['name']} x {rule} done", flush=True)

    replications = pd.DataFrame(rows)
    replications.to_csv(
        RESULTS / "general_replications.csv.gz", index=False,
        compression={"method": "gzip", "compresslevel": 6, "mtime": 0},
    )

    metric_cols = [c for c in replications.columns
                   if c not in {"regime", "obs_rule", "replication"}]
    summary = summarize(replications, metric_cols)
    summary.to_csv(RESULTS / "general_summary.csv", index=False)

    conv = convergence_scan(replications, cfg)
    conv.to_csv(RESULTS / "general_convergence.csv", index=False)

    make_figure6(summary)

    eq_rows = []
    eq_cells = [
        (regime, rule, delta)
        for regime in cfg["regimes"]
        for rule in OBS_RULES
        for delta in cfg["efficacy_grid"]
    ]
    eq_seeds = seed_seq.spawn(len(eq_cells))
    for (regime, rule, delta), seed in zip(eq_cells, eq_seeds):
        local = dict(cfg)
        local["_replications"] = cfg["equivalence_replications"]
        rng = np.random.default_rng(seed)
        cell = simulate_cell(regime, rule, local, rng, efficacy=float(delta))
        apparent = (cell["Y"] & cell["O"]).sum(axis=1) / np.maximum(
            cell["O"].sum(axis=1), 1
        )
        eq_rows.append({
            "regime": regime["name"],
            "obs_rule": rule,
            "efficacy": float(delta),
            "apparent_success_mean": float(apparent.mean()),
            "apparent_success_low": float(np.quantile(apparent, 0.05)),
            "apparent_success_high": float(np.quantile(apparent, 0.95)),
        })
    equiv = pd.DataFrame(eq_rows)
    equiv.to_csv(
        RESULTS / "general_observational_equivalence.csv", index=False
    )
    make_figure7(equiv)
    make_figure8(summary)

    # Equivalent-efficacy solution: for each regime, solve for the exogenous
    # efficacy delta* such that exogenous apparent success at delta* equals
    # endogenous apparent success at zero efficacy. Exact inverse linear
    # interpolation on the efficacy grid; uncertainty propagated by
    # re-solving at +/- 1 Monte Carlo SE of the exogenous cell means.
    eq_rows_out = []
    for regime in cfg["regimes"]:
        name = regime["name"]
        endo0 = equiv.loc[
            (equiv["regime"] == name)
            & (equiv["obs_rule"] == "endogenous")
            & (equiv["efficacy"] == 0.0)
        ]
        exo = equiv.loc[
            (equiv["regime"] == name)
            & (equiv["obs_rule"] == "exogenous")
        ].sort_values("efficacy")
        target = float(endo0["apparent_success_mean"].iloc[0])
        grid = exo["efficacy"].to_numpy(float)
        means = exo["apparent_success_mean"].to_numpy(float)
        rep_se = replications.loc[
            (replications["regime"] == name)
            & (replications["obs_rule"] == "endogenous")
        ]["p_experienced"].std() / np.sqrt(int(cfg["replications"]))
        # MCSE of exo apparent means: sd of 5%/95% band ~ use replication sd
        exo_sd = replications.loc[
            (replications["regime"] == name)
            & (replications["obs_rule"] == "exogenous")
        ]["p_experienced"].std()
        mean_se = exo_sd / np.sqrt(int(cfg["equivalence_replications"]))

        def solve(t: float) -> float:
            if t <= means[0] or t >= means[-1]:
                return np.nan
            return float(np.interp(t, means, grid))

        delta_star = solve(target)
        delta_lo = solve(target - rep_se)
        delta_hi = solve(target + rep_se)
        slope = float(
            np.polyfit(grid, means, 1)[0]
        )
        eq_rows_out.append({
            "regime": name,
            "endo_apparent_zero": target,
            "endo_mcse": rep_se,
            "exo_apparent_slope_per_efficacy": slope,
            "exo_mean_mcse": mean_se,
            "equivalent_efficacy": delta_star,
            "equivalent_efficacy_low": delta_lo,
            "equivalent_efficacy_high": delta_hi,
            "method": "inverse linear interpolation on exogenous efficacy "
                      "grid (np.interp); bounds propagate +/-1 MCSE of the "
                      "endogenous zero-efficacy apparent success",
        })
    pd.DataFrame(eq_rows_out).to_csv(
        RESULTS / "general_equivalent_efficacy.csv", index=False
    )

    print(
        f"General rare-event layer complete: {len(replications):,} "
        f"replication rows, {len(equiv):,} equivalence cells"
    )


if __name__ == "__main__":
    main()
