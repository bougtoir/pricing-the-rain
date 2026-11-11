# Final revision baseline

## Repository state

- Canonical working tree: `bougtoir/wip/pricing-the-rain/`
- Base branch: `master`
- Merged release PR: `bougtoir/wip#506`
- Base commit before final revision: `c6ce46d804fdd8a275f9818dd3d651509fba00ef`
- Safety checkpoint: `0ca82c98557d824564dfecac03d4828c78852e64`
- Previous scientific release checkpoint:
  `ef8c25a5a96e757aa7787fffb2c3b1d4d635c8e8`
- Intended public repository: `bougtoir/pricing-the-rain`
- Public `main` at baseline:
  `2a3f9884eba253e9fe6736b9a74a915758cd6cac`

The public repository matches the canonical project tree except for the five
intentionally excluded audit-source paths listed in `docs/DATA_PROVENANCE.md`: the
captured publisher guide, its ledger, the Akong'a institutional PDF and landing page,
and the corresponding source ledger.

## Canonical sources and generated files

- Manuscript source: `manuscript/manuscript_template.md`
- Manuscript builder: `manuscript/build_manuscript.py`
- Blinded inline review manuscript: `manuscript/manuscript_blinded.docx`
- Figure-separated submission manuscript: `manuscript/manuscript_text.docx`
- Supplement source: `supplement/supplement_template.md`
- Cover-letter source: `manuscript/cover_letter.md`
- Highlights: `manuscript/highlights.txt`
- Declarations: `manuscript/declarations.md`
- Machine-readable manuscript values: `results/manuscript_values.json`
- Figure/table builder: `analysis/build_manuscript_assets.py`
- Weather analysis: `src/weather_analysis.py`
- Principal simulation: `simulation/run_simulation.py`
- Robustness and falsification: `analysis/robustness.py`
- Canonical orchestration: `run_all.py` and `Makefile`
- Provenance: `docs/DATA_PROVENANCE.md` and machine-readable ledgers under
  `data/raw/`

## Manuscript and submission baseline

- Title: “Pricing the Rain: Endogenous Timing, Environmental Valuation, Strategic
  Selection, and Apparent Efficacy under a Zero-Effect Null”
- Target journal: *Ecological Economics*
- Selected category: Analysis
- Main-text words excluding references: 3,589
- Abstract words: 186
- References: 20
- Figures: 5
- Main tables: 4
- Supplementary tables: 5
- Highlights: 5; maximum length 70 characters

The generated package already includes editable DOCX manuscripts, PDF renderings,
separate PDF/PNG figures, an editable figure PPTX, editable table DOCX files, a
supplement, title page, cover letter, highlights, and declarations.

## Baseline analytic propositions

1. Natural rainfall can generate apparent success under zero efficacy:
   demonstrated with observed-weather pseudo-events.
2. Drought-driven demand increases intervention frequency: demonstrated in the
   calibrated model.
3. Drought can increase scenario WTP: demonstrated in a calibrated scenario.
4. Strategic provider selection increases apparent success: demonstrated with
   observed weather in the model comparison.
5. Higher prices are positively associated with apparent success: not supported.
6. Reputation learning creates persistent provider differentiation: demonstrated in
   the model.
7. Selective and recency-weighted memory raises price premia: demonstrated in the
   model.
8. Zero meteorological efficacy implies zero social value: rejected as a logical
   equivalence, not empirically tested.

## Reproducibility baseline

- Exact zero-effect invariant:
  \(R_{rt}(1)=R_{rt}(0)=R_{rt}\).
- Archived analytical weather inputs: eight valid ERA5 snapshots plus eight retained
  invalid all-null ERA5-Land responses.
- Analyzed panel: 87,664 region-days.
- Observed-weather pseudo-events: 2,595.
- Principal simulations: 60,000 total, 10,000 per M0–M5 model.
- Sensitivity simulations: 18,000.
- Test suite: 20 tests.
- Previous deterministic reproduction-manifest SHA-256:
  `3bd0665313a4ef89226d522f81ca369e5fe65ffd3ee786278133630c372e9bca`.
- The pipeline is offline by default and validates archived input size and SHA-256
  records before analysis.

## Defects and revision risks identified at baseline

### Submission-critical

1. QJE 2026 overlap is acknowledged but not mapped in a dedicated, source-level
   differentiation audit. The Introduction and cover letter require a more explicit
   boundary between established endogenous-timing results and this paper's
   ecological-economic extension.
2. The title phrase “Environmental Valuation” may overstate the empirical content
   because WTP and prices are calibrated scenarios rather than observed valuation
   estimates.
3. The failed universal positive price-success proposition is reported, but the
   stock-versus-flow mechanism—past attributed outcomes forming reputation versus
   current hazard determining current success—needs to be made a more visible
   principal result across the manuscript and Figure 4.
4. The phrase “Monte Carlo decomposition” can imply a clean one-factor causal
   decomposition even though M0–M1 shuffle within-year outcomes and M2–M5 restore
   observed ordering. Staged model-comparison language is required.
5. Current journal instructions and Elsevier generative-AI policy must be rechecked
   immediately before packaging rather than relying only on the prior capture.

### High priority

6. WTP, price, premium, transfers, resource costs, social utility, and environmental
   value require a project-wide terminology audit.
7. The negative within-stratum permutation result is exploratory and may be shaped by
   construction and conditioning; its interpretation requires a specific audit.
8. Every manuscript number needs an automated traceability check against canonical
   outputs rather than relying only on template substitution and existing tests.
9. Historical evidence supports context-specific payments or offerings, not a
   universal pricing law; all historical-economic wording must be reverified.
10. Public code/data availability is presently truthful, but the final revision must
    preserve the restricted-source exclusions and confirm public synchronization after
    the new release.

### Administrative

11. Author names and order, affiliations, correspondence, ORCIDs, funding, competing
    interests, CRediT roles, acknowledgements, and originality/exclusive-submission
    confirmation remain unresolved and must be isolated in
    `AUTHOR_ACTIONS_REQUIRED.md`.
