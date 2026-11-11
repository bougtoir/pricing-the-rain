# Critical-Review Response Log

Revision type: reviewer-driven conceptual sharpening (Economic Modelling).
Starting hash: 57c79433c. Freeze contract: rainfall module, seeds, validated
outputs, corrected estimand definitions all frozen. Allowed: derivations from
the existing model, diagnostics from frozen outputs, terminology/claim
corrections, reorganization.

## CR-1 (Issue 6) — Analytic selection-ratio lemma
- Derived E[p_t | O=1] in closed form for the two-state model.
- p enters acceptance only through relative hazard (p_t/base − 1), and demand
  only through the state M_t, so base_prob cancels exactly: the selection
  ratio is IDENTICALLY independent of baseline rarity, not approximately.
- Analytic value: 1.71147 (vs simulated 1.713/1.711/1.710/1.708 across the
  four regimes); analytic gaps 0.218/0.073/0.022/0.007 vs simulated
  0.216/0.072/0.022/0.007. Differences are Monte Carlo error.
- Decision: present 1.71 as a parameter-specific value of a general ratio
  formula; new Lemma in Model section with proof. No rerun needed.

## Final status (post-build)

- All issue changes built into manuscript (5,501 words; abstract 234 words; 25 references).
- Lemma 1 stated in §2.4, cited §3.5/§6.1; derivation in `docs/SELECTION_RATIO_DERIVATION.md`; verified by `test_lemma_selection_ratio`.
- Figure numbering reordered to first-citation order (benchmark figure now Figure 2).
- pytest 25/25 PASS; final_audit PASS; reproduction manifest regenerated.
- Final report: `docs/FINAL_CRITICAL_REVIEW_REVISION_REPORT.md`.
