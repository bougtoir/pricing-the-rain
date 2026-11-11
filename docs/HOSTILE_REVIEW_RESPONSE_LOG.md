# Hostile-review response log — Economic Modelling

Simulated three-referee adversarial review of the post-micro-finishing
submission package. Each reviewer gives pre-revision verdict, five
strongest criticisms, the repairs implemented, and post-revision verdict.

## Reviewer A — Economic theory/modeling

**Pre-revision verdict: Major revision (reject-risk).**

Criticisms:
1. The "price" is an arbitrary mapping, not a market-clearing or
   equilibrium price — calling it a pricing model overclaims.
   → Repair: added an explicit reduced-form microfoundation in §2.1
   (quote = share α of perceived gross surplus v·ŵ + separable reputation
   component γR; no equilibrium/bargaining/welfare claim) and a standing
   definition that "pricing" means model-implied quote formation. Title
   retained: with the definition explicit, "Pricing Rare Events" is
   accurate and materially better than alternatives.
2. Lemma 1 is a narrow two-state result that may look tautological.
   → Repair: generalized to arbitrary state distribution:
   R = E[ms]/(E[m]E[s]) = 1 + Cov(m,s)/(E[m]E[s]), independent of baseline
   p0, with the sign determined by Cov(m,s). Two-state case retained as
   the calibrated special case (docs/SELECTION_RATIO_DERIVATION.md).
3. P1/P2a claim "selection inflates" unconditionally.
   → Repair: P1 and P2a rewritten sign-conditional; the simulation is
   explicitly the positive-covariance calibration.
4. No clear comparative-statics statement for quote composition.
   → Repair: P2c already states the two-channel comparative statics;
   tightened "mispricing" → "absolute deviation from the objective-EV
   benchmark" and added the normative-status caveat (EV benchmark is not
   a welfare optimum).
5. Quote/price/WTP terminology inconsistent.
   → Repair: audited all uses; "model-implied quote" and "posted quote
   under a reduced-form pricing rule" standardized; "market price" only
   in disclaimers; "price-implied index" unchanged.

**Post-revision verdict: Minor revision.**

Residual: the reduced-form quote rule remains non-equilibrium by design —
now stated as a deliberate scope choice, not a defect.

## Reviewer B — Behavioral economics

**Pre-revision verdict: Major revision.**

Criticisms:
1. Prelec weighting presented almost as a behavioral law.
   → Repair: everywhere restated as "one parameterized scenario, not an
   estimate" (§4 already; P3 and Lemma 2 framing updated).
2. P3 "partially reverses underweighting" conflates the weighting function
   with the description–experience mechanism.
   → Repair: P3 renamed "Nonlinear transformation moves the subjective
   layer relative to experience"; description–experience cited as a
   distinct literature; Bayesian/recency/selective memory listed as
   separate alternative transformations.
3. Lemma 2 could read as a universal behavioral theorem.
   → Repair: kept explicitly as a property of the assumed Prelec
   transformation.
4. Human-behavior claims might exceed simulation.
   → Repair: audit confirms all behavioral statements are framed as
   model mechanisms or literature context; §7.3 applications are
   conditional and now sign-aware (Cov(m,s)).
5. "Sparse samples" language could imply untested finite-sample learning
   claims. → Already repaired in the micro-finishing pass ("sparse
   positive outcomes").

**Post-revision verdict: Minor revision.**

## Reviewer C — Applied/empirical economics

**Pre-revision verdict: Major revision (reject-risk).**

Criticisms:
1. P6 "bounds price-based inference" overclaims non-identification from
   prices. → Repair: P6 renamed "Mean-performance equivalence limits
   inference from raw performance"; Abstract, Introduction, §6.4, cover
   letter narrowed to the first-moment claim plus the caution that quotes
   load on transformed beliefs and reputation (not a proved theorem).
2. Real-weather benchmark could be read as validating reputation pricing.
   → Repair: §5 now splits OBSERVED-WEATHER layer (empirical: selection/
   apparent success) from MODEL-OVERLAY layer (calibrated: WTP, quotes,
   reputation); main text states the empirical strength is the first
   layer.
3. Secondary overlay results (scenario-WTP regression, permutation test,
   M4/M5 decomposition) sat in main text next to the empirical
   demonstration. → Repair: moved to supplement §S15; §6.5 retains one
   concise overlay paragraph.
4. "Prices alone cannot separate efficacy from selection" too strong.
   → Repair: replaced everywhere with the first-moment wording.
5. Simulated quotes might be mistaken for observed prices.
   → Repair: §5 and §6.5 disclaimers strengthened; "Prices and acceptance
   strategies are calibrated scenarios" retained.

**Post-revision verdict: Minor revision.**

## Economic Modelling fit verdict

Model-first structure (framework → theory → simulation → benchmark →
results), analytic lemmas with comparative statics, classified
propositions, one in-journal citation added (Shea 2015). Fit: good.

## Cross-cutting repairs implemented

- Novelty reframed around six derived results; coverage matrix added to
  CLOSEST_PRIOR_STUDIES.md; no "first" claims.
- Cross-domain claims made sign-conditional via Cov(m,s).
- Rare-event specificity restated: selection is general; scaling vs the
  objective-EV benchmark, the Prelec scenario, and sparse positive
  outcomes are rarity-specific.
- Zero numerical results changed.
