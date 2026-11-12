# Process log – everything done to produce this folder, in order

Session of 12 November 2026 (UTC): the rerun. Written by the AI coding assistant that did the work (Claude, through Claude Code, using the repository's `data-analyst` skill). Times are UTC and come from `experiment-log.md`, which `common/run_step.py` appends automatically; each step's full console output is in the step log it links to. This file adds what the automatic log cannot show: what was read, what was decided and why, and what went wrong.

## 1. Request, and what this run is

The original request (11 November 2026): do the Level 2 requirement (Prototype Experiment) of `milestones/04/milestone-4.md` with the `data-analyst` skill; write the result to `reports/code`; group everything in folders `aq-<number>`; put data extracted from the dataset in a subfolder `extracted-datasets`; keep a folder `logs` that records everything done; write process and results in Markdown; go deep, because the work is for a real submission.

The request of this session: redo that work end to end as a rerun. The owner had compared the first run's AQ1 and AQ2 with the Milestone 5 report of a team member and found five problems (section 4). The owner did not want single files patched: every result table, log, figure, report and note was to be regenerated in one run and agree with the others. The owner set three constraints: change no AQ3 or AQ4 design choice; say plainly that this is a rerun made after the 2014 outcomes and the team member's results were seen; write only inside `reports/code`, commit nothing.

**History of the first run, kept here because its own files were replaced.** The first run is git commit `11f4aca`. It wrote `PROTOCOL.md` (P01–P20) before its first result, ran its steps from 2026-11-11T22:58:39Z, froze its models at 2026-11-11T23:18:16Z and read the 2014 outcomes for the first time at 2026-11-11T23:19:02Z. Its S1 result was 0.7257 against 0.7044, difference +0.0212 (0.0065 to 0.0364), sign-flip p = 0.0032, 11 runs won and 2 lost. Its process log, experiment log and test-access record can be read with `git show 11f4aca:reports/code/logs/process-log.md` (and the same for `logs/experiment-log.md` and `aq-3/logs/test-access.md`).

## 2. What was read before any code was changed

| Read | Purpose | Contains 2014 outcomes? |
| :---- | :---- | :---- |
| `AGENTS.md` (repository) | Working rules: scripts for every number, logs with UTC time, command and exit status, methods checklists, writing conventions | No |
| `reports/code/README.md`, `PROTOCOL.md`, `logs/process-log.md`, `logs/experiment-log.md`, `logs/ai-decision-log.md`, `logs/check_reports.md`, `logs/tests_lib.md` of the first run | What the first run did and claimed | **Yes** (S1, S3, fairness, AQ1 and AQ2 results of 2014) |
| All code of the first run: `common/` and `aq-1/code` to `aq-4/code` | Review before reuse | No |
| `aq-1/README.md`, `aq-1/NOTES.md`, `aq-2/README.md`, `aq-2/NOTES.md`, `aq-3/README.md`, `aq-3/NOTES.md`, `aq-4/README.md`, `aq-4/NOTES.md` and the AQ2 result tables of the first run | The reports to be replaced, and the numbers under question | **Yes** |
| `reports/milestone-5/report/11-02-aq1-findings.md`, `11-03-aq2-findings.md`, `16-12-aq1-results.md`, `16-13-aq2-results.md`; `reports/milestone-5/code/aq2_sensitivity_continuous.py` | The team member's results and method that the owner compared with | **Yes** |
| `.agents/skills/data-analyst/SKILL.md`, `workflows/analytics-lifecycle.md`, `playbooks/early-warning.md`, `references/example-report.md`, `references/statistics-and-inference.md`, `scripts/stats_helpers.py`, `scripts/chart_style.py` | Method, report voice, helpers; the references the routing table names for the stages in play | No |
| `reports/milestone-4/report/04-01-evaluation-cards.md`, `03-02-descriptive-diagnostic.md` | The Level 1 wording of the AQ1 and AQ2 cards and of the AQ2 criterion | No |

So this rerun started with every 2014 result of the first run and of the Milestone 5 report known. Nothing in it is blind.

## 3. Ad hoc looks at the data before the protocol was revised

Two throwaway queries were run before `PROTOCOL.md` was revised. Neither read an outcome column.

- On `features_d27.parquet`: per run, the number of enrolments and the number carrying each sign and each sensitivity variant. It showed 0 enrolments with a late TMA in both CCC runs.
- On `assessment_due.parquet`: per run, the task types due by day 27. It showed that both CCC runs have only a CMA due by day 27 (day 18), and DDD-2013B a CMA and a TMA. This is the reason protocol P16 now defines the late-TMA sign by the calendar.

Both facts are reproduced by `aq-2/code/01_extract.py` in `aq-2/results/sign_calendar_2013.csv` and `sign_calendar_2014.csv`.

## 4. Decisions taken before running

`PROTOCOL.md` was revised before any script of the rerun produced a number. Rows P01–P15 and P19 are the first run's text, unchanged. The changes:

| Finding of the owner | Decision | Protocol row |
| :---- | :---- | :---- |
| 1. The 2014 late-TMA average counted CCC's 3,521 rows as differences of 0 | Late TMA defined in runs with a TMA due by day 27; every risk difference averaged over the rows with an estimated slope only, with n printed beside it in the main, module, sensitivity and subgroup tables; the script stops if a row outside the support enters an average | P16, P17 |
| 2. Year comparison from overlapping intervals | 2014 − 2013 difference with a Newcombe interval on both denominators; all runs, six shared modules, nine shared module × start-month pairs, per module, per start month; weighted difference over the pairs; share not registered at day 14; recomputed from the raw tables | P18 |
| 3. Residual check too coarse | Residuals by five activity levels and by tenths of predicted risk; one sensitivity run with log(1 + clicks on days 0–27), labelled post hoc | P21, P22 |
| 4. Late TMA in AAA-2014J counted as "same direction" | Direction count reported both ways; module estimates whose interval includes 0 named | P17 |
| 5. Low-activity definition | Half the run median stays primary; the run median is a sensitivity row; the reports say that Milestone 5 uses the median | P16 |
| Status of the run | P20 replaced (the earlier runs have been read); P23 added (rerun rules, first-run freeze kept as history) | P20, P23 |

Two further decisions of method, taken at the same time and not asked for: replication is judged by the change between years with its interval, not by overlapping intervals (P17); and the week-4 share of non-completers with a missed task is also given over the runs that have a task due (P18), because the same error of denominator as finding 1 was present there in a milder form.

## 5. Code reused and code changed

| Code | Status |
| :---- | :---- |
| `aq-3/code/` (12 scripts), `aq-4/code/` (5 scripts) | Reviewed and reused unchanged, except wording: `04_freeze.py` now writes into `freeze.json` and its log that the freeze reproduces the first run's and that the outcomes were known; the docstring of `10_crosscheck_earlier_run.py` no longer says the earlier run was unread. `git diff 11f4aca -- aq-3/code aq-4/code` shows these two files only |
| `common/lib.py` | Loader, guard, list metrics, bootstrap unchanged. Added: constants for the first run's commit and times; the header of the test-access record now says what the record does and does not show; `mh_risk_difference`, `binned_residuals` |
| `common/run_step.py`, `common/tests/test_lib.py`, `aq-1/code/01_extract.py` | Reused unchanged |
| `aq-2/code/aq2_model.py` | Rewritten: calendar-based definition of each sign, support of a sign, averages over the support with n, verdict under both readings, optional continuous adjustment |
| `aq-2/code/01_extract.py`, `02_associations.py`, `03_replication.py`, `04_figures.py` | Changed: task calendar, five activity levels, new residual tables, sensitivity with n and verdict, change between years, figures with titles built from the tables, a third figure |
| `aq-1/code/aq1_common.py`, `02_analyse.py`, `03_checks.py`, `04_figures.py` | Changed: year comparison, share not registered at day 14, week-4 share by population and year, checks C6 and C7, a third figure, titles built from the tables |
| `common/tests/test_aq2_model.py` | New: 21 tests on synthetic inputs, the first group being the test that would have caught finding 1 (a sign absent from one module) |
| `common/compare_first_run.py`, `common/hash_outputs.py` | New: comparison of every result table with commit `11f4aca`; determinism hashes inside the pipeline |
| `common/report_tables.py`, `common/fill_report_tables.py`, `common/check_reports.py` | New and rewritten: every report table is built from the result tables and written into the report by script; the report check compares table rows, quoted numbers, the times of this run and file references, and searches for sentences of the first run that are no longer true |
| `run_all.sh` | Two unit-test steps, the comparison and determinism steps and the three report steps added |

## 6. Execution: a development pass and two passes of the pipeline

| Time (UTC) | What | Outcome |
| :---- | :---- | :---- |
| 15:23:45 to 15:33 | **Development pass, not through the runner.** The changed AQ1 and AQ2 scripts were run directly against the 2013 and 2014 data, with the first run's `freeze.json` still in place so that the guard let them read 2014 rows, and their console output was kept in the session scratchpad. This is where the new numbers were first seen: late TMA +22.5 (n = 9,064); year difference −3.5; low activity failing under the continuous adjustment | Two code errors found and fixed: the synthetic test table had constant covariates (singular matrix), and a legend covered a point in the new AQ2 figure |
| 15:33:44 | **Clean slate.** Deleted inside `reports/code`: every `results/`, `extracted-datasets/`, `figures/` and step-log folder of the four questions (the model files, the first run's `aq-3/results/freeze.json` and `aq-3/logs/test-access.md` among them, with the owner's approval), the top-level logs, and every `README.md` and `NOTES.md`. Left: code, `PROTOCOL.md`, `requirements.txt`, `run_all.sh` | 37 files left, all code or protocol |
| 15:33 to 15:46:21 | **First pass of `REPORT_CHECK=0 bash run_all.sh`.** 26 steps ran with exit status 0 (tests, stage A, freeze at 2026-11-12T15:44:36Z, test, AQ4, AQ2 2014, AQ1 all, verification, cross-check). Step 27, `compare_first_run`, ended with **exit status 1** and the runner stopped | The comparison found every AQ3 and AQ4 number equal to the first run and all 12 model files byte-identical, but it counted one text value as different: the detail of verification check V6, which quotes the freeze time and the number of test accesses. The rule of the comparison was wrong, not a result. Fixed: timestamps and the access count are masked in text columns before comparing |
| during the first pass | `aq-2/code/03_replication.py` was edited before the pipeline reached it, to add `late_tma_average_check.csv` | The step that ran in the first pass was the edited one; the second pass ran it again from the start |
| 15:46 to 15:48 | The first pass's `experiment-log.md`, `compare_first_run.md`, `freeze.json` and `test-access.md` were copied to `logs/attempt-1/` as a record. `run_all.sh` gained the three report steps | – |
| 15:48:06 | **Clean slate again.** Every output of the first pass deleted, its freeze file and test-access record included. The owner's approval covered removing the first run's freeze for the rerun; removing the first pass's freeze belongs to the same rerun and is stated here so that nobody counts it as a further test | Left: code, protocol, the drafted reports and notes, `logs/attempt-1/` |
| 15:48:06 to 16:09:01 | **Second pass of `REPORT_CHECK=0 bash run_all.sh`: 34 steps, all with exit status 0; the script ended with exit status 0.** Everything in the folder comes from this pass | Sections 7 and 8 |
| after 16:09 | Prose of the reports and notes completed from the result tables; `report_tables`, `fill_report_tables` and `check_reports` run through the runner | Section 9 |

The second pass's experiment log holds 0 steps with a non-zero exit status at the end of the pipeline; the one failed step of this session is in `logs/attempt-1/experiment-log.md`.

## 7. The second pass, step by step

| Time (UTC) | Step | Outcome |
| :---- | :---- | :---- |
| 15:48:06 | `tests_lib`, `tests_aq2_model` | 17 of 17 and 21 of 21 code-path tests pass (labelled synthetic inputs) |
| 15:48:10 | `aq-1` extract, analyse, checks (scope 2013) | 13,529 enrolments, 12,076 in the KPI population; both aggregation paths agree in 9 of 9 runs; C1–C5 pass |
| 15:48:11 | `aq-2` extract and associations (scope 2013) | 11,811 enrolments, 5,245 non-completers; 7 runs with a task due and the same 7 with a TMA due (9,960 enrolments); five signs, all "consistent association"; 3 of 5 activity levels outside the residual band |
| 15:48:16 | `aq-3` `01_extract` | Hashes equal the manifest; counts equal Level 1 Table A.6; list-length rule reproduces `capacity_by_run.parquet` in 22 runs; test rows extracted without outcome columns |
| 15:48:18 | `aq-3` `02_dev_folds` (158 s) | 90 fits; the five output files have the SHA-256 of the first run |
| 15:50:56 | `aq-3` `03_choose` | No challenger reaches +0.03 and 7 of 9 folds; **M1 chosen**, as in the first run |
| 15:50:57 | `aq-3` `04_freeze` (474 s) | 12 models tuned, refitted and saved; **frozen at 2026-11-12T15:58:51Z**; the freeze record says that it reproduces the first run's freeze |
| 15:58:51 | `aq-3` `05_test` | Model files unchanged; **first 2014 outcome read by a script at 2026-11-12T15:58:53Z**; S1: 0.7257 against 0.7044, +0.0212 (0.0065 to 0.0364), p = 0.0032, 11 / 0 / 2 → met |
| 15:59:16 | `aq-3` `06_secondary`, `07_error_analysis`, `08_sensitivity` | S3: calibration-in-the-large +0.124, slope 0.873 → bounds met; 5 of 13 runs outside ±0.2; 13 sensitivity variants |
| 15:59:46 | `aq-4` `01_lists`, `02_evaluate`, `03_fairness` | 3,955 list places; recall 41.5% against 25.1% random; FR1: 0 of 3 groups flagged |
| 16:00:22 | `aq-2` extract and associations (scope 2014), `03_replication` | 9 runs with a task due (12,585), 7 with a TMA due (9,064). Late TMA +22.5 (17.9 to 27.2), n = 9,064. All five verdicts equal to 2013; 5 of 5 changes have an interval including 0; 5 of 30 module estimates include 0 |
| 16:00:29 | `aq-1` extract, analyse, checks (scope all) | 32,593 / 28,061 / 138 reproduced; paths agree in 22 of 22 runs; year comparison; C1–C7 pass |
| 16:00:31 | `aq-3` `09_verify`, `10_crosscheck_earlier_run` | V1–V7 and V1b pass; rule list identical to the earlier team run in 13 of 13 runs, model lists differ by 1 non-completer in total |
| 16:00:34 | `compare_first_run` | PASS (section 8) |
| 16:00:36 | `determinism_before`, `aq-3` `02_dev_folds_rerun` (469 s), `determinism_after` | Development folds run again in full; 5 of 5 output files byte-identical |
| 16:08:33 | Figures of the four questions | 3 + 3 + 5 + 3 figures, PNG and SVG |

## 8. Comparison with the first run

`common/compare_first_run.py` read every result table of commit `11f4aca` with `git show` and compared it with the regenerated table (`compare_first_run.md`, `compare_first_run.csv`, `compare_first_run_headlines.csv`).

- **aq-3: 28 of 30 result tables byte-identical.** The other 2 hold the same values and differ only in a column that records run time: `dev_fold_design.csv` (seconds per fold) and `verification.csv` (the freeze time quoted in the detail of V6). All 12 frozen model files have the same SHA-256 as in the first run. 16 of 16 AQ3 headline numbers (S1, model choice, S3) are equal.
- **aq-4: 13 of 13 result tables byte-identical.** 18 of 18 AQ4 headline numbers (fairness gaps and intervals, flags, recall, lift) are equal.
- **aq-1:** the 24 tables that exist in both runs with the same structure are byte-identical; `checks_all.csv` gained C6 and C7; 6 tables are new (year comparison, share not registered, week-4 shares, one 2013 table).
- **aq-2:** 2 tables byte-identical (`model_coefficients_2013.csv`, `model_coefficients_2014.csv`: the main model's coefficients did not change, only what is averaged); 16 tables have new columns; 12 are new; 3 were renamed away (`binned_residuals_*`, `small_cells_2014`). Of the 40 AQ2 headline numbers compared, 37 are equal and 3 differ, all for the late TMA in 2014: rows averaged over 12,585 → 9,064, adjusted difference +0.1623 → +0.2254, unadjusted difference +0.1436 → +0.1732.

## 9. Reports written, and the last three steps

The prose of the four reports and the root `README.md` was written by hand from the regenerated tables. For AQ3 and AQ4 the prose of the first run was kept where the tables are identical, and every sentence about protocol, blindness and the earlier run was rewritten. Every table of the four reports is written into the report by `common/fill_report_tables.py` from the result tables; no table was typed. Prose numbers that the report check does not cover were compared by hand with the step logs and result tables.

Before the three report steps were run through the runner, the fill and the check were tried directly, outside the runner. The first trial of the check failed on six items: three references to the check's own log, which does not exist until the check ends (the check now leaves its own log out), and three places where a document quoted a sentence of the first run in order to say that it was wrong (`README.md`, `aq-2/NOTES.md`, `PROTOCOL.md`); the quotes were reworded. That is the only edit to `PROTOCOL.md` after the pipeline ran, and it changes no choice.

The check was then tested on deliberately broken reports: a table row carrying the first run's late-TMA value, the first pass's freeze time in the AQ3 report, a sentence of the first run in the AQ1 title, and a wrong interval bound in the AQ1 prose. It caught the first three and ended with exit status 1. It did not catch the wrong bound, because the report states the correct bound in another sentence and the check asks only whether the correct text is present. Table rows are therefore checked for equality, row by row; prose numbers are checked for presence, and the remaining prose numbers were compared with the tables by hand. The reports were restored and the check passed.

The three steps were then run through the runner: `report_tables` (30 tables built), `fill_report_tables` (30 tables written into the four reports) and `check_reports`. Their logs are `report_tables.md`, `fill_report_tables.md` and `check_reports.md` in this folder. `check_reports` was run again after each later edit of a document (a line of the folder layout in `README.md`, and this paragraph), so the last row of `experiment-log.md` is the check of the final state of the folder.

## 10. Things that went wrong, and what was done

| What | Cause | Fix | Effect on results |
| :---- | :---- | :---- | :---- |
| First pass stopped at `compare_first_run` (exit status 1, 15:46:21) | The comparison treated the freeze time quoted in a text column as a changed value | Timestamps and the access count are masked in text columns; the pipeline was run again from the first step | None on any result. It cost a second freeze file, which is why the folder's freeze time is 15:58:51 and not 15:44:36 |
| Synthetic test table gave a singular matrix (development pass) | Previous attempts and credits were constants in the toy data | Random values unrelated to the outcome | None; test code only |
| A legend covered a data point in the new AQ2 residual figure (development pass) | Default legend position | Legend moved | None |
| Draft prose quoted three interval bounds that the tables round differently (−4.7 for −4.6, +1.0 for +0.9, twice) | Rounded by eye from the console output of the development pass | Corrected from the built tables before the report check; the check now compares these sentences with the tables | None |
| `03_replication.py` edited while the first pass was running | A number quoted in the AQ2 report (+16.2, the diluted average) had no script behind it | The script now computes it; the second pass ran the final version of every script | None |
| The first run's error of method (finding 1) | A row without a slope has a risk difference of exactly 0, and the average ran over all rows of the runs where the sign was "defined" | Sections 4 and 5; a unit test now covers it | The 2014 late-TMA estimate and the text built on it |

## 11. What was not done

- No commit was made, and `git stash` was not touched. `git status` shows the rerun as uncommitted changes on top of `11f4aca`.
- Nothing outside `reports/code` was written: `reports/milestone-3`, `reports/milestone-4`, `reports/milestone-5`, `datasets/` and the skills are unchanged; verification V7 confirms the hashes of the prepared files after all runs.
- No Vietnamese twin, no Word build, no change to the Level 1 report.
- No HTML report from the skill's template: the request asks for Markdown, and the repository's reports are Markdown sections.
- The companion skills that the lifecycle names for mechanics (`statsmodels`, `scikit-learn`, `validate-data`, `scientific-visualization`) were not called as separate skills; the code of the first run already used those libraries, and the figures were inspected by eye.
- No survival model, no recalibration, no per-tutor-group lists, no dose-response curve of activity (see the unchecked items in each `NOTES.md`).
- The Milestone 5 analysis was not rerun or changed; its numbers are quoted from its report.
