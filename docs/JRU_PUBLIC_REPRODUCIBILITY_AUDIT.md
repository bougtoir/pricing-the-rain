# JRU Public Reproducibility Audit

Verdict: **PASS.** A clean clone of the public mirror, which does not
contain ERA5, reproduces every canonical output. It uses public code and
ERA5 re-acquired from the public Open-Meteo archive API.

## Data policy

ERA5 is not redistributed (author decision, 2026-11-11). The public mirror
excludes `data/raw/weather/` and two derived files that contain the daily
rainfall values: `data/processed/daily_weather_features.csv.gz` and
`analysis/pseudo_events.csv`. The exclusions are listed in
`config/public_mirror_exclusions.txt` and in the `EXCLUDE_MAP` of
`.github/workflows/sync-to-repos.yml`. The private working repository keeps
the original snapshots and their ledger.

## Procedure

1. `git clone https://github.com/bougtoir/pricing-the-rain.git` into a fresh
   directory (mirror commit `f6982ca`). The tree has no `data/raw/weather/`,
   no `data/processed/`, and no `analysis/pseudo_events.csv`.
2. `make reproduce` ran on 2026-11-11, 05:33Z–06:27Z, on a 2-core VM. It
   created a fresh `.venv` from `requirements.txt`. Because the snapshots
   were absent, it ran `src/acquire_weather.py`, which retrieved the 8 ERA5
   series from Open-Meteo using the request parameters in
   `data/raw/acquisition_ledger.csv` and passed the completeness check. It
   then ran `run_all.py`.
3. The pipeline validated 61 raw-input ledger records by size and SHA-256.
   It reported the files listed in `config/public_mirror_exclusions.txt` as
   not redistributed: the ERA5-Land responses (all-null, unused), journal
   guideline pages, and two literature full texts.
4. The pipeline ran every step, including the generic rare-event simulation
   in its formal configuration (3128 s), the manuscript package, the final
   audit, and the test suite (33 passed).

## Result

- All 47 hashed outputs in `results/reproduction_manifest.json` are
  byte-identical to the committed manifest. This includes
  `data/processed/daily_weather_features.csv.gz` and
  `analysis/pseudo_events.csv`, so the re-acquired ERA5 values are identical
  to the authors' snapshots.
- The re-acquired JSON files differ from the archived snapshots in bytes and
  SHA-256 only through response metadata (for example, generation time). The
  daily `time` and `precipitation_sum` arrays are identical for all 8
  locations, as checked separately against the private snapshots. The clone
  rewrites `data/raw/acquisition_ledger.csv` with its own retrieval rows.
- Binary containers (PDF, DOCX, PPTX, ZIP) differ only in embedded
  timestamps.
- The weather benchmark was reproduced unchanged with the existing settings.

## Data routes

- Weather: ERA5 (Copernicus C3S) via the public Open-Meteo archive API
  (`src/acquire_weather.py`). It needs internet access on the first run and
  is not redistributed.
- Literature metadata: Crossref/PubMed JSON is archived. The withheld full
  texts can be re-acquired from the URLs in the ledger.
- No private dependency remains for computation.
