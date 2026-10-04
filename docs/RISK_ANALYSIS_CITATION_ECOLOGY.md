# Risk Analysis citation-ecology audit

Scope: references needed for the retargeted framing (performance evaluation
under heterogeneous baseline risk, selective exposure, hidden counterfactuals,
reputation stocks). All additions verified against the CrossRef API on
2026-10-03; metadata snapshots archived under `data/raw/literature/` and
`analysis/reference_metadata.csv`.

## Additions (5)

- Heckman (1979), *Econometrica* — sample selection bias; canonical treatment of
  selection into observed samples (10.2307/1912352). Supports the formal
  framing of selective acceptance into observed exposure.
- Murphy (1993), *Weather and Forecasting* — "What is a good forecast?" —
  performance evaluation conditioned on baseline difficulty
  (10.1175/1520-0434(1993)008<0281:wiagfa>2.0.co;2). Supports the claim that raw
  outcome rates confound baseline hazard with forecaster/provider skill.
- Dranove, Kessler, McClellan & Satterthwaite (2003), *Journal of Political
  Economy* — provider report cards induced selection (avoiding sick patients)
  rather than performance improvement (10.1086/374180). Empirical anchor that
  raw scorecards can reward selective acceptance.
- Werner & Asch (2005), *JAMA* — unintended consequences of public quality
  reporting, including case selection (10.1001/jama.293.10.1239). Supports the
  scorecard/policy implication paragraph.
- Shahian & Normand (2008), *Circulation* — comparison of "risk-adjusted"
  hospital outcomes; benefits and hazards of risk-adjustment benchmarking
  (10.1161/circulationaha.107.747873). Supports the risk-adjusted evaluation
  framing and its caveats.

These were chosen because each materially supports a specific claim (selection
into observation; baseline-conditioned performance evaluation; scorecards
rewarding selection; risk adjustment limits). No Risk Analysis journal self-
citations were added; no citation padding.

## Retained citations (Ecological Economics version)

The rainmaking/rain-prayer cluster (Espín-Sánchez et al. QJE 2026 + working
paper, Espín-Sánchez & Gil-Guirado 2022, Semenya 2013, Akong'a 1987) remains for
the ground-truth case and QJE differentiation. The attribution/heuristics
cluster (Barnett 2004; Tversky & Kahneman 1974; Skinner 1948), social learning
(Bikhchandani et al. 1992), reputation (Kreps & Wilson 1982), hazard modelling
(Cox 1972), data provenance (Hersbach et al. 2020 ERA5; Muñoz-Sabater et al.
2021 ERA5-Land), and the drought-WTP cluster (Schrieks et al. 2025; Pattanayak &
Kramer 2001; Hensher et al. 2006) are retained where cited. The Vicente-Serrano
et al. (2010) SPEI reference remains available.

## Compressed material

Plural/cultural ecosystem-services valuation references (Chan et al. 2012;
Kenter et al. 2015; Pascual et al. 2017; Chan et al. 2016 PNAS; Kallis et al.
2013; Jacobs et al. 2016; Himes & Muraca 2018; Fish et al. 2016) are compressed
to a single consolidated citation point for the retained social-utility
distinction (§5.4 discussion), per the retarget prompt's instruction to compress
plural/cultural-value material relative to the EE version. They remain in the
reference list only if cited.

## Verification

Every listed DOI resolved on CrossRef (see `analysis/reference_metadata.csv`,
status `verified`, retrieved 2026-10-03). The Akong'a (1987) entry has no
CrossRef record; the Kyoto University repository PDF is archived and checksummed
(`data/raw/literature_source_ledger.csv`).
