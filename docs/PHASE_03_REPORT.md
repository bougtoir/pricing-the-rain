# Phase 3 report: real-weather pseudo-interventions

## Inputs and design

The analysis uses 87,664 daily ERA5 point observations for eight pre-specified
locations from 1991–2020. Hazards are estimated on 1991–2010 and applied
prospectively to fictional 2011–2020 pseudo-events. Event-day rainfall is excluded
from both prior 30-day drought information and post-event success windows.

The first Open-Meteo request used `era5_land` and returned complete date arrays but
all-null precipitation. Those files are retained and registered as invalid inputs.
The validated immutable snapshots explicitly request `era5` and require at least
10,800 non-null daily observations per location.

## Results

The final leakage-audited rules generated 2,595 fictional pseudo-events. Seven-day apparent
success at the primary 1 mm threshold was:

| Timing rule | Events | Apparent success |
|---|---:|---:|
| 30-day deficit threshold | 294 | 0.823 |
| Dry-spell threshold | 727 | 0.601 |
| High prospective hazard | 395 | 0.853 |
| Random drought day | 509 | 0.593 |
| Season-matched placebo | 670 | 0.600 |

The empirical seven-day rainfall hazard was not monotonically increasing across the
pre-specified dry-spell bins in any of the eight locations. This directly rejects the
shortcut assumption that a longer dry spell mechanically implies a higher near-term
rain probability.

In the calibrated observer/WTP scenario, the naive logit coefficient linking
scenario WTP to seven-day apparent success was 0.124 (95% model-based interval
0.086–0.162). It fell to 0.036 (−0.028–0.100) after adjustment for prospective
hazard, drought, location, month, and timing rule. The two-way clustered interval was
−0.039–0.111. These are descriptive scenario associations, not historical price
estimates and not causal effects.

## Interpretation

Actual rainfall alone generates high apparent-success rates under exact zero
meteorological efficacy. Strategic timing based on prospectively estimated hazard
raises apparent success. The real-weather analysis therefore supports moving to the
simulation phase, where demand, selection, observer learning, pricing, and reputation
can be varied separately.

## Limitations fixed for downstream use

- Locations are rainfall-regime stress tests, not identified ritual communities.
- ERA5 point values are reanalysis, not local gauge measurements.
- Scenario WTP is calibrated and must never be described as observed payment.
- The current regression is descriptive; dependence-robust inference and alternative
  specifications belong to Phase 5.
- End-of-series success windows are excluded from model estimation when incomplete.
- Sparse or absent duration cells use a pre-specified training-period location-month
  fallback; all final pseudo-events have complete prospective-hazard covariates.

## Verification

`python src/acquire_weather.py`, `python src/weather_analysis.py`, Python compilation,
diff checks, and the three leakage/zero-effect unit tests passed.
