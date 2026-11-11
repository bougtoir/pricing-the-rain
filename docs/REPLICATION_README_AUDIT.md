# Replication README audit

Date: 2026-10-18. Every substantive claim in the root `README.md` verified
against repository evidence.

| README statement/topic | Source of truth | Status | Unresolved |
|---|---|---|---|
| Title, author, repo URL | manuscript title page; `CITATION.cff`; git remote | VERIFIED | — |
| Two computational components (generic simulation; weather benchmark) | `run_all.py` PIPELINE; manuscript §4–§6 | VERIFIED | — |
| Model-overlay scope of WTP/quote/reputation | manuscript §5/§6.5 layer separation | VERIFIED | — |
| External data = ERA5 via Open-Meteo interface; underlying product ERA5 (C3S), 1991–2020, 8 locations, `precipitation_sum` | `data/raw/acquisition_ledger.csv` (8 rows; request URLs with `models=era5`); `src/acquire_weather.py` | VERIFIED | — |
| ERA5-Land snapshots excluded (all-null) | `data/raw/invalid_acquisition_ledger.csv` (8 rows, `excluded: all precipitation values null`) | VERIFIED | — |
| Crossref records 28 | `data/raw/literature_acquisition_ledger.csv`; `manuscript_metrics.json` refs=28 | VERIFIED | — |
| Archived snapshots suffice for offline reproduction | `run_all.py --validate-only` verified 64 raw records; acquire scripts skip existing files | VERIFIED | — |
| MIT license (code + author data) | `LICENSE`, `CITATION.cff` | VERIFIED | — |
| Redistribution statement for ERA5 | ledger `license` column: "Copernicus C3S data via Open-Meteo; attribution required" | VERIFIED (documented) | AUTHOR CONFIRMATION REQUIRED line retained in README §4 as instructed for the legal certification |
| Python 3.10 / pinned requirements | `requirements.txt`; runtime interpreter 3.10.12 | VERIFIED | — |
| LibreOffice only for PDF rendering | `Makefile`; `build_manuscript.convert_to_pdf` | VERIFIED | — |
| Seeds 20260924 / 20261012 / 20260925 / 20260924 | `config/simulation.yml`, `config/general_simulation.yml`, `analysis/robustness.py` L186, `src/weather_analysis.py` L192 | VERIFIED | — |
| SeedSequence-spawn determinism, no parallelism | `simulation/run_simulation.py` L438–451; `simulation/general_rare_event.py` L594–640 | VERIFIED | — |
| Runtime/memory/storage figures | `docs/REPRODUCIBILITY.md` (validated 2 vCPU / 7.8 GiB); `du` ≈0.5 GiB working tree | VERIFIED (order-of-magnitude, as stated) | — |
| Program map / pipeline order | `run_all.py` PIPELINE literal | VERIFIED | — |
| `make reproduce/validate/test/acquire` commands | `Makefile` targets; `run_all.py --validate-only` run this pass (exit 0, ~1.4 s validate+tests) | VERIFIED | — |
| Table/figure/in-text mapping (Tables 1–4, S1–S10, figs, tokens) | `tables/` listing; `analysis/out/`; token-resolution logic in `build_manuscript.py`; `docs/QREF_NUMERIC_HARDCODE_AUDIT.md` | VERIFIED | — |
| ERA5 data citation (Hersbach et al. 2020, DOI 10.1002/qj.3803) | journal citation; recorded here as provenance | VERIFIED | — |
| Reproduction test | `run_all.py --validate-only` + pytest 25/25 + `analysis/final_audit.py` PASS on frozen outputs; full scientific rerun deliberately skipped (results frozen; Monte Carlo stages unchanged since last validated full run — recorded in `docs/REPRODUCIBILITY.md`) | VERIFIED | — |
| Template-placeholder grep (`INSTRUCTIONS`, `Example:`, `CEPR`, `IPUMS`, `WVS`, `Census`, `Stata`, `Matlab`, `ArcGIS`, `choose one`, `CURRENT YEAR`, `☐`) | grep over final README.md | PASS — zero residual | — |

One author-only item remains: the README §4 legal certification line for
ERA5 snapshot redistribution (per the prompt's AUTHOR CONFIRMATION
mechanism).
