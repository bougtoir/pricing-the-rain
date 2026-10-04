# FINAL RISK ANALYSIS FINISHING REPORT

Narrow final submission finishing pass on the existing Risk Analysis package.
Single persistent VM, strictly sequential. No scientific revision cycle.

## Git checkpoints

- Starting commit (start of this pass): `ee69ab51b` (tip of
  `devin/1791071127-pricing-rain-risk-analysis` at pass start; retarget work
  began at `d3f7be7599c6efe03d8dc14376dc729a545ab703`)
- Ending commit: HEAD of `devin/1791071127-pricing-rain-risk-analysis` after
  this pass

## Analysis freeze — confirmation

Scientific analysis remained completely frozen. `results/manuscript_values.json`,
`tables/table*.csv`, `results/simulation_replications.csv.gz`, all seeds, models
M0–M5, hazard estimation, thresholds/windows, coefficients, intervals, and the
permutation p-value are bit-identical to the pre-pass state except two figure
caption strings and the M3 display label ("Strategic selection" → "Selective
acceptance") — presentation only. No diagnostic was rerun. No numerical
inconsistency was discovered, so no step was stopped.

## Exact textual edits made

1. `manuscript/build_manuscript.py` — cover letter rewritten as an
   editor-facing argument (~450 words): removed "60,000 principal Monte Carlo
   replications" and result enumeration; kept one numerical pair (0.593 → 0.853
   apparent success) as the sharpening figure; switched to first-person
   singular ("I"/"my"); downgraded safeguard wording to "candidate
   safeguards"; added one paragraph noting staged decomposition and
   robustness/falsification without enumerating numbers; kept the
   stock–flow result, Risk Analysis scope statement, QJE differentiation, and
   restrained practical implication.
2. `manuscript/manuscript_template.md` — safeguard language downgraded from
   prescription to implication:
   - §5.3: "Evaluators should compare … and reputation should be separated"
     → "The findings motivate comparing … and separating reputation".
   - §5.4: "are the relevant safeguards" → "may serve as candidate
     safeguards"; "event studies should estimate …" → "the framework suggests
     estimating …".
   - §6: "Credible performance evaluation … requires prospective risk
     adjustment" → "For credible performance evaluation …, the findings
     motivate prospective risk adjustment".
   A full audit found no other "should/must/will reduce/prevents/corrects/
   solves" applied to untested interventions.
3. `figures/figure1_framework.svg` — title text only:
   "Zero-effect ecological-economic generative framework" → "Zero-effect
   performance-evaluation generative framework"; PDF/PNG regenerated, no data
   change.
4. `manuscript/build_manuscript.py` — archive README and supporting-file
   print string updated (highlights wording removed); FINAL reports added to
   the submission archive.
5. `tests/test_manuscript_outputs.py`, `run_all.py`, `requirements.txt` —
   carried over from the retarget commit (APA checks, 7,000-word limit, pytest
   pin); unchanged this pass.
6. `.github/workflows/sync-to-repos.yml` (repo root) — public-mirror mapping
   repointed from `devin/1790254778-pricing-rain-final-revision` to
   `devin/1791071127-pricing-rain-risk-analysis` for BRANCH_MAP, SUBDIR_MAP,
   and EXCLUDE_MAP (exclusions for `data/raw/journal` and non-redistributable
   literature PDFs preserved).

## Figure-presentation-only changes

Figure 1 title reworded (see above). Figures 2–5 visually inspected at journal
viewing size: panel labels, axes, legends, and captions are readable; no panel
is overloaded; no values differ from frozen results. Vector PDF + 500–600 dpi
PNG exports maintained; editable PPTX maintained.

## Narrative hierarchy audit

Abstract, Introduction, section order, Discussion, Conclusion, and cover letter
keep the primary hierarchy: heterogeneous baseline hazard → selective
exposure/acceptance → raw apparent performance → risk-conditioned
interpretation → reputation dynamics → WTP/price as downstream calibrated/
simulated consequences. WTP/price appears only inside §3.4/§4.4 and one
abstract sentence explicitly labeled "calibrated or simulated, not historical
estimates". The negative result (positive reputation-mediated prices do not
imply a positive contemporaneous price-success association) is preserved in
Abstract, §4.5, §6, and the cover letter.

## Author-only placeholders

All unresolved author-only fields are bracketed `[AUTHOR …]` placeholders in
title_page.docx, declarations.md, cover letter, and the Declarations section,
and are itemized in `AUTHOR_ACTIONS_REQUIRED.md`. No author information was
invented; no known information was replaced.

## Live guidelines status

Wiley author-instructions page remains Cloudflare-blocked to automated access
(HTTP 403, 2026-10-03). The latest retrievable official snapshot is the
2025-08-11 Wayback capture, already archived with ledger entries in
`data/raw/journal/`; `RISK_ANALYSIS_COMPLIANCE_CHECKLIST.md` is built on it.
If the author can open the live page in a browser, a final spot-check of the
checklist items is listed as an optional author action.

## Final title, article type, word count

"Apparent Performance under Selective Environmental Risk: Strategic Acceptance
and Reputation under a Zero-Effect Rainfall Null" — Original Research.
Main text 4,049 words; abstract 211 words; 5 keywords; 23 APA references.

## Public repository status

`bougtoir/pricing-the-rain` exists (default branch `main`, last synced
2026-09-25 under the previous EE mapping). The sync mapping now points at this
branch, so the mirror updates on the next scheduled/manual sync run or on push
to this branch after merge — `data/raw/journal` and non-redistributable
literature remain excluded. Until that run executes, the public repo still
carries the EE-era package; the manuscript's data-availability statement
describes the package contents, not a specific snapshot hash, and remains
true.

## Clean build and traceability

- `PYTHONPATH=. .venv/bin/python analysis/build_manuscript_assets.py` →
  "Built manuscript figures, tables, and machine-readable values" (frozen
  outputs only).
- `PYTHONPATH=. .venv/bin/python manuscript/build_manuscript.py` →
  4,049-word manuscript, blinded DOCX/PDF, supplement, title page, cover
  letter, submission archive.
- `run_all.py --validate-only` → "Reproducibility pipeline completed
  successfully"; `pytest tests -q` → 21/21 pass.
- `results/reproduction_manifest.json` regenerated (35 output hashes).
- Numerical traceability: all manuscript numbers flow from
  `results/manuscript_values.json` `{{TOKEN}}` injection; headline values
  unchanged (87,664 region-days; 2,595 pseudo-events; success 0.593–0.853;
  M3>M2 apparent-success increase; M4/M5 prices 3.568/4.610 vs 3.000;
  price-success −2.447/−3.037; permutation −0.0319, p≈0.002; adjusted WTP
  0.0360 CI −0.0388–0.1109 vs naive 0.1237).

## Word/DOCX QC

TNR body/captions, black text; OMML equations (19 blinded + 19 author + 1
supplement); no stray `**`, no LaTeX tokens, no local paths, no TODO/debug
text; blinded manuscript contains no author identity (the only "Devin" hit is
the required COPE AI-disclosure sentence); title page separate; tables editable;
page breaks: title-only p1, abstract+keywords p2, main text p3.

## Secret/private-data/large-file audit

No credentials in tracked files (grep scan clean); no private personal data;
largest tracked file is the 8.5 MB submission ZIP (acceptable); `.venv` and
`build/` untracked.

## Final handling-editor simulation

Reads primarily as a risk-analysis paper (framing §1, §5.2–5.4); zero-effect
benchmark is explicit in title, abstract, §2.1, §3.3; selective exposure is
separated from causal performance throughout; QJE overlap is bounded in §1 and
§5.1 and in the cover letter; risk-adjustment implications are qualified as
candidate/motivated; WTP/price is subordinate; the stock–flow result is stated
in Abstract, §4.5, §5.3, §6; limitations are a full §5.5; rainmaking is
consistently framed as a stress test. No further corrections needed.

## Unresolved author-only actions

See `AUTHOR_ACTIONS_REQUIRED.md`: author names/affiliations/ORCIDs,
acknowledgements, funding, competing interests, CRediT roles, exclusive-
submission confirmation, AI-disclosure confirmation, Research Exchange upload
(wiley.atyponrex.com/journal/RISA), suggested reviewers, OA decision.

## Exact final submission filenames

- `manuscript/manuscript_blinded.docx`, `manuscript/manuscript_blinded.pdf`
- `manuscript/manuscript_text.docx`, `manuscript/manuscript_text.pdf`
- `manuscript/title_page.docx`
- `supplement/supplement.docx`, `supplement/supplement.pdf`
- `manuscript/cover_letter.docx`, `manuscript/cover_letter.pdf`,
  `manuscript/cover_letter.md`
- `manuscript/declarations.md`
- `figures/figure{1..5}_*.{pdf,png}`, `figures/figure1_framework.svg`,
  `figures/figures_editable.pptx`
- `tables/main_tables_editable.docx`, `tables/supplementary_tables_editable.docx`,
  `tables/table1_study_locations.csv`, `table2_pseudo_event_results.csv`,
  `table3_simulation_results.csv`, `table4_hypothesis_classification.csv`
- `docs/RISK_ANALYSIS_COMPLIANCE_CHECKLIST.md`, `AUTHOR_ACTIONS_REQUIRED.md`,
  `docs/FINAL_RISK_ANALYSIS_REPORT.md`, `docs/FINAL_RISK_ANALYSIS_FINISHING_REPORT.md`
- `manuscript/pricing_apparent_environmental_performance_submission.zip`
