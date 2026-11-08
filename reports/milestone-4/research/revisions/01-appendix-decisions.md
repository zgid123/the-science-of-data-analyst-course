# Milestone 4 revision: full draft, then move to appendix (2026-11-08)

User instruction (2026-11-08): rewrite Milestone 4 with the same mechanism: a complete report without a length limit,
then move what is worth moving to the appendices to follow the page suggestion, using the research-report and
build-report skills; the Vietnamese version through the complete build-report flow. Standing rule (2026-11-08): only
content the brief does not require, or content stated twice, may move; size alone is never the reason.

Page target: the brief (milestones/04/milestone-4.md) gives no page count. The user's decision of T02
(2026-11-06, PROGRESS.md) set the main text at 10–12 pages, appendices excluded; that is the working target.
User decision (AskUserQuestion, 2026-11-08, after the table moves at 20.0 / 27.0 pages): "Move the 2 figures too
(Recommended)"; no further moves of explanation.

## Before writing

- Milestone 3 was rewritten on 2026-11-08, so the Milestone 4 baseline was frozen again from it
  (code/freeze_baseline.py, logs/R0_refreeze.log, all five entry conditions PASS). The Milestone 3 changes are in
  wording and detail; the goal, questions, decisions and C01–C13 keep their meaning. Milestone 4 refers to change
  entries by identifier and copies no stale row.
- The tutor-group size of 20 was cited to the data descriptor [2]; the descriptor gives no such figure (Milestone 3
  check), so it is stated as an assumption without citation everywhere.

## Measurements (build-report page_budget.py; pessimistic layout of paginate.py)

| Stage | Optimistic | Pessimistic | Log |
| :---- | ---: | ---: | :---- |
| Condensed version (before this revision) | 12.4 | 18.0 | snapshot condensed-2026-11-08 (research/revisions/snapshots.md) |
| Full draft: prose rewritten in full, every appendix table brought into the main text | 26.9 | 39.0 | logs/R1_full_draft_pages.log, R1_full_draft_blocks.log |
| Moves: tables the brief does not require back to the appendices; repeated bootstrap passage removed | 20.0 | 27.0 | logs/R4_moves_pages.log |
| Moves: the two figures (user decision) | 19.3 | 26.0 | logs/R5_figures_pages.log |

## Block → brief requirement → decision

| Block (pessimistic pages in the full draft) | Brief requirement | Decision |
| :---- | :---- | :---- |
| Table 1.1 AQs (0.6) | §13 part 1: AQs still valid after Milestone 3 | Stays |
| Table 1.2 entry gate (0.4) | §3 Entry Gate | Stays |
| Tables 2.1–2.4 Modeling Briefs (2.0) | Task 1 template; deliverable B (one brief per AQ) | Stay (were summary + appendix in the condensed version) |
| Table 3.1 Candidate Solution Matrix (0.5) | Task 2 template; deliverable C | Stays |
| Tables 3.2–3.4 criteria comparisons (3.3) | §7.1 requires the rationale to address the eight criteria; Sections 3.2–3.4 argue them in prose | Appendix I (A.1–A.3) |
| Tables 4.1–4.4 Evaluation Design Cards (2.0) | §8.1 card, "bắt buộc"; deliverable D | Stay (were summary + appendix) |
| Table 4.5 metric definitions (0.7) | Not a template; Section 4.1 defines the metrics in words | Appendix II (A.4) |
| Table 4.6 protocol steps, 4.7 sample sizes (1.5) | Validation strategy is a card item; Section 4.2 describes every step and gives the key counts | Appendix III (A.5, A.6) |
| Table 4.8 success criteria (0.5) | Card item "success criterion"; §8 | Stays (Table 4.5) |
| Tables 4.9 audit groups, 4.10 checks (1.4) | Card items; Section 4.4 names groups and sizes, the cards hold per-question checks | Appendix IV (A.7, A.8) |
| Table 5.1 Risk and Ethics Notes (0.6) | Deliverable E | Stays |
| Table 5.2 risk register (1.5) | Detail of deliverable E | Appendix V (A.9) |
| Table 6.1 AI Decision Log (1.3) | §11.1 template; deliverable F | Stays (was a summary + appendix) |
| Tables 6.2, 6.3 critique decisions (1.7) | Evidence behind the log | Appendix VI (A.10, A.11) |
| Table 7.1 prototype protocol (0.5) | §13 part 7 only if Level 2 is done; kept as a protocol by the user's T02 decision | Stays |
| Table 8.1 traceability (0.5) | §12.1 template | Stays |
| Tables 8.2 full traceability, 8.3 C14 (1.2) | Deliverable A extends 8.1 with goal and prepared-data columns; Change Log | Appendix VII (A.12, A.13) |
| Figure 2.1 AQ → task map (≈0.7) | Not required; briefs, prose and Table 8.1 carry the mapping | Appendix I (Figure A.1), user decision |
| Figure 4.1 validation protocol (≈0.9) | Not required; Section 4.2 describes every step | Appendix III (Figure A.2), user decision |
| 4.3 bootstrap explanation | Stated in 4.2 as well | Removed from 4.3 (repetition) |

## Mechanics and checks

- Tables were moved into and out of the main text verbatim by scripts (code/insert_tables.py,
  code/restructure_appendices.py, logs/R2_restructure.log); appendices renumbered I–VII and A.1–A.13; references
  rewritten and checked by hand (card pointers to Sections 4.2 and 4.4; prompt references noted as given in this
  report's numbering).
- Citations renumbered by first citation (renumber_refs.py, logs/R3_renumber.log; map in
  research/revisions/02-reference-renumbering.md) and the register's reference map updated; trail check 0 errors.
- English pre-checks: format, structure, style, abbreviations, citations, names, research trail all PASS.

## Reader test and fixes (English)

An independent reader (fresh agent; the built Word document and the brief only) returned 30 items. Fixed:
- Inconsistencies: Table 7.1 step 5 now points to the cards and Table 4.5; the fairness rule renamed FR1 (F1 is the F1
  score of brief §8); the extended set stated once (10 further predictors plus 2 or 4 weekly click counts); Table 3.1
  and Appendix I agree on candidate labels (supplement, extension); Tables 3.1 and 8.1 name the extended-set switch;
  glossary pointers for cut-off and module run; survival set aside for the same two reasons everywhere; the AQ2
  module-specific differences come from the same model; Figure A.1 introduced in Appendix I.
- Followable without appendices: the 19 primary predictors listed by group in Section 3.3; C11 and DQ01–DQ19 in
  words; module codes AAA–GGG and run codes B/J defined in Section 1.1; Holm, Brier score, Nagelkerke R², expected
  shrinkage, registration lead and relative activity defined at first use; the 28.8% given its population (27,535
  enrolments at day 27, all 22 runs, no outcome used); day 14 explained (registration window closes); missing exam
  results explained.
- Brief requirements: class balance stated for AQ3 (checklist 15); confusion matrix reported per run and F1 replaced
  by recall, precision and lift at fixed length (brief §8); every threshold given its reason (logs/R6_threshold_reasons.log,
  code/threshold_reasons.py: ±0.2 → average risk 39.5–49.4%; recall SE 5 points on 100 non-completers, so 10 points ≈
  two SE; 400 × 28% ≈ 112; 7 of 9 folds by chance p ≈ 0.09); AQ2's 5-point threshold stated as the smallest gap worth a
  tutor's attention; one sentence per remaining 7.1 criterion for AQ2 and AQ4; prepared views named for Table 8.1.
- Wording: process phrases removed (C14 sentence, AQ4 readiness, prompts note, Section 6 reflection phrased as checks;
  the "drafter" clause replaced by the team's decision and verification); EU dates attributed to a legal commentary and
  the high-risk reading left for the university's legal staff to confirm.
Not changed: the prepared-view names in Appendix VII (the file names of the delivered Prepared Data Package); the
critique wording inside Appendix VI (AI evidence, as in Milestones 1 and 3). Main content after the fixes: 20.4 pages
optimistic, 28.0 pessimistic (logs/R6_pages.log).

## Vietnamese flow after the English fixes (2026-11-08)

- Rewrite of the 103 reader-test flags (research/reviews/09-vi-rewrite.md): 97 fixed, 2 rejected with reasons,
  4 on protected glossary terms left to the native user (flags 6, 12, 21, 65). The six stale twins synced.
- English aligned with the twins where the rewrite carried a meaning the English stated elsewhere: 04-01 "between model
  and rule"; 05-02 the choice of contact and any ranking by expected benefit stay deferred, AQ4 supplies only the list
  (D1); 08-00 "D1; choice of contact deferred". Twin 10-07 takes the same cell.
- Glossary rows settled (topics/early-warning-evaluation.md): "việc chọn hình thức liên hệ được hoãn" (Replaces "phần
  liên hệ được hoãn"), "biến thay thế" for proxy, one name "bootstrap hai tầng" (Replaces "bootstrap hai tầng ghép
  cặp"), single-test usage "tính điểm rủi ro". Milestone 3 twins 02-02 and 12-06 take the same two terms, so the
  deliverables share one term per concept.
- Checks (logs/R7_vi_rewrite_checks.log): glossary lint 0 errors; parity M1–M4 0 errors; precheck M3 and M4 all PASS.
- Next: fidelity check of the rewrites by a fresh reviewer (fidelity-2026-11-08.md) and a second reader test
  (reader-test-2.md), then make all, Word post-check and page measure.
- Fidelity check of the rewrites (research/reviews/10-vi-fidelity.md): 101 passages, 11 defects fixed in the
  twins (6 meaning or condition, 1 added claim, 2 glossary forms, 2 sentence forms); no English error.
- Second reader test (research/reviews/11-vi-reader-test.md): 112 flags (2 at clarity 1, 52 at 2, 58 at 3). Four
  pointed at the English and were fixed there: the AQ3 card names S2 before S3 (Table 4.5); "second freeze" restated
  where first used (Section 4.2); R4 recalibration "only on a run after the 2014 test runs" (no conflict with Section
  4.3); Table A.7 header "Enrolments in the smallest test run". Proxy returns to "biến đại diện (proxy)", the
  econometric term (glossary Replaces "biến thay thế"; Milestone 3 twin 02-02 likewise). The remaining flags go to
  a rewrite (research/reviews/12-vi-rewrite.md); the protected core terms wait for the native user, with the
  reader's evidence ("kỳ mở" 362 uses, "kiểm định khẳng định" read as a copy of "confirmatory").
- Rewrite 2 (research/reviews/12-vi-rewrite.md): 108 fixed, 1 already fixed, 1 rejected (glossary term),
  2 for the native user. English then fixed where the reader exposed it: Table A.7 header "Fewest enrolments of the
  group in one test run"; 10-01 "Compared with the primary model"; Table A.11 row 6 as R4; 01-01 names AQ3 (C10) and
  AQ4 (C13). Proxy check rows of the glossary aligned to "biến đại diện".
- Fidelity check 2 (research/reviews/13-vi-fidelity.md): 10 defects fixed, one unsupported reason removed;
  45 clarifying definitions kept and added to the English (research/revisions/03-english-additions-scripts/,
  logs/R8_english_additions.log), one rejected and rewritten ("online or blended" → every OULAD run is distance
  learning). The English also corrects the count of dummy terms (module 5, start month 1; 23 parameters).
- Build: make all TASK=milestone-4 exit 0, all checks PASS including the Word post-check (logs/R9_make_all.log).
  Main text 21.0 / 29.0 pages (EN) and 26.5 / 36.0 (VI), optimistic / pessimistic. No further moves: the user's
  decision of 2026-11-08 limits moves to tables and figures.
- Open for the native user: kỳ mở, kiểm định khẳng định, the two list-metric names (reader proposals in
  reader-test-2.md and rewrite-2-2026-11-08.md).
- Consistency with Milestones 1–3 (logs/R10_baseline_consistency.log): the seven Milestone 3 sources of the frozen
  baseline are unchanged since the freeze (hashes match); goal and SMART Goal match Milestone 3 word for word; every
  number in the English main text and appendices is found in the Milestone 1–3 reports or in the computed results and
  logs (44.4% = 5,245 / 11,811); each C01–C13 citation matches its entry. Two drifts fixed: Table 1.1 restored the
  full AQ2 wording of Milestone 3, and "programme" became "program" as in Milestones 1–3. make all: all PASS.

## Transform sentences in 03-03 and prototype package contract (2026-11-08)

- Reason: a check against the brief (§7.1 "Assumptions", §3 entry gate, §8, §14, §15) found one gap. Section 3.3 said "transformed predictors" without naming the transforms. A full table of preprocessing for each predictor would repeat Milestone 3 (`reports/milestone-3/package/src/fit_transforms.py`; M3 Section 6.3, Appendix II). Fixed results tables would leave empty placeholders in a Level 1 report, and the rubric gives them no points.
- Report change: four sentences added to the "Primary approach" paragraph of 03-03:
  - the logistic model's assumption that each predictor shifts the log-odds by a fixed amount per unit;
  - click activity is strongly skewed (602 median, 2,503 beyond the fence; M3 03-03 / DQ16);
  - the transforms: log1p for counts, training median plus a missing-value indicator, standardisation;
  - M3 fitted them on the 2013 runs, M4 refits them in each fold (Section 4.2), and the trees read the predictors untransformed.
- Vietnamese twin: written with glossary terms, then natively reviewed by a fresh agent (9 edits; `research/reviews/14-vi-native-review-transform-sentence.md`). Three glossary rows added to topics/early-warning-evaluation.md: log-odds, standardise, penalty.
- Prototype contract: `reports/milestone-4/package/README.md` (specification only, nothing run). It holds:
  - inputs and hash check;
  - preprocessing inside each fold, for each predictor kind;
  - configurations B1–B3 and M1–M4;
  - output CSVs with fixed columns;
  - experiment log fields;
  - the four places the report changes when results exist.

  It notes that the M3 `model_ready_*` files are not M4 model inputs: they use one column per module level fitted on all 2013 runs, while M4 uses deviation coding refitted in each fold.
- Checks: `make all TASK=milestone-4`, every step PASS, exit 0; parity warnings unchanged at 24 (`logs/R11_transform_sentence.log`).
