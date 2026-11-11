# FINAL RISK ANALYSIS REPORT

Risk Analysis (Wiley) retarget of the Pricing Apparent Environmental Performance
package. Single-VM, strictly sequential execution. Analysis frozen throughout.

## Git checkpoint

- Start commit (before this retarget cycle): `d3f7be7599c6efe03d8dc14376dc729a545ab703`
- End commit: see HEAD of `devin/1791071127-pricing-rain-risk-analysis`
- Branch: `devin/1791071127-pricing-rain-risk-analysis`

## Was the analysis frozen?

Yes. No changes to ERA5/Open-Meteo inputs, the eight locations, the 1991–2010 /
2011–2020 split, pseudo-event construction, thresholds/windows, hazard estimation,
models M0–M5, seeds (20260924/20260925), 10,000 replications per model, WTP/price
calibration, reputation rules, robustness batteries, or the permutation
falsification. Frozen CSVs (`tables/table3_simulation_results.csv`,
`tables/table_s6_accounting.csv`, `results/manuscript_values.json`) contain
identical numeric values; only the M3 row label changed from "Strategic selection"
to "Selective acceptance" (terminology lock, values unchanged). No new diagnostic
was run; none was needed. The decision log (`RISK_ANALYSIS_DECISION_LOG.md`)
records this explicitly.

## Final title and article type

"Apparent Performance under Selective Environmental Risk: Strategic Acceptance and
Reputation under a Zero-Effect Rainfall Null" — Original Research.

- Main text: 4,045 words (limit <7,000, excluding references/tables/figures)
- Abstract: 211 words (limit ≤250, page 2 of the blinded manuscript)
- Keywords: 5 (within 3–5)
- References: 23, APA style, alphabetical, all DOI-verified via CrossRef snapshots
- Figures: 5 (inline placement in the review docx; separate journal-ready
  PDF+PNG in the archive; editable PPTX)
- Main tables: 4; supplementary tables: S1–S6 (editable DOCX)
- Blinded manuscript contains no author names or affiliations; title-only page 1.

## One-sentence contribution

When baseline environmental hazard is heterogeneous and providers select which
cases to accept, raw observed performance can reward favorable risk exposure and
selective acceptance rather than causal performance — demonstrated with a
known-zero-effect rainfall stress test that isolates the mechanism.

## Supported results

- Natural rainfall alone generates substantial apparent success under
  retrospective attribution: 7-day success at 1 mm ranges 0.593 (random) to
  0.853 (high hazard); deficit 0.823, dry-spell 0.601, placebo 0.600 —
  demonstrated with observed weather.
- Selective acceptance on a hazard signal raises apparent success among accepted
  events (M3 > M2) — demonstrated in model using observed weather.
- Reputation is a stock from past attributed outcomes; current performance is a
  hazard-driven flow. M4–M5 sustain price premia (3.568 and 4.610 vs. fixed
  3.000) while contemporaneous price-success differences are negative
  (−2.447, −3.037).
- Within-stratum permutation WTP-success estimate −0.0319 (p ≈ 0.002);
  risk-adjusted WTP 0.0360 (CI −0.0388 to 0.1109) vs. naive 0.1237.

## Not supported (stated as such)

- Positive contemporaneous price-success association (boundary condition; the
  manuscript does not claim it).
- Any real-world treatment effect on rainfall (the intervention is a null by
  construction; claims are bounded to "demonstrated with observed weather" vs.
  "demonstrated in model").

## QJE differentiation

Documented in `docs/QJE_DIFFERENTIATION_AUDIT.md` (Risk Analysis addendum).
Espín-Sánchez, Gil-Guirado, and Ryan establish timing, hazard, persuasion, and
historical foundation; this paper's delta is the performance-evaluation problem:
selective exposure by multiple providers, provider-specific reputation stocks,
attribution, and the stock/flow distinction — not a repackaging of the QJE
result.

## Editor simulation

Likely desk-rejection grounds addressed: (a) "not a risk paper" — reframed around
risk-adjusted performance evaluation under heterogeneous hazard and selective
exposure, with the practical message in §5.4–5.5 (prospective risk adjustment,
rejected-case disclosure for scorecards); (b) fit — see
`docs/RISK_ANALYSIS_FIT_AUDIT.md`; (c) format — Wiley/RISA compliance list in
`docs/RISK_ANALYSIS_COMPLIANCE_CHECKLIST.md`.

## Reviewer simulations (12 challenge questions)

1. *QJE repackaged?* Positioning paragraph §1 and 5.1 state the delta; QJE is
   cited as foundation, not re-derived. PASS.
2. *Rainmaking a gimmick?* The zero-effect null is defended explicitly
   (§1, §3.3, §5.1) as the sharpest identification device: attribution vs.
   treatment cannot otherwise be separated. PASS.
3. *Really risk analysis?* Risk = heterogeneous baseline hazard; the paper is
   about risk adjustment of performance under selective exposure — an
   evaluation-science contribution with a risk-analysis message. Stated in §1
   and §5.4. ARGUABLE but defensible; cover letter makes the case.
4. *Selection bias obvious?* Acknowledged in §5.2; the demonstration quantifies
   how large the distortion is under a known null and links it to scorecards —
   the value is the bounded measurement, not the existence claim.
5. *Value of a zero-effect benchmark?* §5.1/§5.5: only a known null lets
   attribution and selection be separated without identifying assumptions.
6. *Claims too strong?* Boundary-condition table (Table 4) and hedged
   "demonstrated in model using observed weather" phrasing; price-success
   association explicitly not supported.
7. *Calibrated providers?* §3.4, supplement Table S2: only demand/WTP parameters
   are empirically anchored; selection and memory are stress-test machinery —
   stated as such.
8. *WTP distracting?* Demoted to §4.4/§4.6 as one component of the accounting
   chain; the primitive is hazard × acceptance × attribution.
9. *8 locations adequate?* §3.1 frames them as mechanism stress tests, not a
   global sample; regimes contrast deliberately.
10. *Negative price overinterpreted?* §4.5/§5.3 present it as an accounting
    finding (premia coexist with negative contemporaneous association), not a
    policy prescription.
11. *Cultural practices respectful?* §5.5: rainmaking treated as documented
    practice (Akong'a; Pattanayak; Semenya), no mockery; the null is about
    rainfall physics, not belief.
12. *Permutation falsification?* Pre-specified §3.4/§4.6; exploratory WTP
    regression flagged exploratory.

## Audits

- Citation ecology: `docs/RISK_ANALYSIS_CITATION_ECOLOGY.md` (Risk Analysis
  comparator literature added: Shahian & Normand 2008, Werner & Asch 2005,
  Dranove et al. 2003, Heckman 1981, Cox 1955, Barnett et al. 2011, Kreps &
  Wilson 1982, Tversky & Kahneman 1973, Murphy 1993, Skinner 1998, Bikhchandani
  et al. 1998; 5 new DOIs snapshot-archived).
- Numeric traceability: all values injected via `{{TOKEN}}` from
  `results/manuscript_values.json`; build fails on unmapped keys; pytest suite
  (21 tests) passes including APA-reference completeness/alphabetical order,
  figure/table first-citation order, unresolved-token scan, word/abstract limits,
  archive contents, and reproduction-manifest hash match.
- Terminology: "demonstrated with observed weather" vs "demonstrated in model"
  enforced; Table 4 proposition classification kept.
- Causal language: no causal claim on rainfall anywhere; success measures are
  non-causal attribution rules (§2.1 exact zero-effect null).
- DOI verification: 23/23 entries resolved via CrossRef; raw responses archived
  in `data/raw/literature/crossref_*.json` with ledger rows.
- Wiley/RISA compliance: `docs/RISK_ANALYSIS_COMPLIANCE_CHECKLIST.md`
  (double-blind, Original Research, title page separate, abstract ≤250,
  3–5 keywords, APA references, COPE AI disclosure, numbered bold-caps headings
  in the rendered docx, double-spaced TNR, OMML equations: 19 in blinded
  manuscript + 19 in author copy + 1 in supplement, zero residual LaTeX tokens).

## Clean build and public repo

- `run_all.py --validate-only` plus pytest: 21/21 pass on this machine;
  `results/reproduction_manifest.json` regenerated (35 output hashes).
- Reproducibility from the public mirror: acquisition scripts re-fetch ERA5 from
  the Open-Meteo archive with URL/timestamp/SHA-256 ledgers; pinned
  `requirements.txt`; secret scan clean (no credentials in repo). Scientific
  outputs are bit-identical because analysis code/data are unchanged.
- Sync-to-repos: `pricing-the-rain` is mapped in
  `.github/workflows/sync-to-repos.yml`; the pointer update runs on merge to
  master per that workflow.

## Author actions

`AUTHOR_ACTIONS_REQUIRED.md`: author list/affiliations/ORCIDs (title page +
system only), acknowledgements, funding, competing interests, CRediT roles,
exclusive-submission confirmation, AI-disclosure review, Research Exchange
upload decisions.

## Final deliverables (paths)

- `manuscript/manuscript_blinded.docx` / `.pdf` — submission manuscript
- `manuscript/manuscript_text.docx` / `.pdf` / `.md` — author copy (inline
  figures/tables)
- `manuscript/title_page.docx`
- `supplement/supplement.docx` / `.pdf` — supplementary material
- `figures/figure1–5 .pdf/.png` + `figures/figures_editable.pptx`
- `tables/main_tables_editable.docx`, `tables/supplementary_tables_editable.docx`,
  `tables/table*.csv`
- `manuscript/cover_letter.docx` / `.pdf` / `.md`
- `manuscript/pricing_apparent_environmental_performance_submission.zip` —
  submission archive (figures/ + tables/ subfolders, README)
- `docs/RISK_ANALYSIS_{FIT_AUDIT,CITATION_ECOLOGY,COMPLIANCE_CHECKLIST,DECISION_LOG}.md`,
  `docs/QJE_DIFFERENTIATION_AUDIT.md`, `AUTHOR_ACTIONS_REQUIRED.md`
