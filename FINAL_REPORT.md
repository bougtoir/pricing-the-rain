# Final report

## Outcome

The package implements the exact zero-effect null
\(R_{rt}(1)=R_{rt}(0)=R_{rt}\), analyzes actual historical rainfall around fictional
pseudo-events, decomposes timing and selection in six simulation models, and generates
a reproducible *Ecological Economics* submission package. The scientific package is
ready for public release and author review. A pinned full rebuild completed from the
archived inputs, the final audit passed, and all 21 tests passed. It is not
administratively ready for submission until the listed author fields are completed.

## Principal findings

1. Natural rainfall creates high apparent success under some endogenous timing rules
   even though fictional events cannot alter rainfall.
2. Drought-driven demand changes event frequency, whereas prospective provider
   selection can raise apparent success by changing which requests are accepted.
3. Bayesian and selective/recency-weighted reputation mechanisms produce provider
   differentiation and scenario price premia under exact zero efficacy.
4. Price, willingness to pay, causal rainfall value, transfers, social utility,
   revenue, profit, and welfare are not interchangeable.
5. The observed-weather and simulation evidence is consistent with attribution and
   selection mechanisms, not historical ritual efficacy or identified historical
   markets.

## Unsupported or bounded hypotheses

The general proposition that higher prices are positively associated with apparent
success is **not supported**. The hazard-adjusted logit point estimate is positive, but
its two-way clustered interval includes zero. The stricter within-stratum permutation
coefficient is negative, as are the event-level M4–M5 price–success differences.

The package also does not establish:

- a causal effect of any real ritual;
- historical WTP, fee schedules, or provider profit;
- empirically observed Bayesian or selective-memory updating;
- representative global or community-level effects;
- a numerical estimate of cultural, relational, or social value.

## Main limitations

- Eight point locations are climate stress tests, not a representative sample.
- ERA5 point reanalysis is not a local gauge network.
- Pseudo-events can overlap and are not behavioral observations.
- Clustered inference is exploratory; no multiplicity adjustment is used.
- Simulation convergence reduces Monte Carlo error but does not validate calibration.
- Provider strategy, observer rules, social utility, and price functions are stylized.
- Restricted historical and publisher audit sources are not redistributed publicly.

## Journal route

Target: *Ecological Economics*.

Selected category: **Analysis**.

Positioning: ecological variability, scarcity, strategic selection, plural valuation,
hidden counterfactuals, and reputation. Endogenous timing is prior art rather than the
novelty claim.

## Exact reproduction commands

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
PYTHONPATH=. .venv/bin/python run_all.py
PYTHONPATH=. .venv/bin/python run_all.py --validate-only
PYTHONPATH=. .venv/bin/python -m compileall -q run_all.py src simulation analysis manuscript tests
PYTHONPATH=. .venv/bin/python -m pytest tests -q
git diff --check
```

The final reproduction-manifest file SHA-256 is:

```text
039de6835d9cda100455061f4cdb1226b650760865ceff601e72ca4cd7c4b4e5
```

## Final audit and package

- Weather observations: 87,664 region-days across eight locations, with no missing
  precipitation.
- Pseudo-events and regression observations: 2,595.
- Inference clusters: 80 region-year and 40 region-rule clusters.
- Exploratory permutation: 1,000 permutations across 380 strata.
- Principal simulations: 60,000, with 10,000 per M0–M5 model and a common recorded
  weather-year draw within each replication.
- Maximum apparent-success Monte Carlo standard error: 0.002814.
- Manuscript: 3,936 words excluding references; 188-word abstract; 20 references; five
  figures; four main tables; six supplementary tables.
- Submission archive: 26 files, 8,459,268 bytes; SHA-256
  `d7192c76f30c94123ce17ae2694af804d21c9b99625350474bd74a573a453413`.
- Inline manuscript DOCX: 2,404,227 bytes; SHA-256
  `d9ecc126ab146217ee83ca6dddc66fde0f2720b0db11fa70ec1d0ec0a11e9e8b`.

The final audit verifies prior-data-only weather features, no event-day or future
leakage, complete follow-up, training-only hazard construction, clustered sample
counts, permutation configuration, common weather draws, simulation accounting,
robustness outputs, Monte Carlo precision, manuscript limits, unfavorable
price-success-result visibility, and exclusion of raw data from the submission ZIP.

## Remaining manual submission steps

1. Enter author names and order.
2. Add affiliations, corresponding-author contact details, and ORCIDs.
3. Complete funding, competing-interest, CRediT, and acknowledgement statements.
4. Confirm originality and that the manuscript is not under consideration elsewhere.
5. Optionally provide suggested reviewers.
6. Review the cover letter and journal-generated submission PDF.
7. Upload the editable article, title page, separate figures, highlights, tables, and
   supplement using the journal checklist.
