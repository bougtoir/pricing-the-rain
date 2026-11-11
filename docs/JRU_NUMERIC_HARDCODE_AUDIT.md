# JRU numeric hard-code audit

Scope: `manuscript/manuscript_template.md`, `supplement/supplement_template.md`,
cover-letter and caption strings in `manuscript/build_manuscript.py`, and the
proposition table in `analysis/build_manuscript_assets.py`. Method: regex scan
for numerals outside `{{TOKEN}}` placeholders, citation years, section numbers,
and integers ≤ 10, followed by manual classification.

Categories: **A** token from `results/`/`analysis/` outputs; **B** token from
config or a named code constant; **C** method-design constant typed in prose,
verified equal to the code literal; **D** mathematical constant or notation
(e.g. \([0,1]\)); **E** bibliographic/section numbering; **F** unverified or
stale scientific number.

## Fixes in this pass

| Location | Before | After |
|---|---|---|
| Methods (generic simulation inputs) | typed persistence, high-state share, multipliers, prior strength, Prelec α, γ, decay, efficacy grid, regimes | `CFG_*` tokens read from `config/general_simulation.yml` (B) |
| Methods (reputation prior stocks) | typed 0.05 / 0.10 | `PRIOR_SUCCESS_STOCK`, `PRIOR_OBS_STOCK` constants in `simulation/general_rare_event.py` (B) |
| Online Resource 1, S4/S7 replication counts | typed 10,000 / 2,000 | `SIM_REPLICATIONS`, `GEN_REPLICATIONS` (B) |
| Online Resource 1, sensitivity replications and permutations | typed 2,000 / 1,000 | `CFG_SENSITIVITY_REPLICATIONS`, `CFG_N_PERMUTATIONS` from named constants in `analysis/robustness.py` (B; values unchanged) |
| Proposition table P2a/P2b | typed "≈ 1.71", "≈ 0.72 × p_obj" (pre-correction values) | computed from `results/general_summary.csv` (A) |

## Remaining typed numerals (all non-F)

| Text | Category | Source |
|---|---|---|
| 14-day follow-up / window (S1, S2, S4) | C | `src/weather_analysis.py` windows, `success_1mm_14d` |
| 75th-percentile hazard threshold (S2) | C | `src/weather_analysis.py` `.quantile(0.75)` |
| 0.1, 1, 5 mm thresholds; 1, 3, 7, 14 day windows (S4) | C | `src/weather_analysis.py` threshold loop |
| 1991–2010 training, 2011–2020 evaluation | C | ERA5 file names and split in `src/weather_analysis.py` |
| 95% CI | D | convention |
| \([0,1]\), \(\{0,1\}\), \(0<\alpha<1\) | D | notation |
| Section numbers 2.1–7.4 | E | — |

**Category F count: 0.** Weather-analysis literals were not converted to
constants because the user instructed that weather scientific logic remain
unchanged; they are recorded here instead.
