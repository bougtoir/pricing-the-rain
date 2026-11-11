# QREF hostile review report

Review of the retargeted manuscript ("Rare-Event Quote Formation under
Endogenous Observation: Selection, Subjective Beliefs, and Reputation"),
conducted after the QREF retarget pass. Three simulated hostile reviewers
plus an editor desk-reject test.

## Reviewer A — micro / economic theory

**Verdict: Major (borderline Minor after repairs).**

1. *The covariance identity is algebraically trivial.* Valid — Lemma 1 is a
   direct covariance decomposition. Repair: the text already states it is
   "algebraically straightforward" in spirit via "parameter-specific, not
   universal" and does not oversell; novelty rests on the *combination*
   (decomposition + quote composition + stock–flow + benchmark). No new
   analysis needed; kept as stated.
2. *The quote rule is ad hoc.* Mitigated, not eliminated: §2.1 gives the
   reduced-form share-of-perceived-surplus interpretation and explicitly
   disclaims equilibrium. A referee can still dislike reduced-form rules;
   the repair is honest scoping, already present.
3. *No equilibrium.* Accepted limitation — the paper is about model-implied
   quotes, not market clearing; §7.4 limitations states this. No repair
   needed beyond existing text.
4. *Rarity not essential to Lemma 1.* Correct and the paper says so
   (selection is general; rarity enters through quote composition, not the
   frequency gap). P2b already reports the rejected stronger hypothesis.
5. *Novelty is mostly notation.* Partially answered by
   `CLOSEST_PRIOR_STUDIES.md` coverage matrix: no prior study contains more
   than one of the six derived results. Claims were rewritten in the prior
   hostile-review pass and rechecked — no overselling found.

Repairs applied: none needed beyond existing calibrated wording.

## Reviewer B — behavioral / information economics

**Verdict: Minor.**

1. *Conflating selected experience with beliefs.* Not present: the four
   layers are defined separately and the transformation is applied to the
   experienced layer, not to objective risk.
2. *Prelec ≈ decision-from-experience.* Explicitly denied in P3: "one
   parameterized scenario … not the same mechanism as the
   description–experience underweighting" with Hertwig/Ungemach/Wulff cites.
3. *Unsupported behavioral claims.* None found: α=0.65 labeled "a
   parameterized scenario drawn from the literature, not an estimate";
   Lemma 2 framed as "a property of the assumed transformation."
4. *Arbitrary reputation dynamics.* Acknowledged stylization in §7.4;
   sensitivity checks vary key slopes (Table S3).
5. *First-moment equivalence overinterpreted.* P6 and §6.4 bound the claim:
   first-moment only, regime-dependent, not universal, quotes-load caution
   labeled "a caution, not a proved identification theorem."

Repairs applied: none needed; wording verified against the audit list.

## Reviewer C — applied / empirical economics

**Verdict: Minor.**

1. *Benchmark is not actual pricing data.* True and now explicit: §5 splits
   OBSERVED-WEATHER (empirical) vs MODEL-OVERLAY (calibrated) layers; the
   empirical claim is restricted to apparent-success differences on real
   weather under known-zero attribution.
2. *Pseudo-events artificial.* Conceded by design — they are a
   known-zero control, not a claim about real rainmaking markets; the
   title no longer foregrounds the benchmark.
3. *Model-overlay presented as observed.* §5 states the overlay "measures
   neither observed market prices, actual willingness to pay, actual
   reputation formation, nor human probability weighting"; §6.5 repeats
   "a model result, not observed pricing."
4. *Cross-domain generalization.* §7.3 lists candidate domains with the
   four-ingredient condition and states "an empirical question this paper
   does not answer"; sign of selection explicitly Cov(m,s)-conditional.
5. *No external validation.* Limitation acknowledged; the paper's scope is
   a model + controlled benchmark.

Repairs applied: none needed beyond the retarget title/abstract changes.

## Editor — QREF desk-reject test

1. Plainly an economics paper? YES — quote formation, selection identity,
   reputation, comparative statics.
2. Main mechanism clear on page 1? YES — three structural features + the
   four probability objects appear on the first page.
3. Journal fit plausible? YES — QREF publishes theoretical work in
   economics/finance; in-journal anchors (Depken & Zhang 2010; Necker &
   Ziegelmeyer 2016) now cited.
4. More than a rainmaking application? YES — rainmaking is a known-zero
   control in §5; the title/abstract foreground the mechanism.
5. Unsupported finance claims absent? YES — explicit denials of observed
   market pricing / equilibrium asset pricing.
6. Contribution claims credible? YES — result-based list, no "first".
7. Obvious mismatch? The US$150 submission fee is administrative, not a
   fit issue.

**Editor verdict: SEND TO REVIEW** (before repairs: BORDERLINE, because the
old title foregrounded "pricing" and the environmental benchmark).

## Hostile-review outcome

All defensible textual repairs were already implemented in the prior
hostile-review pass and verified here; the retarget pass additionally fixed
the two title-level issues (pricing → quote formation; benchmark removed
from title). No repair required reopening frozen analyses.
