# GENERAL FORMAL MODEL — pricing rare events under endogenous observation

Phase 1–3 output of the generalization pass. Notation is used verbatim in the
manuscript's Conceptual Framework and Theory sections.

## 1. Four probability layers

**A. Objective probability.** \(Y_t \in \{0,1\}\) rare binary event;
\(p_t = P(Y_t = 1 \mid X_t)\). In the simulation \(p_t = b\,m(M_t)\) with
\(M_t\) a two-state persistent hazard and \(m(\cdot)\) a multiplier.

**B. Experienced frequency.** Observation is endogenous:
\(O_t = D_t A_t\), where demand \(D_t\) and provider acceptance \(A_t\) depend
on hazard, demand pressure, provider selectivity, and history. The experienced
frequency is
\[
\hat p_{\mathrm{exp}} = \frac{\sum_t O_t Y_t}{\sum_t O_t}.
\]
Proposition (P1). If \(O_t\) is more likely when \(p_t\) is high
(\(\mathrm{Cov}(O_t, p_t) > 0\)), then
\(E[\hat p_{\mathrm{exp}}] > E[p_t]\) even though the event process is
unchanged. Sufficient conditions: upward bias when observation loads on
high-hazard states; downward bias when it loads on low-hazard states;
unbiased iff \(O_t \perp p_t\) or weights are constant. Formally, writing
\(w_t = O_t / \sum O_t\), \(\hat p_{\mathrm{exp}} = \sum w_t p_t + \sum w_t
(Y_t - p_t)\); the second term is a mean-zero martingale, so
\(E[\hat p_{\mathrm{exp}}] \to \mathrm{plim} = E_w[p]\), the
observation-weighted hazard.

**C. Subjective probability.** Agents see only observed outcomes. Learners:
(1) naive frequency \(\hat p_{\mathrm{subj},t} = \hat p_{\mathrm{exp},t-1}\), the raw
experienced frequency through \(t-1\) (initialized at the prior mean
\(\bar p = b\) before the first observation; initialization, not smoothing);
(2) Bayesian Beta-posterior over observed outcomes;
(3) recency-weighted EWMA;
(4) selective-memory EWMA with asymmetric success/failure weights;
(5) optionally \(q_t = w(\hat p_{\mathrm{subj},t})\) with Prelec
\(w(p) = \exp(-(-\ln p)^{\alpha})\), \(\alpha = 0.65\) — an explicit
behavioral assumption (layer D), not an estimate.

**D. Price-implied index.** Benchmark pricing rules (each a pricing rule,
not a market-clearing equilibrium):
- Model A (objective EV): \(P_t = \alpha p_t V_t\)
- Model B (experienced-EV): \(P_t = \alpha \hat p_{\mathrm{exp},t-1} V_t\) (raw
  experienced frequency; no Bayesian smoothing)
- Model C (weighted subjective): \(P_t = \alpha w(\hat p_{\mathrm{subj},t}) V_t\)
- Model D (reputation-mediated): \(P_t = \alpha w(\hat p_{\mathrm{subj},t}) V_t
  + \gamma R_t\), \(R_t\) a decaying stock of past attributed outcomes.

Price-implied index: \(\hat q_{\mathrm{price},t} = P_t / (\alpha V_t)\).

**Information timing (JRU correction, look-ahead fix).** Every learner state,
reputation stock \(R_{jt}\), and quote \(P_t\) of Models B–D at period \(t\)
uses the observed record through \(t-1\) only.

**Layer gaps (canonical estimands).** \(B_{\mathrm{subj}} = \hat p_{\mathrm{subj}} - p\)
and \(B_{\mathrm{price}} = \hat q_{\mathrm{price}} - p\), each averaged over all
periods (objective-relative). Adjacent-layer increments
(\(\hat p_{\mathrm{subj}} - \hat p_{\mathrm{exp}}\), \(\hat q_{\mathrm{price}} - \hat p_{\mathrm{subj}}\))
are differences of reported layer means and are never labeled \(B\).
NOT a probability in general: under Model D it equals
\(w(\hat p_{\mathrm{subj}}) + \gamma R_t/(\alpha V_t)\), a composite that can
exceed 1. "Probability" is reserved for quantities constrained to \([0,1]\).

## 2. Propositions

- **P1.** Endogenous observation produces experienced frequencies that exceed
  the marginal objective rate with the event process unchanged — a selection
  (composition) gap, \(E[p_t|O=1]-E[p_t]\), not record bias. Under the
  matched estimand (revision log TR-1) the gap is proportional to \(p_t\):
  the ratio stays constant as rarity increases while the absolute gap
  shrinks. (Verified in simulation; see
  GENERIC_PROBABILITY_ESTIMAND_AUDIT.md.)
- **P2.** Experienced-EV prices (Model B) diverge from objective-EV prices
  (Model A) whenever \(E[\hat p_{\mathrm{exp}}] \ne E[p_t]\); the relative
  distortion grows as \(p_t\) falls because the denominator
  \(\alpha p_t V_t\) shrinks while the absolute deviation is driven by
  selection and non-scaling components (absolute \(D_{EV}\) stays
  approximately flat — the relative rise is a composition/denominator
  effect, not growing absolute mispricing).

- **Lemma 1 (selection ratio under multiplicative state risk).** If
  \(p_t = b\,m(S_t)\) and \(P(O=1\mid S=s) = q_s\) (demand and acceptance
  depend on the state or equivalently on the relative hazard \(p_t/b-1\)),
  then
  \(R = [\pi m_H q_H + (1-\pi) m_L q_L] / [\mu(\pi q_H + (1-\pi) q_L)]\),
  independent of \(b\). The absolute gap \(E[p|O=1]-E[p] = b\mu(R-1)\) is
  proportional to rarity. Parameter value in the generic simulation:
  \(R = 1.7115\) (simulated 1.708–1.713). Fails if selection responds to
  the absolute level \(p_t\). Full derivation:
  SELECTION_RATIO_DERIVATION.md.
- **P3.** Probability weighting amplifies divergence under
  overweighting of small probabilities: for \(w(p) > p\),
  \(P_C - P_A = \alpha V_t (w(\hat p) - p) > 0\) even at \(\hat p = p\).
- **P4.** Reputation adds a stock term \(\gamma R_t\): price depends on
  history, not only current \(p_t\) — path dependence.
- **P5.** Contemporaneous price–outcome association is then mechanically
  ambiguous: prices at \(t\) respond to \(R_t\) and to \(\hat p\) (stocks),
  while \(Y_t\) is a hazard-driven flow; the association can be weak, zero,
  or signed opposite to the premium.
- **P6.** \(\hat p_{\mathrm{price},t}\) is not a valid estimator of causal
  efficacy: even at zero true effect it mixes selection bias
  (\(\hat p_{\mathrm{exp}} - p\)), learning error, weighting
  (\(w(\hat p) - \hat p\)), and reputation (\(\gamma R_t / \alpha V_t\)).

## 3. Mean-performance equivalence / identifiability

The equivalence established in this project is FIRST-MOMENT ONLY:
(i) zero efficacy + endogenous observation and (ii) positive efficacy
\(\delta\) + exogenous observation produce the same MEAN apparent success
whenever the selection-driven uplift in mean experienced frequency equals
\(\delta\). No claim is made that the joint distributions of outcomes,
prices, provider identities, or histories coincide. Distinguishing data:

| Additional data | Identifies |
|---|---|
| Rejected requests / declinations | acceptance rule \(A_t\); denominator of \(\hat p_{\mathrm{exp}}\) |
| Baseline hazard \(p_t\) (pre-event forecasts) | selection bias \(E_w[p] - E[p]\); separates P1 from efficacy |
| Price history \(P_t\) + known pricing rule | \(\hat p_{\mathrm{price}}\); weighting vs reputation components |
| Provider identity + acceptance records | selective exposure; ranking distortion |
| Timing history (when interventions occur relative to hazard) | endogenous timing channel |
| Counterfactual / randomized exposure | causal efficacy directly; breaks the equivalence |

## 4. Distortion metrics (Phase 8)

\(B_{\mathrm{exp}} = \hat p_{\mathrm{exp}} - \bar p\);
\(B_{\mathrm{subj}} = \bar{\hat p}_{\mathrm{subj}} - \bar p\);
\(B_{\mathrm{price}} = \overline{\hat p}_{\mathrm{price}} - \bar p\);
\(D_{\mathrm{EV}} = \overline{P - \alpha p V}\);
\(D_{\mathrm{rel}} = \overline{(P - P_A)/P_A}\) with
\(P_A = \alpha p V\) floored at a small \(\epsilon\) (near-zero-denominator
guard). No additive decomposition is claimed; components are reported
separately.
