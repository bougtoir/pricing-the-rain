# Data provenance

This ledger is updated by the acquisition pipeline. Analytical public inputs are stored
as files, never only as URLs or in memory. Audit sources whose redistribution rights
are unclear remain in persistent private provenance storage and are represented in the
public package by acquisition instructions, sizes, and checksums.

## Journal requirements

- Source: Elsevier/ScienceDirect *Ecological Economics* Guide for Authors
- URL: https://www.sciencedirect.com/journal/ecological-economics/publish/guide-for-authors
- Retrieved: 2026-09-24 UTC
- Saved: `data/raw/journal/ecological_economics_guide_2026-09-24.txt`
- SHA-256: `7d7be30ed6b3acc56f1c8ed5c2c69d54acc95f7f27061861dfb38dfcbaf76c19`
- Note: direct curl was blocked with HTTP 403; archived text was retrieved through the
  session's web content fetcher. This is a complete captured text extraction of the
  available page content, supplemented by targeted live searches for field constraints.
- Machine-readable record:
  `data/raw/journal_acquisition_ledger.csv`

## Literature metadata

- Source: Crossref REST API
- Existing snapshot: `data/raw/literature/crossref_praying_for_rain.json`
- DOI: 10.1093/qje/qjag026
- Retrieved: 2026-09-24 UTC
- Size: 25,253 bytes
- SHA-256: `a13f3377051c5e3990cf750a42ab62f7d841e25347fd32f4ce8a3e1566792053`
- License: Crossref metadata terms; bibliographic metadata retained for verification.

The complete DOI audit is registered in
`data/raw/literature_acquisition_ledger.csv`; machine-readable citation fields are in
`analysis/reference_metadata.csv`. The institutional PDF for Akong'a (1987), the NBER
working-paper PDF used for full-text comparison, Harvard Dataverse metadata, and the
CC0 bibliography files are registered in
`data/raw/literature_source_ledger.csv`. The Akong'a and NBER PDFs, repository landing
snapshot, and captured publisher-policy files are excluded from public repository
synchronization because redistribution permission was not established. Their public
provenance ledgers retain URLs, sizes, checksums, and status notes. The Dataverse
metadata and bibliography files are redistributable under CC0 1.0.

## Derived manuscript assets

`analysis/build_manuscript_assets.py` reads preserved processed analysis outputs and
generates all numbered tables, Figure 5, editable figure/table packages, and
`results/manuscript_values.json`. No raw weather or literature file is modified by this
step.

`manuscript/build_manuscript.py` reads that JSON bundle, verified reference
configuration, generated tables, and separate figure files. It
creates review and submission manuscript variants, the supplement, highlights,
declarations, title page, cover-letter draft, and upload ZIP without modifying any raw
input. `analysis/final_audit.py` then verifies temporal construction, follow-up,
training-hazard reproduction, cluster counts, simulation identities, Monte Carlo
precision, manuscript limits, and exclusion of raw sources from the upload ZIP.

## Weather

Source: Open-Meteo Historical Weather API, daily precipitation sum, ERA5
reanalysis access layer, eight pre-specified coordinates, 1991-01-01 to 2020-12-31.
Every raw response is stored under `data/raw/weather/`, checksummed, and registered
in `data/raw/acquisition_ledger.csv`.

An initial `era5_land` request produced structurally complete but all-null responses.
They are retained under `data/raw/weather/*_era5_land_1991_2020.json` as a failed-source
audit trail and are never analyzed. The acquisition script now requests `era5` and
validates non-null coverage before accepting a file. The excluded snapshots are
registered in `data/raw/invalid_acquisition_ledger.csv`.

## Reproduction verification

`run_all.py` validates every saved path, byte count, and SHA-256 value in the three
redistributable core acquisition ledgers before analysis begins. It also validates the
two audit-source ledgers when they are present in private provenance storage. It does
not invoke an acquisition script.
After rebuilding, it records package versions and hashes for deterministic processed
and machine-readable outputs in `results/reproduction_manifest.json`. The final
manifest hash is recorded in `FINAL_REPORT.md` after clean reproduction.
