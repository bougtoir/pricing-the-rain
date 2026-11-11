> **SUPERSEDED — retained only for provenance; do not use for current conclusions. The current final scientific report is `FINAL_TARGETED_REVISION_REPORT.md` and `FINAL_ECONOMIC_MODELLING_FINISHING_REPORT.md`.**

# Final generalization report

## Scope

Starting hash: `b3eedf62b` (tag `checkpoint-pre-generalization-b3eedf62b` on
`master`). Ending hash: `7ca460a4` on branch
`devin/1791802000-pricing-rain-generalization` (plus a doc-only hash update
commit). The work generalizes the rainmaking-specific apparent-performance study
into a framework for pricing rare events under biased experienced frequencies,
per `devin_generalize_rare_event_pricing_single_VM.txt`.

## Preserved analysis (frozen, not recomputed)

- Archived ERA5 rainfall benchmark: 87,664 region-days; 2,595 pseudo-events.
- 7-day apparent success at 1 mm: random 0.593; high prospective hazard 0.853;
  season-matched placebo 0.600.
- Scenario-WTP regressions: naive 0.1237; hazard-adjusted 0.0360
  (95% CI −0.0388, 0.1109); permutation observed −0.0319 (p ≈ 0.002).
- Monte Carlo M0–M5: reputation mean prices 3.568 (M4) and 4.610 (M5) vs fixed
  3.000; mean contemporaneous price-success differences −2.447 (M4) and
  −3.037 (M5). Files under `analysis/` and `results/` are unchanged.

## New theory and analysis

- `docs/GENERAL_FORMAL_MODEL.md`: four probability layers (objective,
  experienced, subjective, price-implied), propositions P1–P6,
  identifiability/observational-equivalence argument, metric definitions.
- `simulation/general_rare_event.py` + `config/general_simulation.yml`:
  generic rare-event simulation; 2,000 replications per cell; four rarity
  regimes (p = 0.30/0.10/0.03/0.01); endogenous vs exogenous observation;
  four learner rules; four pricing models; efficacy sweep {0, .02, .05, .10}.
- `results/general_summary.csv`, `general_convergence.csv`,
  `general_observational_equivalence.csv`; Figures 4–5 of the new manuscript.
- `docs/GENERALIZATION_NOVELTY_AUDIT.md`, `CLOSEST_PRIOR_STUDIES.md`,
  `GENERALIZATION_JOURNAL_SELECTION.md`, `GENERALIZATION_DECISION_LOG.md`,
  `ECONOMIC_MODELLING_{FIT_AUDIT,CITATION_ECOLOGY,COMPLIANCE_CHECKLIST,DECISION_LOG}.md`.

## Strongest supported general result

Experienced-frequency bias under endogenous observation grows monotonically
with rarity (B_exp: 0.216 → 0.072 → 0.021 → 0.007 across common → very-rare
relative to shrinking baselines; the relative gap widens sharply), and
reputation-mediated price distortion D_rel explodes with rarity (1.12 →
11.54 for model D). Endogenous zero-efficacy environments are
observationally equivalent to positive-efficacy exogenous ones — prices alone
cannot separate efficacy from selection.

## Strongest unsupported proposition

P3 (probability weighting moving the subjective layer) is parameter- and
assumption-dependent: the sign and size of B_subj vary across learner rules
(selective ≈ +0.30 vs Bayesian shrinkage) and the Prelec alpha is a labeled
assumption, not an estimate. Cross-domain transfer (medical, insurance) is a
conjectured implication, not a demonstration.

## Does rarity materially change distortion?

Yes. Rarity changes which layer dominates: B_exp relative inflation and D_rel
both grow with rarity; at very rare events the price-implied layer departs
most strongly from every probability layer.

## Do the four probabilities separate in simulation?

Yes. Objective, experienced, subjective, and price-implied layers are
measurably distinct in rare regimes and converge in the common regime
(Figure 4; Table 2; Table S8).

## Role of rainmaking

Demoted to a controlled zero-effect validation environment: every
apparent-success claim is mechanically false by construction, so the
benchmark calibrates what selection + attribution + reputation alone produce.

## Novelty boundary

GO with modification (see GENERALIZATION_NOVELTY_AUDIT.md): the claimed
contribution is the combination — rare event + endogenous observation +
experienced-frequency bias + price formation + zero-effect validation — not
any single mechanism; each component has known prior work.

## Journal

Primary: Economic Modelling (Elsevier), JCR Q1 Economics, JIF ≈ 4.7, hybrid —
no mandatory APC. Backup: Journal of Risk and Uncertainty (Springer), hybrid,
JIF ≈ 2.2, Scopus Q1 / JCR ~Q2. Constraint check: no SAGE/MDPI/Hindawi; no
mandatory APC.

## Clean build

`PYTHONPATH=. .venv/bin/python run_all.py --validate-only` PASSED (63 archived
raw-input records validated; reproducibility pipeline completed), `pytest
tests -q` 21/21 passed, `analysis/final_audit.py` PASSED. Manuscript 4,077
words; abstract 213 words; 31 references; 7 figures; 6 main + 8 supplementary
tables.

## Final filenames

- `manuscript/manuscript_blinded.docx` / `.pdf` (main, double-anonymous)
- `manuscript/manuscript_text.docx` / `.pdf` (text-only + figure legends)
- `manuscript/title_page.docx`, `cover_letter.docx/.pdf`, `declarations.md`
- `supplement/supplement.docx` / `.pdf` (Tables S1–S8)
- `manuscript/pricing_rare_events_economic_modelling_submission.zip`
- `figures/figures_editable.pptx`; `tables/*_editable.docx`
