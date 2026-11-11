# JRU code ↔ manuscript crosswalk

## Manuscript → code

| Manuscript object (section) | Code | Test |
|---|---|---|
| \(p_t\), two-state hazard, persistence, high share, multipliers (§4) | `simulate_cell`, `markov_state`; `config/general_simulation.yml: hazard_state`; Methods tokens `CFG_*` | `test_generic_estimands.py` |
| Rarity regimes 0.30/0.10/0.03/0.01 (§4) | `config: regimes`; tokens `CFG_P_*` | — |
| Observation \(O=D\cdot A\), endogenous vs exogenous (§2.1, §4) | `simulate_cell` | `test_generic_estimands.py` (sign rules) |
| Lemma 1 selection ratio and sign rule (§3) | `rep_metrics: selection_ratio`; analytic value `analytic_selection_ratio` (build) | `test_hand_calculations.py::test_selection_ratio_and_covariance_identity_by_hand` |
| Corollary: ratio invariant to rarity, gap shrinks (§3, §6.1) | `selection_ratio`, `selection_gap` by regime; Fig. 4B | — (reported means) |
| Raw experienced frequency \(\hat p_{exp,t-1}\), initialization (§4) | `cell_arrays: naive` | `test_lookahead.py`, `test_hand_calculations.py` |
| Bayesian / recency / selective learners (§4) | `cell_arrays` | `test_hand_calculations.py` (loop reference) |
| Prelec \(w(p)\), Lemma 2 (§3) | `prelec` | `test_prelec_hand_values_and_lemma2_divergence` |
| Reputation \(R_{jt}\) formula (§2.2), prior stocks, timing (§4) | `cell_arrays: rep`; `PRIOR_SUCCESS_STOCK`, `PRIOR_OBS_STOCK` | `test_hand_calculations.py`, `test_lookahead.py` |
| Models A–D (§2.1, §4) | `cell_arrays: prices` | `test_quotes_match_hand_formulas` |
| \(B_{subj}=\hat p_{subj}-p\), \(B_{price}=\hat q_{price}-p\) (§4) | `rep_metrics: B_subj_*`, `B_price_*` | `test_selection_ratio_and_covariance_identity_by_hand` |
| \(D_{EV}\), \(D_{rel}\), probability/reputation split (§4, §6.2) | `rep_metrics: D_EV_*`, `D_rel_*`, `D_*_D_reputation` | `test_distortion_parts_sum_exactly` |
| Price–success difference (§6.3) | `rep_metrics: price_success_diff_*` | — |
| Reputation–hazard correlation (§6.3) | `rep_metrics: reputation_hazard_corr` | — |
| Provider-rank distortion (§6.3) | `rep_metrics: provider_rank_distortion` | — |
| Mean-performance equivalence, equivalent \(\delta\) (§2.3, §6.4) | `main` (efficacy grid, `np.interp`) → `general_equivalent_efficacy.csv` | — |
| Weather benchmark rules, windows, thresholds (§5) | `src/weather_analysis.py` | `test_weather_analysis.py` |
| WTP / quote overlay M0–M5 (§5, §6.5) | `simulation/run_simulation.py` | `test_simulation.py` |
| Clustered regression, permutation (§6.5, S5) | `analysis/robustness.py` | `test_weather_analysis.py` |

## Code → manuscript

| Computed output | Where reported |
|---|---|
| `general_summary.csv` metrics: selection ratio/gap, p layers, B, D, shares, price–success, reputation–hazard, provider rank | Abstract, §6.1–6.3, Table 2, Table S8, Fig. 4, Fig. 5, cover letter |
| `general_convergence.csv` | Table S7, Methods replication count |
| `general_observational_equivalence.csv`, `general_equivalent_efficacy.csv` | §6.4, Table 4, Fig. 6 |
| B_subj for naive/recency/selective, B_price A–C | Table S8 (all), §6.2 (selective, Bayesian) |
| `reputation_price_corr` | Table S8 only |
| Weather outputs (`analysis/*.csv`, `results/simulation_*`) | §5, §6.5, Tables 3, S1–S6, S9–S10, Figs. 2–5, S1–S3 |

Every value in the rendered text enters through a `{{TOKEN}}` resolved in
`manuscript/build_manuscript.py:replacements()` from `results/manuscript_values.json`
or the config; the build fails on unresolved tokens.
