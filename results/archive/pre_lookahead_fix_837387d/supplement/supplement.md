# Supplementary material for "Rare-Event Quote Formation under Endogenous Observation: Selection, Subjective Beliefs, and Reputation"

## S1. Zero-effect invariant and implementation checks

For every sampled weather sequence, the code stores one rainfall array and never
passes intervention status to a rainfall-generating function. Potential rainfall is
therefore identical under intervention and non-intervention:

\[
R_{rt}(1)=R_{rt}(0)=R_{rt}.
\]

Automated tests verify that the source contains no `ritual_effect`, that event-day rain
is excluded from post-event outcomes, that preceding dry spells use only earlier days,
that all candidate dates have complete 14-day follow-up, that models share sampled
weather years by replication, and that simulation does not mutate weather.

## S2. Pseudo-event definitions

Candidate events occur only in the 2011–2020 evaluation period and at least 14 days
before its endpoint. The dry-spell and rolling-deficit variables are lagged by one day.
The high-prospective-hazard rule uses hazards estimated from 1991–2010 candidate dates
with complete follow-up and a location-specific 75th-percentile threshold defined from
training hazard cells. Random drought dates are sampled from qualifying drought days.
Season-matched placebos preserve region and calendar-month structure.

## S3. Scenario price models

Table S1 reports naive, hazard-adjusted, and two-way-clustered estimates by region-year
and region-rule. Scenario WTP is a calibrated model quantity; these coefficients do
not estimate historical prices or causal efficacy.

{{TABLE_S1}}

## S4. Rainfall threshold and attribution-window sensitivity

Table S2 gives apparent success for all five event rules at 0.1, 1, and 5 mm thresholds
and 1, 3, 7, and 14 day windows.

{{TABLE_S2}}

## S5. Simulation parameter sensitivity

Table S3 varies strategic-selection slopes, Bayesian prior means, and selective-memory
weights. Each scenario uses 2,000 replications and a seed separate from the principal
simulation.

{{TABLE_S3}}

## S6. Monte Carlo convergence

Table S4 evaluates model means and Monte Carlo standard errors at increasing
replication counts. The principal estimands use 10,000 replications per model.
Price–success differences are undefined in replications without both outcome classes.
One M4 replication accepts no event, so its apparent-success and mean-price entries are
also undefined. Summary means omit these undefined event-based cells rather than
assigning artificial zeros.

{{TABLE_S4}}

## S7. Permutation falsification

Table S5 compares the observed adjusted linear-probability coefficient with 1,000
WTP permutations within region–calendar-month–timing-rule strata after stratum
demeaning and adjustment for prospective hazard and drought severity. Exchangeability
is assumed only within the defined strata. This is an exploratory falsification
diagnostic for a constructed scenario-WTP regressor, not confirmatory evidence of a
historical market relationship.

{{TABLE_S5}}

## S8. Stock–flow price mechanism

In M4–M5, past attributed outcomes update a provider-specific reputation stock.
Current simulated WTP and price depend on that stock relative to the current
prospective hazard. Current apparent success is instead the natural-rainfall flow after
the accepted event. Provider-mean-price dispersion therefore differs from reputation
dispersion, and neither implies a positive contemporaneous price–success difference.

## S9. Simulated accounting identities

Table S6 separates community expenditure and provider revenue, which are the two sides
of the same modeled transfer, from provider resource costs, provider profit, community
material-plus-social utility, and total social surplus. These are calibrated scenario
accounts, not historical welfare estimates.

{{TABLE_S6}}

## S10. Analytic-proposition interpretation

“Demonstrated in calibrated scenario” and “demonstrated in model” identify structural
model results, not historical empirical findings. The social-value proposition is a
logical distinction built into plural valuation; it is not an estimate of social
utility.

The strategic-provider-selection proposition is “demonstrated in model using observed
weather”: M3 changes the calibrated acceptance rule relative to M2 while retaining the
observed weather sequence, and the existing selection-slope sensitivity checks that
model-contingent mechanism.

## S11. Generic-simulation Monte Carlo convergence

Table S7 reports generic-simulation metric means and Monte Carlo standard errors at
increasing replication counts. The principal generic estimands use 2,000
replications per regime–rule cell.

{{TABLE_S7}}

## S12. Generic-simulation probability-layer detail

Table S8 reports the subjective-layer and price-layer gaps by learner rule and
pricing model across the four rarity regimes and the two observation rules.
Selective memory and Bayesian updating bound the range of subjective-layer
behavior; the reputation-mediated model D dominates the price-layer separation
in rare regimes.

{{TABLE_S8}}

## S13. Benchmark environment detail

Table S9 reports the study locations, coordinates, rainfall regimes, and
region-day coverage. Figure S1 maps the empirical hazard structure: apparent
success differs across event rules purely because baseline hazard differs.

{{TABLE_S9}}

{{FIGURE_S1}}

## S14. Benchmark Monte Carlo decomposition and robustness

Table S10 reports the full sequential pricing-rule decomposition under M0–M5
(Figure S2); Figure S3 reports robustness across rainfall thresholds,
attribution windows, parameter sensitivity, and Monte Carlo precision.

{{TABLE_S10}}

{{FIGURE_S2}}

{{FIGURE_S3}}

## S15. Benchmark model-overlay detail

The following results belong to the MODEL-OVERLAY layer of the benchmark:
they are calibrated simulation outputs overlaid on real weather, not
observed pricing or estimated human behavior.

Regression-adjusted willingness to pay loads strongly on apparent success
(naive coefficient 0.124, 95% CI
[0.086, 0.162]), and attenuates to 0.036
(CI [-0.028, 0.100]) once baseline hazard and
calendar structure are controlled—an attenuation consistent with hazard, not
intervention, driving both demand and attributed outcomes. A permutation test
that shuffles outcomes within event rules yields observed statistic
-0.0319 versus permuted mean -0.0002 (p ≈ 0.002),
rejecting the naive performance interpretation.

The reputation overlay is the benchmark analogue of the stock–flow
decoupling in the main text, and is sharper: mean contemporaneous
price-success differences are negative (-2.447 under
reputation-mediated pricing M4 and -3.037 under the weighted
variant M5), even though mean prices (3.568 and 4.610 versus
a fixed price of 3.000) and provider-price heterogeneity are
elevated. Reputation premia persist because reputation is a stock of past
attributed outcomes while contemporaneous success is a hazard-driven flow.
