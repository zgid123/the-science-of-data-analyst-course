# Process log – everything done to produce this folder, in order

Session of 11 November 2026 (UTC). Written by the AI coding assistant that did the work (Claude, through Claude Code,
using the repository's `data-analyst` skill). Times are UTC and come from `experiment-log.md`, which
`common/run_step.py` appends automatically; each step's full console output is in the step log it links to. This file
adds what the automatic log cannot show: what was read, what was decided and why, and what went wrong.

## 1. Request

Do the Level 2 requirement (Prototype Experiment) of `milestones/04/milestone-4.md` with the `data-analyst` skill;
write the result to `reports/code`; group everything in folders `aq-<number>`; put data extracted from the dataset in
a subfolder `extracted-datasets`; keep a folder `logs` that records everything done; write process and results in
Markdown; go deep, because the work is for a real submission.

## 2. What was read before any code was written

| Read | Purpose | Contains 2014 outcomes? |
| :---- | :---- | :---- |
| `milestones/04/milestone-4.md` (section 10: the eight prototype steps; section 11: AI policy) | The requirement | No |
| `.agents/skills/data-analyst/SKILL.md`, `playbooks/early-warning.md`, `references/example-report.md`, `scripts/stats_helpers.py`, `scripts/chart_style.py` | Method, report voice, helpers | No |
| `AGENTS.md` (repository) | Working rules: scripts for every number, logs with UTC time, command and exit status, methods checklists | No |
| `reports/milestone-4/report/*.md`: 01-01, 01-02, 02-01, 03-01 to 03-04, 04-01 to 04-04, 07-00, 10-02, 10-03, 10-04 | The frozen Level 1 design: questions, baselines, candidates, evaluation cards, protocol, success criteria | No (Level 1 states no model result) |
| `reports/milestone-4/PROGRESS.md`, `research/design/decisions.md` (grep) | Design facts and decisions of Level 1 | No (outcome counts from 2013 only) |
| `reports/milestone-4/package/README.md` | Found while locating inputs: the specification of the team's earlier prototype (planned layout, no result) | No |
| `reports/milestone-3/package/data/metadata/`: `version_manifest.json`, `predictor_sets.json`, `split_spec.md`, `feature_spec.md`, `data_dictionary.md`, `change_log.md` | The prepared dataset OULAD-N04-prepared-1.0 | No |

Directory listings showed that an earlier prototype run exists (`reports/milestone-4/package/results/`,
`reports/milestone-5/`). Its result files were **not opened** until step 9 below (protocol P20).

One ad-hoc look at the data preceded the protocol: a throwaway query on `features_d27.parquet` printed the row counts
per run, the null counts, the frequency of each rule sign per module **in the 2013 rows**, the 2013 non-completion
rate (44.4%, already in Level 1) and summary statistics of seven predictors in 2013. It printed no 2014 outcome. Its
useful facts (sign frequencies per module) are reproduced by `aq-2/code/01_extract.py`.

## 3. Decisions on layout

- One folder per analytical question, `aq-1` to `aq-4`, each with `code/`, `extracted-datasets/`, `results/`,
  `figures/`, `logs/`, a finding-led report `README.md` and working notes `NOTES.md` (the skill's single notes file:
  brief, decisions, methods checklist, check ledger, open issues).
- `common/` holds the code shared by all four questions (data loading with hash check, the test-outcome guard, list
  metrics, bootstrap, the step runner, unit tests). It sits outside the `aq-*` folders because duplicating it four
  times would let the copies drift apart.
- `logs/` at the top holds the logs that span questions: this file, the automatic experiment log, the AI decision log,
  the unit-test log and the determinism hashes.
- Logs are Markdown: `common/run_step.py` wraps every step and writes its start and end time, command, git commit, exit
  status and console output to `<aq>/logs/<step>.md`; scripts print their tables as Markdown.
- Reports are in English, the language of the Level 1 report sources (`report/*.md`); the Vietnamese twin is a
  separate step of the team's build flow.

## 4. Protocol before results (22:55–22:58)

`PROTOCOL.md` was written before the first step ran. It fixes 20 implementation choices (P01–P20) that Level 1 leaves
open: penalty type and grid, tuning criterion, tree grid, preprocessing, tie-breaking, the completed choice rule,
what is frozen, bootstrap sizes, the Holm procedure, slice definitions, the binary definitions of the five AQ2 signs,
the AQ2 model, the AQ1 second path, and the rule that the earlier run stays unread until the end.

## 5. Stage A – 2013 runs only (22:58–23:06)

| Time | Step | Outcome |
| :---- | :---- | :---- |
| 22:58:39 | `aq-1` extract, analyse, checks (scope 2013) | 13,529 enrolments, 12,076 in the KPI population; both aggregation paths agree in 9 of 9 runs. **Check C4 failed** on its first run (see section 10) and passed after the fix at 22:58:51 |
| 23:00:23 | `aq-2` extract and associations (scope 2013) | 11,811 enrolments, 5,245 non-completers; five signs, all "consistent association" |
| 23:01:56 | `aq-3` `01_extract` | Hashes equal the manifest; counts equal Level 1 Table A.6; the list-length rule reproduces `capacity_by_run.parquet` in 22 runs; test rows extracted **without outcome columns** |
| 23:02:27 | `aq-3` `02_dev_folds` (187 s) | 90 fits (5 configurations × 2 cut-offs × 9 folds), nested tuning; development ceiling 2,976 = Level 1 |
| 23:06:10 | `aq-3` `03_choose` | No challenger reaches +0.03 and 7 of 9 folds (gains −0.001 to −0.002); **M1 chosen** |

## 6. Stage B – second freeze and single test (23:06–23:20)

| Time | Step | Outcome |
| :---- | :---- | :---- |
| 23:06:14 | `aq-3` `04_freeze` (723 s) | 12 models tuned on all 9 runs, refitted, saved with SHA-256; M1 has 23 parameters; **frozen at 23:18:16** (`aq-3/results/freeze.json`) |
| 23:18:44 | `common/tests/test_lib.py` | 17 of 17 code-path tests pass (labelled synthetic inputs) |
| 23:18:58 | `aq-3` `05_test` | Model files unchanged; blind test tables scored and saved; **first 2014 outcome read at 23:19:02**; gate S1: 0.7257 against 0.7044, +0.0212 (0.0065 to 0.0364), p = 0.0032, 11 / 0 / 2 → **met** |
| 23:19:41 | `aq-3` `06_secondary` | S2 reported; S3: calibration-in-the-large +0.124, slope 0.873 → bounds met; 5 of 13 runs outside ±0.2 |
| 23:19:46 | `aq-3` `07_error_analysis` | Errors by run and slice, overlap 77.2%, stability. One display bug found and fixed, rerun at 23:21:48 (section 10) |
| 23:19:53 | `aq-3` `08_sensitivity` | 13 variants; gain 0.014 to 0.035; unpaired runs and CCC alone have intervals including 0 |

## 7. AQ4, then the 2014 parts of AQ2 and AQ1 (23:21–23:25)

| Time | Step | Outcome |
| :---- | :---- | :---- |
| 23:21:51 | `aq-4` `01_lists`, `02_evaluate` | 3,955 list places with reasons; recall 41.5% against 25.1% random and 40.3% rule; tiers 81.0% and 59.9% |
| 23:22:46 | `aq-4` `03_fairness` (51 s) | FR1: 0 of 3 confirmatory groups flagged; age 55 or over not cleared |
| 23:23:49 | `aq-2` extract and associations (scope 2014), `03_replication` | All five verdicts replicate; 26 of 26 sign × module estimates keep their direction |
| 23:23:56 | `aq-1` extract, analyse, checks (scope all) | 32,593 / 28,061 / 138 reproduced; paths agree in 22 of 22 runs; 5 of 5 checks pass |

## 8. Verification (23:24–23:40)

| Time | Step | Outcome |
| :---- | :---- | :---- |
| 23:24:42 | `aq-3` `09_verify` | First run: V1 failed on a tolerance (section 10). Second run 23:25:14: V1–V7 and V1b pass |
| 23:28:04 | `aq-3` `02_dev_folds_rerun` (231 s) | Full rerun of the development folds; the 5 output files are byte-identical to the first run (`determinism_before.sha256` = `determinism_after.sha256`). Logged under a new step name so that the pre-freeze log `02_dev_folds.md` keeps its original time |

## 9. Cross-check with the team's earlier run (23:25:44)

Only now were `reports/milestone-4/package/results/s1_gate.csv`, `s1_per_run.csv`, `calibration.csv`, `freeze.csv`,
`fairness.csv`, `aq2_replication.csv` and the tuning comment in `src/common.py` opened. Result: the rule list is
identical in 13 of 13 runs; the model lists differ by one non-completer in total (2,870 here, 2,871 there); both runs
meet S1; they disagree on S3 (slope 0.873 here, 1.311 there), because the earlier run tuned the penalty on recall at
capacity (C = 0.001) and this one on log loss (C = 10). The disagreement is reported in the AQ3 report, Sections 4
and 6, not resolved in favour of either run.

## 10. Things that went wrong, and what was done

| What | Cause | Fix | Effect on results |
| :---- | :---- | :---- | :---- |
| AQ1 check C4 failed (22:58:41) | The check summed shares that the CSV stores with 6 decimals and compared the sum with 1 at a tolerance of 1e-9 | The check now compares exact counts (the four outcome counts sum to n in every run) | None: a checking-code error |
| `logs/logs/tests_lib.md` | The runner was called with `logs` as the folder name, so it wrote one level too deep | File moved to `logs/tests_lib.md`; the link in the experiment log corrected | None |
| `errors_by_run.csv` showed 4,294,967,292 for a difference of −4 | Unsigned integer subtraction in polars | Counts cast to signed integers; step rerun at 23:21:48 | None on any other number; the two GGG rows now read −4 and −2 |
| Verification V1 failed (23:24:42) | Tolerance 1e-9 against scores stored with 6 decimals (largest difference 5e-07) | Tolerance set to 1e-6 and check V1b added: lists from unrounded scores hold the same 2,870 non-completers | None; the rounding of stored scores moves no list |
| A shell loop for the figure steps passed two words as one argument | zsh does not split unquoted variables | The four mis-named folders it created (`aq-1 04_figures`, …) were deleted and their four rows removed from the experiment log; the steps were rerun | None. This is the only place where rows were removed from the automatic log |
| Figure scripts failed once (23:26:59, exit 1) | `chart_style` imported before the skill folder was on the path | Import moved after the shared import; rerun at 23:27:09 | None |
| A figure title said "one in five" for 16.8% | Wording written before reading the 22-run number | Title changed to "one in six"; figure rerun at 23:28:00 | None |
| AQ3 report draft said "121–129 students per fold" | Misreading of Level 1 Table A.5; the fold log shows 0 to 55 enrolments per fold, 121 students in all | Sentence corrected before delivery | None |
| A module × start-month number was first obtained by a one-off query | – | Moved into `aq-1/code/02_analyse.py`; `02_analyse_all` and `03_checks_all` rerun; report cites `results/rates_module_by_start_month_all.csv` | None |

| The final report check (`common/check_reports.py`) failed on its first run | It found one interval bound quoted as +0.007 where the table holds +0.006 (sensitivity row "without students seen in 2013"), and two sensitivity rows missing from the AQ3 report table; its other failures were its own (plain file names in tables, minus-sign typography, half-up rounding of 26.25%) | Bound corrected, the two rows added, checker repaired; rerun: 304 file references resolve, 0 quoted-number mismatches (`check_reports.md`) | One digit in one sensitivity row of the AQ3 report |

## 11. What was not done

- No commit was made; `reports/code/` is untracked. The extracted datasets (about 42 MB of CSV) are re-created by the
  extraction scripts, so by the repository's "Keep, commit, submit" rule they can stay local with a `.gitignore` line,
  while code, results, logs and reports are small text files to commit.
- No Vietnamese twin, no Word build, no change to the Level 1 report or to `reports/milestone-4/package/`.
- No survival model, no recalibration, no per-tutor-group lists (see the unchecked items in each `NOTES.md`).
- Nothing in `reports/milestone-3/package/` or `datasets/oulad/` was modified; verification V7 confirms the hashes
  after all runs.
