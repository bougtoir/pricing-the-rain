# GENERALIZATION NOVELTY AUDIT — pricing rare events under endogenous observation

Date: 2026-10-12. Scope: Phase 0 of the generalization pass. Verdict: **GO (with
modification)** — see boundary statement at the end.

## Research question under audit

When the event being priced is rare, the counterfactual is hidden, and
observations are endogenously selected, which probability does a price actually
reveal? The generalized framework separates four objects:

1. objective event probability \(p_t\);
2. experienced/observed event frequency under endogenous selection \(\hat p_{\mathrm{exp},t}\);
3. subjective probability after learning/weighting \(\hat p_{\mathrm{subj},t} = w(\hat p_{\mathrm{exp},t})\);
4. price-implied probability \(\hat p_{\mathrm{price},t}\);

with rainmaking retained as a known-zero-effect validation environment, not the
target domain.

## Literature search coverage

Searched (Google Scholar / Crossref / publisher indexes, October 2026):
rare-event probability perception; probability weighting; prospect theory;
experience-based choice; description–experience gap; small-probability
over/underweighting; reinforcement learning; Bayesian learning under
misspecification; endogenous sampling; selective observation; sample-selection
bias; stopping rules; event-triggered observation; endogenous intervention
timing; insurance demand; catastrophe-risk pricing; disaster-risk perception;
WTP for low-probability risk reduction; betting/lottery pricing; prediction
markets; expert reputation; price-implied probabilities; adverse/case
selection; provider performance reporting; rare-event prevention; behavioral
responses to salient outcomes.

## Component coverage in prior work (established)

| Component | Established by | Status |
|---|---|---|
| Rare events are treated differently in experience vs description | Hertwig, Barron, Weber & Erev (2004); Wulff, Mergenthaler-Canseco & Hertwig (2018) | established |
| Sampling error drives much of the experience gap | Ungemach, Chater & Stewart (2009); Hertwig et al. (2004) | established |
| Probability weighting \(w(p)\) functional forms | Tversky & Kahneman (1992); Prelec (1998) | established |
| Selection into observed samples biases estimators | Heckman (1979) | established |
| Agents who learn from endogenously selected data sustain wrong beliefs | Esponda & Pouzo (2016, Berk–Nash); Ettinger & Jehiel-adjacent lab evidence (Quantitative Economics 2018) | established |
| Endogenous timing + hidden counterfactual sustain an inefficacious practice | Espín-Sánchez, Gil-Guirado & Ryan (2026) | established (rainmaking) |
| Reputation as a stock built from attributed outcomes | Kreps & Wilson (1982) | established |
| Report cards / scorecards induce selection rather than improvement | Dranove et al. (2003); Werner & Asch (2005) | established |
| Overoptimism sustained by selection-bias neglect in equilibrium | Jehiel (2018) | established |

## The combination under test

No located paper combines all of: rare event + endogenous
observation/sampling + experienced-frequency bias + probability transformation
+ **price formation / price-implied probability** + dynamic reputation +
**known-zero-effect validation environment**.

Closest partial overlaps:

- Espín-Sánchez, Gil-Guirado & Ryan (2026): endogenous timing, hazard,
  persuasion, hidden counterfactual, persistence — but no pricing layer, no
  experienced-frequency/probability-layer separation, no provider selection
  or reputation stocks, no simulation benchmark.
- Hertwig et al. (2004) and Wulff et al. (2018): experienced vs described
  probabilities, rare-event attenuation — but exogenous sampling, no prices,
  no endogenous observation mechanism, no validation environment.
- Esponda & Pouzo (2016): endogenous-data learning sustaining incorrect
  beliefs — equilibrium framework, no pricing of rare events, no
  four-probability decomposition, no empirical weather benchmark.
- Jehiel (2018): selection-bias neglect and overoptimism — no rare-event
  pricing or experienced-frequency mechanics.
- Dynamic-pricing-with-ratings literature (e.g., Carnehl, Stenzel & Schmidt
  2024; related review/price signaling papers): price and reputation interact —
  but outcomes are continuous reviews, not rare binary events under hidden
  counterfactuals, and no probability-layer decomposition.

## Novelty verdict

**GO with modification.** The defensible contribution is narrow and specific:

1. A formal four-layer probability taxonomy (objective / experienced /
   subjective / price-implied) under endogenous observation, with bias
   conditions for each layer.
2. Demonstration that price-implied probability is not a valid estimator of
   causal efficacy when observation and acceptance are endogenous, with an
   identification table stating which additional data separate the mechanisms.
3. A domain-agnostic rare-event simulation quantifying how the four
   probabilities separate across rarity regimes, learning rules, weighting,
   and reputation — including non-monotone findings where present.
4. The rainfall/rainmaking module repositioned as a **known-zero-effect
   validation environment** in which biased experienced frequencies and
   reputation-mediated prices are produced mechanically with zero true
   efficacy.

Not claimed: novelty of probability weighting, selection bias, reputation,
or the description–experience gap individually; actual historical or market
pricing behavior; human probability weighting parameters (used only as
explicit, literature-anchored behavioral assumptions, layer D).

## Claim-strength rules carried into the manuscript

- Model/simulation statements: "the model shows", "the simulation
  demonstrates".
- Rainfall benchmark statements: "the rainfall benchmark demonstrates with
  observed weather".
- External evidence statements: "existing empirical literature suggests".
- Prohibited: "actual people price", "actual markets price", historical
  rainmaker pricing claims, universal weighting claims.
