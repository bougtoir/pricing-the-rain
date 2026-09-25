# Differentiation from Espín-Sánchez, Gil-Guirado, and Ryan (2026)

## Audit scope and sources

This audit compares the present project with José-Antonio Espín-Sánchez, Salvador
Gil-Guirado, and Nicholas Ryan, “Praying for Rain,” *The Quarterly Journal of
Economics* 141(3), 2363–2422, doi:10.1093/qje/qjag026.

Sources checked on 2026-09-24 were:

- the official OUP article record and open-access article text;
- the February 2026 NBER working-paper PDF, including its appendices
  (doi:10.3386/w31411);
- Harvard Dataverse replication metadata and file inventory
  (doi:10.7910/DVN/H4WS7U);
- the Dataverse bibliography and extended-bibliography files.

The official article is distributed under CC BY 4.0. Direct automated retrieval of its
PDF returned HTTP 403, so the locally archived NBER version was used for page-level
full-text comparison. The NBER PDF, Dataverse metadata, and downloaded supporting
bibliographies are checksummed in `data/raw/literature_source_ledger.csv`. The 1.07 GB
Atlas replication archive was inventoried from complete Dataverse metadata but was not
downloaded because reproducing the QJE estimates was not necessary for this
differentiation audit.

## What the QJE article already establishes

The following territory belongs to the QJE article and must not be presented as this
project's novelty.

| Domain | What the QJE article establishes | Consequence for this manuscript |
|---|---|---|
| Zero meteorological efficacy | The leader cannot bring rain; persuasion can persist although prayer is ineffective. | An ineffective intervention followed by natural rain is not a new premise. The exact potential-outcomes equality used here is a transparent implementation, not a priority claim. |
| Endogenous timing and rainfall hazard | Prayer during a dry spell can appear persuasive when the conditional rainfall hazard rises with spell duration. | Regression to the mean, dry-spell timing, and hazard-based apparent efficacy are prior territory. |
| Demand for rain | Prayer is most persuasive when demand for rain is high; the model includes tangible rainfall benefits and support costs. Cross-cultural results relate rainmaking to agricultural dependence. | Scarcity-dependent demand and a generic benefit-cost channel cannot be claimed as new. |
| Belief and persuasion | People infer efficacy from the contrast between rainfall hazards during and outside prayer, despite the hidden counterfactual. | Apparent belief under an unobserved counterfactual is prior territory. |
| Cultural evolution and persistence | Randomly endowed prayer policies that earn greater support survive; persuasive practices and leaders persist across generations. | Selection of persuasive practices and persistence of support are not absent from prior work. |
| Strategic leader timing | The main model evolves endowed policies, but the paper explicitly discusses an observationally equivalent alternative in which leaders choose prayer timing to maximize support. Murcia evidence is interpreted as consistent with an adaptive rule. | “Strategic timing” alone is not a defensible novelty claim. |
| Benefits, costs, and transfers | Section 2.4 models tangible rainfall benefits and costs of support. Historical discussion includes collections, offerings, alms, municipal or ecclesiastical payment, and donations. | The present paper cannot claim to introduce all economic incentives or all payment evidence into this literature. |
| Historical evidence | More than two centuries of daily church and municipal records from Murcia are used to show that prayer predicts subsequent recorded rainfall in an increasing-hazard environment. | The present pseudo-event analysis is not stronger historical evidence and must not be described as validating real rainmaking behavior. |
| Cross-cultural evidence | Rainmaking is coded for 1,208 ethnic groups from about 370 sources; groups facing an increasing hazard are estimated to be 47% more likely to practice rainmaking. Agricultural demand is also analyzed. | Eight modern weather locations are mechanism stress tests, not a broader or representative cultural sample. |

## What this project adds

The defensible increment is narrower than “timing plus an economic simulation.” It is
an explicit ecological-economic performance-and-pricing system built around the
counterfactual problem.

1. **Request-to-acceptance selection.** Communities generate requests under scarcity,
   while multiple providers may accept or reject requests using prospective ecological
   hazard, quoted price, and reputation. This separates demand timing from the
   composition of observed provider events and retains rejected requests in the
   conceptual performance denominator.
2. **Observed-weather pseudo-event benchmarking.** Five pre-specified timing rules are
   applied to leakage-free, modern daily rainfall histories across eight contrasting
   locations. This is a transparent mechanism stress test, not evidence about ritual
   prevalence or historical efficacy.
3. **Provider-specific price formation.** Scenario willingness to pay, provider quotes,
   revenue, costs, transfers, and surplus are tracked separately. These are calibrated
   model quantities, not historical price or WTP estimates.
4. **Provider-specific reputation and memory.** Bayesian and selective/recency-weighted
   observers generate heterogeneous provider reputation stocks from attributed past
   outcomes. The model links those stocks to later prices while preserving identical
   rainfall potential outcomes.
5. **Stock-flow decoupling as the principal pricing result.** Past attributed outcomes
   form a reputation stock and a current price premium; current apparent success is a
   flow outcome governed by current ecological hazard. The model therefore permits
   reputation-based premia alongside zero or negative contemporaneous price-success
   differences. The observed-weather scenario and M4-M5 results do not support the
   anticipated positive price-success association.
6. **Risk-adjusted performance implications.** The analysis shows why raw success and
   price are not sufficient statistics for provider performance when providers select
   ecological exposure and counterfactual outcomes are hidden.
7. **Explicit plural-value and accounting distinctions.** Environmental-service value,
   causal intervention-created value, scenario WTP, provider price, expenditure
   transfer, resource cost, profit, and non-monetary social or relational value are kept
   analytically distinct.
8. **Auditable staged comparison.** M0-M5 are a sequential generative enrichment, not a
   clean causal decomposition of adjacent model differences. Machine-readable outputs,
   exact-zero tests, and a within-stratum falsification make the limits of each result
   inspectable.

## Claims that must be removed or qualified

- Do not say that the paper is the first to show apparent efficacy from endogenous
  dry-spell timing or an increasing rainfall hazard.
- Do not say that the QJE article lacks demand, costs, payments, strategic timing, or
  persistence mechanisms.
- Do not imply that exact zero efficacy is conceptually unique to this project.
- Do not describe the eight locations as representative ritual communities or as a
  global empirical test.
- Do not call scenario WTP or simulated prices empirical environmental valuation.
- Do not describe M0-M5 as one-factor-at-a-time causal effects.
- Do not imply that the project estimates historical payment schedules, fee escalation,
  or provider profit.
- Do not treat a reputation premium as evidence of higher contemporaneous success.

## Extension verdict

**Proceed as a qualified extension.** The project is publishably distinct only if its
center of gravity is moved from endogenous timing and generic valuation to selective
provider performance, provider-specific reputation-mediated pricing, the stock-flow
decoupling between past attributed success and current ecological hazard, and the
resulting need for risk-adjusted institutional evaluation.

Framed that way, the paper is not simply “Praying for Rain plus simulation”: the QJE
article explains why ineffective prayer can be persuasive and documents where such
belief appears; this paper asks what happens when requests, acceptance, provider
choice, pricing, memory, and performance assessment operate around the same hidden
counterfactual. The unfavorable price-success finding is essential to that distinction,
not an ancillary robustness result.
