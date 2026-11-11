# Final Decomposition Revision Report

Date: 2026-10-13
Source prompt: `Economic_Modelling_PRICE_DECOMPOSITION_FINAL_REVISION.txt`
Starting hash: 51a71594f (`checkpoint-pre-decomp-revision-51a71594f`)
Ending hash: 0a8b3f0db
Checkpoint tag: `checkpoint-decomp-revision-0a8b3f0db`

## Numeric outputs changed?

No. All simulation, rainfall, and derived metric outputs are frozen. The only
"new numbers" are arithmetic component shares computed from frozen outputs
(`prob_share_D_reputation`, `rep_share_D_reputation` columns appended to
Table 2) and one analytic derivation (Lemma 2). No parameters, grids,
regimes, seeds, or rainfall results were changed.

## Component shares of D_rel (Model D, frozen outputs)

Endogenous: common 91.5/8.5%, moderately rare 89.9/10.1%, rare 86.7/13.3%,
very rare 81.9/18.1% (probability/reputation share of total).
Exogenous: common 67.9/32.1%, moderately rare 71.7/28.3%, rare 67.4/32.6%,
very rare 59.6/40.4%.

**Finite-regime dominant component:** the transformed-frequency
(probability) component in EVERY simulated regime under both observation
rules.

## Prelec asymptotic result (Lemma 2)

Implemented weighting: w(p) = exp(−(−ln p)^α), α = 0.65.
With L = ln(1/p): w(p)/p = exp(L − L^α) → ∞ and (w(p)−p)/p → ∞ as p → 0
for 0 < α < 1. The transformed-frequency relative term is therefore itself
unbounded; the prior "bounded transformed-frequency part" wording was
removed everywhere. Stated in §3 as Lemma 2 and cited by P2c and §6.2.

## Revised P2c wording

"P2c (Rarity changes the relative composition of modeled prices through
nonlinear transformation and non-scaling reputation)." Conditions: price
P = αŵV + γR; relative deviation = (ŵ−p)/p + γR/(αpV); first term
diverges under assumed Prelec weighting (Lemma 2); second diverges provided
R does not vanish proportionally with p. Table 1 basis cites both
components and the finite-regime dominance of the transformed term.

## Final role of reputation

Not the majority of the rarity gradient. Its distinct results: history
dependence, stock–flow decoupling, sustained quote premia under weak current
performance, weak/zero/negative contemporaneous quote–success differences,
and making the price-implied index a non-probability composite.

## Final role of rarity

Selection (A) is general and rarity-invariant in ratio (Lemma 1); rarity
shrinks the absolute selection gap proportionally. Rarity's specific
contribution is relative scaling: both the nonlinear transformation term
(B) and the additive reputation term (C) grow relative to the shrinking
objective-EV benchmark, changing the composition of the price signal.
Equivalent efficacy scales downward with the selection gap — the paper no
longer claims equivalence "binds more tightly" or "stays inflated."

## Absolute vs relative distortion

D_EV(Model D) ≈ flat (0.176 → 0.128 endogenous); D_rel rises 1.12 → 11.54.
The rise is a denominator-scaling phenomenon in both non-scaling
components, not growing absolute mispricing; D_EV stays reported beside
D_rel in §6.2 and Table 2.

## Other corrections

- Discussion 7.1: "four layers stay close under common events" removed;
  replaced by the statement that selection is already fully present in the
  common regime (ratio ≈ 1.71, D_rel ≈ 1.12) and rarity changes scaling
  and composition, not existence.
- Equivalence wording aligned to shrinking equivalent efficacies
  (0.072 → 0.022 → 0.0075).
- "Placebo arm" → "known-zero negative-control benchmark"; residual
  "validation" labels in Table 1 → "known-zero benchmark".
- Conclusion: "the signal embedded in a modeled quote is not generally the
  objective risk."
- Figure 4 caption, abstract, cover letter, highlights updated to the
  two-channel, transformation-dominant framing.

## Test/build results

- pytest: 25/25 passed
- final_audit: PASS
- Reproduction manifest regenerated (45 output hashes)
- Manuscript: 5,869 words; abstract 234 words; 25 references; 5 main +
  3 supplement figures; 4 main + supplement tables (Table 2 now carries
  component-share columns)

## Remaining author-only actions

Acknowledgements, funding, competing interests, CRediT roles, author name/
affiliation/contact, suggested reviewers, and author confirmation markers
in declarations and cover letter.

## Final filenames

- `manuscript/manuscript_blinded.docx` / `.pdf`
- `manuscript/manuscript_text.docx` / `.pdf`
- `manuscript/title_page.docx`
- `manuscript/cover_letter.docx` / `.pdf`
- `manuscript/highlights.md`
- `supplement/supplement.docx` / `.pdf`
- `figures/figures_editable.pptx`
- `tables/main_tables_editable.docx`, `tables/supplementary_tables_editable.docx`
- `manuscript/pricing_rare_events_economic_modelling_submission.zip`
- `docs/PRICE_DECOMPOSITION_FINAL_AUDIT.md`
