# JRU Data–Text–Figure Consistency Audit

Run after the corrected formal generic simulation (seed 20261012, R = 2000,
config unchanged) and the final manuscript build.

Command:

```bash
PYTHONPATH=. .venv/bin/python analysis/data_text_figure_check.py
```

Result: **139 checks, 0 failed.**

## What is checked

| Check | Source of truth | Representation compared |
|---|---|---|
| Every numeric cell of Table 2 (regime × observation rule × metric) | `results/general_summary.csv` | `tables/table2_general_regimes.csv` (tolerance 1e-9) |
| Key prose values (D_rel of Model D common/very rare; D_rel of Models B and C, very rare; reputation–hazard correlation; Model-D price–success difference; selective-learner B_subj) | `results/general_summary.csv` | `replacements()` tokens, rounded as printed |
| The same tokens | token values | rendered `manuscript/manuscript.md` |
| Observational-equivalence table row count | `results/general_observational_equivalence.csv` | `tables/table4_observational_equivalence.csv` |
| Fig. 5 caption selection ratio | `results/general_summary.csv` | `results/manuscript_values.json` caption |
| Removed “bounded frequency” wording | Lemma 2 | rendered manuscript and Fig. 5 caption |
| Figs. 4 and 5 regenerated from the corrected summary | file modification order | `figures/figure4_*.png`, `figures/figure5_*.png` |

## Other consistency gates in the build

- `analysis/final_audit.py` (passes): numeric, statistical and package audit,
  including rendered config constants (hazard persistence, high-hazard share,
  multiplier, prior strength, recency decay, selective failure weight,
  Prelec alpha, reputation gamma, horizon, base probabilities) against
  `config/general_simulation.yml`.
- `docs/JRU_RESULT_TRACEABILITY.md`: all 80 template tokens traced to
  config, code constants or canonical result files.
- `tests/test_manuscript_outputs.py`: every figure and table is cited in the
  text, captions use `Fig. N`, reference count equals `REFERENCE_ORDER`.

## Visual inspection

Figures 6 and 8 inspected at 600 dpi after correction. Panel values match
Table 2 (selection ratio ≈ 1.71 endogenous / 1.00 exogenous; Model-D D_rel
1.12 → 11.61; Model-D price–success difference bars equal Table 2). The
Fig. 4 panel B legend was moved to `center right` because it overlapped the
endogenous ratio line; no data changed.
