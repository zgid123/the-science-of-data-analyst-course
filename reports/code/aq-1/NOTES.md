# AQ1 – working notes

## Brief

- **Question (Level 1, Table 2.1).** What share of enrolments end in pass, fail or withdrawal, by module, run, start
  month and year, and in which week do non-completers first miss an assessed task?
- **Level and task.** Descriptive; aggregation. No model.
- **Reader and decision.** Programme leaders: D2 (where advisors' time goes) and D3 (whether to extend after the pilot).
- **Population.** Enrolments still registered at day 14 (28,061 of 32,593). Unit: enrolment; task for the first miss.
- **Primary approach.** Grouped rates with Wilson 95% intervals. **Baselines:** pooled rate; all enrolments as a
  second denominator; KPI population without the flagged enrolments.
- **Success criterion (Table 4.1).** Both aggregation paths agree to the enrolment; every rate carries its
  denominator and interval; no rate compared across runs without its interval. **Result: met.**

## Decisions taken while working

| Decision | Reason |
| :---- | :---- |
| 2013 runs analysed first, 2014 runs added after the AQ3 freeze | A run-level rate of 2014 is a test outcome; Level 1 keeps test outcomes closed until the single test |
| Second path built from `studentInfo.csv` and `studentRegistration.csv` in `datasets/oulad/` | Independent of the Milestone 3 preparation code |
| First missed week recomputed from `assessment_due.parquet` | Checks the stored `first_missed_week` instead of trusting it |
| "Flagged" = registration day missing or Withdrawn without a withdrawal day | Reproduces the 138 enrolments named in the Level 1 card |

## Methods checklist

- [x] Extraction of analysis tables from the prepared dataset, hash-checked – `extracted-datasets/aq1_*.csv` (`logs/01_extract_all.md`)
- [x] Rates by pooled, year, start month, year × start month, module and run, with Wilson intervals – `results/rates_all.csv`
- [x] Module × start month – `results/rates_module_by_start_month_all.csv`
- [x] Three denominators per run and pooled – `results/denominators_by_run_all.csv`, `denominators_pooled_all.csv`
- [x] Outcome shares (Distinction, Pass, Fail, Withdrawn) – `results/outcome_shares_all.csv`
- [x] Week of the first missed task by outcome, cumulative by week, by module – `results/first_missed_task_*_all.csv`
- [x] Task calendar and runs with no task due by day 27 – `results/task_calendar_by_run_all.csv`
- [x] Rates by gender, disability, deprivation band, age band (description) – `results/rates_by_audit_group_all.csv`
- [x] Evaluation checks C1–C5 – `results/checks_all.csv`, `results/checks_2013.csv`
- [x] Figures – `figures/fig-aq1-1-non-completion-by-run.png`, `fig-aq1-2-first-missed-task.png`
- [ ] Rates adjusted for module mix when comparing student groups (not asked by the Level 1 card; description only)

## Check ledger

| Check | Condition evaluated | Result | Evidence |
| :---- | :---- | :---- | :---- |
| C1 | 32,593 enrolments and 28,061 in the KPI population | PASS | `logs/03_checks_all.md` |
| C2 | Per-run counts and events from the prepared view equal those from the raw tables | PASS, 22 of 22 runs | `results/check_two_paths_all.csv` |
| C3 | Stored first missed week equals the recomputed value | PASS, 32,593 of 32,593 | `logs/03_checks_all.md` |
| C4 | Run counts sum to the pooled count; the four outcome counts sum to n in every run | PASS | `logs/03_checks_all.md` |
| C5 | Every rate has a denominator and an interval that contains it | PASS, 38 rates | `logs/03_checks_all.md` |
| Input | SHA-256 of `enrolment.parquet` and `assessment_due.parquet` equal the Milestone 3 manifest | PASS | `logs/01_extract_all.md` |

One check failed on its first run and was corrected: C4 first compared the sum of rounded shares with 1 and failed at
a difference of 0.000001 caused by the six-decimal CSV; it now compares exact counts (`logs/03_checks_2013.md`, and
the row with exit status 1 in `../logs/experiment-log.md`).

## Open issues

- The KPI of the pilot (completion rate, target 75%) has an OULAD analogue of 54.7% completion (100% − 45.3%); the
  70% baseline of the SMART Goal is the university's assumption and is not tested here.
- Whether the February gap reflects the students who start in February or the calendar cannot be told from these data.
