# JEBO retargeting report

Date: 2026-10-20. Baseline: QREF-final state `df3ace91d`
(tag `jebo-retarget-baseline`). Scientific content frozen — this document
records only framing/editorial changes for JEBO.

## Title decision

Options considered (per retargeting prompt Phase 4):

- **A. Keep current title** — "Rare-Event Quote Formation under Endogenous
  Observation: Selection, Subjective Beliefs, and Reputation"
- B. "Selective Experience, Subjective Beliefs, and Reputation in Rare-Event
  Quote Formation"
- C. "Endogenous Observation and Subjective Beliefs in Rare-Event Quote
  Formation"
- D. A new JEBO-oriented title

**Decision: A — keep the current title.** It already leads with the
information structure (endogenous observation), names the three mechanisms
(selection, subjective beliefs, reputation), keeps the honest term "quote
formation" (no market-price or equilibrium implication), and does not make
rainmaking central. Options B and C reorder the same elements without
adding information; B drops "endogenous" (the paper's key word for the
observation process) and C drops "reputation" (one of the three named
mechanisms). No change.

## What changed for JEBO

1. **Journal metadata** (`manuscript/build_manuscript.py`):
   `JOURNAL = "Journal of Economic Behavior & Organization"`,
   `JOURNAL_SHORT = "JEBO"`; submission zip renamed
   `pricing_rare_events_jebo_submission.zip`; `run_all.py` keyword check
   updated to JEBO's 1–7 range.
2. **In-journal anchors** (per handoff guidance): the two QREF-anchored
   citations were replaced with the two closest JEBO papers
   (see `JEBO_CITATION_ECOLOGY.md`):
   - Depken & Zhang (2010, QREF) → **Liu & Sanyal (2012, JEBO)**,
     expert advice under career/reputation concerns (§7.2).
   - Necker & Ziegelmeyer (2016, QREF) → **Matsumoto & Spence (2016, JEBO)**,
     experience-shaped price beliefs (§7.3); sentence reworded to match
     the cited result (price beliefs, not risk taking).
   Reference count unchanged (28 → 28). Both new DOIs are Crossref-verified
   with snapshots and ledger rows.
3. **Cover letter** rewritten for JEBO: single-author "I"; leads with
   selective experience → subjective belief formation → reputation → quote
   formation; four result-based contributions (covariance identity,
   matched-support decomposition + rarity/composition result, stock–flow
   decoupling, first-moment equivalence); real-weather benchmark demoted
   to one supporting sentence; no market-pricing / experimental /
   equilibrium / identification-theorem claims.
4. **Abstract** kept: the QREF abstract already implements the preferred
   JEBO opening logic (selectively generated histories → experienced vs
   objective frequencies → transformation + reputation → quote) and stays
   ≤250 words. No rewrite needed; verified no overclaims.
5. **Introduction/discussion** kept: the QREF revision already
   re-positioned contributions as results (covariance identity,
   matched-support decomposition, four-layer separation, rarity
   composition, stock–flow decoupling, first-moment equivalence,
   known-zero benchmark) with the behavioral framing JEBO requires.
   Verified every locked wording rule still holds (see below).
6. **AUTHOR_ACTIONS_REQUIRED.md** rewritten for JEBO ($175 fee,
   single-anonymized review, ERA5 redistribution item carried over).
7. **Replication README** journal line and hardcode-audit pointer updated.

## Locked wording re-verified (regression check, Phase 0.4)

- "quote"/"pricing" = reduced-form, model-implied only; "market price"
  restricted to real markets — OK.
- Selection inflation scoped to positive risk–observation covariance
  (Lemma 1 sign interpretation; negative covariance → deflation) — OK.
- Rarity does not amplify selection (P2b negative result retained) — OK.
- Prelec = "one parameterized scenario" (P3, §4) — OK.
- P6 = first-moment equivalence only; no price-based identification
  theorem — OK.
- Real-weather benchmark: actual weather + fictional timing + zero causal
  efficacy by construction; WTP/quote/reputation = model overlay — OK.
- Forbidden terms absent: "validation", "placebo arm", "mispricing",
  "observational equivalence" — OK.
- Author placeholders still bracketed — OK.

## JEBO scope self-test

The paper is a model of how selectively generated experience, subjective
probability transformation, and reputation jointly shape economic
inference and model-implied quote formation when outcomes are infrequent
and counterfactuals hidden — matching JEBO's aims (cognitive/
informational characteristics → economic outcomes; simulation modeling
explicitly in scope). It is not a rainmaking paper, weather paper,
empirical pricing paper, experimental-human-behavior paper, or
equilibrium asset-pricing paper, and the text says none of those things.
