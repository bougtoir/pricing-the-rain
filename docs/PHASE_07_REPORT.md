# Phase 7 report: figures, tables, and machine-readable values

## Outputs

- Five numbered English-language figures, each available as a separate high-resolution
  PNG; Figures 2–5 also have vector PDF versions and Figure 1 retains its source SVG.
- A widescreen PPTX with one figure per slide, proportional sizing, titles, and captions.
- Four main tables and five supplementary tables as CSV files.
- Separate editable DOCX files for main and supplementary tables.
- `results/manuscript_values.json`, generated directly from analysis outputs and used as
  the numerical source for manuscript construction.

## Figure set

1. Zero-effect ecological-economic framework.
2. Empirical rainfall hazard by dry-spell bin and location.
3. Observed-weather pseudo-event apparent success.
4. M0–M5 simulation decomposition.
5. Threshold/window robustness, parameter sensitivity, and Monte Carlo precision.

## Table set

1. Locations, rainfall regimes, coordinates, observations, and missingness.
2. Pseudo-event counts, apparent success windows, and scenario WTP.
3. Simulation events, apparent success, prices, reputation, transfers, and surplus.
4. Pre-specified hypothesis classifications.

Supplementary tables report price models, threshold/window sensitivity, parameter
sensitivity, convergence, and the permutation falsification.

## Quality controls

- Tables are generated from CSV results rather than transcribed.
- Manuscript values are generated from the same results in JSON form.
- Figure 5 uses the complete robustness outputs.
- All PNG dimensions exceed ordinary 300-dpi journal requirements at intended print
  widths.
- PPTX and DOCX containers pass archive-integrity checks.
- Figure captions use “apparent success” and “scenario price” rather than causal claims.
