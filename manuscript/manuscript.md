# Apparent Performance under Selective Environmental Risk: Strategic Acceptance and Reputation under a Zero-Effect Rainfall Null

## Abstract

When providers choose which cases to accept, raw outcome rates combine baseline
risk, selective exposure, and any causal provider effect—and the untreated
counterfactual is usually unobserved. We impose an exact zero-effect null,
\(R(1)=R(0)\), so that every mechanism other than efficacy is isolated. Using
daily ERA5 precipitation at eight pre-specified climate stress-test locations,
we estimate prospective rainfall hazards and construct fictional
observed-weather stress tests; a separate calibrated Monte Carlo model adds
drought-driven demand, selective acceptance, scenario willingness to pay (WTP),
Bayesian reputation, and selective memory. Among 2595
fictional events, seven-day apparent success is 0.593 under
random drought timing and 0.853 under high prospective hazard.
Selective acceptance changes accepted-event composition and raises mean
simulated apparent success from 0.493 to 0.676 without
changing rainfall. Reputation models generate mean scenario prices of
3.568 and 4.610 above a fixed 3.000 baseline, yet mean
contemporaneous price-success differences are -2.447 and
-3.037; a cluster-robust scenario-WTP interval includes zero and
an exploratory permutation diagnostic is negative. WTP and prices are calibrated
or simulated, not historical estimates. Raw observed performance can therefore
reward favorable risk exposure and selective acceptance rather than causal
performance; past attributed outcomes form a reputation stock, while current
performance remains a hazard-driven flow.

**Keywords:** performance evaluation; risk adjustment; selective exposure;
attribution; reputation

## 1. INTRODUCTION

Performance evaluation is difficult when baseline risk varies. A provider whose
outcomes are scored on raw success can look effective by taking favorable cases;
an evaluator who cannot observe the untreated counterfactual cannot separate
baseline hazard, selection into exposure, and causal performance. In forecasting,
goodness is assessed relative to the difficulty of the prediction task (Murphy,
1993); in health outcomes research, risk adjustment attempts the same correction
for provider comparisons (Shahian & Normand, 2008). Wherever agents choose their
exposure, selection into observation confounds raw performance measures
(Heckman, 1979), and public scorecards can reward case selection rather than
improvement (Dranove, Kessler, McClellan, & Satterthwaite, 2003; Werner & Asch,
2005).

Hidden counterfactuals make the problem worse. Interventions are often initiated
after unusually adverse conditions, creating regression-to-the-mean risk
(Barnett et al., 2004). Observers use heuristics under uncertainty (Tversky &
Kahneman, 1974), intermittent outcomes sustain beliefs (Skinner, 1948), and
social learning can propagate an attribution once it forms (Bikhchandani,
Hirshleifer, & Welch, 1992). Reputation can then accumulate under imperfect
information (Kreps & Wilson, 1982).

Rainmaking offers a deliberately sharp known-ground-truth stress test: the true
causal effect on rainfall is exactly zero. Espín-Sánchez, Gil-Guirado, and Ryan
(2026) develop an instrumental-belief account in which leaders cannot produce
rain, drought timing and changing rainfall hazards make prayer persuasive,
untreated outcomes are hidden, and persuasive practices can persist. Their
evidence includes long-run Murcia records and a large cross-cultural
classification, and their theory discusses tangible benefits, support costs, and
a strategic-timing alternative; we concede those contributions and claim no
novelty there. Historical evidence places rain-prayer institutions within
broader problems of scarcity, resilience, and social stability (Espín-Sánchez &
Gil-Guirado, 2022). Comparative ethnography describes rainmaking responses to
rainfall scarcity or unreliability (Akong'a, 1987), and other accounts document
specialized roles and stated payments (Semenya, 2013). These sources support
institutional plausibility, not a universal law that providers screened requests
or raised fees with drought; prices and acceptance strategies below are
calibrated scenarios rather than reconstructed history.

Our contribution is to the performance-evaluation problem. We separate requests
from accepted cases, allow multiple providers that differ in selectivity, let
past attributed outcomes create provider-specific reputation stocks, and let
those stocks interact with current hazard in simulated willingness to pay (WTP)
and price. Because efficacy is fixed at exactly zero, observed differences in
raw performance arise only from baseline hazard, selection, attribution, and
learning. The principal result is unfavorable to a simple performance-pricing
story: reputation-mediated price premia coexist with zero or negative mean
contemporaneous price-success differences.

Four distinctions organize the analysis. First, causal efficacy is a
potential-outcome contrast, whereas apparent success is rainfall inside an
attribution window. Second, baseline rainfall hazard is a risk state, not
evidence of treatment response. Third, mean scenario price, provider-price
heterogeneity, a reputation-mediated premium, and the contemporaneous
price-success association are different objects. Fourth, scenario WTP, a
theoretical revenue-maximizing price, expenditure transfers, resource costs, and
non-monetary value are not interchangeable. A separate social-utility term is
retained so that null meteorological efficacy cannot be misread as null social
value; plural environmental values are documented elsewhere (Chan et al., 2012;
Kenter et al., 2015; Pascual et al., 2017; Himes & Muraca, 2018) and are not
estimated here.

We examine eight declared analytic propositions: natural rainfall can generate
apparent success; drought-driven demand increases intervention frequency;
drought can increase scenario WTP; selective acceptance increases apparent
success; higher prices are positively associated with apparent success; learning
creates persistent provider differentiation; selective memory raises price
premia; and zero meteorological efficacy does not logically imply zero social
value.

## 2. CONCEPTUAL FRAMEWORK

Figure 1 represents the data-generating system. Baseline environmental hazard
enters demand, provider acceptance, valuation, attribution, and reputation,
while the pseudo-intervention never changes rainfall. The dashed separation is
the central exclusion: there is no causal arrow from the pseudo-event to
rainfall.

{{FIGURE_1}}

### 2.1. Exact zero-effect null

For location \(r\), day \(t\), and pseudo-intervention indicator \(A_{rt}\), let
\(R_{rt}(a)\) denote potential rainfall under \(a \in \{0,1\}\). The simulation
enforces

\[
R_{rt}(1)=R_{rt}(0)=R_{rt}.
\]

No request, acceptance, provider, price, belief, or reputation variable changes
this array. Apparent success for window \(w\) and rainfall threshold \(c\) is

\[
S_{rt}(w,c)=\mathbf{1}\left\{\max_{j=1,\ldots,w}R_{r,t+j}\geq c\right\}.
\]

The event day is excluded. This definition captures a plausible retrospective
attribution rule but is not an estimator of a treatment effect.

### 2.2. Baseline hazard, demand, and selective exposure

Let \(H_{rt}(w,c)\) be the prospective probability of apparent success
conditional on location, calendar month, and the preceding dry spell—the
risk-conditioning variable for this study. We estimate this hazard from a
training period rather than assume it rises with drought duration. Provider
\(k\) observes a signal of \(H_{rt}\) and accepts a request with a probability
increasing in that signal. Selective acceptance can therefore raise the success
rate among accepted events even though it cannot change rainfall.

Drought affects demand separately from selection. A community is more likely to
request action when the preceding dry spell is long or the rolling rainfall
deficit is large. This changes the timing and frequency of observed events. It
does not imply that rain is more likely merely because the dry spell is longer.

### 2.3. Reputation stock, current flow, and price

Scenario WTP combines an instrumental component related to expected avoided
drought loss with a separate social-utility component. This construction is
motivated by empirical evidence that people value drought-risk adaptation and
supply security (Schrieks et al., 2025; Pattanayak & Kramer, 2001; Hensher et
al., 2006), but its numerical scale is not estimated from historical rainmaking
payments. Payments are transfers from communities to providers; provider costs
are resource costs; profit is revenue minus those costs. Because the
pseudo-intervention creates no rainfall, its actuarially fair causal rainfall
price is zero. The theoretical revenue-maximizing price is also distinct from
the implemented quote, which is a fixed share of calibrated WTP.

Observers update provider beliefs only after accepted events. A Bayesian
observer applies a Beta-Binomial update. A selective-memory observer gives
greater weight to apparent successes than failures and discounts older
observations. In M4–M5, the reputation stock \(\rho_{jt}\) is determined by
outcomes before \(t\), while current hazard \(H_{rt}\) enters the simulated
quote:

\[
\operatorname{WTP}_{jrt}=B(D_{rt})\left[
U^S+V^R(D_{rt})\max(0,\rho_{jt}-H_{rt})\right],
\qquad p_{jrt}=0.8\operatorname{WTP}_{jrt}.
\]

Current apparent success remains natural rainfall after the event. Past
attributed outcomes can therefore create a reputation-mediated price premium and
provider-price heterogeneity without making current price positively associated
with current success. Informational cascades (Bikhchandani et al., 1992) and
reputation under imperfect information (Kreps & Wilson, 1982) provide familiar
economic analogues, but the mechanisms remain calibrated and stylized.

## 3. METHODS

### 3.1. Design and rainfall data

The study uses daily precipitation from 1 January 1991 through 31 December 2020
at eight pre-specified point locations spanning contrasting rainfall regimes.
The points are mechanism stress tests, not identified ritual communities or a
representative global sample. Table 1 reports coordinates, regimes,
observations, and missingness. The analyzed panel contains
87664 region-days.

{{TABLE_1}}

Rainfall was acquired through the Open-Meteo historical archive with the ERA5
model. ERA5 is a global atmospheric reanalysis (Hersbach et al., 2020). Raw JSON
responses are preserved with URLs, UTC retrieval times, byte sizes, and SHA-256
checksums. An initial ERA5-Land request returned complete date arrays but all
precipitation values were null; those snapshots are retained as invalid audit
material and excluded.

### 3.2. Prospective baseline hazard

The years 1991–2010 form the training period and 2011–2020 the evaluation
period. The primary rain-day threshold is 1 mm, with 0.1 and 5 mm sensitivity
thresholds. Apparent success windows are 1, 3, 7, and 14 days. Preceding
dry-spell duration and 30-day rainfall totals use only days before a candidate
event. Candidate dates in both periods are truncated 14 days before the period
boundary so every outcome window has complete follow-up. Training hazards
condition on location, month, and dry-spell bins. This flexible stratification
is used instead of a monotonic duration assumption. Cells with fewer than 20
training days use the corresponding location-month mean. The high-hazard
threshold is the training-cell 75th percentile within location and never uses
evaluation-period rainfall. Duration-based hazards are a descriptive survival
object rather than a treatment response (Cox, 1972).

### 3.3. Known-zero-effect stress tests

Five fictional event rules are constructed from evaluation-period days without
using event-day or future rainfall:

1. a dry-spell threshold;
2. a 30-day rainfall-deficit threshold;
3. a random drought day;
4. a high prospective-hazard threshold; and
5. a season-matched placebo.

Event-day rainfall is unavailable to every rule. Outcomes are always future
observed rainfall, never generated or modified by an event. Rule-specific
apparent success is reported across all thresholds and windows.

### 3.4. Scenario WTP and descriptive association

Scenario WTP increases with drought loss, social utility, and perceived
probability of success. Rainfall and pseudo-event dates in this component are
observed; WTP is constructed from calibrated quantities. We estimate a naive
logit of seven-day apparent success on scenario WTP and a risk-conditioned model
including prospective hazard, drought severity, location, calendar month, and
timing-rule effects. Standard errors are two-way clustered by region-year and
region-rule, allowing arbitrary dependence within the weather-year and
timing-rule series. Because rules can select the same or nearby dates,
attribution windows can overlap, WTP is constructed from calibrated quantities,
and the event is fictional, these regressions are exploratory model-consistent
associations rather than estimates of demand, historical prices, or causal
efficacy.

### 3.5. Staged Monte Carlo model comparison

The simulation samples one observed evaluation-year rainfall sequence per
replication and uses the same sampled region-year across M0–M5. M0–M1
independently permute outcomes within that year to remove calendar structure;
M2–M5 retain the observed local and seasonal ordering. The sequence is a
mechanism decomposition or sequential generative enrichment, not a clean
one-factor causal decomposition: restoring ordering between M1 and M2 changes
multiple properties of the weather process. Each model has
10,000 replications and four providers:

- **M0 Random timing:** exogenous requests and shuffled outcomes.
- **M1 Drought demand:** requests respond to drought, with shuffled outcomes.
- **M2 Realistic hazard:** drought demand operates on local seasonal rainfall.
- **M3 Selective acceptance:** providers condition acceptance on prospective
  hazard.
- **M4 Bayesian reputation:** outcomes update provider beliefs and
  belief-mediated WTP.
- **M5 Selective/recency memory:** successes and failures receive unequal,
  discounted weights.

Primary outputs are event frequency, apparent success, mean scenario price,
provider-mean-price dispersion, event-level price–success difference, reputation
dispersion, provider revenue, community expenditure, provider resource cost,
provider profit, community material-plus-social utility, total social surplus,
and provider-revenue dispersion. Event-level price–success differences are
defined only for replications containing both successes and failures;
event-based quantities are undefined when no event is accepted, and summaries
omit only those undefined cells.

### 3.6. Robustness and falsification

Robustness analysis varies rainfall thresholds and attribution windows, provider
selection slopes, Bayesian prior means, and memory weights. A 1,000-permutation
falsification demeans outcomes and WTP within region–calendar-month–timing-rule
strata, adjusts for hazard and drought severity, and shuffles WTP within the
same strata. Exchangeability is assumed only within those strata. Monte Carlo
precision is evaluated at 500, 1,000, 2,500, 5,000, and 10,000 replications. All
propositions retain unfavorable or mixed results; no parameter was retuned to
manufacture the anticipated sign. P-values are descriptive and exploratory: no
multiplicity adjustment is used, and classifications rely on the full pattern
across observed-weather, falsification, and simulation results rather than a
0.05 threshold. Detailed models, sensitivities, convergence, falsification, and
accounting results are reported in the Supplementary material (Tables S1–S6).

## 4. RESULTS

### 4.1. Baseline hazard is heterogeneous and not monotone in dry-spell duration

Figure 2 shows substantial seasonal and geographic variation in seven-day
rainfall hazards. The ordering of dry-spell bins is not uniformly increasing: a
longer preceding dry spell can coincide with higher, lower, or similar
prospective rainfall probability depending on location and month. The empirical
hazard therefore rejects the shortcut that rain must become mechanically more
likely as a dry spell lengthens.

{{FIGURE_2}}

### 4.2. Raw apparent performance varies under exact zero efficacy

The five event rules produce 2595 fictional events. Table 2
reports counts and success across attribution windows. At the primary seven-day,
1-mm outcome, apparent success is 0.823 for the
rainfall-deficit rule, 0.601 for the dry-spell rule,
0.853 for high prospective hazard, 0.593 for a
random drought day, and 0.600 for the season-matched placebo.

{{TABLE_2}}

Figure 3 emphasizes the mechanism: prospective-hazard selection has the highest
apparent success, whereas drought timing alone does not guarantee a favorable
counterfactual comparison. Every bar is generated by natural rainfall under the
exact zero-effect null.

{{FIGURE_3}}

### 4.3. Selective acceptance changes observed risk composition

Table 3 reports the staged model comparison. Moving from M0 to M1 increases mean
event frequency from 24.36 to 68.95 while apparent success
remains near 0.635 and 0.634. Restoring realistic local and
seasonal rainfall in M2 changes apparent success to 0.493. Selective
acceptance in M3 reduces the number of accepted events to 16.92 and
raises apparent success to 0.676, with rainfall still unchanged. This
M2–M3 contrast shows how the acceptance rule changes accepted-event
composition; it is not an estimate of historical provider behavior.

{{TABLE_3}}

### 4.4. Risk conditioning changes the naive WTP-success association

The naive scenario-WTP coefficient is 0.124 (95% model-based
interval 0.086–0.162). Conditioning on prospective hazard
and drought covariates reduces it to 0.036
(-0.028–0.100). Two-way clustering gives a 95%
interval of -0.039–0.111 across 80 clusters
by region-year and 40 by region-rule (\(n=2595\)).

The adjusted linear-probability coefficient is -0.0319, compared with
a permutation mean of -0.0002 and two-sided \(p=0.002\). The
permutation diagnostic has a negative within-stratum association rather than the
declared positive one. Because it assumes exchangeability within the defined
strata, uses a constructed scenario-WTP regressor, and retains overlapping
outcome windows, it is exploratory rather than confirmatory historical evidence.
Together with the negative mean M4–M5 event-level price–success differences
below, it does not support the general positive price-success proposition.

### 4.5. Reputation and price persist as stocks while current performance remains hazard-driven

M0–M3 use a fixed scenario price of 3.000. Bayesian reputation in M4
generates mean scenario price 3.568, a mean premium of
0.568, reputation dispersion 0.117, and
provider-mean-price dispersion 0.887.
Selective/recency memory in M5 produces 4.610, 1.610,
0.138, and 1.373, respectively. These are
calibrated simulation quantities, not historical currencies or estimates.

Contrary to a simple performance-pricing story, the mean event-level
price(success)-price(failure) difference is -2.447 in M4 and
-3.037 in M5. Thus mean price relative to baseline, provider price
heterogeneity, and a reputation-mediated premium can all be positive while the
contemporaneous price-success difference is negative. Past attributed outcomes
enter the reputation stock, whereas current apparent success remains a flow from
current natural hazard.

Figure 4 visualizes these margins. Drought demand expands event frequency;
provider selection changes accepted-event composition and current success;
learning creates reputation and provider-price dispersion; and price premia
coexist with negative mean contemporaneous price-success differences.

{{FIGURE_4}}

### 4.6. Findings are stable across thresholds, parameters, and replication counts

Figure 5A shows that apparent success increases with the attribution window and
falls with the rainfall threshold, as expected from the definition. Figure 5B
shows monotonic increases in M3 apparent success as the selection slope rises
from 2 to 8. M4 prices increase with the Bayesian prior mean, and M5 prices
increase with stronger selective memory. Figure 5C shows falling Monte Carlo
standard errors; at 10,000 replications, apparent-success standard errors are at
most 0.0028 among the six main models.

{{FIGURE_5}}

Table 4 classifies the analytic propositions by evidence domain. Natural-rainfall
apparent success is demonstrated with observed weather, whereas selective
acceptance is demonstrated in the model using observed weather. Demand, WTP,
learning, and memory results are model- or calibration-contingent; the
price–success proposition is not supported; and the separation of
meteorological from social value is a logical distinction rather than an
empirical finding.

{{TABLE_4}}

## 5. DISCUSSION

### 5.1. Selective exposure can masquerade as performance

The QJE comparator already establishes that endogenous prayer timing, changing
rainfall hazards, hidden counterfactuals, and strategic leader timing can make
an ineffective practice persuasive (Espín-Sánchez et al., 2026). Our narrower
extension separates requests from acceptance and adds multiple provider
identities, provider-specific reputation stocks, simulated provider prices, and
explicit accounting.

Scarcity changes who requests action and when; the calibrated provider rule
changes which requests become accepted events; attribution maps natural rainfall
into apparent success; and learning maps past outcomes into reputation. Demand
can increase without success changing. Selection can increase current success
without treatment. Reputation can persist without provider-specific efficacy.
Price premia can arise without positive contemporaneous price-success
associations.

### 5.2. Raw performance versus risk-adjusted performance

When baseline risk is heterogeneous and exposure is selective, raw outcome rates
answer the wrong question. They combine the baseline risk of accepted cases, the
selection rule, and any causal effect; this benchmark fixes the last term at
zero, so the apparent provider differences arise entirely from the first two plus
attribution and learning. Risk adjustment exists precisely because evaluators
who ignore baseline differences reward favorable case mix rather than
performance (Shahian & Normand, 2008), and public scorecards have induced
selection rather than improvement in other settings (Dranove et al., 2003;
Werner & Asch, 2005). Prospective hazard estimates like ours supply the
conditioning variable such an adjustment would need—but they condition on a
limited state vector and do not identify causal effects by themselves.

### 5.3. Reputation is a stock; current outcome is a risk-conditioned flow

The unfavorable price result is substantively informative. In the
observed-weather scenario, the adjusted logit point estimate is positive, but
the two-way clustered interval includes zero; the exploratory within-stratum
permutation diagnostic is negative. In M4 and M5, mean event-level
price-success differences are also negative, although their Monte Carlo
percentile intervals include positive values. Reputation is a stock formed from
earlier attributed outcomes, whereas current apparent success is a flow
generated by current hazard. A high-reputation provider can charge more when the
reputation-hazard gap is large and still encounter unfavorable natural rainfall.

This is a boundary condition, not a defect to be removed by retuning. Mean
prices, provider-price heterogeneity, and reputation premia can reflect
accumulated belief without identifying current causal performance. The
findings motivate comparing provider outcomes with prospective risk-adjusted
benchmarks rather than raw success, and separating reputation from current
causal performance rather than treating it as its measure.

### 5.4. Decision and institutional implications

For provider scorecards and public performance reporting, the benchmark warns
that raw outcome comparisons can reward selective acceptance and favorable
exposure; risk-adjustment and disclosure of baseline hazard—and of rejected
cases—may serve as candidate safeguards (Dranove et al., 2003; Werner & Asch, 2005;
Shahian & Normand, 2008). The same structure applies wherever agents choose
cases or exposure and are judged on raw outcomes: environmental-service
contracts in which payments follow post-intervention observations, expert
forecasting scored without conditioning on task difficulty (Murphy, 1993), and
performance contracts with hidden counterfactuals. For empirical evaluation,
the framework suggests estimating prospective natural hazards, excluding
event-day information from timing rules, modeling selection into observed
events, and distinguishing apparent outcomes from causal effects. These implications are
inferences from a calibrated benchmark; we do not claim the safeguards were
empirically tested.

### 5.5. Limitations

First, the eight locations are point-based stress tests. They span major
rainfall regimes but do not establish global representativeness and are not
matched to historical ritual communities. Spatially distributed precipitation,
forecast information, and measurement error could alter hazards.

Second, the WTP, prices, costs, provider count, acceptance function, and
observer rules are calibrated scenarios. They are not estimates of historical
beliefs or payment schedules. Historical sources support the institutional
relevance of rainmaking but not a universal claim of drought-contingent fee
escalation (Espín-Sánchez & Gil-Guirado, 2022; Akong'a, 1987; Semenya, 2013).

Third, the hazard estimator conditions on a limited state vector. A provider
could use richer forecasts, cloud observations, or local environmental
knowledge. Such information would likely strengthen selection possibilities,
but its effect is not estimated here.

Fourth, apparent success is defined by fixed rainfall thresholds and windows.
The robustness grid demonstrates sensitivity expected from that definition, not
a uniquely correct cultural attribution rule.

Fifth, pseudo-event rules can select identical or nearby dates, observer states
persist over time, and attribution windows overlap. Two-way clustered covariance
addresses dependence within region-years and region-rule series, but the
scenario-WTP regressions remain exploratory and no multiplicity-adjusted
confirmatory test is claimed.

Sixth, social utility is separated conceptually but not empirically measured.
The analysis rejects the logical equivalence between meteorological and social
value; it does not demonstrate that every ritual creates positive welfare.

Finally, a zero-effect design is intentionally a limiting case. It establishes
what demand, selection, attribution, and learning can generate without efficacy.
It cannot show that real-world environmental interventions are ineffective.

## 6. CONCLUSION

When providers choose their exposure, raw outcome rates combine baseline risk,
selection, and causal performance. Under an exact zero-effect null, the causal
term is removed and the remaining machinery still produces apparent
performance: natural rainfall generates apparent success, drought-driven demand
determines when communities seek action, selective acceptance shifts observed
risk composition, attribution turns subsequent rain into perceived performance,
and learning turns perceived performance into persistent reputation and price
premia.

The positive contemporaneous price-success proposition is not supported:
reputation-mediated mean prices and provider-price heterogeneity coexist with
negative mean event-level price-success differences, because reputation is a
stock of past attributed outcomes while current performance is a hazard-driven
flow. For credible performance evaluation under heterogeneous environmental
risk, the findings motivate prospective risk adjustment, disclosure of the case
mix that was not accepted, and separation of natural performance, causal
performance, scenario price, transfers, costs, and plural values.

## Acknowledgements

[AUTHOR INPUT REQUIRED: provide acknowledgements or confirm that none are
required.]

## Declarations

### Data and code availability

Code, legally redistributable inputs, frozen analytical outputs, and
manuscript-generation files are publicly available at
https://github.com/bougtoir/pricing-the-rain. The repository preserves raw
rainfall snapshots with machine-readable acquisition ledgers and checksums.
Sources whose redistribution rights are unclear are not redistributed; the
ledgers provide URLs, checksums, status notes, and retrieval instructions
instead. Fictional pseudo-events and all simulation outputs are reproducible
from the archived rainfall snapshots.

### Funding

[AUTHOR INPUT REQUIRED: identify funding sources or state that no specific
funding was received.]

### Competing interests

[AUTHOR INPUT REQUIRED: declare competing interests or state that none exist.]

### Author contributions

[AUTHOR INPUT REQUIRED: provide CRediT roles for each author.]

### Ethics

The study uses public environmental data, bibliographic metadata, and simulated
fictional events. It includes no human participants, personal data, or animal
research.

### Generative AI disclosure

During preparation of this work, the authors used Devin (Cognition AI) to assist
with code development, manuscript drafting, and language organization. [AUTHOR
CONFIRMATION REQUIRED: after using this tool, the authors reviewed and edited
the content as needed and take full responsibility for the content of the
publication.] No generative-AI image tool was used to create or alter the
scientific figures, and no generative AI was used to fabricate data or
references.

## References

Akong'a, J. (1987). Rainmaking rituals: A comparative study of two Kenyan societies. *African Study Monographs*, *8*(2), 71–85. https://doi.org/10.14989/68028

Barnett, A. G. (2004). Regression to the mean: what it is and how to deal with it. *International Journal of Epidemiology*, *34*(1), 215-220. https://doi.org/10.1093/ije/dyh299

Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades. *Journal of Political Economy*, *100*(5), 992-1026. https://doi.org/10.1086/261849

Chan, K. M. A., Satterfield, T., & Goldstein, J. (2012). Rethinking ecosystem services to better address and navigate cultural values. *Ecological Economics*, *74*, 8-18. https://doi.org/10.1016/j.ecolecon.2011.11.011

Cox, D. R. (1972). Regression Models and Life-Tables. *Journal of the Royal Statistical Society Series B: Statistical Methodology*, *34*(2), 187-202. https://doi.org/10.1111/j.2517-6161.1972.tb00899.x

Dranove, D., Kessler, D., McClellan, M., & Satterthwaite, M. (2003). Is More Information Better? The Effects of “Report Cards” on Health Care Providers. *Journal of Political Economy*, *111*(3), 555-588. https://doi.org/10.1086/374180

Espín-Sánchez, J. A., & Gil-Guirado, S. (2022). Praying for rain, resilience, and social stability in Murcia (southeast Spain). *Ecology and Society*, *27*(2). https://doi.org/10.5751/es-12875-270209

Espín-Sánchez, J. A., Gil-Guirado, S., & Ryan, N. (2026). Praying for Rain. *The Quarterly Journal of Economics*, *141*(3), 2363-2422. https://doi.org/10.1093/qje/qjag026

Heckman, J. J. (1979). Sample Selection Bias as a Specification Error. *Econometrica*, *47*(1), 153. https://doi.org/10.2307/1912352

Hensher, D., Shore, N., & Train, K. (2006). Water Supply Security and Willingness to Pay to Avoid Drought Restrictions. *Economic Record*, *82*(256), 56-66. https://doi.org/10.1111/j.1475-4932.2006.00293.x

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz‐Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A., Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G., Bidlot, J., Bonavita, M., …, Thépaut, J. N. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, *146*(730), 1999-2049. https://doi.org/10.1002/qj.3803

Himes, A., & Muraca, B. (2018). Relational values: the key to pluralistic valuation of ecosystem services. *Current Opinion in Environmental Sustainability*, *35*, 1-7. https://doi.org/10.1016/j.cosust.2018.09.005

Kenter, J. O., O'Brien, L., Hockley, N., Ravenscroft, N., Fazey, I., Irvine, K. N., Reed, M. S., Christie, M., Brady, E., Bryce, R., Church, A., Cooper, N., Davies, A., Evely, A., Everard, M., Fish, R., Fisher, J. A., Jobstvogt, N., Molloy, C., …, Williams, S. (2015). What are shared and social values of ecosystems? *Ecological Economics*, *111*, 86-99. https://doi.org/10.1016/j.ecolecon.2015.01.006

Kreps, D. M., & Wilson, R. (1982). Reputation and imperfect information. *Journal of Economic Theory*, *27*(2), 253-279. https://doi.org/10.1016/0022-0531(82)90030-8

Murphy, A. H. (1993). What Is a Good Forecast? An Essay on the Nature of Goodness in Weather Forecasting. *Weather and Forecasting*, *8*(2), 281-293. https://doi.org/10.1175/1520-0434(1993)008<0281:wiagfa>2.0.co;2

Pascual, U., Balvanera, P., Díaz, S., Pataki, G., Roth, E., Stenseke, M., Watson, R. T., Başak Dessane, E., Islar, M., Kelemen, E., Maris, V., Quaas, M., Subramanian, S. M., Wittmer, H., Adlan, A., Ahn, S., Al-Hafedh, Y. S., Amankwah, E., Asah, S. T., …, Yagi, N. (2017). Valuing nature’s contributions to people: the IPBES approach. *Current Opinion in Environmental Sustainability*, *26-27*, 7-16. https://doi.org/10.1016/j.cosust.2016.12.006

Pattanayak, S. K., & Kramer, R. A. (2001). Pricing ecological services: Willingness to pay for drought mitigation from watershed protection in eastern Indonesia. *Water Resources Research*, *37*(3), 771-778. https://doi.org/10.1029/2000wr900320

Schrieks, T., Botzen, W. J. W., Haer, T., & Aerts, J. C. J. H. (2025). Preferences for drought risk adaptation support in Kenya: Evidence from a discrete choice experiment and three decision-making theories. *Ecological Economics*, *227*, 108425. https://doi.org/10.1016/j.ecolecon.2024.108425

Semenya, D. K. (2013). The making and prevention of rain amongst the Pedi tribe of South Africa: A pastoral response. *HTS Teologiese Studies / Theological Studies*, *69*(1). https://doi.org/10.4102/hts.v69i1.1175

Shahian, D. M., & Normand, S. L. T. (2008). Comparison of “Risk-Adjusted” Hospital Outcomes. *Circulation*, *117*(15), 1955-1963. https://doi.org/10.1161/circulationaha.107.747873

Skinner, B. F. (1948). 'Superstition' in the pigeon. *Journal of Experimental Psychology*, *38*(2), 168-172. https://doi.org/10.1037/h0055873

Tversky, A., & Kahneman, D. (1974). Judgment under Uncertainty: Heuristics and Biases. *Science*, *185*(4157), 1124-1131. https://doi.org/10.1126/science.185.4157.1124

Werner, R. M., & Asch, D. A. (2005). The unintended consequences of publicly reporting quality information. *JAMA*, *293*(10), 1239–1244. https://doi.org/10.1001/jama.293.10.1239
