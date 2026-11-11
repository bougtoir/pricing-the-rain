# Look-ahead correction audit (generic simulation)

## Defect

In `simulation/general_rare_event.py::cell_arrays` (baseline commit
`837387d71`), cumulative sums and exponentially weighted sums included the
current period. The Bayesian, recency, and selective-memory learners, the
provider reputation stock, and therefore the quotes of models B–D at period
\(t\) used the period-\(t\) outcome \(Y_t\). The manuscript states that quotes
and reputation use information through \(t-1\). The weather benchmark
(`simulation/run_simulation.py`) sets prices before updating and was not
affected.

Two further implementation–specification mismatches were resolved with the
author at the same time:

- Model B priced a Bayesian posterior (prior strength 2) and the naive learner
  was a Laplace ratio \((1+\sum Y)/(2+\sum O)\). Both now use the raw
  experienced frequency \(\hat p_{exp,t-1}=\sum_{\tau<t}Y_\tau O_\tau/\sum_{\tau<t}O_\tau\);
  before the first observation the pre-specified initial value
  (`prior_mean_scale` × base probability, the same prior mean as the Bayesian
  learner) is used as an initialization only. The Bayesian learner is kept as a
  separate subjective-learning variant.
- \(B_{subj}\) and \(B_{price}\) are defined relative to the objective
  probability (as implemented); the manuscript previously described them as
  adjacent-layer increments. Increments are not labelled \(B\).

## Correction

- Commit `0c926a8ab` ("generic simulation uses t-1 information only; raw
  experienced frequency for Model B and naive learner").
- Cumulative learners: `cumsum(x) - x`. Exponentially weighted learners and
  reputation: `lag1(ewma(x))`, i.e. the state at the end of \(t-1\).
- Regression tests: `tests/test_lookahead.py` flips \(Y_t\) and checks that
  Bayesian state, reputation, and B/C/D quotes at \(t\) and earlier are
  unchanged while some later value changes; the pre-correction code fails
  these tests. `tests/test_hand_calculations.py` checks every learner and the
  reputation stock against a loop implementation written from the Methods
  text.

## Invariance

- `config/general_simulation.yml`: all parsed values equal those at
  `837387d71` (only a comment line changed). Seed 20261012, 2,000
  replications, 1,500 equivalence replications, horizon 4,000, burn-in 200,
  6 providers, regimes, efficacy grid unchanged.
- The formal rerun used the full configuration (not the diagnostic R = 300).
- Pre-correction outputs are archived unchanged in
  `results/archive/pre_lookahead_fix_837387d/` with `MANIFEST.sha256`.
- `results/general_observational_equivalence.csv` and
  `results/general_equivalent_efficacy.csv` are identical before and after
  (they depend only on the data-generating process, not on learners or
  quotes). Selection ratio, selection gap, and provider-rank distortion are
  identical (they do not depend on learner timing).

## Before/after values (endogenous observation; full table in
`results/lookahead_correction_diff_summary.csv`)

| Metric | Regime | Old | Corrected | Abs. change | Rel. change | Qualitative conclusion changed? |
|---|---|---|---|---|---|---|
| Selection ratio | all | 1.708–1.713 | identical | 0 | 0 | NO |
| Selection gap | common → very rare | 0.2161 → 0.0072 | identical | 0 | 0 | NO |
| \(B_{subj}\) naive | rare | 0.0285 | 0.0205 | −0.0080 | −28% | NO (Laplace bias removed) |
| \(B_{subj}\) naive | very rare | 0.0154 | 0.0069 | −0.0085 | −55% | NO |
| \(B_{subj}\) Bayesian | all | — | — | ≤ 0.0001 | < 0.1% | NO |
| \(B_{subj}\) selective | rare | 0.3106 | 0.3107 | 0.0000 | 0.0% | NO |
| \(B_{price}\) model B | rare | 0.0204 | 0.0205 | +0.0002 | +0.8% | NO |
| \(B_{price}\) model D | very rare | 0.0934 | 0.0942 | +0.0008 | +0.9% | NO |
| \(D_{EV}\) model D | common / very rare | 0.1756 / 0.1280 | 0.1755 / 0.1294 | ≤ 0.0013 | ≤ 1.1% | NO (flat across regimes) |
| \(D_{rel}\) model D | common / very rare | 1.122 / 11.538 | 1.124 / 11.612 | ≤ 0.074 | ≤ 0.6% | NO (rises with rarity) |
| \(D_{rel}\) probability part | very rare | 9.4542 | 9.4547 | +0.0005 | 0.0% | NO |
| \(D_{rel}\) reputation part | very rare | 2.084 | 2.157 | +0.073 | +3.5% | NO (share rises with rarity) |
| Price–success diff., model D | common | 0.1447 | 0.1194 | −0.0252 | −17% | NO |
| Price–success diff., model D | rare | 0.0446 | 0.0131 | −0.0315 | −71% | NO ("small and positive") |
| Price–success diff., model D | very rare | 0.0441 | 0.0040 | −0.0401 | −91% | NO (still positive; MCSE 0.0002) |
| Reputation–hazard corr. | common | 0.2248 | 0.0900 | −0.1347 | −60% | NO (sign unchanged) |
| Reputation–hazard corr. | rare | −0.1413 | −0.1595 | −0.0182 | −13% | NO |
| Provider-rank distortion | all | — | identical | 0 | 0 | NO |
| Equivalent efficacy | moderately rare / rare / very rare | 0.0722 / 0.0217 / 0.0075 | identical | 0 | 0 | NO |

Sign changes across all 232 audited cells: 3, all in \(B_{subj}\) naive
under exogenous observation (common, moderately rare, rare), where the
corrected raw frequency is unbiased and the means are within about one MCSE
of zero (old positive values were the Laplace-smoothing bias). No claimed
result depends on these cells.

## Affected and unaffected manuscript elements

- Affected (regenerated from canonical outputs): §6.2–6.3 values
  (\(D_{rel}\), shares, \(D_{EV}\), reputation–hazard correlation,
  price–success difference), Table 2, Table S7, Table S8, Fig. 4 (panels A, C,
  D), Fig. 5 (panel B), abstract and cover-letter values that cite these
  tokens.
- Unaffected: Lemma 1/2 and corollaries; selection ratio and gap (Fig. 5A,
  §6.1); mean-performance equivalence and equivalent efficacy (§6.4, Table 3,
  Fig. 6); every weather-benchmark result (§5, §6.5, Table 4, Figs. 2, 3, 7, 8,
  Tables S1–S6, S9–S10).
- Unchanged main claims: covariance sign rule; rarity invariance of the
  selection ratio with shrinking absolute gap; relative distortion rising with
  rarity through a dominant transformed-frequency part and a growing
  reputation share with flat \(D_{EV}\); stock–flow decoupling (weaker
  contemporaneous association); first-moment equivalence; zero-efficacy
  benchmark.
- Text corrected while regenerating: "models A–C remain near one" (false
  before and after) replaced by model-specific values; "near zero by
  construction" for the reputation–hazard correlation replaced by "weak and
  negative".

## Other look-ahead checks

| Path | Result |
|---|---|
| Recency and selective-memory learners | corrected (`lag1`) |
| Provider reputation in model D | corrected (`lag1`), enters only when the provider's case is observed |
| Model A | uses \(p_t\) by definition (objective benchmark) |
| Acceptance/demand decisions | depend on \(p_t\) / hazard state, not on \(Y_t\) |
| Metrics (B, D, price–success, correlations) | computed ex post from period arrays; not inputs to quotes |
| Weather benchmark `simulate_one` | prices set before the period's update; unchanged |
| Weather pseudo-events | dry-spell and deficit variables lagged one day; follow-up excludes event day (tests in `test_weather_analysis.py`) |
| Hazard training/evaluation split | training 1991–2010, evaluation 2011–2020 |

No further look-ahead path was found.
