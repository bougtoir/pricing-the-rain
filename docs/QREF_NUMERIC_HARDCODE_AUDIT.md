# QREF numeric hard-code audit

Date: 2026-10-18. Scope: all numeric literals appearing in manuscript,
abstract, tables, figures, captions, supplement, cover letter, and
highlights, classified A–E per the audit rubric.

## Result: PASS (after remediation below)

### Remediation applied this pass (category D → programmatic)

| claim | old literal | remediation |
|---|---|---|
| Analytic Lemma-1 ratio | `R ≈ 1.7115` (2 sites) | now `{{SEL_RATIO_ANALYTIC}}`, computed in `build_manuscript.py` from `config/general_simulation.yml` (demand × acceptance observation probabilities via the two-state formula; evaluates to 1.7115) |
| Simulated ratio range | `1.708–1.713` | now `{{SEL_RATIO_ENDO_MIN}}–{{SEL_RATIO_ENDO_MAX}}`, min/max over `results/manuscript_values.json` general summary endogenous `selection_ratio` rows (1.7078/1.7131) |
| parameter-specific "1.71" | literal | `{{SEL_RATIO_ANALYTIC_2DP}}` |

### Automated validation added (category E)

`analysis/final_audit.py` now includes `audit_config_prose_literals()`:
every model/design constant stated in manuscript prose is asserted present
in `config/general_simulation.yml` — hazard persistence 0.97, high-hazard
share 30%, multiplier 2.0, prior strength 2.0, recency decay 0.995,
selective failure weight 0.35, Prelec α 0.65, reputation γ 0.5, horizon
4,000, and all four regime base probabilities (0.30/0.10/0.03/0.01).
Run as part of the standard audit; failure aborts the audit.

### Classification of remaining literals

- **A — design constants** (allowed): the config constants above (now
  auto-validated); supplement constants (14-day follow-up, 75th-percentile
  threshold, 1/3/7/14 windows, 2,000/10,000/1,500 replication counts,
  seed separation note) — all match `config/*.yml`; citation years.
- **B — layout constants**: PPTX/DOCX inches, DPI, font sizes in
  `analysis/build_manuscript_assets.py` and `build_manuscript.py`.
- **C — canonical-derived results**: all headline numbers flow through
  `{{TOKEN}}` placeholders resolved from `results/manuscript_values.json`
  (region-days 87,664; pseudo-event counts; apparent success 0.853;
  selection ratios/gaps; D_rel 1.122→11.538; shares 91.5%→81.9% and
  8.5%→18.1%; D_EV flat; equivalent efficacy 0.072/0.022/0.0075;
  regression coefficients, CIs, permutation p; replication counts).
  `render_template` raises on any unresolved non-figure/table token.
- **D — suspicious hard-codes**: none remaining after the remediation above.
- **E — prose literals**: config constants (now auto-validated) and section
  numbering only.

### Traceability spot-check (canonical sources)

| claim | value | source |
|---|---|---|
| total region-days | 87,664 | `manuscript_values.json` → `study.region_days` |
| hazard-rule apparent success 7d | 0.853 | `empirical.pseudo_events[HAZARD].Apparent_success_7d` |
| selection ratio (common, endo) | 1.71 | `general.summary[common,endogenous,selection_ratio]` |
| D_rel model D endo common→very rare | 1.12→11.54 | `general.summary[*,endogenous,D_rel_D_reputation]` |
| equivalent efficacy rare | 0.022 | `general.equivalent_efficacy[rare]` |
| replication count | 2,000 | `general.convergence` max sample_size |

Status: PASS — every major manuscript numeric claim traces to a canonical
machine-readable source; no manual result literals remain.
