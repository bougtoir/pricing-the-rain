# Replication README completion report

- **Starting Git hash:** `895727aa0` (QREF final zip commit)
- **Ending Git hash:** `ba1625155` (content commit; the following metadata-only
  commit records this hash).
- **Template source:** author-supplied `README.docx` (standard social-science
  replication README/guidance), used as structural checklist only; all
  instructional/example content removed.
- **Sections completed:** title/identification, overview, data availability
  and provenance, statement about rights, license for data, summary of
  availability, per-source detail table, dataset list (in detail table +
  program map), computational requirements (software/randomness/resources),
  program map, code license, replicator instructions, detailed flow,
  table/figure/in-text reproduction map, references, acknowledgements.
- **External data documented:** ERA5 daily precipitation via Open-Meteo
  archive API (8 locations, 1991–2020, `precipitation_sum`), Crossref
  metadata for 28 references; ERA5-Land null-response snapshots archived and
  excluded.
- **Redistribution-rights status:** documented legitimate access + reuse
  basis (C3S attribution terms recorded in acquisition ledger); one
  `AUTHOR CONFIRMATION REQUIRED:` line retained in README §4 for the
  redistribution certification, per prompt rules.
- **Data-license status:** MIT for author-generated data/code; C3S
  attribution terms remain controlling for the ERA5 snapshots.
- **Code-license status:** MIT (`LICENSE` at repo root).
- **Software/environment:** Python 3.10, pinned `requirements.txt`, GNU
  Make, LibreOffice for PDF only; `make reproduce` single entry point.
- **PRNG seeds documented:** 20260924 (principal sim + pseudo-events),
  20261012 (generic simulation), 20260925 (robustness/permutation) — all
  read from canonical configs/code, deterministic via `SeedSequence` spawn;
  no parallelism.
- **Runtime/storage:** CPU-bound Monte Carlo; tens of minutes–few hours on
  2 vCPU/7.8 GiB; tree ≈0.5 GiB; RAM <4 GiB sufficient.
- **Program paths:** all verified against `run_all.py` PIPELINE and
  `Makefile`.
- **Table/figure/in-text mapping:** complete — Tables 1–4 + S1–S10, all
  figures, and every in-text number mapped to `results/manuscript_values.json`
  / config (see `QREF_NUMERIC_HARDCODE_AUDIT.md`).
- **Reproduction test:** `run_all.py --validate-only` → 64 raw records
  verified (size+SHA-256), all required outputs present, 25/25 tests pass,
  `final_audit.py` PASS. A stale validator (EM-era keyword/zip-name checks
  in `run_all.py`) was fixed to QREF limits as part of this pass — metadata
  fix only, no scientific change. A full scientific rerun was deliberately
  skipped: results are frozen and the Monte Carlo pipeline was previously
  validated end-to-end (`docs/REPRODUCIBILITY.md`).
- **Template-placeholder grep:** zero residual template/example strings.
- **Unresolved author-only items:** one — ERA5 redistribution
  certification line (README §4).
- **Output filenames:** `README.md`, `README.docx`, `README.pdf` (repo
  root); `docs/REPLICATION_README_AUDIT.md`; this report; replication
  copies embedded in the submission zip under `replication/`;
  `CITATION.cff` title updated to the QREF title.
- **Final verdict: B — README COMPLETE EXCEPT AUTHOR LEGAL
  CONFIRMATION** (the single ERA5 redistribution certification; all
  technical fields populated and verified).
