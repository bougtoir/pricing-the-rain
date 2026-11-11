# JRU citation audit

Method: every reference in `REFERENCE_ORDER` (`manuscript/build_manuscript.py`)
was checked against its saved Crossref record (`data/raw/literature/crossref_*.json`,
ledger `data/raw/literature_acquisition_ledger.csv`) or a manual source
(`data/raw/literature_source_ledger.csv`). Authors, year, title, journal, volume,
issue, pages, and DOI in the rendered reference list come from those records;
overrides are documented in code. The build fails if a reference is not cited
in the text (`REFERENCE_CITE_TOKENS`).

Result: 37 references; 37 exist; 37 DOIs resolve to the cited work; 0 fabricated;
3 metadata defects corrected; 0 unsupported citation–claim pairs after repair.

## Metadata defects found and fixed

| Defect | Fix |
|---|---|
| Text cited "Dranove & Satterthwaite, 2000" (not in the list; the listed DOI 10.1086/374180 is Dranove, Kessler, McClellan & Satterthwaite 2003) | Citations changed to "Dranove et al., 2003" (2 places) |
| Text cited "Shahian et al., 2011"; listed DOI 10.1161/circulationaha.107.747873 is Shahian & Normand (2008) | Citations changed (2 places) |
| Crossref lists only Barnett and the 2004 online date for 10.1093/ije/dyh299 | Reference set to Barnett, van der Pols & Dobson (2005), IJE 34(1):215–220, from PubMed 15333621 (saved) |
| Candidate DOI 10.1287/mnsc.1110.1381 (intended Abdellaoui et al.) resolves to a different paper | Not used |
| Candidate DOI 10.1007/s11166-022-09388-2 has no Crossref record | Not used |

## Claim–support pairs (added and framing-critical references)

| Claim in manuscript | Reference | Supported? |
|---|---|---|
| Endogenous sampling biases experience-based estimates because observation depends on the learner's state or choices | Denrell & March 2001 (hot stove effect); Fiedler 2000 (sampling approach); Denrell 2005 (experience sampling) | Yes — each paper's central result |
| The bias survives Bayesian updating | Le Mens & Denrell 2011 ("Rational learning and information sampling") | Yes — title result |
| Selected-sample means differ from population means by a covariance term | Heckman 1979 | Yes — selection bias as omitted-variable term |
| Selective acceptance distorts provider report cards | Dranove et al. 2003; Werner & Asch 2005 | Yes — both document selection responses to report cards |
| Rare events are underweighted when experienced through sampling | Barron & Erev 2003; Hertwig et al. 2004; Hertwig & Erev 2009; Wulff et al. 2018 | Yes |
| Stated probabilities differ from experienced ones | Ungemach et al. 2009 | Yes — description vs experience of rare outcomes |
| Low probabilities are hard to use in decisions | Camerer & Kunreuther 1989; Kunreuther et al. 2001 | Yes — "Decision processes for low probability events"; "Making low probabilities useful" |
| Endogenous feedback can make mislearning persistent | Esponda & Pouzo 2016; Jehiel 2018; Esponda & Vespa 2018 | Yes — Berk–Nash; selection bias in investment; lab endogenous sample selection |
| Probability weighting supplies the transformation layer; inverse-S shape | Tversky & Kahneman 1992; Prelec 1998; Gonzalez & Wu 1999 | Yes |
| Risk-adjusted outcome comparison problems | Shahian & Normand 2008; Barnett et al. 2005 | Yes — risk adjustment; regression to the mean |
| ERA5 reanalysis data | Hersbach et al. 2020 | Yes |
| Rain prayer timed to hazard | Espín-Sánchez et al. 2026; Espín-Sánchez & Gil-Guirado 2022 | Yes |
| Superstitious reinforcement | Skinner 1948 | Yes |
| Reputation under imperfect information; information cascades | Kreps & Wilson 1982; Bikhchandani et al. 1992 | Yes |

The remaining entries (Akong'a 1987; Cox 1972; Hensher et al. 2006; Liu & Sanyal
2012; Matsumoto & Spence 2016; Murphy 1993; Pattanayak & Kramer 2001; Shea 2015;
Tversky & Kahneman 1974) were audited in the JEBO pass for the same sentences,
which are unchanged; their records were re-verified against Crossref (or the
Kyoto University repository for Akong'a) in this pass.
