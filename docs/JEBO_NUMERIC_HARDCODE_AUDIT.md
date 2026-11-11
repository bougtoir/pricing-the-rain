# JEBO numeric hard-code audit

Date: 2026-10-20. Scope: all numeric literals in manuscript, abstract,
tables, figures, captions, supplement, highlights, cover letter, and README,
classified A–F per the audit rubric. Baseline: the QREF-final audit
(`QREF_NUMERIC_HARDCODE_AUDIT.md`), whose remediation remains in effect —
every scientific result flows through `{{TOKEN}}` placeholders resolved from
`results/manuscript_values.json` or computed from `config/*.yml` at build
time, and `analysis/final_audit.py::audit_config_prose_literals`
auto-validates every config-derived prose literal.

## JEBO-pass delta check

All new prose written for JEBO (Introduction no-data sentence, §7.4
institution/accumulation caveats, anchor-swap sentences, cover letter,
declarations) was scanned: the only new numeric literals are the journal's
own submission-fee amount (US$175, an editorial constant, not a scientific
result) and integer contribution counts ("three/four contributions").
The two new citations introduce author-year strings only. **Zero new
scientific literals were added manually.**

## Classification (full re-scan)

- **A — design constants** (allowed): config constants auto-validated —
  hazard persistence 0.97, high-hazard share 30%, multiplier 2.0, prior
  strength 2.0, recency decay 0.995, selective failure weight 0.35,
  Prelec α 0.65, reputation γ 0.5, horizon 4,000, regime base
  probabilities 0.30/0.10/0.03/0.01; supplement constants (14-day
  follow-up, thresholds, replication counts, seed note) match
  `config/*.yml`.
- **B — seed/config constants**: seeds 20260924 / 20261012 / 20260925 live
  in `config/simulation.yml`, `config/general_simulation.yml`,
  `analysis/robustness.py`.
- **C — layout constants**: PPTX/DOCX inches, DPI, font sizes in
  `analysis/build_manuscript_assets.py`, `build_manuscript.py`.
- **D — programmatic results**: all headline numbers via `{{TOKEN}}`
  (region-days 87,664; pseudo-events 2,595; apparent success 0.853 /
  placebo 0.600 / random 0.593; selection ratio ~1.71 analytic
  1.7115; selection gaps 0.216→0.007; D_rel 1.122→11.538; shares
  91.5%→81.9% / 8.5%→18.1%; D_EV flat; equivalent efficacy
  0.072/0.022/0.0075; regression coefficients, CIs, permutation p;
  replication counts). `render_template` raises on unresolved tokens.
- **E — cross-validated prose literals**: config constants above via
  `audit_config_prose_literals` (automated, aborts the audit on failure).
- **F — suspicious hard-coded results**: **0**.

## Provenance spot-table (canonical sources)

| manuscript claim | value | canonical file | key/row | generating script |
|---|---|---|---|---|
| total region-days | 87,664 | results/manuscript_values.json | study.region_days | src/weather_analysis.py |
| hazard-rule apparent success 7d | 0.853 | results/manuscript_values.json | empirical.pseudo_events[HAZARD].Apparent_success_7d | src/weather_analysis.py |
| selection ratio (common, endo) | 1.71 | results/manuscript_values.json | general.summary[common,endogenous,selection_ratio] | simulation/general_rare_event.py |
| analytic selection ratio | 1.7115 | computed at build | config/general_simulation.yml | manuscript/build_manuscript.py |
| D_rel model D endo common→very rare | 1.122→11.538 | results/manuscript_values.json | general.summary[*,endogenous,D_rel_D_reputation] | simulation/general_rare_event.py |
| prob/reputation shares | 91.5→81.9% / 8.5→18.1% | results/manuscript_values.json | general.summary D_rel components | simulation/general_rare_event.py |
| equivalent efficacy | 0.072/0.022/0.0075 | results/general_equivalent_efficacy.csv | regime rows | simulation/general_rare_event.py |
| replication count | 2,000 | results/manuscript_values.json | general.convergence | simulation/general_rare_event.py |

Status: **PASS** — category F = 0; every manuscript-facing scientific
number traces to a canonical machine-readable source.
