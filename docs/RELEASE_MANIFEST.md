# Public-release manifest

## Release identity

- Working repository: `bougtoir/wip`
- Release branch: `devin/1790232699-pricing-the-rain`
- Scientific release checkpoint:
  `ef8c25a5a96e757aa7787fffb2c3b1d4d635c8e8`
- Public synchronization target: `bougtoir/pricing-the-rain`
- Project subdirectory: `pricing-the-rain`
- License: MIT for project code; third-party data retain source terms
- Deterministic output manifest: `results/reproduction_manifest.json`
- Manifest SHA-256:
  `3bd0665313a4ef89226d522f81ca369e5fe65ffd3ee786278133630c372e9bca`

## Included in the public release

- source code, tests, configuration, Makefile, and pinned Python requirements;
- eight validated ERA5 rainfall snapshots and eight retained invalid ERA5-Land audit
  snapshots, with acquisition ledgers and checksums;
- archived Crossref metadata and DOI audit records;
- processed weather features, pseudo-events, regression outputs, permutation outputs,
  simulation replications, summaries, sensitivities, and convergence results;
- machine-readable manuscript values and reproduction manifest;
- manuscript Markdown, editable DOCX files, rendered PDFs, declarations, highlights,
  and cover-letter draft;
- five journal-ready figures in vector PDF and high-resolution PNG;
- editable PPTX figures and editable DOCX tables;
- supplement, phase reports, formal model, decision log, assumptions, provenance,
  literature and historical-evidence audits, adversarial review, and final QC.

## Deliberately excluded from public synchronization

| Path or class | Reason |
|---|---|
| `data/raw/journal/` | Captured publisher instructions; redistribution permission not established |
| `data/raw/journal_acquisition_ledger.csv` | Refers to the excluded captured guide |
| `data/raw/literature/akonga_1987_repository_landing.html` | Captured institutional page; redistribution permission not established |
| `data/raw/literature/akonga_1987_rainmaking_rituals.pdf` | Copyrighted institutional article; redistribution permission not established |
| `data/raw/literature_source_ledger.csv` | Refers to the excluded article and landing snapshot |

The excluded files remain in persistent private project storage and are not deleted.
Public documentation retains the source URLs, retrieval procedure, byte sizes,
checksums, and title discrepancy. They are not analytical rainfall inputs; the public
offline build treats these audit ledgers as optional. An exact excluded-path copy was
rebuilt successfully with 43 validated public records, the same 33-output manifest
hash, and all 20 tests passing.

## Reproduction

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
PYTHONPATH=. .venv/bin/python run_all.py
```

Networked reacquisition is separate:

```bash
make acquire
```

Acquisition fetches only absent snapshots and never overwrites preserved raw files.
