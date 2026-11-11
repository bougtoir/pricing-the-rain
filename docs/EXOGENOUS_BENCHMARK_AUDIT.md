# Exogenous-observation benchmark audit

## What equality should hold

Under a truly exogenous observation rule, O_t is independent of p_t, so the
observed support is representative:

    E[p_ref_observed] = E[p_t | O=1] = E[p_t] = p_bar
    E[p_experienced]  = E[Y | O=1]   = E[p_t | O=1]  (at δ = 0)

i.e. `selection_gap = 0`, `selection_ratio = 1`, `B_abs = 0` up to Monte Carlo
error.

## What the previous implementation did

The previous "exogenous" rule made *demand* exogenous (constant request
probability equal to the endogenous marginal) but left *acceptance* selective:
`accept_prob` still increased in relative hazard `p_t/base − 1`. Observation
O = D_exo ∧ A was therefore still shifted toward high-hazard periods — case C
in the prompt ("exogenous observation still samples a nonrepresentative state
mixture due to another mechanism"). That is why `p_experienced` exceeded
`p_objective` under the exogenous benchmark.

## Fix applied

In `simulate_cell`, the exogenous rule now sets `accept_prob` to the constant
`expit(intercept)` for all periods and providers: demand and acceptance are
both state-independent, so O ⊥ p_t holds by construction. The endogenous rule
is unchanged. (Provider selectivity is also removed under exogenous; it is
mean-zero across providers, so removing it changes only variance, not the
benchmark's expectation.)

## Sign expectations (verified by unit tests)

`tests/test_generic_estimands.py` runs small controlled cells:

- homogeneous p (high_share = 0), exogenous: |p_exp − p_bar| within MC error;
- heterogeneous p_t, exogenous: p_exp ≈ p_bar and selection_ratio ≈ 1;
- endogenous observation increasing in p_t: selection_gap > 0;
- a decreasing-in-p observation rule (negative acceptance slope): selection_gap < 0.

## Consequence for the manuscript

The exogenous series is now a clean representative-support benchmark. Numbers
reported under "exogenous" in the revised tables differ from the previous run
precisely because the previous exogenous series was contaminated by selective
acceptance; this is a benchmark-definition fix, not a retune (the endogenous
results are unchanged by the fix).
