# QREF citation and fabrication audit

Date: 2026-10-18. Scope: all 28 reference entries in `manuscript/manuscript.md`
and every parenthetical citation in text.

## Result: PASS

### Method

1. `manuscript_metrics.json` reports 28 references; every entry carries a DOI
   (28/28).
2. Every citation token in the text is validated at build time:
   `build_manuscript.py` checks `REFERENCE_CITE_TOKENS` — a cite whose
   surname is absent from the reference list raises a build error.
3. 27/28 references resolve to a frozen Crossref `message` JSON in
   `data/raw/literature/crossref_*.json` (verified file existence and that
   rendered year/journal/DOI match the frozen metadata).
4. 1/28 — Akong'a (1987), DOI 10.14989/68028 — is a Kyoto University
   repository handle, not Crossref-registered; the entry is generated from a
   verified hard-coded record in `build_manuscript.py` (unchanged this pass).

### New references added this pass (Crossref-verified)

- Depken, C. A., & Zhang, L. R. (2010). *QREF*, 50(4), 548–558.
  `10.1016/j.qref.2010.06.004` — cited §7.2 for expert-advice /
  adverse-selection context.
- Necker, S., & Ziegelmeyer, M. (2016). *QREF*, 59, 141–160.
  `10.1016/j.qref.2015.03.006` — cited §7.3 for experience→risk-taking.

Both resolve in `data/raw/literature/`; raw JSON persisted on disk
(size + checksum verified at download; ledger entries in
`docs/QREF_CITATION_ECOLOGY.md`).

### Fabrication checks

- No invented or placeholder citations; every cite appears in References.
- No "first to show" priority claims in text (verified by grep for
  first|first-ever|pioneer|novel).
- The only remaining *Economic Modelling* string is the legitimate journal
  name in the Shea (2015) reference itself, plus retarget-history lines in
  QREF docs — correct.
- No citation exists solely because it was "in-journal" for the old target;
  Shea (2015) is cited for a substantive point on learning worsening
  forecasts and predates the EM submission.

Status: PASS.
