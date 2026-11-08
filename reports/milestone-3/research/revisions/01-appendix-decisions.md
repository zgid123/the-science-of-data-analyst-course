# Milestone 3 revision: full draft, then move to appendix (2026-11-08)

User instruction (2026-11-08): continue the process on Milestone 3: write the comprehensive report first, then reduce
the main text by moving non-critical information to appendices, following `milestones/03/milestone-3.md`.
User reminder (same day): run the complete build-report flow for the Vietnamese document.
User decision (AskUserQuestion, 2026-11-08, after move 2 at 23.6 pages): "Move explanations (Recommended)": keep every
brief template table in the main text; move the long per-aspect evidence and per-question reasoning to the appendices,
each leaving a full-sentence summary and pointer. Estimate offered: about 17–19 pages.

## Before writing

- Milestones 1 and 2 were rewritten on 2026-11-07. The Milestone 3 baseline was frozen again from them
  (`code/freeze_baseline.py`, logs/R0_refreeze.log: 8 Milestone 1 files unchanged against Milestone 2's pins, 11
  Milestone 2 files hashed, 6 of 6 inputs present).
- Change Log rows C01–C08 are now copied from Milestone 2 by `code/sync_change_log.py` (logs/R0_sync_change_log.log):
  C02 (semester length not fixed in Milestone 1; eight to nine months) and C06 (on OULAD the early-sign rule counts one
  missed or late task) had drifted; 0 differences after the sync.
- C10 (package change_log.md and research/fit/aq-data-fit.md) now starts from the C06 form of the rule; DQ18 impact
  and the AQ3 fit row name both forms. The AI Decision Log intro says "all seven roles" (13 entries cover seven roles).
- Appendices regenerated (logs/R0_refreeze.log): only C02, C06, C10 (Appendix IV) and DQ18 (Appendix I) changed.
  The Vietnamese appendices are translated files, not generated: they are updated in the Vietnamese pass.

## Rule applied to every block

As in Milestones 1 and 2: the main text keeps every element of the brief's section 16.1 structure and every template
table the brief prints (Dataset Understanding Map 6.1, Data Quality Issue Log 7.1, AQ–Data fit decisions 8, missing
value / variable distinction 8.2, Preparation Decision Matrix 9, leakage rules 11, before/after checks 13, Model
Readiness Matrix 12.1, AI roles 14), the result of each step in full sentences, the definition of every term it uses
and one reason per choice. A block moves when it is evidence detail, a derivation, a per-item explanation or a table
that an appendix already holds; it leaves a summary with its numbers and identifiers and a pointer.

## Measurements (reports/milestone-1/code/estimate_parts.py, line model of build-report)

| Stage | Main content (Parts 1–10) | Log |
| :---- | :---- | :---- |
| Condensed version (before this revision) | 12.6 pages | snapshot condensed-2026-11-08 (research/revisions/snapshots.md) |
| Full draft, no length limit | 27.4 pages | logs/R1_full_draft_pages.log, R1_full_draft_blocks.log |
| Move 1: tables already in the appendices (A.1, A.2, A.3, A.7, A.11, A.12, A.13); evidence column of Table 3.1 | 23.9 pages | logs/R2_move1_pages.log |
| Move 2: pipeline step notes; entry-conditions table (new A.19) | 23.6 pages | logs/R3_move2_pages.log |
| Move 3 (user decision): per-aspect evidence of 3.1–3.4; per-question fit reasoning; split controls; before/after explanations; Milestone 2 changes in full | 21.4 pages | logs/R4_move3_pages.log |
| Move 4: measures of 2.2; feature choices and predictor sets; synthetic-data levels; AI decision detail and reflection; Part 1 signpost | 20.8 pages | logs/R5_move4_pages.log |
| Move 5: entry-condition restatement; package layout; traceability chain in the Part 8 introduction | 20.6 pages | logs/R6_move5_pages.log |

## Blocks moved

| Block (main text) | Moved to | Main text keeps |
| :---- | :---- | :---- |
| 1.2 Table of the six inputs | Appendix I, Table A.1 | "All six inputs are complete" with pointer |
| 2.2 Table of key-field meanings; measures paragraph | Appendix I, Table A.2; detail-01 | Meaning of each date field in a sentence; banked results, mark timing, weights and credits in one paragraph |
| 2.3 Table of sensitive attributes | Appendix I, Table A.3 | The six attributes, the 20-student limit, the smallest groups |
| 3.1–3.4 full evidence and reasoning | Appendix I (detail-01) | One summary per aspect with every finding, its number and DQ identifier |
| 3.5 Evidence column of Table 3.1 | Appendix I, Table A.4 (and the summaries of 3.1–3.4) | All 19 issues with variable, impact, severity and decision |
| 4.1 Per-question reasoning (AQ1–AQ4) | Appendix IV (detail-04) | Table 4.1 and one paragraph stating C09–C13 with their reasons |
| 1.1 Milestone 2 changes C01–C08 one by one | Appendix IV (detail-04) | One paragraph naming the effect of every change |
| 4.2 Five levels of the synthetic-data policy | Appendix IV (detail-04) | The level used (A) and its limits |
| 6.1 Table of the ten steps; step notes; stage list; package layout | Appendix II, Tables A.7, A.8; detail-02 | Steps and their main results in one paragraph; single command, logs, rerun identity |
| 6.2 Feature choices; predictor sets | Appendix III (detail-03) | Missed-task rule, activity ratio, 20 + 10 predictors, role of demographics |
| 6.3 Repeating students; fitted transforms in full | Appendix II (detail-02) | One paragraph with the flag, the folds, train-only fitting and its check |
| 7.1 Two explanations; unit tests and manual check | Appendix VI (detail-06) | One paragraph with the 189 enrolments, the failing design and the tests |
| 7.2 Lineage table of main variables | Appendix III, Table A.12 | What the table holds, 88 rows, one worked example |
| 8.1 Table of views by level | Appendix III, Table A.11 | Views, populations and results per level in prose |
| 8.2 Table of entry conditions | Appendix VI, Table A.19 | The six conditions hold for AQ1–AQ3 |
| 8.3 Updated traceability section | Appendix IV, Table A.13 | Definition of the chain and what it leaves to the pilot |
| 10 Second accepted-in-part decision; reflection | Appendix V (detail-05) | Roles table, critique counts, the four rules, the rejected request |

## Not moved, with reason

The template tables listed above stay because the brief prints them as the content of its sections. Section 9
(ethics) and Section 7.3 (residual risks) stay whole: the brief asks for every limitation in the main text.

## Result against the estimate

The main content is 20.6 pages, above the 17–19 pages estimated when the option was offered and above the brief's
8–12. Every remaining block is a template table or the explanation its section needs; further cuts would condense
sentences again. The estimate was optimistic for the same reason as in Milestone 1: the summaries left in place of
moved blocks keep their numbers and definitions and so cost more than a pointer.

## New scripts and logs

- `code/sync_change_log.py` (C01–C08 from Milestone 2), logs/R0_sync_change_log.log
- `code/count_submission_types.py` (168,953 TMA/CMA submissions, 4,959 exam rows), logs/R1_submission_types.log
- `code/count_zero_click_change.py` (3,365 + 189 = 3,554 enrolments without clicks), logs/R1_zero_click_change.log
- `code/build_appendices.py`: appends `research/appendix/detail-NN.md` to Appendix NN.

## Reader test and fixes (English)

An independent reader (fresh agent, reading only the built Word document and the brief) returned 30 items. Fixed:

- Brief template content restored to the main text: a short Evidence column in Table 3.1; a six-row lineage excerpt
  (Table 7.2); Table 10.1 in the brief's AI Decision Log format (the roles table moved to Appendix V); the traceability
  chain per question (Part 8 introduction); the six entry conditions named (Section 8.2).
- Consistency: critique 4 is "Accepted in part" everywhere (package ai_decision_log A8); exclusion of Withdrawn
  enrolments without a day at both cut-offs (89 and 90); six sensitive attributes, five audit-only, highest education
  a predictor that is audited; Section 7.3 claim limited to the first three risks; all ten extended predictors listed;
  the six features of V11 named; capacity per list and week stated, with the support-office 30–40 from Milestone 1.
- Clarity: module codes AAA–GGG introduced; populations named for 65.7/46.6%, 24.9–58.3% and 45.7–73.8%; the 70%
  baseline separated from OULAD's 54.7%; missingness over time (0.13–5.89% by run) and co-occurrence (not examined)
  stated; Riazy et al. metric named (disparate impact, percentage points); seven glossary terms added.
- Accuracy: tutor-group size sourced to Hlosta et al. [9] ("a few tens of students"), 20 an assumption (also in the
  package feature_spec.md); run time "about 20 seconds" from the log time stamps; the 7-day CMA lag stated as a 2025
  rule assumed for 2013–2014; cma_score_mean_c marked "prepared, not a predictor"; V13 described as the click check it
  is; the fold rule of Milestone 4 (students in the held-out run removed from that fold's training data); "check log
  T08" removed from DQ05.

Not changed: length (user decision); process wording inside the AI evidence tables of Appendix V (decision evidence,
as in Milestone 1); file names inside the verbatim AI prompts. Main content after the fixes: 21.7 pages
(logs/R9_pages.log).

## Vietnamese flow (build-report reference.md 4.3, all six stages)

| Stage | Work | Record |
| :---- | :---- | :---- |
| 1 Terms | Open terms settled in the topic glossary before translation, and every term raised by translators, reviewers and reader tests settled once; rows that clashed with Milestones 1, 2 or 4 scoped so all four reports keep 0 parity errors | logs/R8_vi_terms.log |
| 2 Front matter | Abbreviation and terms pages translated first (EDA added later in both languages) | 00-1, 00-2 .vi.md |
| 3 Translation | Four parallel groups: A Parts 1–3, B Parts 4–7, C Parts 8–10 with Appendices IV–V, D Appendices I–III and VI | translator reports |
| 4 Native review | One fresh reviewer per group: 56 (A), 70 (B), 110 (C), 54 (D) edits | research/vi-review/review-2026-11-08-{A,B,C,D}.md |
| 5 Consistency and reader tests | Consistency pass (65 edits); reader test 1 (99 flags: 6/70/23 by clarity 1/2/3) → rewrite (99 fixed) → fidelity check (15 fixes); reader test 2 (82 flags: 1/51/30) → rewrite (76 fixed, 6 core glossary terms left to the user) → fidelity re-read (80 of 82 clear on first reading; 10 fixes) | consistency-2026-11-08.md, reader-test-2026-11-08.md, rewrite-2026-11-08.md, rewrite2-2026-11-08.md |
| 6 Build | `make all TASK=milestone-3`: 14/14 steps; both documents 30 numbered headings, 4 figures, 31 tables; skill self-tests 147/147 and 55/55 | logs/R13_make_all.log |

English sources clarified on translators' and readers' findings (no new content): appendix self-citation, "Measures in full" antecedent, fold rule; "three issues"; "three other gaps"; EDA defined; critique-4 sentence; Table 10.1 "at least 7 days"; V13 logic; "a row is a logging record"; AQ4 RED reason; one-task rule and 45% random-list reasons; "three further controls"; duplicate-row test spelled out; entry-gate core; 4.1 split into five paragraphs with 28,119 explained; cohort statistic; altered test rows; 10% coverage scope; 30–40 per review point; "outside both predictor sets"; "a single click record".

Open for the user: six core Vietnamese glossary terms flagged by the second reader test ("kỳ mở", "lượt đăng ký học … còn hiệu lực", "Chỉ định", "nhóm tính KPI", "phiên bản cơ sở", "kỳ mở huấn luyện"; plus "độ chính xác của danh sách" for precision). They are shared with the Milestone 2 and 4 reports, so they change only on the user's decision.

Final size (logs/R13_pages_EN.log, R13_pages_VI.log): main content 22.0 pages in English, 27.0 in Vietnamese. The Vietnamese document turns Table A.11 landscape (longer cell text), hence 17 Word sections against 15; the main text and front pages have the same structure in both.

## Review against the brief with the pessimistic page budget (2026-11-08)

User request: revisit the brief's task requirements and report structure (section 16.1) and say whether anything is
worth moving by the page estimate. Measurements: logs/R22_page_budget.log (`make pages TASK=milestone-3 BUDGET=12`):
main content 30.0 pages pessimistic (22.0 optimistic) in English, 37.0 (27.0) in Vietnamese; the last main-text page
is 83% full in English and 41% in Vietnamese, so a cut saves a page only above 0.83 or 0.41 of a page.

| Part (pessimistic EN pages) | Brief requirement | Verdict |
| :---- | :---- | :---- |
| 1 Baseline and dataset (2.8) | 16.1 §1 (M1/M2 summary, dataset/version, scope, current AQs); section 3 inputs and entry gate | Required |
| 2 Data understanding (3.4) | 16.1 §2; Task 1 (population, unit, keys, outcome, time, measures, codes, sensitive); Dataset Understanding Map 6.1 | Required |
| 3 Profiling and quality (5.3) | 16.1 §3; Task 2's ten aspects; Data Quality Issue Log 7.1 with evidence | Required |
| 4 AQ–data fit (3.1) | 16.1 §4; Task 3 (GREEN/YELLOW/RED, procedure 8.1, missing value/variable 8.2, synthetic policy 8.3); change log C09–C13 | Required |
| 5 Preparation plan (2.5) | 16.1 §5; Task 4 Decision Matrix and 9.1 guidance | Required; the closing "three decisions" paragraph (0.24) partly repeats 6.2 and 6.3 |
| 6 Pipeline (3.9) | 16.1 §6; Task 5 ten steps and 10.1 structure; Task 6 split and leakage rules | Required |
| 7 Validation (3.6) | 16.1 §7; Task 8 checks and Lineage Table 13.1; residual risks | Required |
| 8 Readiness (2.5) | 16.1 §8; Task 7 views and Readiness Matrix 12.1; questions not yet feasible; section 19 conditions; deliverable B summary | Required |
| 9 Ethics and limitations (1.1) | 16.1 §9 | Required; one sentence overlaps 3.4 (results checked on the university's records), each section needs it |
| 10 Generative AI (1.8) | 16.1 §10; AI Decision Log 14.1 | Required |

Repeated content totals about 0.3 page in English and about 0.35 in Vietnamese, below the free space on the last page
in both languages, so removing it saves no page. Decision: no move and no writing change; no translation work follows.
