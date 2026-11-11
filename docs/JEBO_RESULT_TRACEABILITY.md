# JEBO result traceability map

Date: 2026-10-20. Every manuscript-facing display item and major in-text
number mapped to its canonical source. All items reproduce via
`run_all.py` → `analysis/build_manuscript_assets.py` →
`manuscript/build_manuscript.py` ({{TOKEN}} injection from
`results/manuscript_values.json`).

## Main tables

| item | displayed statistics | generating script | canonical input | canonical result | manuscript use |
|---|---|---|---|---|---|
| Table 1 | P1–P6 proposition/evidentiary status | analysis/build_manuscript_assets.py | model definitions | tables/table1_proposition_classification.csv | §3 |
| Table 2 | per-regime 4-layer probabilities, B/D metrics | analysis/build_manuscript_assets.py | results general sim | tables/table2_general_regimes.csv | §4, §6 |
| Table 3 | mean apparent success by efficacy × regime × rule | analysis/build_manuscript_assets.py | general sim | tables/table4_observational_equivalence.csv | §6.4 |
| Table 4 | pseudo-event apparent success | src/weather_analysis.py | data/raw/weather/* | tables/table5_pseudo_event_results.csv | §6.5 |

## Main figures

| item | content | generating script | canonical input | caption/text use |
|---|---|---|---|---|
| Figure 1 | framework diagram | src/model_diagram.py | model spec | §2 |
| Figure 2 | pseudo-event success rates by rule | analysis/build_manuscript_assets.py | pseudo-event results | §5, §6.5 |
| Figure 3 | four probability layers + decomposition | analysis/build_manuscript_assets.py | general summary | §6.1–6.2 |
| Figure 4 | distortion decomposition by regime | analysis/build_manuscript_assets.py | general summary | §6.2 |
| Figure 5 | mean-performance equivalence map | analysis/build_manuscript_assets.py | equivalent-efficacy grid | §6.4 |

## Supplement

| item | source table/figure |
|---|---|
| Tables S1–S10 | tables/table_s1..s8_*.csv, table3_study_locations.csv, table6_simulation_results.csv |
| Figures S1–S3 | figure2_empirical_hazard, figure4_simulation_decomposition, figure5_robustness |

## Major in-text numbers

| claim | value | canonical source | key |
|---|---|---|---|
| region-days | 87,664 | manuscript_values.json | study.region_days |
| pseudo-events | 2,595 | manuscript_values.json | study.pseudo_events |
| apparent success (hazard rule, 7d) | 0.853 | manuscript_values.json | empirical.pseudo_events[HAZARD].Apparent_success_7d |
| placebo/random success | 0.600/0.593 | manuscript_values.json | empirical.pseudo_events rows |
| selection ratio sim | 1.708–1.713 | manuscript_values.json | general.summary selection_ratio |
| selection ratio analytic | 1.7115 | config/general_simulation.yml | computed in build |
| selection gaps | 0.216/0.072/0.021/0.007 | manuscript_values.json | general.summary selection_gap |
| D_rel model D endo | 1.122→11.538 | manuscript_values.json | general.summary D_rel_D_reputation |
| shares prob/reputation | 91.5→81.9%, 8.5→18.1% | manuscript_values.json | general.summary components |
| equivalent efficacy | 0.072/0.022/0.0075 | results/general_equivalent_efficacy.csv | regime rows |
| Prelec α | 0.65 | config/general_simulation.yml | auto-validated literal |

Reproduction status: PASS (pipeline re-run 2026-10-20; see
JEBO_PUBLIC_REPRODUCIBILITY_AUDIT.md).
