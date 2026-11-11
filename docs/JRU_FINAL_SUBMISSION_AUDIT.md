# JRU Final Submission Audit

Target: *Journal of Risk and Uncertainty* (Springer), original research article.
Guidelines snapshot: `data/raw/journal/jru_*_2026-11-09.txt` (ledger:
`data/raw/journal_acquisition_ledger.csv`).

Verdict: **scientific, reproducibility and package gates PASS; submission is
blocked only by the author-supplied items in `AUTHOR_ACTIONS_REQUIRED.md`.**

## Scientific correction (see `JRU_LOOKAHEAD_CORRECTION_AUDIT.md`)

- Look-ahead leakage in the generic simulation fixed (commit `0c926a8ab`):
  learner states, provider reputation and Model B–D quotes at period t use
  information through t−1 only. Model B and the naive learner use the raw
  experienced frequency; the Bayesian learner is kept as a separate
  subjective-learning variant.
- B_subj and B_price are objective-relative throughout text, tables, figures
  and Online Resource 1; adjacent-layer increments are not labelled B.
- Formal rerun with unchanged seed (20261012), replications (2000),
  equivalence replications (1500), horizon, burn-in, providers and parameter
  grid. Pre-fix outputs preserved in `results/archive/pre_lookahead_fix_837387d/`.
- Before/after comparison: `results/lookahead_correction_diff_summary.csv`
  (232 rows) and `results/lookahead_correction_diff_equivalent_efficacy.csv`.
  Main claims unchanged; the Model-D price–success difference and the common
  regime reputation–hazard correlation decrease and the text reports the
  corrected values.
- No new hypotheses, parameter changes or exploratory analyses were added.

## Gates

| Gate | Evidence | Status |
|---|---|---|
| JRU guidelines and compliance | `JRU_COMPLIANCE_CHECKLIST.md` | PASS |
| Closest prior studies / novelty | `JRU_CLOSEST_PRIOR_STUDIES_MATRIX.md`, `JRU_NOVELTY_GATE.md` (adequate incremental novelty; no "first" claims) | PASS |
| Retitle, abstract, citation ecology | `JRU_RETARGETING_REPORT.md`, `JRU_CITATION_ECOLOGY.md` | PASS |
| Semantic code audit | `JRU_SEMANTIC_CODE_AUDIT.md` | PASS |
| Independent synthetic / hand-calculation tests | `tests/test_lookahead.py`, `tests/test_hand_calculations.py` | PASS |
| Code ↔ manuscript crosswalk | `JRU_CODE_MANUSCRIPT_CROSSWALK.md` | PASS |
| Numeric hard-code audit (Category F = 0) | `JRU_NUMERIC_HARDCODE_AUDIT.md`; `analysis/final_audit.py` checks rendered config constants | PASS |
| Result traceability | `JRU_RESULT_TRACEABILITY.md` (80 tokens) | PASS |
| Data–text–figure consistency | `JRU_DATA_TEXT_FIGURE_CONSISTENCY.md` (139 checks, 0 failed) | PASS |
| Visual inspection | Figures 6 and 8 re-inspected; legend overlap fixed | PASS |
| Citation existence / claim support | `JRU_CITATION_AUDIT.md` (37 references, DOIs verified against archived metadata) | PASS |
| Hostile review and editor gate | `JRU_HOSTILE_REVIEW_REPORT.md` | PASS |
| Clean public reproduction | `JRU_PUBLIC_REPRODUCIBILITY_AUDIT.md` (clean clone of the ERA5-free mirror, ERA5 re-acquired from Open-Meteo; 47/47 output hashes identical) | PASS |
| Full test suite | `pytest`: 33 passed | PASS |
| Secret scan | pattern scan of all changed files: no hits | PASS |

## Package (`manuscript/pricing_rare_events_jru_submission.zip`)

- Blinded manuscript (DOCX/PDF, 38 pages), separate title page, cover letter,
  Statements and Declarations, Online Resource 1, figure files, editable
  figures/tables, replication README.
- Abstract 232 words (limit 150–250); 6 keywords (4–6); JEL D81–D84;
  37 references in author–year style, alphabetical; 8 figures with `Fig. N`
  captions; 4 main and 10 supplementary tables; all cited in the text.
- No raw or restricted source data in the ZIP.

## Open author items (block submission, not the science)

Author names/affiliations/ORCID, acknowledgements, funding, competing
interests, CRediT roles, originality confirmation, generative-AI disclosure
review, open-access route, and
confirmation of the Model D reputation timing. See
`AUTHOR_ACTIONS_REQUIRED.md`.
