# JRU compliance checklist

Sources: Springer pages for *Journal of Risk and Uncertainty* — Aims and scope,
Submission guidelines, and Journal updates/Open access fees — retrieved
2026-11-09 through the browser (plain HTTP returned a script challenge);
extracted text saved locally during the session. Verify again on the day of
submission.

| Requirement (official wording summarised) | Status | Evidence |
|---|---|---|
| Scope: risk-bearing behaviour, decisions under uncertainty, experimental and real-world risk, behavioural models, risk and policy | Pass | Research question is learning about rare-event risk from selected experience |
| Out of scope: finance/behavioural finance, game theory, notes, cardinal Likert use | Pass | None used; no strategic equilibrium analysis |
| Research article; no fixed word limit, long papers discouraged (≈40 pages preferred, 50 maximum) | Pass | Blinded PDF page count in `manuscript/manuscript_metrics.json` (`pages_blinded_pdf` ≤ 50; checked by `run_all.py`, `analysis/final_audit.py`, tests) |
| Abstract 150–250 words | Pass | `abstract_words` in `manuscript_metrics.json`; gate in build tests |
| 4–6 keywords | Pass | 6 keywords; gate in tests |
| JEL codes | Pass | D81; D82; D83; D84 |
| Double-blind: anonymised manuscript, separate title page | Pass | `manuscript/manuscript_blinded.docx/.pdf`; `submission/title_page.docx`; blinded-file scan in `analysis/final_audit.py` |
| Author–year citations; alphabetical reference list | Pass | APA-style list sorted by author sequence then year; citation–reference completeness enforced by build |
| Figures cited in text, numbered, captions "Fig. 1" without trailing period | Pass | `jru_caption()`; test `test_every_figure_and_table_is_cited` |
| Tables numbered, cited, with captions | Pass | Same test |
| Supplementary material as Electronic Supplementary Material, referred to as "Online Resource 1" | Pass | `supplement/supplement.pdf`; text references |
| Statements and Declarations: funding, competing interests, ethics, consent, data/code availability, author contributions | Author action | Section present; author-specific placeholders in `AUTHOR_ACTIONS_REQUIRED.md` |
| Data availability statement (required for original research) | Pass (pending URL confirmation) | Statement names public mirror and ERA5 route |
| Generative-AI use beyond copy-editing must be declared; LLMs not authors | Author action | Disclosure placeholder in declarations |
| No submission fee; hybrid journal; Open Choice APC optional | Info | Recorded fees at retrieval: £2290 / $3190 / €2590 (verify) |
| Editable source files (Word or LaTeX) | Pass | DOCX supplied |
