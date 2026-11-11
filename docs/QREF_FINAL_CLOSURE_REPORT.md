# QREF final closure report

Closure pass only; no scientific revision cycle. All analyses, numbers,
figures, tables, and theory remained frozen.

- **Starting hash:** `8ec945400` ("Retarget manuscript to QREF + adversarial
  review and numeric hard-code audit").
- **Ending hash:** `ddf9a4ca9` (content-final checkpoint; the metadata-only
  hash-insert commit after it is the definitive branch tip).
- **Conclusion correction (Fix 1):** the over-broad sentence "the simulation
  demonstrates that endogenous selection inflates experienced frequencies by
  a selection ratio that is analytically independent of rarity" was replaced
  by the calibration-scoped form: "under the positive risk–observation
  covariance calibration used here, endogenous selection inflates
  experienced frequencies by a selection ratio that is analytically
  independent of baseline rarity under multiplicative scaling". A
  manuscript-wide grep found two further unscoped inflation statements —
  the §7.1 sign-paragraph ("Under rare events, endogenous selection
  inflates the experienced layer") and the §7.3 prediction "(a)
  experienced-frequency inflation concentrated in the observation-selected
  segment" — both now carry the positive-covariance qualifier (with the
  negative-covariance deflation noted). Statements already scoped
  (identity sign paragraph, domain-conditional deflation, cover letter,
  abstract) were left unchanged.
- **No scientific number changed:** confirmed; no token value, config,
  result file, figure, or table was altered.
- **Hard-code re-audit:** PASS; suspicious hard-coded scientific result
  count: **0** (details in `QREF_NUMERIC_HARDCODE_AUDIT.md`; config prose
  literals auto-validated by `analysis/final_audit.py`).
- **Data–text–figure consistency:** PASS — no Economic Modelling-era
  output, no superseded title, no stale caption or wording; the only
  "Economic Modelling" strings remaining are the legitimate journal name
  in the Shea (2015) reference and retarget-history lines in QREF docs.
- **Citation audit:** PASS — 28/28 DOI-verified; no invented cites; no
  fit-only cite without substantive relevance; no "first" claims.
- **Build/tests/traceability:** clean rebuild of all DOCX/PDF assets and
  the submission ZIP; `pytest tests/` 25/25; `final_audit.py` passed;
  `results/reproduction_manifest.json` regenerated (re-hash only).
- **Final title:** "Rare-Event Quote Formation under Endogenous
  Observation: Selection, Subjective Beliefs, and Reputation".
- **Word counts:** main text 6,467 words (excluding references);
  abstract 248 words.
- **Unresolved author-only actions:** author name/affiliation/ORCID on
  the title page; Editorial Manager submission incl. the US$150
  non-refundable fee; suggested reviewers; Elsevier form answers
  (see `AUTHOR_ACTIONS_REQUIRED.md`).
- **Final editorial verdict (Phase 8 gate):** (1) clearly an economics
  paper — yes; (2) generalized selection statement internally
  consistent everywhere — yes after Fix 1; (3) quote formation described
  as reduced-form — yes; (4) real-weather results correctly scoped — yes;
  (5) identification claims limited — yes; (6) residual fit concern —
  none beyond the administrative fee; (7) unresolved scientific reason —
  none. **Verdict: SUBMIT TO QREF.**
- **Final filenames:** `manuscript/manuscript.md`,
  `manuscript_blinded.{docx,pdf}`, `manuscript_text.{docx,pdf}`,
  `title_page.docx`, `cover_letter.{md,docx,pdf}`, `declarations.md`,
  `highlights.md`, `tables_editable.docx`,
  `supplement/supplement.{md,docx,pdf}`, `supplement/tables_editable.docx`,
  `analysis/out/fig*.png` + `fig*_editable.pptx`,
  `manuscript/pricing_rare_events_qref_submission.zip`, and the seven
  `docs/QREF_*` reports.
