# Pricing Apparent Environmental Performance: Strategic Selection and Reputation under a Zero-Effect Rainfall Null

## Abstract

Environmental providers may be evaluated when natural hazards vary, providers select
requests, and untreated counterfactuals are hidden. We impose an exact zero-effect null,
\(R(1)=R(0)\), and use daily ERA5 precipitation for eight pre-specified climate stress
tests to estimate prospective hazards and construct fictional observed-weather
pseudo-events. A separate calibrated Monte Carlo model adds drought-driven demand,
strategic acceptance, scenario willingness to pay (WTP), Bayesian reputation, and
selective memory. Among {{TOTAL_PSEUDO_EVENTS}} pseudo-events, seven-day apparent success
is {{RANDOM_SUCCESS_7D}} under random drought timing and {{HAZARD_SUCCESS_7D}} under
high prospective hazard. Strategic acceptance changes accepted-event composition and
raises mean simulated apparent success from {{M2_SUCCESS}} to {{M3_SUCCESS}} without
changing rainfall. Reputation models generate mean scenario prices of {{M4_PRICE}} and
{{M5_PRICE}}, above the fixed {{FIXED_PRICE}} baseline, yet mean contemporaneous
price-success differences are {{M4_PRICE_SUCCESS}} and {{M5_PRICE_SUCCESS}}. The
cluster-robust scenario-WTP interval includes zero, and an exploratory within-stratum
permutation diagnostic is negative. WTP and prices are calibrated or simulated, not
historical estimates. The ecological-economic contribution is a stock-flow result:
past attributed outcomes support reputation and price, while current apparent
performance remains a natural-rainfall flow governed by current ecological hazard.

**Keywords:** attribution; ecological-economic modelling; environmental uncertainty;
rainfall hazard; reputation; strategic selection; valuation

## 1. Introduction

Environmental decisions are frequently made under uncertainty about both natural
processes and causal counterfactuals. A drought intensifies demand for action at the
same time that seasonal rainfall probabilities change. Providers may select when and
where to act. Communities observe what happened after an intervention but not what
would have happened without it. Prices, beliefs, and reputations can therefore respond
to an outcome process that the intervention never changed.

Rainmaking offers a sharp stress test. Espín-Sánchez, Gil-Guirado, and Ryan develop an
instrumental-belief account in which leaders cannot produce rain, drought timing and
changing rainfall hazards make prayer persuasive, untreated outcomes are hidden, and
persuasive practices can persist [1]. Their evidence includes long-run Murcia records
and a large cross-cultural classification, and their theory discusses tangible
benefits, support costs, and a strategic-timing alternative.
Historical evidence also places rain-prayer institutions within broader problems of
scarcity, resilience, and social stability [2]. Comparative ethnography describes
rainmaking responses to rainfall scarcity or unreliability and their socio-psychological
implications [3], while other accounts document specialized roles and stated payments
[4]. These sources support institutional plausibility, not a universal law that
providers screened requests or raised fees with drought. Prices and acceptance
strategies below are therefore calibrated scenarios rather than reconstructed history.

The attribution problem is broader than rainmaking. Interventions are often initiated
after unusually adverse conditions, creating regression-to-the-mean risk [5].
Observers use heuristics under uncertainty [6], and reinforcement can sustain beliefs
when outcomes occur intermittently [7]. In environmental governance, a narrow monetary
metric can additionally obscure cultural ecosystem services [8], shared and social
values [9], and political choices embedded in valuation [10]. Nature's contributions
are plural [11]; integrated valuation should preserve diverse value domains [12], and
relational values need not be reducible to instrumental willingness to pay (WTP) [13].

We develop a qualified extension rather than another timing explanation. Requests and
accepted events are separated; multiple providers differ in selectivity; past
attributed outcomes create provider-specific reputation stocks; those stocks interact
with current hazard in simulated WTP and price; and transfers, resource costs, profit,
surplus, and non-monetary value are separately accounted. The principal boundary result
is unfavorable to a simple performance-pricing story: reputation-mediated price premia
coexist with zero or negative mean contemporaneous price-success differences.

Four distinctions organize the analysis. First, causal efficacy is a potential-outcome
contrast, whereas apparent success is rainfall inside an attribution window. Second,
baseline rainfall hazard is an ecological probability, not evidence of treatment
response. Third, mean scenario price, provider-price heterogeneity, a
reputation-mediated premium, and the contemporaneous price-success association are
different objects. Fourth, the economic value of rainfall, intervention-created
rainfall value, scenario WTP, a theoretical revenue-maximizing price, expenditure
transfers, resource costs, and social or relational value are not interchangeable.

We examine eight declared analytic propositions: natural rainfall can generate apparent
success; drought-driven demand increases intervention frequency; drought can increase
scenario WTP; strategic acceptance increases apparent success; higher prices are
positively associated with apparent success; learning creates persistent provider
differentiation; selective memory raises price premia; and zero meteorological
efficacy does not logically imply zero social value.

## 2. Conceptual framework

Figure 1 represents the data-generating system. Natural rainfall generates
environmental scarcity. Scarcity affects requests and valuation; providers may accept
requests using prospective hazard information; observed rainfall becomes apparent
success; and apparent success updates belief and reputation. The dashed separation is
the central exclusion: there is no causal arrow from the pseudo-event to rainfall.

{{FIGURE_1}}

### 2.1 Exact zero-effect null

For location \(r\), day \(t\), and pseudo-intervention indicator \(A_{rt}\), let
\(R_{rt}(a)\) denote potential rainfall under \(a \in \{0,1\}\). The simulation enforces

\[
R_{rt}(1)=R_{rt}(0)=R_{rt}.
\]

No request, acceptance, provider, price, belief, or reputation variable changes this
array. Apparent success for window \(w\) and rainfall threshold \(c\) is

\[
S_{rt}(w,c)=\mathbf{1}\left\{\max_{j=1,\ldots,w}R_{r,t+j}\geq c\right\}.
\]

The event day is excluded. This definition captures a plausible retrospective
attribution rule but is not an estimator of a treatment effect.

### 2.2 Environmental hazard, demand, and selection

Let \(H_{rt}(w,c)\) be the prospective probability of apparent success conditional on
location, calendar month, and the preceding dry spell. We estimate this hazard from a
training period rather than assume it rises with drought duration. Provider \(k\)
observes a signal of \(H_{rt}\) and accepts a request with a probability increasing in
that signal. Selection can therefore raise the success rate among accepted events even
though it cannot change rainfall.

Drought affects demand separately from selection. A community is more likely to
request action when the preceding dry spell is long or the rolling rainfall deficit is
large. This changes the timing and frequency of observed events. It does not imply that
rain is more likely merely because the dry spell is longer.

### 2.3 Valuation, price, and reputation

Scenario WTP combines an instrumental component related to expected avoided drought
loss with a separate social-utility component. This construction is motivated by
empirical evidence that people value drought-risk adaptation and supply security
[14–16], but its numerical scale is not estimated from historical rainmaking payments.
Payments are transfers from communities to providers; provider costs are resource
costs; profit is revenue minus those costs. Because the pseudo-intervention creates no
rainfall, its actuarially fair causal rainfall price is zero. The theoretical
revenue-maximizing price is also distinct from the implemented quote, which is a fixed
share of calibrated WTP.

Observers update provider beliefs only after accepted events. A Bayesian observer
applies a Beta-Binomial update. A selective-memory observer gives greater weight to
apparent successes than failures and discounts older observations. In M4–M5, the
reputation stock \(\rho_{jt}\) is determined by outcomes before \(t\), while current
hazard \(H_{rt}\) enters the simulated quote:

\[
\operatorname{WTP}_{jrt}=B(D_{rt})\left[
U^S+V^R(D_{rt})\max(0,\rho_{jt}-H_{rt})\right],
\qquad p_{jrt}=0.8\operatorname{WTP}_{jrt}.
\]

Current apparent success remains natural rainfall after the event. Past attributed
outcomes can therefore create a reputation-mediated price premium and provider-price
heterogeneity without making current price positively associated with current success.
Informational cascades [17] and reputation under imperfect information [18] provide
familiar economic analogues, but the mechanisms remain calibrated and stylized.

## 3. Methods

### 3.1 Design and rainfall data

The study uses daily precipitation from 1 January 1991 through 31 December 2020 at
eight pre-specified point locations spanning contrasting rainfall regimes. The points
are mechanism stress tests, not identified ritual communities or a representative
global sample. Table 1 reports coordinates, regimes, observations, and missingness.
The analyzed panel contains {{TOTAL_REGION_DAYS}} region-days.

{{TABLE_1}}

Rainfall was acquired through the Open-Meteo historical archive with the ERA5 model.
ERA5 is a global atmospheric reanalysis [19]. Raw JSON responses are preserved with
URLs, UTC retrieval times, byte sizes, and SHA-256 checksums. An initial ERA5-Land
request returned complete date arrays but all precipitation values were null; those
snapshots are retained as invalid audit material and excluded.

### 3.2 Prospective rainfall hazard

The years 1991–2010 form the training period and 2011–2020 the evaluation period. The
primary rain-day threshold is 1 mm, with 0.1 and 5 mm sensitivity thresholds. Apparent
success windows are 1, 3, 7, and 14 days. Preceding dry-spell duration and 30-day
rainfall totals use only days before a candidate event. Candidate dates in both periods
are truncated 14 days before the period boundary so every outcome window has complete
follow-up. Training hazards condition on location, month, and dry-spell bins. This
flexible stratification is used instead of a monotonic duration assumption. Cells with
fewer than 20 training days use the corresponding location-month mean. The high-hazard
threshold is the training-cell 75th percentile within location and never uses
evaluation-period rainfall. Duration-based hazards are a descriptive survival object
rather than a treatment response [20].

### 3.3 Observed-weather pseudo-events

Five fictional event rules are constructed from evaluation-period days without using
event-day or future rainfall:

1. a dry-spell threshold;
2. a 30-day rainfall-deficit threshold;
3. a random drought day;
4. a high prospective-hazard threshold; and
5. a season-matched placebo.

Event-day rainfall is unavailable to every rule. Outcomes are always future observed
rainfall, never generated or modified by an event. Rule-specific apparent success is
reported across all thresholds and windows.

### 3.4 Scenario WTP and descriptive association

Scenario WTP increases with drought loss, social utility, and perceived probability of
success. Rainfall and pseudo-event dates in this component are observed; WTP is
constructed from calibrated quantities. We estimate a naive logit of seven-day apparent
success on scenario WTP and a hazard-adjusted model including prospective hazard,
drought severity, location, calendar month, and timing-rule effects. Standard errors are
two-way clustered by region-year and region-rule, allowing arbitrary dependence within
the weather-year and timing-rule series.
Because rules can select the same or nearby dates, attribution windows can overlap, WTP
is constructed from calibrated quantities, and the event is fictional, these
regressions are exploratory model-consistent associations rather than estimates of
demand, historical prices, or causal efficacy.

### 3.5 Staged Monte Carlo model comparison

The simulation samples one observed evaluation-year rainfall sequence per replication
and uses the same sampled region-year across M0–M5. M0–M1 independently permute
outcomes within that year to remove calendar structure; M2–M5 retain the observed
local and seasonal ordering. The sequence is a mechanism decomposition or sequential
generative enrichment, not a clean one-factor causal decomposition: restoring ordering
between M1 and M2 changes multiple properties of the weather process. Each model has
{{SIM_REPLICATIONS}} replications and four providers:

- **M0 Random timing:** exogenous requests and shuffled outcomes.
- **M1 Drought demand:** requests respond to drought, with shuffled outcomes.
- **M2 Realistic hazard:** drought demand operates on local seasonal rainfall.
- **M3 Strategic selection:** providers condition acceptance on prospective hazard.
- **M4 Bayesian reputation:** outcomes update provider beliefs and belief-mediated WTP.
- **M5 Selective/recency memory:** successes and failures receive unequal, discounted
  weights.

Primary outputs are event frequency, apparent success, mean scenario price,
provider-mean-price dispersion, event-level price–success difference, reputation
dispersion, provider revenue, community expenditure, provider resource cost, provider
profit, community material-plus-social utility, total social surplus, and
provider-revenue dispersion. Event-level price–success differences are defined only for
replications containing both successes and failures; event-based quantities are
undefined when no event is accepted, and summaries omit only those undefined cells.

### 3.6 Robustness and falsification

Robustness analysis varies rainfall thresholds and attribution windows, provider
selection slopes, Bayesian prior means, and memory weights. A 1,000-permutation
falsification demeans outcomes and WTP within region–calendar-month–timing-rule strata,
adjusts for hazard and drought severity, and shuffles WTP within the same strata.
Exchangeability is assumed only within those strata.
Monte Carlo
precision is evaluated at 500, 1,000, 2,500, 5,000, and 10,000 replications. All
propositions retain unfavorable or mixed results; no parameter was retuned to
manufacture the anticipated sign. P-values are descriptive and exploratory: no
multiplicity adjustment is used, and classifications rely on the full pattern across
observed-weather, falsification, and simulation results rather than a 0.05 threshold.
Detailed models, sensitivities, convergence, falsification, and accounting results are
reported in the Supplementary material (Tables S1–S6).

## 4. Results

### 4.1 Estimated hazards are not mechanically increasing in dry-spell duration

Figure 2 shows substantial seasonal and geographic variation in seven-day rainfall
hazards. The ordering of dry-spell bins is not uniformly increasing: a longer preceding
dry spell can coincide with higher, lower, or similar prospective rainfall probability
depending on location and month. The empirical hazard therefore rejects the shortcut
that rain must become mechanically more likely as a dry spell lengthens.

{{FIGURE_2}}

### 4.2 Natural rainfall generates apparent success

The five event rules produce {{TOTAL_PSEUDO_EVENTS}} fictional events. Table 2 reports
counts and success across attribution windows. At the primary seven-day, 1-mm outcome,
apparent success is {{DEFICIT_SUCCESS_7D}} for the rainfall-deficit rule,
{{DRYSPELL_SUCCESS_7D}} for the dry-spell rule, {{HAZARD_SUCCESS_7D}} for high
prospective hazard, {{RANDOM_SUCCESS_7D}} for a random drought day, and
{{PLACEBO_SUCCESS_7D}} for the season-matched placebo.

{{TABLE_2}}

Figure 3 emphasizes the mechanism: prospective-hazard selection has the highest
apparent success, whereas drought timing alone does not guarantee a favorable
counterfactual comparison. Every bar is generated by natural rainfall under the exact
zero-effect null.

{{FIGURE_3}}

### 4.3 Scenario WTP varies with drought, but positive price evidence fails

The naive scenario-WTP coefficient is {{NAIVE_WTP_COEF}} (95% model-based interval
{{NAIVE_CI_LOW}}–{{NAIVE_CI_HIGH}}). Adjustment for prospective hazard and drought
covariates reduces it to {{ADJUSTED_WTP_COEF}} ({{ADJUSTED_CI_LOW}}–
{{ADJUSTED_CI_HIGH}}). Two-way clustering gives a 95% interval of
{{CLUSTER_CI_LOW}}–{{CLUSTER_CI_HIGH}} across {{CLUSTERS}} clusters
by region-year and {{RULE_CLUSTERS}} by region-rule (\(n={{REGRESSION_N}}\)).

The adjusted linear-probability coefficient is {{PERM_OBSERVED}}, compared with a
permutation mean of {{PERM_MEAN}} and two-sided \(p={{PERMUTATION_P}}\). The permutation
diagnostic has a negative within-stratum association rather than the declared positive
one. Because it assumes exchangeability within the defined strata, uses a constructed
scenario-WTP regressor, and retains overlapping outcome windows, it is exploratory
rather than confirmatory historical evidence. Together with the negative mean M4–M5
event-level price–success differences, it does not support the general positive
price-success proposition.

### 4.4 Demand, selection, and learning have distinct effects

Table 3 reports the staged model comparison. Moving from M0 to M1 increases mean event
frequency from {{M0_EVENTS}} to {{M1_EVENTS}} while apparent success remains near
{{M0_SUCCESS}} and {{M1_SUCCESS}}. Restoring realistic local and seasonal rainfall in
M2 changes apparent success to {{M2_SUCCESS}}. Strategic acceptance in M3 reduces the
number of accepted events to {{M3_EVENTS}} and raises apparent success to
{{M3_SUCCESS}}, with rainfall still unchanged. This M2–M3 contrast shows how the
acceptance rule changes accepted-event composition; it is not an estimate of historical
provider behavior.

{{TABLE_3}}

M0–M3 use a fixed scenario price of {{FIXED_PRICE}}. Bayesian reputation in M4
generates mean scenario price {{M4_PRICE}}, a mean premium of {{M4_PRICE_PREMIUM}},
reputation dispersion {{M4_REPUTATION}}, and provider-mean-price dispersion
{{M4_PROVIDER_PRICE_DISPERSION}}. Selective/recency memory in M5 produces
{{M5_PRICE}}, {{M5_PRICE_PREMIUM}}, {{M5_REPUTATION}}, and
{{M5_PROVIDER_PRICE_DISPERSION}}, respectively. These are calibrated simulation
quantities, not historical currencies or estimates.

Contrary to a simple performance-pricing story, the mean event-level
price(success)-price(failure) difference is {{M4_PRICE_SUCCESS}} in M4 and
{{M5_PRICE_SUCCESS}} in M5. Thus mean price relative to baseline, provider price
heterogeneity, and a reputation-mediated premium can all be positive while the
contemporaneous price-success difference is negative. Past attributed outcomes enter
the reputation stock, whereas current apparent success remains a flow from current
natural hazard.

Figure 4 visualizes these margins. Drought demand expands event frequency; provider
selection changes accepted-event composition and current success; learning creates
reputation and provider-price dispersion; and price premia coexist with negative mean
contemporaneous price-success differences.

{{FIGURE_4}}

### 4.5 Findings are stable across thresholds, parameters, and replication counts

Figure 5A shows that apparent success increases with the attribution window and falls
with the rainfall threshold, as expected from the definition. Figure 5B shows
monotonic increases in M3 apparent success as the selection slope rises from 2 to 8.
M4 prices increase with the Bayesian prior mean, and M5 prices increase with stronger
selective memory. Figure 5C shows falling Monte Carlo standard errors; at 10,000
replications, apparent-success standard errors are at most {{MAX_SUCCESS_MCSE}} among
the six main models.

{{FIGURE_5}}

Table 4 classifies the analytic propositions by evidence domain. Natural-rainfall
apparent success is demonstrated with observed weather, whereas strategic selection
is demonstrated in the model using observed weather. Demand, WTP, learning, and memory
results are model- or calibration-contingent; the price–success proposition is not
supported; and the separation of meteorological from social value is a logical
distinction rather than an empirical finding.

{{TABLE_4}}

## 5. Discussion

### 5.1 Selection and stock-flow feedback extend the timing account

The QJE comparator already establishes that endogenous prayer timing, changing rainfall
hazards, hidden counterfactuals, and strategic leader timing can make an ineffective
practice persuasive [1]. Our narrower extension separates requests from acceptance and
adds multiple provider identities, provider-specific reputation stocks, simulated
provider prices, and explicit economic accounting.

Scarcity changes who requests action and when; the calibrated provider rule changes
which requests become accepted events; attribution maps natural rainfall into apparent
success; and learning maps past outcomes into reputation. Demand can increase without
success changing. Selection can increase current success without treatment. Reputation
can persist without provider-specific efficacy. Price premia can arise without positive
contemporaneous price-success associations.

### 5.2 Ecological-economic interpretation

The ecological component is not background noise. Seasonal and local rainfall hazards
determine the opportunity set in which economic and institutional behavior operates.
In the model, a provider who selectively accepts high-hazard requests can monetize
information about nature without producing rainfall. A community that pays more during
scarcity expresses a value of relief, coordination, or hope, but the transfer does not
establish that the intervention created the environmental service.

This distinction matters for environmental valuation. The economic value of rainfall
can be high, while the causal rainfall value of a zero-effect intervention is zero.
Scenario WTP can be positive because it incorporates perceived efficacy or separate
social utility. The theoretical revenue-maximizing price is distinct from the
implemented quote, and neither is a historical estimate. Community expenditure and
provider revenue are the two sides of a transfer; provider cost is a resource cost;
profit and social surplus apply different accounting boundaries. Collapsing these
objects into a single “value” would obscure both welfare and causality.

Plural valuation further limits what can be concluded from the null. Cultural,
relational, psychological, coordination, and solidarity values may be real without
meteorological efficacy [8–13]. Our model includes a separate social-utility term to
prevent an invalid inference from “no rain effect” to “no social value.” We do not
estimate that term or claim that it represents any particular community.

### 5.3 Why price premia do not imply positive price–success associations

The unfavorable price result is substantively informative. In the observed-weather
scenario, the adjusted logit point estimate is positive, but the two-way clustered
interval includes zero; the exploratory within-stratum permutation diagnostic is
negative. In M4 and M5, mean event-level price-success differences are also negative,
although their Monte Carlo percentile intervals include positive values. Reputation is
a stock formed from earlier attributed outcomes, whereas current apparent success is a
flow generated by current hazard. A high-reputation provider can charge more when the
reputation-hazard gap is large and still encounter unfavorable natural rainfall.

This is a boundary condition, not a defect to be removed by retuning. Mean prices,
provider-price heterogeneity, and reputation premia can reflect accumulated belief
without identifying current causal performance. Evaluators should compare provider
outcomes with prospective risk-adjusted benchmarks rather than raw success.

### 5.4 Limitations

First, the eight locations are point-based stress tests. They span major rainfall
regimes but do not establish global representativeness and are not matched to historical
ritual communities. Spatially distributed precipitation, forecast information, and
measurement error could alter hazards.

Second, the WTP, prices, costs, provider count, acceptance function, and observer rules
are calibrated scenarios. They are not estimates of historical beliefs or payment
schedules. Historical sources support the institutional relevance of rainmaking but
not a universal claim of drought-contingent fee escalation [2–4].

Third, the hazard estimator conditions on a limited state vector. A provider could use
richer forecasts, cloud observations, or local ecological knowledge. Such information
would likely strengthen selection possibilities, but its effect is not estimated here.

Fourth, apparent success is defined by fixed rainfall thresholds and windows. The
robustness grid demonstrates sensitivity expected from that definition, not a uniquely
correct cultural attribution rule.

Fifth, pseudo-event rules can select identical or nearby dates, observer states persist
over time, and attribution windows overlap. Two-way clustered covariance addresses
dependence within region-years and region-rule series, but the scenario-WTP regressions
remain exploratory and no multiplicity-adjusted confirmatory test is claimed.

Sixth, social utility is separated conceptually but not empirically measured. The
analysis rejects the logical equivalence between meteorological and social value; it
does not demonstrate that every ritual creates positive welfare.

Finally, a zero-effect design is intentionally a limiting case. It establishes what
timing, selection, and learning can generate without efficacy. It cannot show that all
real-world environmental interventions are ineffective.

### 5.5 Implications

For empirical research, event studies of environmental interventions should estimate
prospective natural hazards, exclude event-day information from timing rules, model
selection into observed events, and distinguish apparent outcomes from causal effects.
Negative controls and within-season permutations can reveal residual structure but do
not replace a credible counterfactual.

For policy and market design, provider performance measures should be risk-adjusted.
Reputation systems based on raw success can reward selective acceptance and favorable
ecological exposure. Transparent disclosure of baseline hazard and rejected requests
would reduce this distortion.

For ecological economics, the framework illustrates why environmental valuation needs
both causal accounting and value pluralism. Monetary demand can be behaviorally real
yet causally misattributed; non-monetary value can be meaningful yet absent from market
prices. Keeping these dimensions separate permits a more respectful and analytically
coherent evaluation.

## 6. Conclusion

Under an exact zero-effect null, natural rainfall still produces apparent success.
Drought-driven demand determines when communities seek action; strategic providers can
select favorable ecological states; attribution turns subsequent rain into perceived
performance; and learning turns perceived performance into persistent reputation and
price premia. None of these processes requires the intervention to change rainfall.

The strongest conclusion is therefore not that price proves efficacy or that zero
meteorological efficacy erases social value. The positive contemporaneous
price-success proposition is not supported: reputation-mediated mean prices and
provider-price heterogeneity coexist with negative mean event-level price-success
differences. Ecological hazard, endogenous behavior, valuation, and institutions
jointly determine what observers see and pay for, but credible evaluation must keep
natural performance, causal performance, scenario price, transfers, costs, and plural
values distinct.

## Acknowledgements

[AUTHOR INPUT REQUIRED: provide acknowledgements or confirm that none are required.]

## Declarations

### Data and code availability

Code, legally redistributable inputs, frozen analytical outputs, and
manuscript-generation files are publicly available at
https://github.com/bougtoir/pricing-the-rain. The repository preserves raw rainfall
snapshots with machine-readable acquisition ledgers and checksums. Sources whose
redistribution rights are unclear are not redistributed; the ledgers provide URLs,
checksums, status notes, and retrieval instructions instead. Fictional pseudo-events
and all simulation outputs are reproducible from the archived rainfall snapshots.

### Funding

[AUTHOR INPUT REQUIRED: identify funding sources or state that no specific funding was
received.]

### Competing interests

[AUTHOR INPUT REQUIRED: declare competing interests or state that none exist.]

### Author contributions

[AUTHOR INPUT REQUIRED: provide CRediT roles for each author.]

### Ethics

The study uses public environmental data, bibliographic metadata, and simulated
fictional events. It includes no human participants, personal data, or animal research.

### Generative AI declaration

During preparation of this work, the authors used Devin (Cognition AI) to assist with
code development, manuscript drafting, and language organization. [AUTHOR CONFIRMATION
REQUIRED: after using this tool, the authors reviewed and edited the content as needed
and take full responsibility for the content of the publication.] No generative-AI
image tool was used to create or alter the scientific figures, and no generative AI
was used to fabricate data or references.

## References

{{REFERENCES}}
