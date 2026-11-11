# Final hostile-review revision report — Economic Modelling

- **Starting Git hash:** 3a664d86e
- **Ending Git hash:** (recorded at commit; commit f247abe7f)
- **Scientific numbers changed:** NONE. No simulation, rainfall,
  decomposition, equivalence, or parameter output was rerun or altered;
  `results/manuscript_values.json` untouched. No code defect found.
  One exception to "no new artifacts": a new reference's Crossref metadata
  (Shea 2015) was added under `data/raw/literature/` per the acquisition
  ledger — bibliographic metadata only, no numerical input.

## Generalized covariance identity

Lemma 1 now covers an arbitrary risk state X with multiplier m(X) > 0,
p(X) = p0·m(X), observation weight s(X) ≥ 0 independent of p0:
R = E[ms]/(E[m]E[s]) = 1 + Cov(m,s)/(E[m]E[s]) — independent of p0, with
the absolute gap proportional to p0. Two-state case retained as the
calibrated special case; derivation in docs/SELECTION_RATIO_DERIVATION.md.

## Final sign interpretation of selection

Risk-correlated selection shifts experienced frequency with sign set by
Cov(m,s): positive inflates, zero leaves composition unchanged, negative
deflates. The calibrated simulation is the positive-covariance case
(R ≈ 1.71). P1, P2a, §6.1 heading, abstract, and §7.3 applications all
sign-conditional.

## Microfoundation / interpretation of the quote rule

§2.1: quote = α·v·ŵ (share α of perceived gross surplus) + γR (separable
reputation/trust/amenity component, γ the reputation-to-quote exchange
rate). Explicitly reduced-form: no equilibrium, bargaining, or
welfare-optimality claim; the objective-EV benchmark is normative only in
the limited objective-EV sense, not a welfare optimum.

## "Pricing" terminology / title

Title retained — "Pricing Rare Events under Endogenous Observation:
Selection, Reputation, and a Zero-Effect Environmental Benchmark" — with
an explicit standing definition in §1 that "price"/"pricing" means
model-implied quote formation under a reduced-form pricing rule.
Terminology standardized: model-implied quote; market price used only in
disclaimers; P4 renamed to "Model-implied quotes mix hazard and
transformation".

## Narrowed P6 claim

P6 renamed "Mean-performance equivalence limits inference from raw
performance". Valid claim: mean apparent performance alone cannot
distinguish zero-efficacy endogenous selection from positive-efficacy
exogenous observation in several simulated rarity regimes; observed quote
data do not automatically solve it (quotes load on transformed beliefs
and reputation) — a caution, not an identification theorem.

## Real-weather benchmark scope

§5 now separates OBSERVED-WEATHER layer (empirical: selection/timing
produces large apparent-success differences under known-zero efficacy)
from MODEL-OVERLAY layer (calibrated: WTP, quotes, reputation, selective
memory). Empirical strength attributed to the first layer only.

## Prelec scenario wording

One parameterized transformation scenario; not estimated; not the same
mechanism as description–experience underweighting; Bayesian/recency/
selective memory are separate alternative transformations. P3 renamed
"Nonlinear transformation moves the subjective layer relative to
experience"; Lemma 2 framed as a property of the assumed specification.

## Main-text vs supplement benchmark reallocation

Scenario-WTP regressions, permutation falsification, and M4/M5
quote-reputation decomposition moved from §6.5 to new supplement §S15;
§6.5 keeps the apparent-success demonstration plus one concise overlay
sentence.

## Three reviewer verdicts

Before: A Major (reject-risk), B Major, C Major (reject-risk).
After: A Minor, B Minor, C Minor. Details in
docs/HOSTILE_REVIEW_RESPONSE_LOG.md.

## Economic Modelling fit verdict

Model-first comparative-statics paper; citation ecology documented in
docs/ECONOMIC_MODELLING_CITATION_ECOLOGY.md; one in-journal citation added
(Shea 2015). Fit confirmed.

## Clean-build/test result

- build_manuscript.py clean build: 6,404 words main text; abstract 246
  words (≤250); 5 highlights ≤85 chars; keywords 5.
- pytest: 25/25 passed.
- analysis/final_audit.py: PASS (numerical traceability, package,
  unfavorable-result checks).
- Reproduction manifest regenerated (45 output hashes).
- Reference count 25 → 26.

## Unresolved author-only actions

Identity/affiliation, ORCID, acknowledgements, funding, competing
interests, CRediT, originality confirmation, suggested reviewers,
submission upload — all remain bracketed placeholders.

## Exact filenames

- manuscript/manuscript_blinded.docx/.pdf; manuscript_text.docx/.pdf;
  title_page.docx/.pdf; cover_letter.docx/.pdf; highlights.md/.docx;
  supplement/supplement.docx/.pdf;
  manuscript/pricing_rare_events_economic_modelling_submission.zip;
  tables/main_tables_editable.docx, tables/supplementary_tables_editable.docx;
  figures (PDF+PNG+PPTX);
  docs/HOSTILE_REVIEW_RESPONSE_LOG.md;
  docs/ECONOMIC_MODELLING_CITATION_ECOLOGY.md;
  docs/SELECTION_RATIO_DERIVATION.md (generalized);
  docs/CLOSEST_PRIOR_STUDIES.md (coverage matrix appended);
  docs/FINAL_HOSTILE_REVIEW_REPORT.md.
