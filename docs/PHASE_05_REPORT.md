# Phase 5 report: robustness, falsification, and classification

## Empirical robustness

The hazard-, location-, month-, and timing-rule-adjusted logit price coefficient was
0.036. Its two-way clustered 95% interval across 80 region-year and 40 region-rule
clusters was −0.039–0.111. A 1,000-draw within-region–month–rule permutation
falsification produced an adjusted linear-probability coefficient of −0.0319 against
a null mean of −0.0002 (\(p=0.002\)). The declared positive price–apparent-success
proposition is therefore classified as **not supported**.

Apparent success was recomputed for all combinations of 0.1, 1, and 5 mm thresholds;
1, 3, 7, and 14-day windows; and all five timing rules. The qualitative conclusion
that natural rainfall generates apparent success is stable, while magnitudes depend
substantially on the attribution window and rainfall threshold as expected.

## Simulation sensitivity

Increasing the provider-selection hazard slope from 2 to 5 to 8 raised mean apparent
success from 0.554 to 0.679 to 0.737 without changing rainfall. This supports the
strategic-selection mechanism.

Changing the Bayesian prior mean from 0.25 to 0.50 to 0.75 changed mean price from
2.890 to 3.548 to 4.692 but left apparent success near 0.673. Selective-memory
strength changed mean price and reputation dispersion without producing a positive
event-level price–outcome difference. These sensitivities identify prices as
belief-dependent scenario outputs rather than structural empirical estimates.

## Monte Carlo precision

At 10,000 principal replications per model, Monte Carlo standard errors were:

- 0.0018–0.0028 for apparent success;
- 0.0119 for M4 mean price and 0.0142 for M5 mean price;
- 0.0005 for M4 reputation dispersion and 0.0010 for M5.

The principal replication target is adequate for the reported model means. Wide
replication-level intervals reflect real cross-region/year and stochastic heterogeneity,
not Monte Carlo imprecision.

## Falsification conclusions

- Season-matched placebo events also show substantial apparent success.
- Fixed-price M0–M3 correctly produce a zero price–success difference.
- Within-stratum permutation yields a negative association rather than the declared
  positive association.
- No model modifies the rainfall sequence, and unit tests verify that invariant.
- Unfavorable negative M4–M5 price–outcome differences were preserved.

## Hypothesis classification

Natural-rainfall apparent success, demand-frequency, strategic-selection, reputation,
and model-based price-premium mechanisms are supported within their declared evidence
domains. A generally positive price–apparent-success association is not supported.
Social value is kept conceptually separate from rainfall efficacy and is not
empirically estimated.
