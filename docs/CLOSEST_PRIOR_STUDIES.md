# CLOSEST PRIOR STUDIES — generalization pass

Approximately nearest papers to the generalized question (rare event +
endogenous observation + experienced-frequency bias + probability
transformation + price formation + reputation + zero-effect validation).
Columns follow the handoff template.

## 1. Espín-Sánchez, Gil-Guirado & Ryan (2026), *QJE* — "Praying for Rain"

- Citation: Espín-Sánchez, Gil-Guirado & Ryan (2026), QJE 141(3):2363–2405.
- Research question: when does rainfall prayer persuade/persist as an
  instrumental belief?
- Data: two centuries of Murcia prayer records; cross-cultural ethnic-group
  classification; rainfall hazards.
- Event type: rainfall after prayer (rare-ish binary, seasonal).
- Probability object: believers' inferred efficacy under endogenous prayer
  timing.
- Observation process: prayer initiated in drought — endogenous timing.
- Pricing/WTP mechanism: none (support/persuasion, not prices).
- Learning mechanism: persuasion via hazard-coincident timing; cultural
  evolution.
- Reputation: leader support, not a priced reputation stock.
- Causal identification: true effect is zero by construction of the physical
  claim; persuasion proven under increasing hazard.
- **What this project adds:** formal separation of objective/experienced/
  subjective/price-implied probabilities; provider-side selective acceptance;
  priced reputation stocks; a simulation layer; price-implied-probability
  invalidity result; the evaluation/pricing problem rather than belief
  persistence.

## 2. Hertwig, Barron, Weber & Erev (2004), *Psychological Science*

- Citation: Hertwig et al. (2004), Psych. Science 15(8):534–539.
- Research question: do decisions from experience differ from decisions from
  description, especially for rare events?
- Data: lab experiments.
- Event type: rare outcomes in lotteries.
- Probability object: decision weights implied by choices.
- Observation process: free sampling — endogenous in effort, exogenous in
  content; no strategic or hazard-driven selection.
- Pricing/WTP: choice equivalents only.
- Learning: sampling-based experience.
- Reputation: none.
- Causal identification: experimental.
- **Adds:** endogenous (hazard- and acceptance-driven) observation rather than
  i.i.d. sampling; price formation; reputation; zero-effect field benchmark.

## 3. Wulff, Mergenthaler-Canseco & Hertwig (2018), *Psychological Bulletin*

- Citation: Wulff et al. (2018), Psych. Bulletin 144(2):140–176.
- Research question: meta-analysis of the description–experience gap.
- Data: meta-analytic aggregation.
- Event type: rare lottery outcomes.
- Probability object: as-if weighting of rare events.
- Observation process: sampling paradigms.
- Pricing: none beyond choice tasks.
- Learning: experience-based.
- Reputation: none.
- Identification: experimental aggregation.
- **Adds:** endogenous observation economics, pricing, reputation, field
  validation environment.

## 4. Ungemach, Chater & Stewart (2009), *Psychological Science*

- Citation: Ungemach, Chater & Stewart (2009), Psych. Science 20(4):473–479.
- Research question: is the DE gap produced by sampling bias?
- Data: lab experiments with controlled samples.
- Event type: rare outcomes.
- Probability object: experienced frequency vs described probability.
- Observation process: manipulated samples — exogenous.
- Pricing: choice equivalents.
- Learning: frequency exposure.
- Reputation: none.
- **Adds:** selection that is endogenous to hazard/strategy (not experimenter-
  controlled), price-implied probabilities, reputation persistence.

## 5. Tversky & Kahneman (1992), *Journal of Risk and Uncertainty* — CPT

- Citation: Tversky & Kahneman (1992), JRU 5:297–323.
- Research question: cumulative representation of choice under uncertainty.
- Data: experiments.
- Probability object: weighting function \(w(p)\).
- Observation process: described outcomes.
- Pricing: certainty equivalents.
- Learning/reputation: none.
- **Adds:** \(w(\cdot)\) is one of four layers here, applied to
  endogenously-generated experienced frequencies, then inverted through a
  price mapping — the layer separation is the contribution, not the
  weighting function.

## 6. Prelec (1998), *Econometrica* — weighting function

- Citation: Prelec (1998), Econometrica 66(3):497–527.
- Role: supplies the one-parameter weighting form used as an explicit
  behavioral assumption (layer C→D), not as an estimated object.
- **Adds:** same as #5.

## 7. Esponda & Pouzo (2016), *Econometrica* — Berk–Nash

- Citation: Esponda & Pouzo (2016), Econometrica 84(4):1093–1130.
- Research question: equilibrium when agents hold misspecified models and
  feedback is endogenous.
- Probability object: subjective beliefs under misspecification.
- Observation process: endogenous distributions via own actions.
- Pricing: none specific to rare events.
- Learning: Bayesian-like updating on endogenous data.
- Reputation: none.
- **Adds:** rare binary events, four-layer probability decomposition, explicit
  price formation and price-implied probability, a physical zero-effect
  benchmark that pins the identification problem.

## 8. Quantitative Economics (2018), "Endogenous sample selection: A
laboratory study"

- Citation: Esponda & Vespa (2018), Quantitative Economics 9(1):183–216, DOI 10.3982/QE650.
- Research question: do decision makers account for endogenous sample
  selection?
- Data: laboratory experiment.
- Observation process: endogenous selection with full information available.
- Probability object: inferred distributions.
- Pricing/learning/reputation: partial heuristics; no reputation.
- **Adds:** prices and reputation stocks; rare-event regimes; zero-effect
  field benchmark.

## 9. Jehiel (2018), *American Economic Review*

- Citation: Jehiel (2018), AER 108(6):1582–1597.
- Research question: overoptimism sustained by selection-bias neglect in
  equilibrium.
- Observation process: investors observe selected histories.
- Probability object: beliefs about returns.
- Pricing: investment choice, not event pricing.
- **Adds:** rare binary events, explicit experienced-frequency mechanics,
  price-implied probability, validation environment.

## 10. Dranove, Kessler, McClellan & Satterthwaite (2003) / Werner & Asch (2005)

- Citation: Dranove et al. (2003), JPE 111:555–606; Werner & Asch (2005),
  JAMA 293:1239–1244.
- Research question: do report cards induce selection rather than improvement?
- Observation process: provider case selection.
- **Adds:** rare-event probability layers and price formation; the rainfall
  benchmark pins the zero-effect case.

## Derived-results coverage matrix (hostile-review revision)

The manuscript's six derived results, and whether each nearest prior study
contains them (✓ = contains, ~ = partial/adjacent, — = absent):

| Result | 1 Espín-Sánchez | 2 Hertwig | 3 Wulff | 4 Heckman-tradition | 5 Berk–Nash | 6 Misspec. learning | 7 Esponda & Pouzo | 8 Esponda & Vespa | 9 Jehiel | 10 Report cards |
|---|---|---|---|---|---|---|---|---|---|---|
| Generalized selection-ratio / covariance identity | — | — | — | ~ | — | — | — | — | — | — |
| Matched-support decomposition (composition vs record) | — | — | — | ~ | — | — | — | — | — | ~ |
| Three-way separation: selection / transformation / reputation | ~ | ~ | ~ | — | — | — | — | — | — | — |
| Stock–flow decoupling of reputation vs contemporaneous performance | — | — | — | — | — | — | — | — | — | ~ |
| Mean-performance equivalence (first-moment confounding) | ~ | — | — | — | ~ | ~ | ~ | ~ | ~ | ~ |
| Real-weather known-zero benchmark | ~ | — | — | — | — | — | — | — | — | — |

No single prior study contains more than one of the six results; the paper
does not claim "first" on any ingredient, only that the combination makes
these specific derivations possible.
