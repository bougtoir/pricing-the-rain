# Generic probability estimand audit

Revision pass (docs/RARE_EVENT_TARGETED_REVISION_LOG.md). Every probability-like
quantity in `simulation/general_rare_event.py`, with conditioning set, weighting
measure, and whether it is a population estimand or a sample estimate.

Notation: replication r, period t, state M_t ∈ {low, high}, demand D_t,
acceptance A_t, observed event O_t = D_t ∧ A_t, attributed outcome Y_t.
`p_t = base × m(M_t)` is the conditional success probability given the state;
`base` is the rarity-regime parameter.

| Quantity | Definition in code | Conditioning | Weighting | Estimand vs estimate |
|---|---|---|---|---|
| p_objective | `p.mean()` over all retained periods | none (marginal over state mixture) | time-weighted | population estimand E[p_t] |
| p_event_conditional_on_state | `p_t = base·(low_mult or high_mult)` | state M_t | state-conditional | population parameter |
| p_ref_observed | `p[O].mean()` = mean of p_t over observed events | O = 1 | observation-weighted | population estimand E[p_t \| O=1] |
| p_experienced | `(Y & O).sum() / O.sum()` | O = 1 | observation-weighted | sample estimate of E[Y \| O=1] |
| p_subj_{learner} | per-learner running estimate `e_t`, then `mean(e)` | none | time-weighted mean of the learner state | estimate of the learner's reported probability |
| p_subj_naive | raw `cumY_{t-1}/cumO_{t-1}`; prior mean `base*prior_mean_scale` before first observation | O = 1, tau < t | observation-weighted through t-1 | raw experienced frequency at quote time |
| B_subj_{learner} | `mean(e_t - p_t)` | none | time-weighted | objective-relative subjective gap (canonical) |
| B_price_{model} | `mean(P_t/(alpha V_t) - p_t)` | none | time-weighted | objective-relative price-layer gap (canonical) |
| p_weighted | `prelec(bayesian)` elementwise | none | time-weighted | transformed estimate |
| p_price_implied | `P / (α·V)` pointwise, `mean` | none | time-weighted | model-implied quantity |
| price_success_diff | `mean(P\|Y∧O) − mean(P\|~Y∧O)` | O ∧ Y vs O ∧ ~Y | event-weighted | sample contrast |
| provider_success | `Y[O ∧ provider=j].mean()` | O, provider | provider-observation-weighted | sample estimate |
| regime average | metrics averaged over 2,000 replications | regime × rule | equal replication weight | Monte Carlo mean |

## The critical estimand question

**Are p_objective and p_experienced the same estimand? — No.**

- p_objective is a *time-weighted marginal*: E[p_t] over all periods.
- p_experienced is an *observation-weighted conditional*: empirical E[Y | O=1].

Their difference `p_exp − p_bar` mixes two distinct things:

1. a *composition (selection) difference*: E[Y|O=1] − E[p_t] — the observed
   support is shifted toward high-hazard periods when O correlates with M_t;
2. *record/estimand bias*: E[Y|O=1] − E[p_t|O=1] — discrepancy between the
   true event probability on the observed support and what the record shows
   (zero here, since Y is generated at p_t + δ·O with δ = 0).

Resolution implemented in code (decision TR-2): report the decomposition

    p_exp − p_bar = selection_gap + B_abs
    selection_gap = p_ref_observed − p_bar   (E[p|O=1] − E[p])
    B_abs         = p_exp − p_ref_observed   (≈ 0 at zero efficacy)

with the ratio companion `selection_ratio = p_ref_observed / p_bar` and the
relative record distortion `B_rel = (p_exp − p_ref) / p_ref`. The term "bias"
is used only for B_abs / B_rel (same-support comparisons); the composition
difference is called *selection gap / selection ratio*, not bias.

## What the old B_exp actually measured

Old `B_exp = p_exp − p_bar` ≈ selection_gap (because B_abs ≈ 0). Its
near-proportionality to `base` — 0.216 / 0.072 / 0.021 / 0.007 across
regimes — is therefore a *composition effect that scales with p*, not a
record bias that "grows with rarity." The old statement "experienced-frequency
bias grows monotonically with rarity" conflated the two.

## Where quantities appear in the manuscript

- p_objective, p_ref_observed, p_experienced, p_subj (Bayesian/selective),
  price-implied (model D): Table 2, Figure 4A (panel A of
  figure6_four_probabilities.png).
- selection_gap, selection_ratio, B_abs, B_rel: Table 2, Figure 4B, Figure 5.
- D_EV, D_rel and the probability/reputation split
  (D_rel_prob_D, D_rel_rep_D): Table 2, Figure 4C, Figure 5, Figure S-support.
- price_success_diff, reputation correlations, provider-rank distortion:
  Table 2, Figure 4D, Table S8.

## Information timing (JRU correction)

All learner states, reputation stocks, and Model B–D quotes at column t use
information through t-1 only (`cumsum - current`, `lag1(ewma)`), verified by
`tests/test_lookahead.py`. Model B uses the raw experienced frequency
(`naive`), not the Bayesian posterior. Pre-correction outputs are archived in
`results/archive/pre_lookahead_fix_837387d/`.
