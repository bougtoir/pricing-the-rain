# JRU semantic code audit

Scope: every scientific quantity reported in the manuscript, checked at the
line level against its implementation. "Verdict" is PASS when the code
computes what the manuscript says, CORRECTED when a defect or description
mismatch was found and fixed in this pass, and DOCUMENTED when the code
behaviour is a design choice that the manuscript now states explicitly.
Independent checks: `tests/test_hand_calculations.py` (loop-based
re-implementation), `tests/test_lookahead.py` (information timing),
`tests/test_generic_estimands.py` (synthetic sign rules).

## Generic rare-event simulation (`simulation/general_rare_event.py`)

| Quantity | Code | Definition implemented | Verdict |
|---|---|---|---|
| Objective probability \(p_t\) | `simulate_cell` | \(p_t = \bar p\,[(1-M_t)\ell + M_t h]\), two-state Markov hazard \(M_t\) | PASS |
| Observation \(O_t=D_tA_t\) | `simulate_cell` | Endogenous: request and acceptance logits load on \(M_t\) and on relative hazard \(p_t/\bar p-1\); exogenous: constant request rate equal to the endogenous marginal rate and constant acceptance | PASS (`docs/EXOGENOUS_BENCHMARK_AUDIT.md`) |
| Outcome \(Y_t\) | `simulate_cell` | \(Y_t\sim\text{Bernoulli}(\min(1,p_t+\delta O_t))\) | PASS |
| Selection ratio | `rep_metrics` | \(E[p\mid O=1]/E[p]\); equals \(1+\operatorname{Cov}(O,p)/(E[O]E[p])\) (hand test) | PASS |
| Selection gap | `rep_metrics` | \(E[p\mid O=1]-E[p]\) | PASS |
| Experienced frequency (estimand) | `rep_metrics` | full-record \(\sum OY/\sum O\) | PASS |
| Naive learner state | `cell_arrays` | raw \(\hat p_{exp,t-1}\); initialized at \(\bar p\cdot\)`prior_mean_scale` before the first observation | CORRECTED (was Laplace \((1+\sum Y)/(2+\sum O)\) and included \(Y_t\)) |
| Bayesian learner | `cell_arrays` | Beta(\(\bar p s, (1-\bar p)s\)), \(s=2\), posterior mean on data through \(t-1\) | CORRECTED (included \(Y_t\)) |
| Recency learner | `cell_arrays` | EWMA success / EWMA observation, decay 0.995, prior stocks 0.05/0.10, lagged one period | CORRECTED (included \(Y_t\)) |
| Selective memory | `cell_arrays` | success weight 1.0, failure weight 0.35, same EWMA and prior stocks, lagged | CORRECTED (included \(Y_t\)) |
| Prelec weighting | `prelec` | \(w(p)=\exp(-(-\ln p)^{0.65})\), applied to the Bayesian learner | PASS (hand values) |
| Reputation \(R_{jt}\) | `cell_arrays` | decaying success rate over provider \(j\)'s own observed outcomes before \(t\), decay 0.995, prior stocks 0.05/0.10 | CORRECTED (timing); manuscript §2.2 formula rewritten to the implemented ratio form |
| Reputation in model D quote | `cell_arrays` | reputation enters at periods in which the provider's case is observed; otherwise D = C | DOCUMENTED (Methods now says so; numbers unchanged) |
| Model A | `cell_arrays` | \(\alpha p_t V_t\) | PASS |
| Model B | `cell_arrays` | \(\alpha \hat p_{exp,t-1} V_t\) (raw) | CORRECTED (was Bayesian posterior) |
| Model C | `cell_arrays` | \(\alpha w(\hat p_{Bayes,t-1}) V_t\) | PASS after timing fix |
| Model D | `cell_arrays` | \(\alpha w(\hat p_{Bayes,t-1}) V_t + \gamma R_{jt}\), \(\gamma=0.5\) | PASS after timing fix |
| \(B_{subj}\) | `rep_metrics` | mean of (learner − \(p_t\)) — objective-relative | PASS; manuscript definition CORRECTED to objective-relative (user decision) |
| \(B_{price}\) | `rep_metrics` | mean of (\(P_t/(\alpha V_t)\) − \(p_t\)) — objective-relative | PASS; manuscript definition CORRECTED |
| \(\Delta_{subj}, \Delta_{price}\) | text only | adjacent-layer increments, reported as differences of the B metrics | DOCUMENTED, not labelled B |
| \(D_{EV}\), \(D_{rel}\) | `rep_metrics` | mean(\(P-\alpha pV\)), mean(\((P-\alpha pV)/(\alpha pV)\)) | PASS |
| Probability / reputation split | `rep_metrics` | pointwise \(\alpha V(w-p)+\gamma R\); parts sum exactly (hand test) | PASS |
| Price–success difference | `rep_metrics` | mean quote at observed successes − at observed failures | PASS |
| Reputation–hazard correlation | `rep_metrics` | Pearson corr of \(R\) and \(M\) over observed events | PASS |
| Provider-rank metric | `rep_metrics` | Spearman corr of provider selectivity and provider observed success rate | PASS |
| Equivalent efficacy | `main` | interpolated exogenous \(\delta\) whose mean apparent success equals the zero-efficacy endogenous value | PASS (first moment only) |

## Weather benchmark (`src/weather_analysis.py`, `simulation/run_simulation.py`)

| Quantity | Verdict |
|---|---|
| Rainfall rules: success = rain ≥ threshold in days \(t+1..t+w\) after the pseudo-event (`shift(-lag)`, lag ≥ 1) | PASS — outcome window starts after the event day |
| Hazard and 30-day rainfall predictors: `shift(1)` before rolling sums; hazards are training-period climatology (`training_thresholds`) | PASS — no same-day or future information |
| Strategic pseudo-event onset: first day of a high-hazard spell (`shift(1)` on the indicator) | PASS |
| WTP / quote / reputation overlay: price computed before the provider's Beta or memory update for that event | PASS — no look-ahead (logic unchanged) |
| Regression / clustered price–success models and permutation falsification (`analysis/robustness.py`) | PASS — permutations reassign prices within the declared blocks (1,000 draws); seed 20260924 fixed in code (see hardcode audit) |

## Look-ahead audit result

The only information-timing defect was in `cell_arrays` (generic
simulation). After the correction every learner, reputation stock, and
quote at column \(t\) is a function of \((O_\tau, Y_\tau)_{\tau<t}\) and
contemporaneous state variables \((p_t, M_t, V_t)\) only;
`tests/test_lookahead.py` flips \(Y_t\) and checks that columns \(\le t\)
are unchanged and column \(t+1\) changes. No other module computes a state
from same-period outcomes.
