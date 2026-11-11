# JEBO hostile review report

Fresh hostile review of the JEBO-targeted manuscript, 2026-10-20.
Four skeptical reviewers + editor simulation. Verdicts reflect the
pre-repair draft; repairs are textual/structural only (frozen science).

## Reviewer A — JEBO / behavioral economics — MAJOR (pre-repair)

1. **No actual human-subject or market data.** The paper cannot claim
   behavioral findings; the manuscript is a model.
   *Repair:* make the no-data status explicit on page 1, not only in
   §7.4. Implemented — added one sentence to the Introduction stating the
   paper contains no human-subject or market-transaction data and that
   claims concern what model-implied quotes can encode.
2. **Prelec is one arbitrary transformation.** Repair: already handled —
   P3 states it is "one parameterized scenario," compared against Bayesian
   updating, recency, and selective memory in the simulation. No change
   needed; verified.
3. **Conflation of experience and beliefs.** The four-layer split keeps
   experienced frequency and subjective probability as distinct objects;
   the confusion risk is in casual prose. Verified no conflation; no
   repair required.
4. **Weak behavioral contribution.** Defense: the contribution is the
   information structure (what selected experience does to inference and
   quotes), which JEBO's scope covers explicitly; the paper does not claim
   a behavioral effect estimate. Text already calibrated.
5. **Overclaiming real-world relevance.** Candidate domains §7.3 are
   conditional ("whether each ingredient holds… is an empirical question
   this paper does not answer"). Verified.

Post-repair verdict: MINOR.

## Reviewer B — information / micro theory — MAJOR (pre-repair)

1. **The covariance identity is algebraically trivial.**
   Defense/repair: the lemma's content is the *signed, rarity-independent*
   comparative statics implication plus the matched-support
   decomposition that separates composition from record bias — the
   combination, not the algebra, is what the component literatures lack.
   The Introduction already frames the contribution this way; verified.
2. **Quote rule is ad hoc.** Already given an explicit reduced-form
   interpretation (share of perceived gross surplus + separable
   reputation); §7.4 now also notes it is one possible pricing
   institution, so comparative statics are mechanism-conditional.
   Implemented.
3. **No equilibrium.** By design — the paper claims reduced-form
   comparative statics, not equilibrium; text says so repeatedly. No
   repair.
4. **First-moment equivalence too weak.** It is stated as a negative
   result bounding what mean performance reveals, not an identification
   theorem; that is the honest claim. No repair.
5. **Rarity not essential.** Correct — and the paper says so (§7.1:
   selection is general; rarity changes scaling/composition). The rarity
   result is what changes under rarity, which is the claim. No repair.

Post-repair verdict: MINOR.

## Reviewer C — reputation / organization — MINOR→MAJOR (pre-repair)

1. **Reputation dynamics arbitrary.** The ρ-weighted stock is standard
   exponential smoothing of attributed outcomes; limitations now note
   alternative accumulation rules could shift magnitudes (not the sign
   or the decoupling). Implemented as one clause in §7.4.
2. **Stock–flow result parameter-specific.** It is a possibility result:
   premia *can* coexist with negative contemporaneous gaps. Text never
   claims necessity. Verified.
3. **Provider heterogeneity underdeveloped.** Provider-specific
   selectivity is in the simulation (acceptance slope heterogeneity);
   rank-distortion metric quantifies the consequence. Bounded claim; no
   repair.
4. **Organization contribution thin.** Reputation is one of three
   mechanisms, not the whole paper; stock–flow decoupling is an
   organizationally meaningful statement (payment need not track current
   delivery). No repair.
5. **Decoupling not structural enough.** It is a statement about the
   model's objects (stock vs flow), which is precisely the structural
   content; no repair.

Post-repair verdict: MINOR.

## Reviewer D — applied / empirical — MAJOR (pre-repair)

1. **Weather benchmark is not behavioral evidence.** Already demoted:
   empirical content is the observed-weather layer only; the
   quote/reputation overlay is labeled a calibrated model result.
   Verified.
2. **Pseudo-events artificial.** By construction — they exist to impose a
   known zero. The text states every causal attribution is false by
   construction. Verified.
3. **No observed quotes/WTP.** True and disclosed; benchmark measures
   apparent-success generation, not prices. Verified.
4. **External validity.** Rainmaking is institutional-plausibility
   framing only; candidate domains are conditional. Verified.
5. **Selected examples driving interpretation.** Both ends reported:
   P2b is a disclosed negative result; the common-regime
   equivalence-grid failure is reported (P6). Verified.

Post-repair verdict: MINOR.

## Editor — desk-reject test

1. Within JEBO scope? Yes — information/belief structure → economic
   outcomes; simulation within remit.
2. First page communicates behavioral/information mechanism? Yes.
3. More than an algebraic decomposition? Yes — decomposition + rarity
   comparative statics + stock–flow decoupling + first-moment bound.
4. Avoids pretending human data? Yes, now stated on page 1.
5. Quote rule honestly characterized? Yes — reduced-form, named limits.
6. Reputation meaningful? Yes — decoupling result, not an add-on.
7. Weather benchmark supportive not distracting? Yes — one section,
   clearly layered.
8. Reason to send to reviewers? Yes — a derivable structure for a known
   empirical pathology (apparent performance under selected
   observation).
9. "Interesting but not a fit"? No — mechanism is core JEBO territory.

**Editor verdict: SEND TO REVIEW** (post-repair).

## Repairs implemented

1. Introduction (¶2): added explicit no-human-data sentence.
2. §7.4 Limitations: added reduced-form-institution caveat and
   reputation-accumulation-rule caveat.

No frozen scientific output, parameter, figure, or table was touched.
