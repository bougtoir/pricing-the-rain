# JEBO citation / fabrication audit

Date: 2026-10-20. Scope: all 28 references in the final reference list.

## Method

- Every DOI in `REFERENCE_ORDER` is resolved from a local archived
  Crossref snapshot (`data/raw/literature/crossref_*.json`) with a ledger
  row in `data/raw/literature_acquisition_ledger.csv` (URL, retrieval
  UTC, bytes, SHA-256, status).
- Every reference requires its citation token present in the rendered
  manuscript (`REFERENCE_CITE_TOKENS`, enforced at build).
- `apa_sort_key` alphabetizes by first family name + year.

## Results

- 28/28 references resolve to real Crossref records or a documented
  exception: Akong'a (1987) — Crossref record returns HTTP 404; the
  reference is rendered from a verified hand-entered record plus the
  archived repository landing page and PDF in `data/raw/literature/`;
  ledger status "unavailable: HTTP 404" is disclosed.
- Werner & Asch (2005) — Crossref page metadata incomplete; corrected
  manually with page range 1239–1244, verified against the article.
- 2 new JEBO references verified against Crossref snapshots:
  Liu & Sanyal (2012), *JEBO* 84, 1–16, 10.1016/j.jebo.2012.07.006;
  Matsumoto & Spence (2016), *JEBO* 126, 243–254,
  10.1016/j.jebo.2016.03.008. Claim support verified: Liu & Sanyal model
  expert advice under career/reputation concerns (cited for
  adverse-selection/reputation forces in expert advice); Matsumoto &
  Spence show consumers' price beliefs track experienced distributions
  (cited for experience shaping price beliefs).
- 0 fabricated citations; 0 hallucinated DOIs; 0 unsupported "first"
  claims; no mischaracterized prior study found.
- No citation padding: 2 JEBO-anchor candidates (Brandts & Figueras 2003;
  Montero & Sheth 2021) were audited and deliberately NOT added —
  recorded in JEBO_CITATION_ECOLOGY.md.

Status: **PASS**.
