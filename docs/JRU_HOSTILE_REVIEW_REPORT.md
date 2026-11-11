# JRU hostile review and editor gate

Four adversarial reports were written against the rebuilt manuscript before
submission (internal pre-review). Each objection is answered by a change or
by an explicit scope statement; nothing below adds an analysis or parameter.

## Reviewer 1 — decision theory / probability weighting

| Objection | Response |
|---|---|
| "Subjective probability" is a model construct, not an elicited belief | Stated in §2.1 and §7.4; no claim about actual beliefs |
| Prelec with α < 1 overweights small probabilities, the opposite of the description–experience underweighting | P3 states the Prelec layer is a parameterized scenario and not the same mechanism as experience-based underweighting; learners are compared separately |
| Lemma 2 divergence is a known property of Prelec weighting | Presented as a property of the functional form (Prelec 1998), not as a contribution (`JRU_NOVELTY_GATE.md`) |
| The quote is not a market price | §2.1 defines "price/pricing" as the reduced-form mapping; no market-clearing claim |

## Reviewer 2 — econometrics / identification

| Objection | Response |
|---|---|
| Lemma 1 is the covariance identity for selected samples | Introduced as an application of a standard identity (Heckman 1979; Denrell 2005); the contribution is the rarity comparative static and the decomposition |
| Earlier version used period-\(t\) outcomes in period-\(t\) quotes | Corrected and audited (`JRU_LOOKAHEAD_CORRECTION_AUDIT.md`); regression test `tests/test_lookahead.py` |
| \(B\) layer definitions were ambiguous between objective-relative and incremental gaps | Defined objective-relative throughout (§4, Table 2, Table S8) |
| Mean-performance equivalence is a first-moment statement | Stated as first-moment only; no distributional equivalence claim |
| Identification routes are speculative | §7.2 lists them as design routes "within the present framework" |

## Reviewer 3 — behavioural / empirical risk

| Objection | Response |
|---|---|
| The rainfall benchmark does not observe prices or WTP | §5, §6.5, and §7.4 call WTP, quotes, and reputation model overlays on real weather; only rainfall is data |
| Generalisation to medicine/insurance is asserted | §7.3 frames these as candidate domains that require four ingredients; sign of Cov(m,s) is domain-specific |
| Rarity regimes and demand/acceptance forms are arbitrary | Pre-specified in `config/general_simulation.yml` (unchanged by the correction); sensitivity in Online Resource 1 |

## Reviewer 4 — simulation and reproducibility

| Objection | Response |
|---|---|
| Monte Carlo error not reported | MCSE in Table S7 and S4; replication counts read from config |
| Numbers typed by hand | Every reported value is a build token from `results/` or config (`JRU_NUMERIC_HARDCODE_AUDIT.md`) |
| Reproduction depends on private material | Clean reproduction from the public mirror and public ERA5 route (`JRU_PUBLIC_REPRODUCIBILITY_AUDIT.md`) |
| Model D reputation enters only in observed periods | Stated in Methods; listed as an author design confirmation in `AUTHOR_ACTIONS_REQUIRED.md` |

## Editor gate

| Check | Verdict |
|---|---|
| Scope fit (risk and decisions under uncertainty; not finance/game theory) | Pass |
| Contribution proportionate to novelty gate | Pass — `ADEQUATE INCREMENTAL NOVELTY`; no "first" claims |
| Length and format | Pass — see `JRU_COMPLIANCE_CHECKLIST.md` |
| Open author items | Declarations content, Model D timing confirmation (ERA5: resolved, not redistributed) |
