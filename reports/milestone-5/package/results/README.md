# Results: AQ1 and AQ2 on the runs of 2013, of 2014 and on all 22 runs; AQ3 and AQ4 trained on 2013, tested on 2014

This note maps every result file to the item of the Milestone 4 analysis plan it answers, states the populations of
each scope, how the code keeps each scope to its own runs, and lists every deviation from the plan and every planned
item not computed, with the reason. The plan is the Milestone 4 report: Section 1.1 (AQ wording, early-sign rule C10),
Section 3.2 (AQ1 and AQ2 methods, C14), Section 4.1 Tables 4.1 and 4.2 (Evaluation Design Cards of AQ1 and AQ2),
Sections 4.3 and 4.4, and Appendices II–IV. Change Log entries (C10, C12, C14, C15, …) are in
`data/metadata/change_log.md`. Under C15, AQ1 and AQ2 are computed on both years of OULAD, while the AQ3 test keeps the
design Milestone 4 fixed on the 2013 runs alone. The AQ3 and AQ4 results (files `aq3_*` and `aq4_*` in the same four folders) are
described in their own section below ("AQ3 and AQ4").

## How to rebuild

`bash run_all.sh` from the package folder rebuilds every file below (steps 08–18; see the package `README.md`).

| Folder | Runs | Written by |
| :---- | :---- | :---- |
| `results/2013/` | the 9 runs of 2013 | `src/analysis/aq_analysis.py` (step 08), `aq2_sensitivity_continuous.py` (step 10) |
| `results/2014/` | the 13 runs of 2014 | `aq_analysis.py --scope 2014` (step 12), `aq2_sensitivity_continuous.py --scope 2014` (step 14) |
| `results/all_runs/` | all 22 runs | `aq_analysis.py --scope all` (step 13), `aq2_sensitivity_continuous.py --scope all` (step 15) |
| `results/compare/` | 2013 against 2014 | `src/analysis/aq_year_compare.py` (step 16); the three cross-check files `*_published.csv` by `aq_analysis.py` (step 08) and `aq1_year_shared_modules.py` (step 09) |

- `results/` itself holds this note and `checksums.csv`. The three scope folders hold the same set of 18 files, built
  by the same code; each has an `aq_summary.md` that names its writer (`src/analysis/aq_analysis.py --scope <scope>`)
  and states each table in words.
- `results/compare/` holds the comparison of both years computed from the prepared views of each year, its own
  `aq_summary.md` with one line on each comparison table, and three cross-checks that compare 2013 with the 2014
  outcome counts Milestone 3 published (`aq1_year_comparison_published.csv`, `aq1_year_difference_published.csv`,
  `aq1_year_shared_modules_published.csv`). The report uses `compare/aq1_year_comparison_computed.csv`.
- `src/analysis/aq_checks.py` (step 11, 96 checks and 3 notes) compares the 2013 populations and rates with the numbers Milestones 3 and 4
  report, checks the interval and risk-difference code against statsmodels and scans the 2013 result files for 2014
  rows (`logs/11_aq_checks.log`).
- `src/analysis/aq_checks_years.py` (step 17, 53 checks) compares the 2014 outcome counts per run and outcome with the
  counts Milestone 3 published, the 22-run totals with the figures Milestone 3 reported (32,593 enrolments, 28,061
  registered at day 14, 54.7% completion among them), checks the two aggregation paths and the first missed week in
  2014 and over 22 runs, checks that each scope's files hold only its own runs, that every AQ2 model converged and that
  the year comparison reproduces each year's own rates, and recounts the concurrent enrolments of C12 (1,382 at day
  14, 12 of them in 2013 runs) (`logs/17_aq_checks_years.log`).
- All result files are deterministic: a rebuild gives byte-identical files, checked in step 18 against the 63 SHA-256
  values in `checksums.csv` (`data/metadata/rebuild_check_results.csv`).
- Inputs: the prepared views in `data/processed/`, the raw tables in `data/raw/` (second aggregation path of the AQ1
  validation) and `data/metadata/fig_outcome_by_run.csv` (outcome counts per run published by Milestone 3).
- Rounding: the CSV files store rates to 4 decimals and percentage points to 2 decimals
  (`compare/aq2_year_comparison.csv` to 4). A value stored on a final 5, such as 0.4495, is rounded to one decimal
  from the counts or the unrounded estimate, not from the stored value: 7,185 of 15,985 is 44.9%.

## Populations and denominators

| Population | Definition | 2013 (9 runs) | 2014 (13 runs) | 22 runs | Used by |
| :---- | :---- | :---- | :---- | :---- | :---- |
| All enrolments | every enrolment of the scope (`enrolment.parquet`) | 13,529; 6,959 non-completers (51.4%) | 19,064; 10,249 (53.8%) | 32,593; 17,208 (52.8%) | AQ1 second denominator |
| Day-14 population (KPI) | still registered at day 14 (`enrolled_d14`) | 12,076; 5,515 (45.7%) | 15,985; 7,185 (44.9%) | 28,061; 12,700 (45.3%) | AQ1 primary denominator |
| Day-14 population without flagged | without the enrolments flagged for an unknown withdrawal or registration day | 12,068; 5,507 (45.6%) | 15,894; 7,095 (44.6%) | 27,962; 12,602 (45.1%) | AQ1 baseline (card: "without the 138 flagged") |
| Day-27 population | registered at day 27 (`features_d27.parquet`) | 11,811; 5,245 (44.4%) | 15,724; 6,911 (44.0%) | 27,535; 12,156 (44.1%) | AQ2, all signs |
| Day-27, runs with a task due by day 27 | runs other than those of EEE and GGG | 7 runs, 9,960 | 9 runs, 12,585 | 16 runs, 22,545 | AQ2 task signs (missed task, late TMA) |

Sources: `aq_results.json` of each folder (`aq1.*.n`, `aq2.population`), `aq1_rates.csv`, `aq2_associations.csv`.
"Non-completion" is `final_result` Fail or Withdrawn; completion is Pass or Distinction (Milestone 3 data dictionary).

## Scope of each analysis and how it is enforced

- `aq_analysis.py` and `aq2_sensitivity_continuous.py` take `--scope 2013 | 2014 | all` (2013 by default). Every
  prepared view and raw table is read with `scan_parquet`/`scan_csv` followed by a filter on `code_presentation`
  that keeps the runs of the scope; polars pushes the filter into the reader, so rows of other runs are not
  materialised. `assert_scope` then stops the run if any row lies outside the scope (functions `load_view`,
  `load_raw`):

  | Scope | Presentations kept | `year` | `split` | Results folder |
  | :---- | :---- | :---- | :---- | :---- |
  | `2013` | 2013B, 2013J | 2013 | `train` | `results/2013/` |
  | `2014` | 2014B, 2014J | 2014 | `test` | `results/2014/` |
  | `all` | 2013B, 2013J, 2014B, 2014J | 2013 or 2014 | `train` or `test` | `results/all_runs/` |

- No outcome column is touched before that filter. `model_ready_*` views are not used by any analysis step.
- `tests/test_scope.py` checks the guard on synthetic rows: a loader keeps its own runs and stops on any other, and
  the results folder follows the scope.
- `aq_checks.py` scans the 2013 result files for "2014B"/"2014J" and checks the labels of the published 2014 rows in
  `compare/aq1_year_comparison_published.csv`;
  `aq_checks_years.py` checks that no file of `results/2014/` names a 2013 run and no 2013 file a 2014 run.
- 2014 outcomes enter only AQ1 and AQ2. The transforms of step 05 are fitted on the 2013 runs only, and the AQ3 test
  keeps the predictors, candidate configurations, selection rule and gate that Milestone 4 fixed on 2013 (C15).

## Output map

The files of the first table exist in `results/2013/`, `results/2014/` and `results/all_runs/`, each on the runs of
its scope; the second table lists the files of `results/compare/` and of `results/` itself (paths relative to
`results/`).

| File | Plan item | What it holds |
| :---- | :---- | :---- |
| `aq1_rates.csv` | AQ1 card primary metric (Table 4.1); Section 3.2 | Completion, non-completion, Pass, Distinction, Fail and Withdrawn shares overall, per module, run and start month, under three denominators (day-14, all enrolments, day-14 without flagged), each with events, denominator and 95% Wilson interval |
| `aq1_denominator_shift.csv` | AQ1 card error analysis: "runs whose rate moves by more than its interval between the two denominators" | Each rate under both denominators; `outside_day14_interval` = the all-enrolment rate lies outside the day-14 interval |
| `aq1_first_missed_week_cumulative.csv` | AQ1 card secondary metric; Section 3.2 "week in which each enrolment first misses an assessed task, compared by outcome" | Cumulative share with a first missed TMA/CMA by week 1–34, by final result and by completion, both denominators, Wilson intervals |
| `aq1_first_missed_week_summary.csv` | as above | Share with any missed task, share by week 4, quartiles of the first missed week, by outcome |
| `aq1_runs_task_due.csv` | AQ1 card error analysis: "runs with no task due by day 27" | Per run: tasks due by day 27, first due day, missed-task counts and timing |
| `aq1_subgroup_rates.csv` | AQ1 card fairness / subgroup check (description only) | Completion and non-completion by gender, disability, deprivation band and age band, both denominators |
| `aq1_validation_two_paths.csv` | AQ1 card validation strategy and success criterion | Outcome counts per run from the prepared view and from the raw tables (`studentInfo.csv`, `studentRegistration.csv`, day-14 rule recomputed), both denominators: 72 of 72 cells agree in 2013, 104 of 104 in 2014 and 176 of 176 over 22 runs; `first_missed_week` recounted from `assessment_due`: 13,529 of 13,529, 19,064 of 19,064 and 32,593 of 32,593 agree (`aq_results.json` `aq1.validation`) |
| `aq2_associations.csv` | AQ2 card primary and secondary metrics, baseline and success criterion (Table 4.2); Section 3.2 | Per sign: rates with and without, unadjusted risk difference (Newcombe) and odds ratio (Woolf); adjusted one sign at a time; mutually adjusted average risk difference (pp, 95% CI) and odds ratio at the average module; modules with the same direction; verdict |
| `aq2_module_effects.csv` | AQ2 card secondary metric: "module-specific risk differences from the sign × module terms" | Per sign and module: unadjusted and mutually adjusted risk difference and odds ratio |
| `aq2_model_coefficients.csv` | Section 3.2 model | All coefficients of the main model with HC1 robust SE, z, p and odds ratio |
| `aq2_sign_rates_by_run.csv` | AQ2 card validation ("task-based signs only in runs with a task due by day 27") | Prevalence of every sign, late CMA and the C10 rule per run |
| `aq2_binned_residuals.csv` | AQ2 card error analysis: "binned residuals by run and activity level" | Observed − predicted (pp) with ±2 SE band by run, by five activity levels and by predicted-risk decile |
| `aq2_sign_correlation.csv` | AQ2 card error analysis: "correlation among the click-based signs" | Pearson correlation (phi between two binary signs) of the five signs and three click measures |
| `aq2_sensitivity.csv` | AQ2 card error analysis: sensitivity runs | Mutually adjusted estimates under each variant (see below) |
| `aq2_subgroups.csv` | AQ2 card fairness / subgroup check: "associations by gender, disability and deprivation band, described, not adjusted away" | Per group and sign: non-completion rate, unadjusted risk difference, mutually adjusted risk difference from a within-group refit |
| `aq2_sensitivity_continuous.csv` | Post-hoc sensitivity, not in the Milestone 4 plan; prompted by the binned-residual check (`aq2_binned_residuals.csv`, activity levels outside ±2 SE) | Main AQ2 model and the same model with log(1 + clicks on days 0–27) added: mutually adjusted average risk difference (pp, 95% CI), modules with the same direction and verdict per sign; the refit's residuals by the five activity levels are printed in the step's log (`logs/10_aq2_sensitivity.log`, `14_aq2_sens_2014.log`, `15_aq2_sens_all.log`) |
| `aq_results.json` | – | Key numbers of all the above |
| `aq_summary.md` | – | The tables in Markdown, each with one line in words on what it shows |

| File | Plan item | What it holds |
| :---- | :---- | :---- |
| `compare/aq1_year_comparison_published.csv` | Cross-check of the AQ1 year comparison | Outcome shares by year, module × year, start month × year over all enrolments; 2013 computed (equal to the published counts), 2014 the counts published in Milestone 3, each such row labelled "published in Milestone 3 (fig_outcome_by_run.csv); not recomputed" |
| `compare/aq1_year_difference_published.csv` | as above | Non-completion 2014 − 2013 (pp) with Newcombe interval from the same counts, overall, per module (CCC excluded: no 2013 run) and per start month |
| `compare/aq1_year_shared_modules_published.csv` | as above | Non-completion 2013 and 2014 over the six modules that ran in both years (all enrolments, 2014 published), difference in pp with a Wald 95% interval, and the 2014 rate of CCC alone |
| `compare/aq1_year_comparison_computed.csv` | AQ1 card primary metric "by year", both denominators (C15) | Non-completion per year under the day-14 and all-enrolment denominators, overall, over the six shared modules, per start month, per shared module and per module and start month present in both years, with the 2014 − 2013 difference (Newcombe 95% interval); CCC as its own row without a difference |
| `compare/aq1_first_missed_week_by_year.csv` | AQ1 card secondary metric, by year | Share of the day-14 population with a missed assessed task, share by week 4 and median first missed week, by year and completion group, with the 2014 − 2013 difference of the shares |
| `compare/aq1_left_before_day14.csv` | AQ1 card error analysis (denominator shift), by year | Share of all enrolments not registered at day 14, by year, overall and over the six shared modules, with the 2014 − 2013 difference; it explains why the year difference changes sign between the denominators |
| `compare/aq2_year_comparison.csv` | AQ2 card validation strategy (replication on 2014, Appendix III step 8) | Mutually adjusted average risk difference of each sign in 2013 and 2014 (four decimals), the difference of the two (independent samples; normal interval from the two delta-method robust standard errors), modules with the same direction and verdict in each year |
| `compare/aq2_concurrent_2014.csv` | Milestone 3 readiness matrix; C12 | The sign "tasks missed in several modules at once", 2014 only: enrolments registered at day 27 with a missed task by day 27 in this enrolment and in another enrolment of the same student in the same presentation, against the rest, among all 2014 enrolments and among the concurrent ones; unadjusted; with the count of concurrent enrolments at day 27 in each year |
| `compare/aq_summary.md` | – | Every comparison table in Markdown, each with one line in words on what it shows |
| `checksums.csv` | – | SHA-256 of the 63 result files, the reference for step 18 of `run_all.sh` |

## Methods as implemented

**Intervals.** Every proportion carries a 95% Wilson score interval; every difference of two proportions a 95%
Newcombe hybrid score interval (Wilson limits combined); a crude odds ratio a 95% Woolf (log) interval. Both
implementations match statsmodels to 8–10 decimals (`logs/11_aq_checks.log`).

**AQ2 signs at day 27** (from `features_d27`, rows of the scope):

| Sign | Definition | Defined in |
| :---- | :---- | :---- |
| `missed_task` | a TMA or CMA due by day 27 with no non-banked submission by day 27 (`tasks_missed_c ≥ 1`, equal to `rule_missed`) | runs with a task due by day 27 (7 of 2013, 9 of 2014) |
| `late_tma` | a TMA due by day 27 submitted late by day 27 (`tma_late_c ≥ 1`, equal to `rule_tma_late`, C10) | same runs |
| `inactive_last7` | no click on days 21–27 (C10) | all runs |
| `low_relative_activity` | clicks on days 0–27 below the median of the same run (`activity_ratio_run < 1`) | all runs |
| `no_pre_start_activity` | no click before day 0 (`clicks_pre = 0`) | all runs |

**AQ2 model.** Logistic regression of non-completion on the five signs, a fixed effect per run, previous attempts
(linear) and credits studied (linear, per 30 credits), and sign × module terms coded as deviations from the average
module over the modules where the sign is defined and varies. Covariance HC1 (heteroskedasticity-robust), no
clustering, as Section 3.2 fixes. In the runs of EEE and GGG the task signs are 0 by construction, so these runs
inform only the click signs and the background terms.

| Scope | Enrolments | Run dummies | Modules with a module term, task signs / click signs | Parameters | McFadden pseudo-R² |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2013 | 11,811 | 8 | 4 / 6 | 37 | 0.145 |
| 2014 | 15,724 | 12 | missed task 5, late TMA 4 / 7 | 45 | 0.135 |
| 22 runs | 27,535 | 21 | missed task 5, late TMA 4 / 7 | 54 | 0.138 |

Every model converged (`aq_results.json` `aq2.model`).

- **Module terms where a sign never occurs.** A module in which a sign is defined but never occurs gets no sign ×
  module term, so the model stays estimable and the rows of that module take the average-module effect. This applies
  to the late-TMA sign in module CCC: no CCC enrolment had a late TMA by day 27 in 2014 (`aq2_sign_rates_by_run.csv`
  in `results/2014/`), so the late-TMA verdict counts 4 modules in 2014 and over 22 runs. `tests/test_scope.py`
  checks this rule on synthetic data.
- Average risk difference of a sign = mean over the enrolments where the sign is defined of the predicted risk with
  the sign set to 1 minus set to 0 (every other variable at its observed value, sign × module term following the
  sign), in percentage points; 95% interval by the delta method with the HC1 covariance. Checked against statsmodels
  `get_margeff` on the model without sign × module terms (identical to 8 decimals).
- Odds ratio = exp of the sign's main coefficient, which under deviation coding is the odds ratio at the average
  module (geometric mean of the module odds ratios); module odds ratios in `aq2_module_effects.csv`.
- Three columns side by side: unadjusted; adjusted for run, background and the sign's module terms, one sign at a
  time (`rd_adj_single_*`); mutually adjusted (all signs, `rd_adj_mutual_*`), as Section 3.2 asks.
- Verdict (Table 4.2): "consistent association" when the mutually adjusted average risk difference is ≥ 5 pp with an
  interval excluding 0 and has the same direction in at least two-thirds of the modules where the sign is defined;
  otherwise "weak or inconsistent". p-values are reported in `aq2_associations.csv` and `aq2_model_coefficients.csv`
  but take no part in the verdict.
- Year difference of a sign (`compare/aq2_year_comparison.csv`): 2014 estimate minus 2013 estimate, with a normal 95%
  interval whose standard error combines the two delta-method robust standard errors, the two years being independent
  samples.

**Sensitivity runs** (`aq2_sensitivity.csv`, column `origin`), the same variants in each scope:

| Variant | Origin | Change |
| :---- | :---- | :---- |
| `dedup_clicks` | AQ2 card | relative-activity sign recomputed from de-duplicated clicks (`clicks_0c_dedup`, run median of the same); inactivity and pre-start signs unchanged, since removing exact duplicate rows never empties an active day |
| `late_tma_or_cma` | AQ2 card | late sign counts late CMAs too (`tasks_late_c ≥ 1`); a late CMA by day 27 occurs only in DDD 2013B in 2013 (85.65% of its enrolments) and only in CCC 2014B and CCC 2014J in 2014 (86.00% and 88.52%) (`aq2_sign_rates_by_run.csv`) |
| `excl_flagged` | AQ2 card | without the day-27 enrolments flagged for an unknown withdrawal or registration day (8 in 2013, 92 in 2014) |
| `drop_no_task_runs` | AQ2 card | the runs of EEE and GGG removed (9,960 enrolments in 2013, 12,585 in 2014) |
| `below_half_median` | added | relative-activity sign at half the run median instead of the median |
| `no_interactions` | added | common sign effect across modules (no sign × module terms) |

## Deviations from the Milestone 4 plan and specification choices

1. **Threshold of the relative-activity sign.** The plan names the sign ("activity against the run's median") but
   fixes no cut. We use "below the run median" (`activity_ratio_run < 1`, the literal reading; by construction about
   half of each run), and add "below half the median" as a sensitivity run. Results in 2013: 13.36 pp against
   14.70 pp (`2013/aq2_sensitivity.csv`).
2. **Fifth sign "no activity before the start".** The AQ2 wording lists four kinds of sign; the AQ2 Modeling Brief
   (Milestone 4 Table 2.2) adds "activity before the start" to the inputs. It is included as a binary sign (no click
   before day 0); removing it would change the mutual adjustment of the other click signs.
3. **Functional form of the background terms.** The plan names "previous attempts and credits studied" without a
   form; both enter linearly (credits per 30).
4. **Robust covariance flavour.** The plan fixes robust standard errors without clustering; HC1 is used.
5. **Odds ratio with sign × module terms.** With module-specific terms there is no single odds ratio; the reported
   one is at the average module (deviation coding, the module coding Appendix III fixes for AQ3), with the module
   values beside it. A module where a sign never occurs gets no module term (see "AQ2 model").
6. **AQ2 subgroup estimates.** The card asks for associations by gender, disability and deprivation band,
   described, not adjusted away. We report the unadjusted risk difference per group and a mutually adjusted one from
   a refit within the group without sign × module terms (too few enrolments per group and module), fitted only when
   the group holds at least 100 non-completers and 100 completers (the size Section 4.4 uses for a stable estimate)
   and the refit converges. All 15 groups get the adjusted estimate in 2013; in 2014 and over 22 runs the refit of
   the group with a missing deprivation band (610 and 1,028 enrolments) does not converge, and that group is
   reported crude only (column `adjusted_note`: "crude only: … or no convergence"), so 14 of 15 groups carry an
   adjusted estimate. Age band is not in the AQ2 card and is not reported for AQ2 (it is for AQ1).
7. **Activity levels for binned residuals.** The card names "activity level" without levels; five are used: no
   click on days 0–27, below half the run median, half to the median, median to twice the median, twice the median
   or more. Residuals by predicted-risk decile are added. Residuals by run are zero by construction (run fixed
   effects with an intercept reproduce each run's rate) and are kept only to show this.
8. **Year comparison.** The year comparison is computed from the prepared views under both denominators
   (`compare/aq1_year_comparison_computed.csv`). The comparison with the 2014 outcome counts that Milestone 3
   published (all-enrolment denominator; `compare/aq1_year_comparison_published.csv`,
   `compare/aq1_year_difference_published.csv`, `compare/aq1_year_shared_modules_published.csv`) gives the same all-enrolment difference, +2.3 pp, and is kept as a cross-check.
9. **Pooled baselines.** The AQ1 card's "pooled rate over all runs" and "rate without the 138 flagged enrolments" are
   computed in each scope; over all 22 runs the day-14 population without flagged enrolments holds 27,962 of 28,061
   (`all_runs/aq1_rates.csv`).
10. **Denominator-shift rule.** "Moves by more than its interval" is read as: the all-enrolment rate lies outside
    the 95% Wilson interval of the day-14 rate.
11. **Several-modules sign.** C12 describes it for 2014 only and keeps it out of the AQ3 predictors. It is reported
    unadjusted, as a share of non-completers with and without the sign (`compare/aq2_concurrent_2014.csv`), and is
    not a term of the AQ2 model, because it marks 28 enrolments.

## AQ3 and AQ4

**Plan items.** Milestone 4 report: Section 3.3 (candidates), Section 4.1 Tables 4.3 and 4.4 (Evaluation Design Cards of
AQ3 and AQ4), Section 4.3 Table 4.5 (S1, S2, S3, FR1), Section 4.4 (fairness groups) and Appendix III (validation and
test protocol). Implementation details the plan leaves open follow the team's Level 2 prototype; the one choice made
after 2014 results existed is the tuning criterion (Change Log C18).

**Populations.** Development: the 9 runs of 2013, 11,811 enrolments registered at day 27 (5,245 non-completers) and
12,080 at day 13. Test: the 13 runs of 2014, 15,724 enrolments at day 27 (6,911 non-completers) and 15,989 at day 13.

**How the year split is enforced.** `aq3_develop.py` (step 19) reads each feature view with a 2013 filter pushed to the
reader and asserts it; it ends by writing `data/interim/aq3/freeze.json` with the choices and the SHA-256 of all 10
fitted models (5 configurations × 2 cut-offs). `aq3_test.py` (step 20) and `aq4_lists.py` (step 21) stop if the
freeze record is missing or a model changed; the 2014 runs are scored once (`data/interim/aq3/scores_d*.csv`, not
shipped) and every view is computed from those scores, without refitting or recalibration. Step 26 checks that the
freeze precedes the scores.

**Scopes.** AQ3 and AQ4 use the same four folders as AQ1 and AQ2, with one difference in what each folder means,
because the two years play different roles in a predictive test:

| Folder | AQ3/AQ4 scores | How to read |
| :---- | :---- | :---- |
| `2013/` | Each of the 9 runs of 2013 scored by the leave-one-run-out model that left it out (`data/interim/aq3/scores_dev_d27.csv`); also the model choice | Development estimates: the plan uses these folds to choose the model, not to state its performance |
| `2014/` | The 13 runs of 2014 scored once by the models frozen on 2013 | The test: gate S1 and every AQ3/AQ4 number of the report |
| `all_runs/` | The 22 runs pooled, each scored by a model that did not see it (2013 out-of-fold, 2014 test) | Description of all runs; no model is fitted on all 22 runs |
| `compare/` | 2013 development estimates against the 2014 test | How much the model keeps on a later year; cannot change S1 |

Every AQ3/AQ4 table has a column `scores` naming its basis. Day 13 exists for `2014/` only (the development folds were
run at the main operating point, day 27).

**Output map.** Files with the same name hold the same view in `2013/`, `2014/` and `all_runs/`.

| File | Plan item |
| :---- | :---- |
| `2013/aq3_dev_folds.csv`, `2013/aq3_dev_choice.csv`, `2013/aq3_final_tuning.csv`, `2013/aq3_choice.json`, `2013/aq3_coefficients.csv` | Appendix III steps 2–5: leave-one-run-out folds, choice rule (margin 0.03 and 7 of 9 folds), tuning, frozen hyperparameters; coefficients of the chosen model |
| `aq3_by_run.csv`, `aq3_pooled.csv` | Table 4.3: lists of every configuration, the rule-ranked list (B2), the background-only model (B3) and a random list, per run and pooled, 3 and 5 per 20 (day 13 in `2014/` only) |
| `aq3_discrimination_calibration.csv` | Table 4.3 secondary metrics; S3 pooled and per run |
| `aq3_capacity_curve.csv`, `aq3_model_vs_rule.csv`, `aq3_errors_by_slice.csv` | Table 4.3 error analysis: list length, list overlap, recall by activity, history, registration, kind and reach |
| `aq4_list_summary.csv`, `aq4_contact_yield.csv`, `aq4_reach.csv`, `aq4_fairness_descriptive.csv` | Table 4.4: lists at 3 and 5 per 20, lift over random and rule, yield of each contact, kind of non-completion on the list, descriptive rates by gender, age, disability, deprivation band |
| `2014/aq3_s1_gate.csv`, `2014/aq3_sensitivity.csv`, `2014/aq3_calibration_bins.csv`, `2014/aq3_lead_time.csv` | Table 4.5 S1 (first row) and context; Appendix III step 7 sensitivity views; calibration bins; timing of listed non-completers |
| `2014/aq4_reasons.csv`, `2014/aq4_fairness_confirmatory.csv` | Table 4.4 "signs behind each name"; Section 4.4 and FR1 |
| `compare/aq3_dev_vs_test.csv`, `compare/aq4_dev_vs_test.csv` | 2013 development estimates against the 2014 test |
| `aq3_summary.md`, `aq4_summary.md` (each folder) | Plain-text summaries |

**Methods as implemented.** Capacity k = 5 (or 3) × ⌈n/20⌉ per run; exact ties broken by one fixed random number per
enrolment (seed 20261112, key order). Rule-ranked list: number of rule signs, then lower activity relative to the run
median. Candidates: penalised (L2) logistic regression on the background variables (B3), on the 19 primary predictors
(M1) and with the extended predictors and weekly clicks (M2); gradient-boosted trees on the primary (M3) and extended
(M4) sets. Logistic preprocessing refitted in every fold: deviation coding of module and start month, ordinal
education, log(1 + x) for counts, training-median fill with a missing indicator, standardisation. Grids: C ∈ {0.001,
0.003, 0.01, 0.03, 0.1, 0.3, 1, 10}; depth ∈ {2, 3, 4} × trees ∈ {100, 200, 400} × learning rate ∈ {0.05, 0.1}. S1:
paired two-level bootstrap (runs, then enrolments; 2,000 replicates) and exact one-sided sign-flip test on the 13 run
differences. FR1: the same bootstrap with 5,000 replicates, Holm adjustment over three groups. Reasons: the predictor
group with the largest positive contribution (coefficient × standardised value); module and start month count as course
context, not as a reason.

**Deviations and specification choices.** (1) Tuning criterion: pooled log loss of an inner leave-one-run-out loop
(C18); under the recall-based tuning of the Milestone 4 draft package S3 is not met, under log loss it is met on the
pooled estimates but in 5 of 13 runs only, so in both cases the lists show ranks and reasons, not probabilities.
(2) Against the Milestone 4 draft package the rule-ranked list is identical at the main operating point (2,786
non-completers listed at day 27, 5 per 20); at day 13 and at 3 per 20 the two implementations differ by 2 to 5 listed
students through the handling of ties, and the model lists differ by up to 4 (2,868 against 2,871 at the main point).

**Items not computed.** The labels-available variant (2013 February runs → 2014 February runs), net benefit, the
area between ROC curves (ABROCA), the proxy check of the fairness groups and the stability of list membership under
the bootstrap: descriptive extras of the plan that cannot change S1 or FR1.

## Items not computed and why

| Planned item | Reason |
| :---- | :---- |
| Concurrent runs (another enrolment of the same student in the same presentation) as an input of the AQ2 model (Milestone 3 readiness matrix, C12) | 1,288 concurrent enrolments at day 27 in 2014 and 12 in 2013 (`compare/aq2_concurrent_2014.csv`); C12 keeps the sign descriptive and out of the AQ3 predictors |
| Module CCC in a year difference | No 2013 run; CCC appears as a 2014 row of its own |
| AQ3 and AQ4 descriptive extras (labels-available variant, net benefit, ABROCA, proxy check, list stability) | Cannot change S1 or FR1; see "AQ3 and AQ4" above |

## Results in brief

- **AQ1, 2013.** 45.7% (44.8–46.6) of the 12,076 enrolments still registered at day 14 did not complete; 51.4%
  (50.6–52.3) of all 13,529 enrolments. By module (day 14) from AAA 24.9% (20.7–29.5, n = 370) to DDD 53.5%
  (51.7–55.3, n = 2,872); by run from AAA 2013J 24.9% to DDD 2013B 57.5% (54.7–60.2, n = 1,197). The rate moves
  outside its interval between the two denominators overall and in 7 of 9 runs (all but AAA 2013J and GGG 2013J), by
  up to 9.9 pp (BBB 2013J). Of the day-14 non-completers, 78.1% missed an assessed task (19.6% by week 4; median first
  missed week 9), against 21.9% of completers (0.5% by week 4; median week 24) (`2013/aq1_*.csv`).
- **AQ1, 2014.** 44.9% (44.2–45.7) of the 15,985 enrolments registered at day 14 did not complete; 53.8% (53.1–54.5)
  of all 19,064. By module from AAA 27.7% (23.3–32.6, n = 350) to CCC 54.3% (52.7–55.9, n = 3,670), which ran only in
  2014; by run from AAA 2014J 27.7% to CCC 2014B 58.3% (55.9–60.7, n = 1,591). The rate moves outside its interval
  between the denominators overall and in 10 of 13 runs (all but AAA 2014J, GGG 2014B and GGG 2014J), by up to
  13.6 pp (BBB 2014J). Of the non-completers, 72.7% (71.7–73.7) missed an assessed task and 14.7% (13.9–15.5) by week
  4 (median first missed week 9), against 19.4% of completers (0.6% by week 4; median week 22)
  (`2014/aq1_*.csv`, `compare/aq1_first_missed_week_by_year.csv`).
- **AQ1, 22 runs.** 45.3% (44.7–45.8) of the 28,061 enrolments registered at day 14 did not complete (completion
  54.7%, as Milestone 3 reported); 52.8% (52.3–53.3) of all 32,593. By module from AAA 26.3% (23.2–29.6, n = 720) to
  CCC 54.3%; the rate moves outside its interval between the denominators in 17 of 22 runs (`all_runs/aq1_*.csv`).
- **AQ1, year comparison.** The sign of the year difference depends on the denominator. Over all enrolments
  non-completion was 2.3 pp higher in 2014 (1.2 to 3.4); among students registered at day 14 it was 0.7 pp lower
  (−1.9 to 0.5), and 3.5 pp lower (−4.8 to −2.3) over the six modules run in both years. The reason is the
  registration at day 14: 16.2% (15.6–16.7) of 2014 enrolments against 10.7% (10.2–11.3) of 2013 were not registered
  at day 14, a difference of 5.4 pp (4.7 to 6.1) (`compare/aq1_year_comparison_computed.csv`,
  `compare/aq1_left_before_day14.csv`). The share of non-completers with a missed task by week 4 fell from 19.6% to
  14.7%, a difference of −4.9 pp (−6.3 to −3.6) (`compare/aq1_first_missed_week_by_year.csv`).
- **AQ2, 2013** (mutually adjusted average risk difference, pp, 95% CI; unadjusted beside it): missed task 40.8
  (37.7–43.9) vs 50.3; late TMA 20.2 (15.9–24.5) vs 18.5; inactive last 7 days 14.5 (11.3–17.6) vs 25.3; below run
  median 13.4 (11.5–15.2) vs 27.3; no pre-start activity 10.6 (7.8–13.3) vs 21.2. All five meet the card's criterion
  "consistent association" (same direction in 4/4 or 6/6 modules), and every sensitivity run keeps each sign above
  5 pp with an interval excluding 0 (`2013/aq2_associations.csv`, `2013/aq2_sensitivity.csv`).
- **AQ2, 2014 replication** (15,724 enrolments, task signs on 12,585; values from `compare/aq2_year_comparison.csv`):
  missed task 39.3 (36.4–42.1) vs 48.8 unadjusted; late TMA 20.3 (15.6–24.9) vs 14.4; inactive last 7 days 15.8
  (13.3–18.3) vs 26.5; below run median 14.6 (13.0–16.2) vs 27.0; no pre-start activity 8.7 (6.4–10.9) vs 17.9. All
  five are consistent associations, with the same direction in 5/5, 3/4, 7/7, 7/7 and 7/7 modules, and every
  sensitivity run keeps each sign above 5 pp with an interval excluding 0 (`2014/aq2_sensitivity.csv`). The one module
  against the direction is AAA for a late TMA, −1.2 pp (−14.4 to 12.1) (`2014/aq2_module_effects.csv`). No sign moves
  by more than two points between the years: 2014 − 2013 is −1.6 (−5.8 to 2.6) for a missed task, +0.1 (−6.3 to 6.4)
  for a late TMA, +1.4 (−2.7 to 5.4) for inactivity, +1.2 (−1.2 to 3.7) for activity below the run median and −1.9
  (−5.4 to 1.6) for no pre-start activity.
- **AQ2, 22 runs** (27,535 enrolments, task signs on 22,545 in 16 runs; two decimals as stored): missed task 39.75
  (37.68–41.81), late TMA 20.56 (17.58–23.54), inactive 14.66 (12.77–16.55), below run median 14.03 (12.81–15.26),
  no pre-start activity 9.44 (7.73–11.16); all five consistent associations (`all_runs/aq2_associations.csv`).
- **Several-modules sign, 2014.** 28 of the 15,724 enrolments registered at day 27 missed a task in this and another
  module at once; 27 of them did not complete, 96.4% (82.3–99.4) against 43.9% (43.1–44.6) of the others
  (`compare/aq2_concurrent_2014.csv`). The sign is too rare to change a list.
- **Activity gradient.** Binned residuals by activity level lie outside ±2 SE in all five levels in 2013 (no-click
  enrolments 5.6 pp above prediction) and in 2014 (from +5.1 pp for no click to −5.3 pp for twice the median or more),
  so the binary activity signs do not capture the full activity gradient; by predicted-risk decile all residuals lie
  within the band in 2013 and all but decile 6 in 2014 (2.53 pp against a band of 2.48) (`aq2_binned_residuals.csv`
  of each folder). With log(1 + clicks on days 0–27) added (`aq2_sensitivity_continuous.csv`), every sign stays a
  consistent association in 2013, the below-run-median sign falling to 5.8 pp (3.4–8.3) in 5 of 6 modules. In 2014
  that sign falls to 5.9 pp (3.7–8.1) with the same direction in only 4 of 7 modules, verdict "weak or inconsistent";
  the other four stay consistent: missed task 35.6 (32.4–38.8), late TMA 19.5 (14.9–24.1), inactive 10.7 (8.0–13.4),
  no pre-start activity 6.5 (4.3–8.8). The refit's residuals by activity level lie inside ±2 SE in all five levels in
  2013, while in 2014 and over 22 runs three of the five levels stay outside (`logs/10_aq2_sensitivity.log`,
  `14_aq2_sens_2014.log`, `15_aq2_sens_all.log`).
- **Further observations.** Late TMA reads larger adjusted than unadjusted because it is negatively correlated with
  the missed-task sign (phi −0.079 in 2013, `2013/aq2_sign_correlation.csv`). In 2013, module intervals include 0 for
  inactivity in AAA and GGG, for low relative activity in AAA and for no pre-start activity in AAA and GGG; in 2014
  for late TMA, inactivity, low relative activity and no pre-start activity in AAA and for no pre-start activity in
  BBB and DDD (`aq2_module_effects.csv` of each folder).
- **AQ3, 2013 → 2014.** Development chose M1: no challenger gained the 0.03 margin (pooled normalised recall M1 0.750,
  M2 0.749, M3 0.749, M4 0.748, rule 0.727; `2013/aq3_dev_choice.csv`). On the 13 runs of 2014, at day 27 and 5 per 20, the
  M1 lists hold 2,868 of the 6,911 non-completers (recall 41.5%, precision 72.5%) against 2,786 for the rule-ranked
  list and 1,737.9 expected from a random list: pooled normalised recall 0.725 against 0.704, difference +0.021
  (+0.006 to +0.036), sign-flip p = 0.0035, 11 of 13 runs won, so gate S1 is met (`2014/aq3_s1_gate.csv`). Calibration:
  in the large 0.117 and slope 0.886 pooled (S3 met), 5 of 13 runs within the bounds
  (`2014/aq3_discrimination_calibration.csv`). Of the 6,911 non-completers, 4,193 had normal activity at day 27 (at least
  half the run median); the lists hold 19.1% of them (model) and 15.6% (rule) (`2014/aq3_errors_by_slice.csv`).
- **AQ4, 2014.** The n-th contact per tutor group of 20 finds a non-completer with probability 92.4% (1st), 57.6%
  (5th), 55.2% (6th) and 47.3% (7th) against a base rate of 44.0% (`2014/aq4_contact_yield.csv`). Rule FR1 flags 0 of 3
  confirmatory groups: declared disability +5.5 points, deprivation band 0–10% +1.3, band missing −7.4 (−16.8 to
  +2.3) (`2014/aq4_fairness_confirmatory.csv`). For 80.7% of listed students the main reason is behavioural (low activity,
  a missed task or a late submission); for 14.2% it is prior education (`2014/aq4_reasons.csv`).
