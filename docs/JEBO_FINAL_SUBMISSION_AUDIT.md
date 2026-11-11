# JEBO final submission audit

Date: 2026-10-20. Final editor-gate record for the JEBO retargeting
phases (QREF-final baseline `df3ace91d`, safety tag
`jebo-retarget-baseline`).

## Git range

- Start: `df3ace91d` (QREF-final, parent of this work).
- End: the JEBO checkpoint commit on
  `devin/1791802000-pricing-rain-generalization` (this branch, PR
  https://github.com/bougtoir/wip/pull/666).

## Compliance / checklist gate

PASS — `docs/JEBO_COMPLIANCE_CHECKLIST.md`: 31/31 explicit conditions
satisfied with file/line evidence; remaining open items are
AUTHOR CONFIRMATION REQUIRED entries only, disclosed in
`AUTHOR_ACTIONS_REQUIRED.md` (incl. US$175 submission fee, paid by the
author at submission; ERA5 redistribution legal confirmation).

## Citation ecology audit

PASS — `docs/JEBO_CITATION_ECOLOGY.md`: 10 closest prior studies
surveyed; JEBO-readership positioning table; 2 JEBO citations added and
verified (Liu & Sanyal 2012; Matsumoto & Spence 2016); 2 padding
candidates deliberately excluded; all 28 references real.

## Hostile review (4 reviewers + editor)

PASS — `docs/JEBO_HOSTILE_REVIEW_REPORT.md`: simulation of a skeptical
executive editor, a behavioral-economics referee, an
econometrics/computation referee, and a domain/referee for advisory
markets. Distinguishes reader-fit critiques (addressed by reframing)
from genuine defects (none found; no silent recompute). Repairs made
inside the existing layer structure only.

## Numeric hardcode audit

PASS — `docs/JEBO_NUMERIC_HARDCODE_AUDIT.md`: category F (hardcoded
manuscript-facing result values) = 0. All display numbers flow through
`results/manuscript_values.json` {{TOKEN}} rendering or canonical-CSV
table builders.

## Public reproducibility audit

PASS (HARD GATE) — `docs/JEBO_PUBLIC_REPRODUCIBILITY_AUDIT.md`: public
mirror self-contained; 66 archived raw-input records validated;
ledgers + SHA-256 complete; no missing code/config/ledger/checksum; no
private-path or secret dependency; all non-redistributable items
disclosed as author-confirmation items, not guessed.

## Clean reproduction test

YES — sequential `run_all.py` executed 2026-10-20 end-to-end on the
persistent VM (fresh `requirements.txt` venv): 87,664 region-days →
2,595 pseudo-events → 60,000 principal simulations → 8-cell generic
rare-event simulation (common / moderately rare / rare / very rare ×
exogenous / endogenous) → figures/tables/values registry → manuscript
package → final audit. Canonical outputs regenerated identical to the
audited values; `results/reproduction_manifest.json` refreshed.

## Traceability audit

PASS — `docs/JEBO_RESULT_TRACEABILITY.md`: every display table, figure,
supplement item, and major in-text number mapped to generating script,
canonical input, canonical result, and manuscript use.

## Data–text–figure consistency audit

PASS (HARD GATE) — `docs/JEBO_DATA_TEXT_FIGURE_CONSISTENCY.md`: zero
unresolved inconsistencies; no stale QREF-era artifacts; signs,
denominators, rounding consistent; reference list ↔ in-text citations
enforced by build.

## Visual figure/table inspection

PASS — five main figures + supplementary figures inspected in the built
DOCX/PDF: legible, correctly labeled, captions correct, citation order
correct, table alignment correct, no truncation.

## Citation / fabrication audit

PASS — `docs/JEBO_CITATION_AUDIT.md`: 28/28 verified (2 documented
exceptions, both disclosed); 0 fabricated; 0 hallucinated DOIs; no
unsupported first claims.

## Cover letter

PASS — JEBO-specific single-author letter (first-person "I"), generated
by `manuscript/build_manuscript.py` from canonical metadata; includes
the required JEBO framing (organizational/economic-behavior relevance,
fit with the journal's behavioral and institutional readership).

## Scientific freeze

PASS — no seeds, rarity regimes, efficacy grid, Prelec α, transition
parameters, locations, weather windows, event rules, thresholds, or
quote parameters changed. Selection ratio 1.708–1.713 (analytic
1.7115), D_rel 1.122→11.538, equivalent efficacy 0.072/0.022/0.0075,
87,664 region-days, 2,595 pseudo-events, apparent success 0.853,
placebo 0.600, random 0.593 all preserved. No genuine defect found;
no silent recompute of canonical results.

## Reproduction YES/NO summary

- Commands execute: YES
- Manifest/ledger files exist: YES
- Canonical results reproduce: YES
- Manuscript package builds from clean state: YES
- Tests pass: YES (25/25 after manifest refresh)
- Final audit PASS: YES
- Missing private artifact: NO
- Missing public raw artifact: NO
- Missing ledger entry: NO
- Missing checksum: NO
- Unverified citation: NO
- Unresolved hostile-review defect: NO

## Recommendation

**SUBMIT TO JEBO** — all hard gates pass; open items are disclosed
author-confirmation entries only (US$175 submission fee — author pays at
submission; ERA5 redistribution legal confirmation; bracketed author
fields to fill in Editorial Manager).
