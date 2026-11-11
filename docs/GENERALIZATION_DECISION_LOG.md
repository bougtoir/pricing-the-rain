# GENERALIZATION DECISION LOG

Decisions taken during the generalization pass (single-VM contract: choose the
strongest defensible default, record, continue).

| # | Decision | Rationale |
|---|---|---|
| D1 | Generic simulation is a separate module `simulation/general_rare_event.py` with its own config; rainfall module untouched. | Frozen-analysis constraint; clean domain separation. |
| D2 | Rare-event DGP: persistent two-state hazard \(M_t\) multiplying a base rate; four regimes {0.30, 0.10, 0.03, 0.01}. | Simplest stochastic model that admits state-dependent rarity and clustered events; covers common→very-rare span per Phase 6. |
| D3 | Endogenous observation = demand \(D_t\) (loads on \(M_t\)) × provider acceptance \(A_t\) (loads on relative hazard \(p_t/b-1\) and provider selectivity). | Relative-hazard acceptance keeps selection operative when \(p_t-b\) is tiny in rare regimes; mirrors drought-demand/rainmaker acceptance channels. |
| D4 | Exogenous comparator: constant request probability equal to the endogenous marginal of the same regime. | Isolates selection, not observation volume. |
| D5 | Primary subjective learner = Bayesian Beta posterior (strength 2, prior mean = base rate); naive, recency, selective reported in supplement. | Canonical benchmark; alternatives shown as sensitivity. |
| D6 | Weighting: Prelec one-parameter \(\alpha=0.65\). | Literature-anchored behavioral assumption (Prelec 1998; CPT estimates); labeled assumption, not estimated. |
| D7 | Pricing: V_t scales with hazard state; α normalized to 1; reputation γ=0.5, EWMA decay 0.995 per provider. | Transparent decomposition; γ chosen to give a visible but non-dominant stock term. |
| D8 | Price–outcome association reported as signed difference, not forced negative. | Simulation gives a positive but small contemporaneous association under Model D while reputation premia are large — reported as stated (P5 wording: "can be weak or ambiguously signed"). |
| D9 | Provider ranking distortion measured as Spearman(provider selectivity, provider experienced success); result is negative — conservative providers look better on experienced frequency. | Honest non-monotone/negative finding retained, per "do not assume monotonicity". |
| D10 | Equivalence scan: efficacy δ ∈ {0, .02, .05, .10} on intervened periods under both rules; 1,500 replications per cell. | Quantifies which δ under exogenous observation reproduces the endogenous zero-efficacy uplift. |
| D11 | Journal: primary Economic Modelling (JCR Q1, hybrid, no mandatory APC); backup Journal of Risk and Uncertainty. | See docs/GENERALIZATION_JOURNAL_SELECTION.md. |
| D12 | New references (8): Hertwig 2004, Wulff 2018, Ungemach 2009, Tversky & Kahneman 1992, Prelec 1998, Esponda & Pouzo 2016, Jehiel 2018, QE 2018 endogenous-sample-selection lab study. | Citation ecology for the generalized framing; Crossref snapshots archived. |
| D13 | Frozen rainfall numbers unchanged; new tokens only read results/general_*.csv + frozen rainfall outputs. | Frozen-analysis constraint. |
