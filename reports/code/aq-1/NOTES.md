# AQ1 – working notes

## Brief

- **Question (Level 1, Table 2.1).** What share of enrolments end in pass, fail or withdrawal, by module, run, start month and year, and in which week do non-completers first miss an assessed task?
- **Level and task.** Descriptive; aggregation. No model.
- **Reader and decision.** Programme leaders: D2 (where advisors' time goes) and D3 (whether to extend after the pilot).
- **Population.** Enrolments still registered at day 14 (28,061 of 32,593). Unit: enrolment; task for the first miss.
- **Primary approach.** Grouped rates with Wilson 95% intervals; differences between years with Newcombe 95% intervals. **Baselines:** pooled rate; all enrolments as a second denominator; KPI population without the flagged enrolments.
- **Success criterion (Table 4.1).** Both aggregation paths agree to the enrolment; every rate carries its denominator and interval; no rate compared across runs without its interval. **Result: met.**
- **Status of the run.** Rerun of 12 November 2026, made after the first run of 11 November (commit `11f4aca`) and the Milestone 5 report had been read. The 2014 rates were known when the year comparison was designed.

## Lifecycle record (data-analyst skill, stages 1–10)

| Stage | Record |
| :---- | :---- |
| 1 Business understanding | Brief above; decision D2 and D3; KPI = completion on the day-14 population |
| 2 Analytic approach | Descriptive: grouped rates; comparison = module, start month, year, denominator; baseline = pooled rate. Alternative that could fool the reader: a different mix of runs between years (CCC only in 2014), tested with like-for-like sets of runs and a weighted difference |
| 3 Data requirements | Outcome per enrolment, registration and unregistration day, task due days and submissions: all available; answerable |
| 4 Data collection | `enrolment.parquet`, `assessment_due.parquet` of OULAD-N04-prepared-1.0 (hash-checked); raw `studentInfo.csv`, `studentRegistration.csv` for the second path |
| 5 Data understanding | 138 enrolments flagged for a missing withdrawal or registration day; 6 runs with no task due by day 27; CCC has no 2013 run |
| 6 Data preparation | None beyond selecting columns; counts reconcile with Level 1 (C1) |
| 7 Modeling | Rates, differences, cumulative first-miss curves; three figures |
| 8 Evaluation | Checks C1–C7 below; year comparison recomputed from the raw tables and by a second implementation of the interval |
| 9 Deployment | `README.md` (finding-led report); tables written from the result tables by `../common/fill_report_tables.py` |
| 10 Feedback | Received: the owner's comparison with the Milestone 5 report (finding 2: the year comparison was too weak). Acted on in this rerun. Outcome review of the pilot KPI: pending |

## Decisions taken while working

| Decision | Reason |
| :---- | :---- |
| 2013 runs read first, 2014 runs after the AQ3 freeze of the rerun | The order Level 1 fixes; in this rerun it documents order, not blindness |
| Second path built from `studentInfo.csv` and `studentRegistration.csv` in `datasets/oulad/` | Independent of the Milestone 3 preparation code |
| First missed week recomputed from `assessment_due.parquet` | Checks the stored `first_missed_week` instead of trusting it |
| "Flagged" = registration day missing or Withdrawn without a withdrawal day | Reproduces the 138 enrolments named in the Level 1 card |
| Year compared by the 2014 − 2013 difference with a Newcombe interval, on both denominators, for all runs, the six shared modules and the nine shared module × start-month pairs (`../PROTOCOL.md` P18) | Overlap of two pooled intervals is not a test of their difference; the pooled 2014 rate includes CCC; the answer depends on the denominator. Decided after the 2014 rates were known |
| Weighted difference over the nine pairs added | Rules out the mix of runs as the source of the difference |
| Week-4 share also given over the 16 runs with a task due by day 27 | A student with nothing due has an undefined missed-task status, not "nothing missed" (skill playbook, opportunity-based denominators) |

## What the rerun changed against the first run, and what it found

| Item | First run (commit `11f4aca`) | Rerun |
| :---- | :---- | :---- |
| Every rate of the first run (pooled, year, start month, module, run, outcome shares, denominators, first missed task) | – | Same values; `../logs/compare_first_run.md` lists each table |
| Year comparison | "The intervals of 2013 and 2014 overlap, so the two years do not differ" | Six shared modules, registered at day 14: −3.5 points (−4.8 to −2.3). Six shared modules, all enrolments: −0.2 points (−1.4 to +0.9). The Milestone 5 report gives the same −3.5 (−4.8 to −2.3) |
| Share not registered at day 14 | Not computed | 10.7% in 2013, 16.2% in 2014 |
| Week-4 share of non-completers with a missed task | 16.8% over all runs, with the runs that have no task due inside the denominator | 16.8% over all runs and 19.7% over the 16 runs with a task due |
| Figure titles | Typed by hand | Built from the result tables |

## Methods checklist

- [x] Extraction of analysis tables from the prepared dataset, hash-checked – `extracted-datasets/aq1_*.csv` (`logs/01_extract_all.md`)
- [x] Rates by pooled, year, start month, year × start month, module and run, with Wilson intervals – `results/rates_all.csv`
- [x] Module × start month – `results/rates_module_by_start_month_all.csv`
- [x] Year comparison: 2014 − 2013 with Newcombe intervals, two denominators, overall, shared modules, shared pairs, per module, per start month, per pair; weighted difference over the pairs – `results/year_comparison_all.csv`
- [x] Share not registered at day 14 by year – `results/not_registered_d14_by_year_all.csv`
- [x] Three denominators per run and pooled – `results/denominators_by_run_all.csv`, `denominators_pooled_all.csv`
- [x] Outcome shares (Distinction, Pass, Fail, Withdrawn) – `results/outcome_shares_all.csv`
- [x] Week of the first missed task by outcome, cumulative by week, by module – `results/first_missed_task_by_outcome_all.csv`, `first_missed_task_cumulative_all.csv`, `first_missed_task_by_module_all.csv`
- [x] Week-4 share over all runs and over runs with a task due, by year, with the year difference – `results/first_missed_by_week4_all.csv`, `first_missed_by_week4_year_difference_all.csv`
- [x] Task calendar and runs with no task due by day 27 – `results/task_calendar_by_run_all.csv`
- [x] Rates by gender, disability, deprivation band, age band (description) – `results/rates_by_audit_group_all.csv`
- [x] Evaluation checks C1–C7 – `results/checks_all.csv`, `results/checks_2013.csv`
- [x] Figures, titles built from the result tables – `figures/fig-aq1-1-non-completion-by-run.png`, `fig-aq1-2-first-missed-task.png`, `fig-aq1-3-year-difference.png`
- [ ] Rates adjusted for module mix when comparing student groups (not asked by the Level 1 card; description only)
- [ ] Year comparison adjusted for student background (the data cannot tell earlier leaving from better completion; see open issues)

## Check ledger

| Check | Condition evaluated | Result | Evidence |
| :---- | :---- | :---- | :---- |
| C1 | 32,593 enrolments and 28,061 in the KPI population | PASS | `logs/03_checks_all.md` |
| C2 | Per-run counts and events from the prepared view equal those from the raw tables | PASS, 22 of 22 runs | `results/check_two_paths_all.csv` |
| C3 | Stored first missed week equals the recomputed value | PASS, 32,593 of 32,593 | `logs/03_checks_all.md` |
| C4 | Run counts sum to the pooled count; the four outcome counts sum to n in every run | PASS | `logs/03_checks_all.md` |
| C5 | Every rate has a denominator and an interval that contains it | PASS, 38 rates | `logs/03_checks_all.md` |
| C6 | Counts behind the year comparison, recomputed from the raw tables by a second code path (plain loops, no shared function), equal the result table: 3 scopes × 2 denominators × 2 years | PASS, 12 of 12 count pairs | `logs/03_checks_all.md` |
| C7 | Every Newcombe interval of the year comparison equals the statsmodels implementation | PASS, 48 intervals, largest difference 5e-07 (6-decimal storage) | `logs/03_checks_all.md` |
| Input | SHA-256 of `enrolment.parquet` and `assessment_due.parquet` equal the Milestone 3 manifest | PASS | `logs/01_extract_all.md` |
| Unit tests | Year comparison on a synthetic table with a module that runs in one year only; weighted difference in a case where the mix differs | PASS, 21 of 21 | `../logs/tests_aq2_model.md` |
| Reproduction | The 24 result tables that exist in both runs with the same structure are byte-identical to the first run | PASS, 24 of 24; `checks_all.csv` gained C6 and C7; 6 tables are new | `../logs/compare_first_run.md` |
| Milestone 5 | Year difference, six shared modules, day-14 population | −3.5 (−4.8 to −2.3) in both analyses | `reports/milestone-5/report/11-02-aq1-findings.md` |

7 of 7 checks pass (`results/checks_all.csv`); the 2013 scope passes C1–C5 (`results/checks_2013.csv`). No step failed in the final pass.

## Open issues

- **Why the 2014 day-14 rate is lower.** More students left before day 14 in 2014. Whether these are students who would have failed or withdrawn later anyway cannot be told from OULAD; the registration and unregistration days of the two years could be compared in a later step.
- The KPI of the pilot (completion rate, target 75%) has an OULAD analogue of 54.7% completion (100% − 45.3%); the 70% baseline of the SMART Goal is the university's assumption and is not tested here.
- Whether the February gap reflects the students who start in February or the calendar cannot be told from these data.
