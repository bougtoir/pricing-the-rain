# JRU retargeting report

Base: branch `devin/1791802000-pricing-rain-generalization`, commit
`837387d71c82481f52e0783ff2d774f2e3408f2d` (tag `jru-retarget-baseline`,
JEBO-formatted). Working branch: `devin/1794204012-pricing-rain-jru`.
Official sources read: JRU Aims & Scope and Submission Guidelines
(Springer, retrieved 2026-11-09; see `docs/JRU_COMPLIANCE_CHECKLIST.md`).

## Scientific changes (approved by the author before implementation)

1. Look-ahead correction in the generic simulation: learner states,
   reputation, and quotes of models B–D at period \(t\) now use information
   through \(t-1\) only (`docs/JRU_LOOKAHEAD_CORRECTION_AUDIT.md`).
2. Model B and the naive learner use the raw experienced frequency
   \(\hat p_{exp,t-1}\) (previously a Bayesian posterior and a Laplace
   ratio, respectively); the Bayesian learner remains a separate
   subjective-learning variant.
3. \(B_{subj}\) and \(B_{price}\) are defined relative to the objective
   probability, as implemented; adjacent-layer increments are not labelled
   \(B\).

Seed, config values, and model parameters are unchanged (verified by
comparing the parsed `config/general_simulation.yml` with the baseline tag).
No new hypothesis, parameter, or exploratory analysis was added.

## Framing changes

| Item | JEBO version | JRU version | Reason |
|---|---|---|---|
| Title | Rare-Event Quote Formation under Endogenous Observation: Selection, Subjective Beliefs, and Reputation | Selected Experience and Rare-Event Risk: Endogenous Observation, Subjective Transformation, and Reputation under Hidden Counterfactuals | JRU scope is risk and decisions under uncertainty; the object of study is experienced risk, not price formation |
| Abstract | quote-formation first | experienced risk → transformation/reputation → inference under hidden counterfactuals; 150–250 words | Matches the declared research question |
| Keywords | 6, quote-centred | decisions from experience; endogenous observation; rare events; probability weighting; reputation; selection | JRU 4–6 keywords |
| Contribution claims | "closed-form selection ratio … the component literatures do not separately produce" | Selection identity and Prelec divergence presented as established / known applications; incremental contributions limited to the rarity comparative static, the decomposition, two simulation results, and the zero-efficacy benchmark | Novelty gate (`docs/JRU_NOVELTY_GATE.md`) |
| Prior literature | 28 references | 37 references; adds the sampling and decisions-from-experience literature (Denrell & March 2001; Denrell 2005; Le Mens & Denrell 2011; Fiedler 2000; Hertwig & Erev 2009; Barron & Erev 2003), low-probability risk (Camerer & Kunreuther 1989; Kunreuther et al. 2001, JRU), and probability weighting (Gonzalez & Wu 1999) | Closest-prior audit |
| Highlights | required by JEBO | removed | Not a JRU requirement |
| Declarations | "Declarations" | "Statements and Declarations" (Funding, Competing interests, Author contributions, Ethics, Data and code availability, Generative AI) | JRU guideline wording |
| Figure captions | "Figure 1." | "Fig. 1" with no punctuation after the number or at the end | JRU guideline |
| Supplement | "supplement" | "Online Resource 1" | Springer ESM naming |
| Length rule | 8,000 words | ≤ 50 pages (40 preferred) checked on the blinded PDF | JRU guideline |
| Submission ZIP | `pricing_rare_events_jebo_submission.zip` | `pricing_rare_events_jru_submission.zip` | Retarget |
| Cover letter | JEBO fit | JRU fit; downgraded contribution wording | Retarget + novelty gate |

## Description fixes found during the semantic audit (no numeric effect)

- Reputation formula in §2.2 rewritten to the implemented decayed success
  rate with prior stocks; Methods states that reputation enters model D only
  in observed periods for that provider.
- Methods now states the low-hazard multiplier, and every simulation input
  quoted in Methods is a token read from the config.
- Fig. 5 panel title no longer calls the probability part "bounded"
  (Lemma 2).
- Citation fixes: Dranove & Satterthwaite (2000) → Dranove et al. (2003)
  (the listed reference); Shahian et al. (2011) → Shahian & Normand (2008);
  Barnett reference completed to three authors and the 2005 print issue
  (PubMed 15333621).
- `config/general_simulation.yml` acceptance comment corrected to the
  implemented relative-hazard form (values unchanged).
