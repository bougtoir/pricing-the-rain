# Rare-event targeted revision log

Scope: generic rare-event simulation and its interpretation only. Rainfall
module frozen. Checkpoint tag `checkpoint-pre-targeted-revision-29781ff64`.

- TR-1. Estimand audit first (GENERIC_PROBABILITY_ESTIMAND_AUDIT.md):
  p_objective (time-weighted E[p_t]) and p_experienced (observation-weighted
  E[Y|O=1]) are different estimands; their difference is a composition
  (selection) gap, not a record bias. New decomposition
  p_exp − p_bar = selection_gap + B_abs.
- TR-2. Exogenous benchmark fix: previous "exogenous" rule left acceptance
  state-dependent, contaminating the benchmark (see
  EXOGENOUS_BENCHMARK_AUDIT.md). Code now sets constant acceptance under
  exogenous so O ⊥ p_t. Endogenous rule untouched.
- TR-3. New metrics: p_ref_observed, selection_gap, selection_ratio, B_abs,
  B_rel, plus the exact analytic split of model-D distortion
  D_EV = D_prob_abs + D_rep_abs and D_rel = D_rel_prob + D_rel_rep.
- TR-4. Convergence scan metrics updated to the new distortion set.
- TR-5. Equivalent efficacy solved explicitly (inverse linear interpolation
  with MCSE bounds) for every regime → results/general_equivalent_efficacy.csv.
- TR-6. New figure 8: frequency vs price distortion decomposition
  (figure8_distortion_decomposition). Figure 6 panel B revised to absolute gap
  + ratio; panel A adds the matched p_ref series.
- TR-7. Unit tests test_generic_estimands.py: exogenous unbiasedness
  (homogeneous + heterogeneous p), endogenous positive gap, decreasing rule
  negative gap.
- TR-8. Original "rarity amplifies frequency bias" hypothesis: FAILED under
  the matched estimand — reported transparently (negative-result discipline);
  replaced by P2a/P2b/P2c in the manuscript propositions.
