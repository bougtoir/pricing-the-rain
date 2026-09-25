# Phase 4 report: Monte Carlo mechanism decomposition

## Design

Six nested models were run for 10,000 replications each using pre-specified parameters
and seed 20260924. Each replication samples one observed 2011–2020 region-year and
four stylized providers. Rainfall outcomes are never altered by requests, acceptance,
price, belief, or reputation.

- **M0:** random timing with shuffled within-year outcomes.
- **M1:** drought-driven demand with shuffled outcomes.
- **M2:** drought-driven demand with observed local/seasonal outcome ordering.
- **M3:** provider acceptance responds to prospectively estimated rainfall hazard.
- **M4:** provider-specific Beta-Binomial reputation and belief-mediated WTP.
- **M5:** selective-success and recency-weighted reputation.

Prices, rainfall value, social utility, and provider cost are scenario units. They are
not historical estimates.

## Principal results

| Model | Events | Apparent success | Mean price | Reputation dispersion |
|---|---:|---:|---:|---:|
| M0 | 24.36 | 0.635 | 3.000 | 0.000 |
| M1 | 68.95 | 0.634 | 3.000 | 0.000 |
| M2 | 68.98 | 0.493 | 3.000 | 0.000 |
| M3 | 16.92 | 0.676 | 3.000 | 0.000 |
| M4 | 16.95 | 0.674 | 3.568 | 0.117 |
| M5 | 16.88 | 0.673 | 4.610 | 0.138 |

Drought-driven demand increased intervention frequency without increasing efficacy.
Restoring realistic local and seasonal ordering reduced average apparent success
relative to shuffled outcomes because drought requests concentrate in low-hazard
periods. Strategic acceptance then increased apparent success from 0.493 to 0.676
while meteorological efficacy remained exactly zero.

Reputation learning generated persistent provider differentiation and a price premium.
Selective/recency-weighted memory increased mean price and reputation dispersion
further. The within-replication difference between prices attached to eventual
successes and failures was negative on average in M4 and M5. This is retained rather
than tuned away: higher prices arise when perceived reputation exceeds a sometimes-low
baseline hazard, so a positive price premium does not guarantee a positive
event-level price–outcome association.

## Welfare accounting

The model distinguishes transfers from surplus. Provider revenue equals community
expenditure. Because causal rainfall benefit is zero, total modeled surplus is social
utility minus provider cost, while community material-plus-social utility subtracts
payment. M4 and M5 can therefore create provider revenue and expenditure without
creating a causal rainfall benefit. This does not imply that real ritual has zero
cultural or social value.

## Reproducibility

The machine-readable outputs contain 60,000 replication rows and model-level means,
standard deviations, and empirical 95% intervals. The complete test suite passed.
