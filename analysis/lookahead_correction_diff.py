"""Compare archived pre-correction generic outputs with the corrected ones."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "results" / "archive" / "pre_lookahead_fix_837387d" / "results"
RESULTS = ROOT / "results"
KEYS = ["regime", "obs_rule", "metric"]
AUDITED = [
    "selection_ratio", "selection_gap",
    "p_subj_naive", "p_subj_bayesian", "p_subj_recency", "p_subj_selective",
    "B_subj_naive", "B_subj_bayesian", "B_subj_recency", "B_subj_selective",
    "B_price_A_objective", "B_price_B_experienced", "B_price_C_weighted",
    "B_price_D_reputation",
    "D_EV_A_objective", "D_EV_B_experienced", "D_EV_C_weighted",
    "D_EV_D_reputation",
    "D_rel_B_experienced", "D_rel_C_weighted", "D_rel_D_reputation",
    "D_rel_prob_D_reputation", "D_rel_rep_D_reputation",
    "price_success_diff_B_experienced", "price_success_diff_C_weighted",
    "price_success_diff_D_reputation",
    "reputation_hazard_corr", "reputation_price_corr",
    "provider_rank_distortion",
]


def main() -> None:
    old = pd.read_csv(ARCHIVE / "general_summary.csv")
    new = pd.read_csv(RESULTS / "general_summary.csv")
    merged = old[KEYS + ["mean", "mcse"]].merge(
        new[KEYS + ["mean", "mcse"]], on=KEYS, suffixes=("_old", "_new"),
        how="outer",
    )
    merged = merged.loc[merged["metric"].isin(AUDITED)].copy()
    merged["abs_change"] = merged["mean_new"] - merged["mean_old"]
    merged["rel_change"] = np.where(
        merged["mean_old"].abs() > 1e-12,
        merged["abs_change"] / merged["mean_old"].abs(),
        np.nan,
    )
    mcse = merged[["mcse_old", "mcse_new"]].max(axis=1).replace(0, np.nan)
    merged["change_in_mcse"] = merged["abs_change"].abs() / mcse
    merged["sign_changed"] = (
        np.sign(merged["mean_old"]) != np.sign(merged["mean_new"])
    ) & (merged[["mean_old", "mean_new"]].abs().min(axis=1) > 0)
    merged.to_csv(RESULTS / "lookahead_correction_diff_summary.csv", index=False)

    eq_old = pd.read_csv(ARCHIVE / "general_equivalent_efficacy.csv")
    eq_new = pd.read_csv(RESULTS / "general_equivalent_efficacy.csv")
    eq = eq_old.merge(eq_new, on="regime", suffixes=("_old", "_new"))
    eq.to_csv(
        RESULTS / "lookahead_correction_diff_equivalent_efficacy.csv", index=False
    )
    obs_old = pd.read_csv(ARCHIVE / "general_observational_equivalence.csv")
    obs_new = pd.read_csv(RESULTS / "general_observational_equivalence.csv")
    print("observational equivalence identical:", obs_old.equals(obs_new))
    print("sign changes:", int(merged["sign_changed"].sum()))
    print("Wrote look-ahead correction comparison", flush=True)


if __name__ == "__main__":
    main()
