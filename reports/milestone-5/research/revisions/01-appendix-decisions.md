# Appendix decisions (T15): from the full draft to a 25-page main text

The full draft (commit `a6a8d5a`, listed in `snapshots.md`) wrote every section in full. T15 moved detail to sixteen
appendices so that the main text fits the brief's 15–25 pages (brief Section 7) while every element of the brief's
Section 2 table stays in the main text. This record gives the rules, the measurements, one row per moved or cut block,
and the loss check.

## Rules applied

1. Write full, then move: blocks move verbatim (`code/t15_move_to_appendix.py` copies them from `a6a8d5a`, rewriting
   only table numbers, references to subsections that moved, and "(Milestone N, Section x)" to "(Milestone N)"); the
   main text is rewritten as full sentences, never condensed into fragments.
2. Map before moving: each block was matched to the brief's required structure (Section 2 table, 3, 3.1, 4.1, 5, 6.1,
   7, 9) before it moved. Brief-required tables stay in the main text, in compact form where the full form is long:
   final SMART/KPI table (2.1), final AQ table with the quality check (3.1), AQ Revision Log (3.2, brief 3.1),
   AQ–Data Requirement and Dataset Selection Matrices (4.1, 4.2), data dictionary (5.1), AQ–Data Fit Matrix with status
   (5.2), profiling and quality tables (6.1, 6.2), Preparation Decision Matrix (7.1), Model/Method Selection Matrix
   (8.1), Evaluation Plan (9.1), Final Project Traceability Matrix (11.1, brief 3), AQ answers table (11.2, brief 5),
   limitation log (12.1). The AI Decision Log goes to Appendix XVI, which the brief allows ("Đưa phụ lục hoặc file
   riêng", brief Section 7).
3. A fact stated twice may be cut to one statement; the cut copy leaves a pointer.
4. Each moved block leaves its result in the main text in full sentences with a pointer "(Table A.n, Appendix N)".
5. Main text ≤ 25 pages on the pessimistic layout; part targets ≈ 1–3: 3.5, 4–5: 3, 6–7: 5, 8–9: 4, 10: 0.5,
   11–12: 6.5, 13–14: 2 pages. The total is the binding limit; per-part targets guide where to cut.
6. Appendix tables are numbered A.1–A.41 in order of appearance; main tables restart in each part.

## Measurements

Commands and full output: `logs/T15_move_appendix.log` (measures 0–4), built with `report.py build milestone-5 --lang
en --force` and measured with `page_budget.py … --budget 25 [--blocks]`.

| Part | Target (pages) | Full draft, pessimistic | Final (measure 4), pessimistic | Final, optimistic |
| :---- | :---- | :---- | :---- | :---- |
| 1–3 Context, goal, questions | 3.5 | 22.5 | 5.85 (2.00 + 1.46 + 2.39) | 4.4 |
| 4–5 Requirements, dataset | 3 | 11.1 | 2.84 (1.40 + 1.44) | 2.0 |
| 6–7 Understanding, preparation | 5 | 16.9 | 3.76 (2.30 + 1.46) | 2.9 |
| 8–9 Modeling, evaluation | 4 | 14.5 | 3.61 (1.89 + 1.72) | 2.7 |
| 10 Experiment | 0.5 | 2.0 | 0.31 | 0.3 |
| 11–12 Findings, limitations | 6.5 | 40.8 | 5.80 (4.67 + 1.13) | 4.4 |
| 13–14 AI, conclusion | 2 | 7.1 | 2.82 (1.13 + 1.69) | 1.6 |
| Main text | ≤ 25 | 115.0 (77.3 optimistic) | 25.0 | 18.2 |

Parts 1–3 run 2.4 pages over their guide because the three brief-required tables of Part 3 (final questions with the
quality check, AQ Revision Log) take 1.4 pages; Parts 6–9 and 11–12 run under theirs, so the total meets the limit.
Section 14 shows a layout gap of 0.84 pages from the page break before the back matter; the text itself is 0.86 pages.
The appendices take 116.4 pages.

## Blocks moved or cut

Pages are those of `--blocks` in measure 0 (full draft). "Kept" means the result stays in the main text in full
sentences; the appendix holds the verbatim block.

| Block (pages in the full draft) | Brief requirement | Decision | Where now |
| :---- | :---- | :---- | :---- |
| 1 Educational setting, regulation, published studies, problem (1.72) | §2 row 1: context, motivation | Kept: setting, Circulars 01/2024 and 83/2026 [S115, S116], late notice, 2–4-week window [S112]; detail moved | Section 1; Appendix I |
| 1.1 lead-in (0.44) | §2 row 1: motivation, stakeholders | Kept as the 1.1 opening; signposting cut | Section 1.1 |
| Table 1.1 Stakeholders, needs, decisions (0.57) | §2 row 1: stakeholders | Moved; actors of D1–D3 and their needs kept in sentences | Table A.1, Appendix I; Section 1.1 |
| Text after Table 1.1: how needs were established, needs, conflicts, published practice (1.27) | §2 row 1: "stakeholder needs synthesised" | Moved; simulated-interview caveat, list at weeks 3 and 5, capacities, support only, OU Analyse [S112] kept | Appendix I; Section 1.1 |
| 1.2 scope, outside scope, objective, stand-in data, how far the project goes, chain (2.64) | §2 row 1: scope, objective | Kept: scope, five exclusions, objective, stand-in, status of AQ1–AQ4, Figure 1.1; detail moved; "how far the project goes" cut as duplicate of Table 3.1 and Section 10 | Section 1.2; Appendix I |
| 2 Business Goal, SMART Goal, pilot design, why assumed (1.03) | §2 row 2: Business Goal, SMART Goal | Kept: goal, SMART Goal, pilot courses, assumption; justification moved | Section 2; Appendix II |
| Table 2.1 SMART check + text (0.73) | §2 row 2 | Moved; "meets the five SMART criteria" kept with pointer | Table A.2, Appendix II |
| 2.1 KPI definitions (1.60) | §2 row 2: primary/secondary KPI | Kept: proxy at day 14, early-sign rule (C10, C17), contact parts in the pilot; full definitions moved | Section 2.1; Appendix II |
| Table 2.2 Final SMART Goal and KPIs (0.58) + text (0.42) | §2 row 2 evidence: final SMART/KPI table | Kept compact as Table 2.1; recount years and full definitions in Appendix II | Table 2.1; Appendix II |
| Table 2.3 Decisions and evidence (0.55) + text (0.26) | §2 row 2: decision needs | Moved; D1–D3 with their evidence level kept in sentences | Table A.3, Appendix II; Section 2.1 |
| 3 How the questions connect, levels, definitions, status (0.88) | §2 row 3: final AQ, levels | Kept: unit, reading by level, status scale, normalised recall and lift; detail moved | Section 3; Appendix III |
| Table 3.1 Final analytical questions (0.84) + text (0.75) | §2 row 3; brief 5 reading rules | Kept, with a quality-check column added; text after moved | Table 3.1; Appendix III |
| 3.1 lead-in and criteria (0.39) | §2 row 3: AQ quality check | Kept (criteria defined) | Section 3.1 |
| Table 3.2 Quality check with reasons (0.93) + text (0.49) | §2 row 3 evidence: AQ quality check | Result merged into Table 3.1 and stated in 3.1; table with reasons moved | Table A.4, Appendix III |
| 3.2 changes that touch every question (0.91) | brief 3.1 | Kept: link to Change Log, YELLOW/RED, C15–C17; detail moved | Section 3.2; Appendix III |
| Table 3.3 AQ Revision Log (4.00) | brief 3.1 (required table) | Kept compact as Table 3.2; every cell in full moved | Table 3.2; Table A.5, Appendix III |
| Table 3.4 Status scales + reading the actions, three entries, what did not change (1.35) | brief 3.1 | Moved; Controlled Change Log C01–C17 added as Table A.7 | Tables A.6–A.7, Appendix III |
| 4 Sources, shared requirements, time (0.90) | §2 row 4: unit, outcome, time, population | Kept in one paragraph; detail moved | Section 4; Appendix IV |
| Table 4.1 AQ–Data Requirement Matrix (0.99) | §2 row 4 evidence: Data Requirement Matrix | Kept compact as Table 4.1; source systems moved | Table 4.1; Table A.8 |
| Gates, optional variables, declared gaps (0.76) | §2 row 4 | Kept: gates G1–G5 and the declared contact gap; reasons moved | Section 4; Appendix IV |
| 4.1 Search procedure (0.86) | §2 row 4: candidate datasets | Kept: repositories, seven candidates, scoring; procedure and keywords moved | Section 4.1; Appendix IV |
| Table 4.2 Dataset Selection Matrix (0.94) + text (1.06) | §2 row 4 evidence: Selection Matrix; selection rationale | Kept compact as Table 4.2 (totals, gates, decision); per-criterion scores and reasons moved | Table 4.2; Table A.9, Appendix IV |
| Table 4.3 Provenance, version, licence (0.40) + text (0.24) | §2 row 4: provenance/licence; brief 7 | Kept: DOI, version, access date, checksums, CC BY 4.0 [S002]; table moved | Section 4.1; Table A.10 |
| 5 Population, unit, files, keys (0.57) | §2 row 5: files/tables, keys, dimensions | Kept: runs, coding, day 0, keys (sentence added after the brief check), counts | Section 5; Appendix V |
| Table 5.1 Tables of OULAD (0.49) + text (0.30) | §2 row 5: files/tables | Moved; key-variable sources and scales restored as a paragraph after it | Table A.11, Appendix V |
| Table 5.2 Key variables (0.54) | §2 row 5 evidence: data dictionary | Kept as Table 5.1 (source column to Appendix V text) | Table 5.1; Appendix V |
| Sample, coverage, raw gaps (0.63) | §2 row 5: sample, coverage, gaps | Kept: sample counts, 2013/2014 coverage, tasks due by day 27; detail moved | Section 5; Appendix V |
| 5.1 lead-in (0.41) | §2 row 5 | Kept: GREEN/YELLOW/RED scale | Section 5.1 |
| Table 5.3 AQ–Data Fit Matrix (0.75) | §2 row 5 evidence: AQ–Data Fit Matrix with status | Kept compact as Table 5.2 with action and status; full cells moved | Table 5.2; Table A.12 |
| Table 5.4 Gap classes + why no other dataset, status, unsupported questions (1.07) | §2 row 5: "which questions are not supported" | Kept: no imputation or simulation, three parts that need university records, none dropped; table moved | Section 5.1; Table A.13, Appendix V |
| 6 Unit, outcome, balance, distributions (1.40) | §2 row 6: distribution, imbalance | Kept: 10.9M rows, 13 recounts, outcome balance, module mix, click skew; detail moved | Section 6; Appendix VI |
| Table 6.1 Populations (0.49) | §2 row 6 evidence: profiling tables | Kept as Table 6.1 (description column merged) | Table 6.1 |
| 6.1 lead-in (0.42) | §2 row 6: quality findings | Kept: severity scale | Section 6.1 |
| Table 6.2 Data Quality Issue Log (1.62) | §2 row 6 evidence: quality findings | Kept compact as Table 6.2 (grouped IDs); evidence column moved | Table 6.2; Table A.14 |
| Duplicates, missing values, validity, outliers, issues that could change a conclusion (1.80) | §2 row 6: missingness, duplicates, invalids, outliers | Kept: three High and two Medium issues with numbers; detail moved | Section 6.1; Appendix VI |
| 6.2 Temporal coverage, representativeness (1.09) | §2 row 6: temporal coverage, representativeness | Kept in summary; detail moved | Section 6.2; Appendix VI |
| Table 6.3 Sensitive attributes + threshold of 20, privacy (1.14) | §2 row 6: sensitive fields | Kept: six attributes, [S906], [S907], [S913]; table and detail moved | Section 6.2; Table A.15 |
| 7 Decisions before change, governing decisions (0.61) | §2 row 7: cleaning, missing handling | Kept: V01–V15, three governing decisions | Section 7 |
| Table 7.1 Preparation Decision Matrix (1.53) + text (0.84) | §2 row 7 evidence: Preparation Decision Matrix | Kept compact as Table 7.1; reasons, population rule and ten steps moved | Table 7.1; Table A.16, Appendix VII |
| 7.1 Timing rule (0.50) | §2 row 7: leakage control | Kept | Section 7.1 |
| Table 7.2 Derived variables + predictor sets, encoding (1.86) | §2 row 7: derived variables, encoding | Kept: main derived variables, 19 predictors / 23 parameters, deviation coding, refit per fold; table moved | Section 7.1; Table A.17 |
| Table 7.3 Leakage risks + split (1.05) | §2 row 7: leakage control | Kept: definition, four controls, 1,586 flagged, failing date-filter check; table moved | Section 7.1; Table A.18 |
| 7.2 lead-in (0.27) | §2 row 7: final dataset/version | Kept | Section 7.2 |
| Table 7.4 Before-and-after checks (1.09) | §2 row 7 evidence: reproducible pipeline | Kept: 22 checks, 55,604 rows, 88 variables; table moved | Section 7.2; Table A.19 |
| Table 7.5 Prepared views + reproducibility, KPI sensitivity, synthetic data (1.10) | §2 row 7: final dataset/version | Kept: Parquet views, rebuild command, licence, synthetic data only in tests; detail moved | Section 7.2; Table A.20, Appendix VII |
| 8 Readiness, why ranking, development data, purpose, Modeling Briefs (1.64) | §2 row 8: AQ → type → task | Kept: Level 1 status, purpose rule [S900], need for ranking, four tasks; detail moved | Section 8; Appendix VIII |
| Table 8.1 Modeling Briefs (0.80) + text (0.33) | §2 row 8 | Moved | Table A.21, Appendix VIII |
| 8.1 Criteria (0.72) | §2 row 8: rationale | Kept in summary | Section 8.1 |
| Table 8.2 Model and Method Selection Matrix (0.84) | §2 row 8 evidence: Model/Method Selection Matrix | Kept as Table 8.1 | Table 8.1 |
| Rationale per question (2.39) | §2 row 8: rationale; brief 4.1 "explain rationale" | Kept as "Rationale in brief" (one argued sentence group per AQ); full rationale moved | Section 8.1; Appendix VIII |
| 9 One design, capacity, metric definitions (1.22) | §2 row 9: metric | Kept: TRIPOD+AI [S901], capacity, recall and lift definitions; detail moved | Section 9; Appendix IX |
| Table 9.1 Evaluation Plan (0.74) | §2 row 9 evidence: Evaluation Plan | Kept as Table 9.1 | Table 9.1 |
| 9.1 Validation per question (1.81) | §2 row 9: split/validation, success criterion | Kept: five-point threshold [S903], calibration [S902], separation [S901], folds, challenger margin, C16; detail moved | Section 9.1; Appendix IX |
| Table 9.2 Success criteria + validation design (1.57) | §2 row 9 | Moved | Table A.22, Appendix IX |
| 9.2 Leakage in evaluation, fairness rationale (0.97) | §2 row 9: leakage/fairness/interpretability | Kept in summary with FR1 | Section 9.2 |
| Table 9.3 Audit groups + error analysis, interpretability (1.46) | §2 row 9 | Kept: groups with counts, model card [S910]; table and detail moved | Section 9.2; Table A.23, Appendix IX |
| 10 Status and reasons (0.90) | §2 row 10; brief 4.2 Level 1 case | Kept: Level 1, prototype unrun and why, AQ1/AQ2 not a prototype; protocol detail moved | Section 10; Appendix X |
| Table 10.1 Configurations + eight steps, logged test, what would change (1.10) | brief 4.2 | Moved | Table A.24, Appendix X |
| 11 Reading by level, confidence grades (1.07) | §2 row 11; brief 5 reading rules | Kept: reading rules [S900, S904], confidence grades | Section 11 |
| Table 11.1 How each answer is read (0.58) | brief 5 reading rules | Moved | Table A.25, Appendix XI |
| 11.1 Lead-in and status rule (0.71) | brief 3 | Kept in summary | Section 11.1 |
| Table 11.2 Traceability Matrix, compact (2.07) + text (0.29) | brief 3 (central table) | Kept as Table 11.1 with shorter cells; detailed cells moved | Table 11.1; Table A.26 |
| Table 11.3 Status justification (0.57) | brief 3 status | Moved | Table A.27, Appendix XI |
| 11.2 and 11.2.1–11.2.5 with Tables 11.4–11.7 (6.6) | §2 row 11: answer AQ1 | Kept: method, criterion met, all headline rates with intervals, Figure 11.1, first missed week, year comparison, confidence, D2 meaning; subsections moved | Section 11.2; Tables A.28–A.31, Appendix XII |
| 11.3 and 11.3.1–11.3.6 with Tables 11.8–11.11 (7.6) | §2 row 11: answer AQ2 | Kept: population, model, five estimates, Figure 11.2, module and sensitivity consistency, continuous adjustment, groups, open parts, confidence; subsections moved | Section 11.3; Tables A.32–A.35, Appendix XIII |
| 11.4 and 11.4.1–11.4.3 with Table 11.12 (3.1) | §2 row 11; brief 4.2 (no metric) | Kept: expected outputs and deciding criteria; detail moved | Section 11.4; Table A.36, Appendix XIV |
| 11.5.1 with Table 11.13 Final answers (9.81) | brief 5 (required table) | Kept compact as Table 11.2; detailed cells moved | Table 11.2; Table A.37 |
| 11.5.2–11.5.3 with Table 11.14 Decision support (2.13) | §2 row 11: decision support | Kept: options to test for D1, D2, D3; table and hypotheses moved | Section 11.5; Table A.38, Appendix XIV |
| 12 Kinds of limit (2.50) | §2 row 12: gaps, generalisability, causal and model limits | Kept: three situations, scope [S908], confounding [S904], labelling risk [S905]; detail moved | Section 12; Appendix XV |
| Table 12.1 Limitation log (1.80) | §2 row 12 evidence: limitation log | Kept compact as Table 12.1; effect column moved | Table 12.1; Table A.39 |
| 12.1 with Table 12.2 Future work (2.40) | §2 row 12: deferred AQ, next data | Kept: five steps, laws [S914, S915], pilot [S904], adoption [S113]; table, legal duties and pilot design moved | Section 12.1; Table A.40, Appendix XV |
| 13 Lead-in (0.30) | §2 row 13 | Kept (rule for AI use) | Section 13 |
| 13.1 with Table 13.1 AI Decision Log (3.37) | §2 row 13 evidence; brief 6.1, 7 (appendix allowed) | Moved; each milestone's use, verification and decision kept in sentences | Section 13.1; Table A.41, Appendix XVI |
| 13.2 Reflection (1.47) | §2 row 13: reasoning vs evidence | Kept in summary with UNESCO [S909]; full reflection moved | Section 13.2; Appendix XVI |
| 14 Conclusion (2.00) | §2 row 14: no new conclusion | Rewritten from Sections 2–12; numbers stated twice cut to one statement in 11.2/11.3; [S112] caution kept in Appendix XIV | Section 14 |

## Loss check

`code/t15_loss_check.py` splits every English body file 01-* … 14-* of `a6a8d5a` into sentences and table rows,
normalises markup and cross-references, and lists each unit found nowhere in the current English report (main text and
appendices); log and review: `logs/T15_loss_check.log`.

- Checked 990 sentences, 329 table rows, 47 headings and 63 run-in labels; 137 units unmatched after the restorations.
- Signposting and transitions with no fact (46 sentences, 4 labels, 1 caption fragment): cut.
- Reworded or merged (about 55 sentences and 18 table rows): each fact named in its new place in the log.
- Deliberate duplicates (5 sentences of Section 14): one statement kept in 11.2, 11.3, 12 or Appendix XIV.
- Facts missing and restored (7): the key-variable sources and scales (score 0–100, below 40 a fail; empty
  unregistration day for non-withdrawers; roles of attempts and credits; deprivation and disability never predictors)
  in Appendix V; the reason the evaluation was fixed before code ran (Appendix IX); why the 2014 test can be used only
  once (Appendix X); the search keywords (Appendix IV); "these results support the judgement of the staff … rather than
  replace it" (Appendix I). The restorations are in `RESTORED` in `code/t15_move_to_appendix.py`, so a rerun of the
  move rebuilds them.
- Brief check of the main text found one gap, the keys of the tables in Section 5, filled with one sentence.

## T22 table fit

The English Word post-check failed on three tables (build log: `logs/T22_build_en.log`): the 11-column Traceability
Matrix (main text) broke words in six columns on a portrait page, and the landscape appendix tables AQ Revision Log and
Final answers wrapped cells to 22–32 lines (limit 20); the pessimistic main text stood at 26.0 pages (budget 25). The
layout settings (`part_breaks = false`, `landscape_appendices = true`) stay unchanged.

| Decision | Brief anchor | Result |
| :---- | :---- | :---- |
| Table 11.1 split into Table 11.1 "(goal to data)" and Table 11.2 "(method to decision)", both led by AQ-ID; cells unchanged, one row per AQ | brief 3 columns, one row per final AQ | Fits portrait; full cells stay in Table A.27 |
| Table 11.2 Final answers renumbered Table 11.3 | brief 5 | Reference in Section 11.5 updated |
| Table A.5 AQ Revision Log split into A.5 "(questions and findings)" and A.6 "(actions and effects on method)"; full Milestone 1 wording kept | brief 3.1 columns | Max cell within 20 lines |
| Old Table A.37 Final answers split into A.38 "(evidence and method)" and A.39 "(findings and implications)" | brief 5 columns | Max cell within 20 lines |
| Appendix tables renumbered: old A.6–A.36 → A.7–A.37, old A.37 → A.38 + A.39, old A.38–A.41 → A.40–A.43, in every section (`Table A.n` was the only reference form) | – | 43 appendix tables, consecutive |
| 8.1 paragraph "Rationale in brief" moved out; Section 8.1 points to the Rationale column of Table 8.1 and to Appendix VIII | brief §2 row 8 (rationale): kept by the table's Rationale column; content stated twice | Every fact already in Appendix VIII ("AQ1: grouped rates" … "AQ4: proposed ranking"), so not appended again |
| 11.2 sentence on withdrawal vs fail by module and rates by disability and deprivation band → pointer to Appendix XII | supporting detail | Facts already in Appendix XII, "Differences by module, start month and run" |
| 11.3 sentence on the missed-task sign in 15 groups → pointer to Appendix XIII | supporting detail | Facts already in Appendix XIII, "Groups of students and the 2014 replication" |
| Figures 11.1 and 11.2 placed at the end of Sections 11.2 and 11.3 (introducing sentence moved with them), so the text fills the page instead of an empty gap | layout only | Pessimistic gaps 2.6 → 1.8 pages |
| 13.1 per-milestone sentences for Milestones 1–4 → appended verbatim to Appendix XVI as "Milestones 1 to 4 in brief"; Section 13.1 keeps a summary sentence and the Milestone 5 counts | brief §2 row 13: AI Decision Log evidence in Table A.43 | Facts kept |

Gates after the changes: `report.py build milestone-5 --lang en` PASS; `report.py postcheck milestone-5 --lang en` PASS
(0 errors, 59 tables); `page_budget.py … --budget 25`: 25.0 pages pessimistic (last page 86% full), 18.1 optimistic;
`make precheck TASK=milestone-5`: all English steps PASS, citation order unchanged (no renumbering of references).
