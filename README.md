# Pricing Apparent Environmental Performance

Reproducible ecological-economic analysis of endogenous timing, strategic provider
selection, scenario valuation, attribution, and reputation under an exact zero-effect
rainfall null:

```text
R_rt(ritual = 1) = R_rt(ritual = 0) = R_rt
```

The project combines archived ERA5 daily precipitation for eight contrasting
locations (1991–2020), fictional observed-weather pseudo-events, and six Monte Carlo
models. Ritual, request, acceptance, provider, price, and reputation variables never
modify rainfall.

## Principal findings

- Natural rainfall produces substantial apparent success under zero causal efficacy.
- Drought-driven demand changes event frequency.
- Strategic acceptance raises apparent success without changing rainfall.
- Past attributed outcomes generate provider-specific reputation, scenario-price
  premia, and provider-price heterogeneity.
- Mean contemporaneous price–success differences are negative in the reputation
  models; the positive association proposition is not supported.
- Rainfall value, causal intervention value, scenario WTP, simulated price, transfers,
  resource costs, profit, surplus, and plural values are distinct objects.

## Reproduce everything

Requirements:

- Python 3.10 or compatible
- GNU Make
- LibreOffice available as `libreoffice`
- Internet access only for first-time Python package installation; all analytical
  weather inputs and Crossref metadata are archived locally

From this directory:

```bash
make reproduce
```

This creates `.venv`, installs exact Python dependencies, verifies every archived raw
input against its size and SHA-256 ledger, rebuilds the framework, weather analysis,
60,000 principal simulations, 18,000 sensitivity simulations, robustness analyses,
figures, tables, manuscript values, manuscript, supplement, and reproduction manifest,
then runs the final statistical/package audit and test suite.

Useful shorter commands:

```bash
make validate    # verify archived inputs and existing outputs
make test        # run invariant and manuscript-package tests
make manuscript  # rebuild figures, tables, and manuscript from existing analyses
```

`make acquire` is optional and networked. It only retrieves a source when its archived
snapshot is absent; existing raw snapshots are never overwritten.

## Repository map

- `config/`: locations, model parameters, seeds, and verified reference roles
- `data/raw/`: immutable weather and redistributable metadata snapshots with ledgers
- `data/processed/`: deterministic weather features
- `src/`: acquisition, weather analysis, and conceptual-framework generation
- `simulation/`: M0–M5 Monte Carlo implementation
- `analysis/`: robustness analysis and manuscript-asset generation
- `results/`: replications, summaries, classifications, manuscript values, and manifest
- `figures/`: separate high-resolution figures and editable PPTX
- `tables/`: CSV tables and editable DOCX packages
- `manuscript/`: templates, submission text, inline review version, title page,
  highlights, declarations, and cover letter
- `supplement/`: supplementary source, DOCX, and PDF
- `docs/`: model, assumptions, provenance, phase reports, journal fit, and QC records
- `tests/`: zero-effect, leakage, simulation, citation, and packaging invariants

## Submission artifacts

- `manuscript/manuscript_text.docx`: figure-separated submission manuscript
- `manuscript/manuscript_blinded.docx`: inline-figure review manuscript
- `manuscript/title_page.docx`: separate title page with author placeholders
- `supplement/supplement.docx`: supplementary material
- `manuscript/highlights.txt`: five journal-length highlights
- `manuscript/cover_letter.docx`: cover-letter draft
- `figures/figure1_framework.png` through `figures/figure5_robustness.png`
- `figures/figures_editable.pptx`: editable figure package
- `tables/main_tables_editable.docx` and
  `tables/supplementary_tables_editable.docx`
- `manuscript/pricing_apparent_environmental_performance_submission.zip`: complete
  generated upload bundle

Author names/order, affiliations, correspondence, funding, competing interests, CRediT
roles, acknowledgements, and exclusive-submission confirmation remain explicit
placeholders and must be supplied before submission.

## Interpretation boundaries

The eight locations are rainfall-regime stress tests, not a sample of ritual
communities. Prices and willingness to pay are calibrated scenarios, not reconstructed
historical payments. The study does not infer actual ritual beliefs or efficacy.
Zero meteorological efficacy does not imply zero cultural, psychological, coordination,
solidarity, or relational value.

## Data and licensing

Weather is ERA5 accessed through Open-Meteo and is subject to Copernicus/Open-Meteo
attribution terms. Crossref and Dataverse metadata retain their source terms. The
institutional article, NBER working-paper PDF, and captured publisher-policy files are
retained in private provenance storage but excluded from public synchronization when
redistribution permission is unclear; their URLs, checksums, and acquisition
instructions remain documented. Project code is MIT licensed; third-party data are not
relicensed. See `docs/DATA_PROVENANCE.md` and the machine-readable ledgers under
`data/raw/`.
