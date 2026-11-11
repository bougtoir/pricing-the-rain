# Final Submission Pass Report — Economic Modelling

Date: 2026-10-13
Source prompt: `Economic_Modelling_FINAL_SUBMISSION_PASS.txt`
Starting hash: a42113eef (`checkpoint-pre-final-submission-a42113eef`) (`checkpoint-pre-final-submission-a42113eef`)
Ending hash: 2aec5c1d7

## Scientific analysis frozen — confirmed

No simulation, rainfall benchmark, estimand, seed, parameter, rarity
regime, learner rule, pricing rule, efficacy grid, or canonical numeric
result was changed in this pass. All changes are presentation/terminology
and package organization. pytest 25/25 and final_audit confirm every
manuscript number still matches the canonical machine-readable results.

## FIX 1 — Cover letter

The generated cover letter previously stated that "a history-dependent
reputation component becomes relatively dominant in the price as objective
expected value shrinks" — attributing the rarity gradient to reputation
alone. Corrected in the generator (`build_manuscript.py`) to the
two-channel statement: the relative composition of the quote changes with
rarity through a nonlinear probability-transformation term (quantitatively
the larger share in the simulated regimes) and a history-dependent
reputation term; reputation's distinct contribution is the stock–flow
decoupling between premia and contemporaneous performance.

## FIX 2 — Abstract

The abstract previously closed the distortion sentence with
"—history-dependent components become relatively dominant, not larger in
absolute terms." Replaced by: "through two channels that do not scale with
that benchmark—nonlinear probability transformation, the quantitatively
larger component in the simulated regimes, and additive reputation—while
the absolute deviation stays flat. Reputation's distinct role is a
history-dependent stock that decouples modeled quotes from current
performance." Abstract remains 234 words (≤ 250 limit).

## FIX 3 — Missing audit/revision reports added to the package

The submission ZIP now includes, and its README correctly indexes:
- `PRICE_DECOMPOSITION_FINAL_AUDIT.md` (frozen decomposition, component
  shares, finite-regime dominance, Prelec asymptotics, reputation role)
- `FINAL_DECOMPOSITION_REVISION_REPORT.md` (starting/ending hashes,
  corrections, interpretations, build results, filenames)
- `SELECTION_RATIO_DERIVATION.md`, `CRITICAL_REVIEW_RESPONSE_LOG.md`,
  `FINAL_CRITICAL_REVIEW_REVISION_REPORT.md`,
  `FINAL_SUBMISSION_PASS_REPORT.md`

Superseded finals (`FINAL_TARGETED_REVISION_REPORT`,
`FINAL_ECONOMIC_MODELLING_FINISHING_REPORT`,
`FINAL_CRITICAL_REVIEW_REVISION_REPORT`, plus the archived generalization
report) carry a "SUPERSEDED — retained only for provenance" header; the
README states which reports are current.

## Component-share interpretation (frozen)

Transformed-frequency share of D_rel(Model D): endogenous 91.5% → 81.9%
(common → very rare); exogenous 67.9% → 59.6%. The probability component
is dominant in every finite regime; the reputation share rises with rarity
but never overtakes it. Both relative terms are asymptotically unbounded
(Lemma 2 for the Prelec term; the reputation term whenever R does not
vanish proportionally with p). Absolute deviation D_EV stays flat.

## Terminology audit (global grep)

Across manuscript, abstract, highlights, cover letter, supplement, figure
and table captions, README, compliance checklist, and current reports:
- "price-implied index" used for the fourth layer; no probability
  attribution outside [0,1];
- "model-implied quote"/modeled price used where no market clearing is
  modeled;
- benchmark labeled "known-zero(-effect) environmental benchmark"/
  "real-weather benchmark"/"negative-control benchmark" — no residual
  "validation" or "placebo arm" wording;
- equivalence limited to "mean-performance" / first-moment;
- selection ratio flagged as parameter-specific (≈1.71), not universal;
- relative vs absolute price distortion distinguished throughout;
- no claim that rarity amplifies the selection ratio, that reputation is
  the sole/dominant driver, or that actual people/markets follow the
  simulated pricing rule.

## P2c / Discussion / Conclusion check

P2c states both non-scaling mechanisms with explicit conditions and cites
Lemma 2 (Prelec divergence) and Lemma 1 (selection-ratio invariance).
Discussion and Conclusion carry the three-way split (selection /
transformation / reputation), keep the negative result (rarity does not
amplify the absolute selection gap), and make none of the prohibited
claims (common-event closeness, rising equivalent efficacy, full
observational equivalence, welfare loss, benchmark-as-validation).

## Journal compliance (live rules)

Elsevier guide for authors re-verified 2026-10-13: research article;
abstract ≤ 250 (234); 1–7 keywords (5); 3–5 highlights ≤ 85 chars (5,
max 64); double-anonymized review (blinded manuscript + separate title
page); no mandatory APC; declarations present with author placeholders.

## Title

"Pricing Rare Events under Endogenous Observation: Selection, Reputation,
and a Zero-Effect Environmental Benchmark"

## Build/test results

- Clean build from frozen outputs: manuscript 5,880 words, abstract 245.
- pytest: 25/25 passed.
- final_audit: PASS (numerical traceability; every manuscript number
  matches the machine-readable registry).
- Reproduction manifest regenerated (45 output hashes).
- Public repository: synced to bougtoir/pricing-the-rain via the
  sync-to-repos workflow on push.

## Unresolved author-only actions

Identity/affiliation/ORCID, acknowledgements, funding, competing
interests, CRediT roles, originality/exclusive-submission confirmation,
suggested reviewers, open-access choice, final Editorial Manager upload
(see AUTHOR_ACTIONS_REQUIRED.md).

## Final filenames

- `manuscript/manuscript_blinded.docx` / `.pdf`
- `manuscript/manuscript_text.docx` / `.pdf`
- `manuscript/title_page.docx`
- `manuscript/cover_letter.docx` / `.pdf`
- `manuscript/highlights.md`
- `manuscript/declarations.md`
- `supplement/supplement.docx` / `.pdf`
- `figures/figures_editable.pptx`, `figures/figure*.{pdf,png}`
- `tables/main_tables_editable.docx`, `tables/supplementary_tables_editable.docx`,
  `tables/*.csv`
- `manuscript/pricing_rare_events_economic_modelling_submission.zip`
- `docs/PRICE_DECOMPOSITION_FINAL_AUDIT.md`,
  `docs/FINAL_DECOMPOSITION_REVISION_REPORT.md`,
  `docs/FINAL_SUBMISSION_PASS_REPORT.md`
