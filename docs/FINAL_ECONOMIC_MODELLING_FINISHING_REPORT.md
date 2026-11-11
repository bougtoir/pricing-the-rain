> SUPERSEDED — retained only for provenance. Current final reports: FINAL_DECOMPOSITION_REVISION_REPORT.md, PRICE_DECOMPOSITION_FINAL_AUDIT.md, FINAL_SUBMISSION_PASS_REPORT.md.

# FINAL finishing-pass report — Economic Modelling

- Starting Git hash: `9b602f4da` (tag `checkpoint-pre-finishing-pass-9b602f4da`)
- Ending Git hash: `64a3dc3c0` (tag `checkpoint-finishing-pass-64a3dc3c0`)
- Frozen analyses: generic simulation outputs, matched p_ref definitions,
  exogenous benchmark, distortion metrics, decomposition, observational
  equivalence, rainfall validation, all seeds/MC outputs — unchanged. Only
  text, terminology, packaging, and document regeneration were touched.

## The five consistency fixes

1. **Four-layer coincidence claim (intro).** "These four quantities coincide
   under dense, exogenous observation" → under exogenous observation the
   objective and experienced layers coincide in expectation on the same
   support; subjective transformation and reputation can still separate the
   later layers; endogenous observation adds a composition gap.
2. **Table 1 / proposition terminology.** P1 basis changed from
   "B_exp > 0 under endogenous observation" to
   "selection_gap > 0 under endogenous observation". Residual "experienced-
   frequency bias" phrasings recast as selection/composition gap or matched
   record bias as appropriate; the three-way distinction (selection gap,
   same-support record bias, total objective-to-experienced difference) is
   preserved.
3. **P6 observational-equivalence claim.** "bounded below by apparent
   performance under positive efficacy" → "can reproduce, and in some
   regimes exceed"; regime-dependence stated (common regime has no solution
   in the scanned grid, disclosed in §6.4); intro and abstract calibrated to
   "in the simulated rare regimes". Machine-readable inverse solution
   retained in results/general_equivalent_efficacy.csv.
4. **Identification language.** "requires at least one of…" / "requires
   case-mix disclosure…" downgraded to "can be aided by additional
   information such as rejected-case disclosure, exogenous observation,
   pre-event risk information, or known-zero benchmarks … other
   identification strategies may also be possible" (Discussion, Conclusion,
   cover letter, highlights). Within-framework bounds (P6, §6.4) keep their
   force.
5. **Superseded report cleanup.** `FINAL_GENERALIZATION_REPORT.md` renamed
   to `docs/ARCHIVED_PRE_TARGETED_REVISION_REPORT.md` with a prominent
   SUPERSEDED header; zip manifest, README, and references updated. The one
   clearly current final scientific report is
   `FINAL_TARGETED_REVISION_REPORT.md` (this file is the finishing-pass
   administrative record).

Additional label/terminology QC: figure captions ("diverges" → "grows"),
supplement "price-layer divergence" → "separation", P2c given an explicit
maintained assumption for the unbounded reputation term, §6.2 "diverges from
every probability layer" → "separates".

## Cover-letter changes

- "the four objects diverge systematically as events become rarer" → "the
  layers separate for different reasons: endogenous selection changes the
  experienced case mix, nonlinear transformation alters subjective
  probability, and reputation loads price with history-dependent
  information".
- "diverges by more than an order of magnitude" → "rises more than tenfold
  across the simulated rarity regimes".
- Reproducibility sentence → "All code, acquisition records, checksums,
  machine-readable results, and reproducibility materials are available
  through the accompanying public repository…".
- Practical implication softened to "without additional information such as
  rejected-case disclosure, exogenous observation, or a known-zero
  benchmark".

## Final title

"Pricing Rare Events under Biased Experienced Frequencies: A General
Framework with a Zero-Effect Environmental Validation"

## Word count / formats

Main text 4,703 words (limit 8,000); abstract 245 words (≤250); 5 keywords;
31 references; 8 figures; 6 main + 8 supplement tables; highlights 5 items,
max 72 chars.

## Current probability-layer interpretation

Objective p_t (time-weighted), matched objective on observed support
p_ref = E[p_t|O=1], experienced p_exp, transformed subjective, and
price-implied layers. Under exogenous observation objective and experienced
layers coincide in expectation on the same support; endogenous observation
adds a selection/composition gap.

## Final rarity interpretation

The selection ratio is approximately stable (≈1.71) across all simulated
rarity regimes; the absolute selection gap shrinks with p. Rarity amplifies
relative price distortion because non-scaling components (additive
reputation stock, history dependence) do not shrink with objective expected
value — not because frequency bias grows. The prior
"rarity-amplifies-bias" story appears nowhere in the package except in
clearly labeled negative-result/archival context.

## Final observational-equivalence wording

"Endogenous selection under zero efficacy can reproduce, and in some
regimes exceed, the apparent performance generated by positive efficacy
under exogenous observation" — regime-dependent, not universal; explicit
inverse-interpolation solution with MCSE bounds in
results/general_equivalent_efficacy.csv.

## Clean build / traceability

Build: `python analysis/build_manuscript_assets.py` then
`python manuscript/build_manuscript.py` on frozen outputs — succeeded.
`pytest tests/` 25/25 pass; `analysis/final_audit.py` passes
(results/final_audit.json); reproduction manifest regenerated (45 output
hashes); all manuscript values are injected from
results/manuscript_values.json — no manual numbers.

## Public-repository status

Branch `devin/1791802000-pricing-rain-generalization` (PR #666 to
bougtoir/wip); sync-to-repos mirrors to bougtoir/pricing-the-rain. The only
CI failure is a pre-existing `workflow`-scope PAT limitation on an
unrelated branch (summary-codec); the pricing-the-rain sync succeeds.

## Unresolved author-only actions

Affiliation/contact details, funding, competing interests, CRediT roles,
acknowledgements, originality confirmation, suggested reviewers — all listed
in `AUTHOR_ACTIONS_REQUIRED.md` and kept as bracketed placeholders.

## Final filenames

manuscript_blinded.docx/.pdf, manuscript_text.docx/.pdf, title_page.docx,
cover_letter.docx/.pdf, declarations.md, highlights.md,
supplement.docx/.pdf, figures/figure{1,2,3,4,5,6,7,8}_*.{pdf,png},
figures_editable.pptx, tables/*_editable.docx, tables/table{1..6}_*.csv,
submission archive `pricing_rare_events_economic_modelling_submission.zip`.
