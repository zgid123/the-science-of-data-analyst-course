# T08 results: AQ1 and AQ2 on the 9 module runs of 2013

Working methods note for task T08 of Milestone 5. It maps every output file to the item of the Milestone 4 plan it
answers, states the populations, the 2013-only rule and how the code enforces it, and lists every deviation from the
plan and every planned item deferred, with the reason. The plan is the Milestone 4 report: Section 1.1 (AQ wording,
early-sign rule C10), Section 3.2 (AQ1 and AQ2 methods, C14), Section 4.1 Tables 4.1 and 4.2 (Evaluation Design Cards
of AQ1 and AQ2), Sections 4.3 and 4.4, and Appendices II–IV.

## How to rebuild

```bash
bash reports/milestone-5/code/run_T08.sh     # aq_analysis.py then aq_checks.py; appends to logs/T08_*.log
```

- `code/aq_analysis.py` writes every file below; it is deterministic (two consecutive runs give byte-identical
  results, SHA-256 per file in `logs/T08_aq_analysis.log`).
- `code/aq_checks.py` compares the 2013 populations and rates with the numbers Milestones 3 and 4 report, checks the
  interval and risk-difference code against statsmodels and scans the results for 2014 rows
  (`logs/T08_checks.log`: 95 PASS, 0 FAIL, 3 INFO).
- Dependencies: `reports/milestone-5/requirements.txt` (shared `venv`).

## Populations and denominators

| Population | Definition | Enrolments | Non-completers | Used by |
| :---- | :---- | :---- | :---- | :---- |
| All 2013 enrolments | every enrolment of the 9 runs of 2013 (`enrolment.parquet`) | 13,529 | 6,959 (51.4%) | AQ1 second denominator |
| Day-14 population (KPI) | still registered at day 14 (`enrolled_d14`) | 12,076 | 5,515 (45.7%) | AQ1 primary denominator |
| Day-14 population without flagged | day-14 population without the enrolments flagged for an unknown withdrawal or registration day | 12,068 | 5,507 (45.6%) | AQ1 baseline (card: "without the 138 flagged") |
| Day-27 population | registered at day 27 (`features_d27.parquet`) | 11,811 | 5,245 (44.4%) | AQ2, all signs |
| Day-27, runs with a task due by day 27 | 7 runs (all except EEE 2013J and GGG 2013J) | 9,960 | see `aq2_associations.csv` | AQ2 task signs (missed task, late TMA) |

Sources: `aq_results.json` (`aq1.*.n`, `aq2.population`), `aq1_rates.csv`, `aq2_associations.csv`. "Non-completion" is
`final_result` Fail or Withdrawn; completion is Pass or Distinction (Milestone 3 data dictionary).

## The 2013-only rule and how it is enforced

- Every prepared view and raw table is read with `scan_parquet`/`scan_csv` followed by a filter on
  `code_presentation` starting with "2013"; polars pushes the filter into the reader, so 2014 rows are not
  materialised. `assert_2013` then stops the run if any row has a presentation other than 2013B/2013J, a year other
  than 2013 or a split other than `train` (function `load_view`, `load_raw`).
- No outcome column is touched before that filter. `model_ready_*` views are not used.
- The only 2014 information is the per-run outcome counts that Milestone 3 published in
  `package/data/metadata/fig_outcome_by_run.csv`, used in `aq1_year_comparison.csv` and `aq1_year_difference.csv`,
  every 2014 row labelled "published in Milestone 3 (fig_outcome_by_run.csv); not recomputed".
- `aq_checks.py` scans every other result file for "2014B"/"2014J" (none found) and checks the labels of the
  published 2014 rows.

## Output map

| File | Plan item | What it holds |
| :---- | :---- | :---- |
| `aq1_rates.csv` | AQ1 card primary metric (Table 4.1); Section 3.2 | Completion, non-completion, Pass, Distinction, Fail and Withdrawn shares overall, per module, run and start month, under three denominators (day-14, all enrolments, day-14 without flagged), each with events, denominator and 95% Wilson interval |
| `aq1_denominator_shift.csv` | AQ1 card error analysis: "runs whose rate moves by more than its interval between the two denominators" | Each rate under both denominators; `outside_day14_interval` = the all-enrolment rate lies outside the day-14 interval |
| `aq1_year_comparison.csv` | AQ1 card primary metric "by year"; AQ1 wording | Outcome shares by year, module × year, start month × year over all enrolments; 2013 computed (equal to the published counts), 2014 published in Milestone 3 |
| `aq1_year_difference.csv` | as above | Non-completion 2014 − 2013 (pp) with Newcombe interval, overall, per module (CCC excluded: no 2013 run) and per start month |
| `aq1_first_missed_week_cumulative.csv` | AQ1 card secondary metric; Section 3.2 "week in which each enrolment first misses an assessed task, compared by outcome" | Cumulative share with a first missed TMA/CMA by week 1–34, by final result and by completion, both denominators, Wilson intervals |
| `aq1_first_missed_week_summary.csv` | as above | Share with any missed task, share by week 4, quartiles of the first missed week, by outcome |
| `aq1_runs_task_due.csv` | AQ1 card error analysis: "runs with no task due by day 27" | Per run: tasks due by day 27, first due day, missed-task counts and timing |
| `aq1_subgroup_rates.csv` | AQ1 card fairness / subgroup check (description only) | Completion and non-completion by gender, disability, deprivation band and age band, both denominators |
| `aq1_validation_two_paths.csv` | AQ1 card validation strategy and success criterion | Outcome counts per run from the prepared view and from the raw tables (`studentInfo.csv`, `studentRegistration.csv`, day-14 rule recomputed), both denominators: 72 of 72 cells agree; `first_missed_week` recounted from `assessment_due`: 13,529 of 13,529 agree (`aq_results.json` `aq1.validation`) |
| `aq2_associations.csv` | AQ2 card primary and secondary metrics, baseline and success criterion (Table 4.2); Section 3.2 | Per sign: rates with and without, unadjusted risk difference (Newcombe) and odds ratio (Woolf); adjusted one sign at a time; mutually adjusted average risk difference (pp, 95% CI) and odds ratio at the average module; modules with the same direction; verdict |
| `aq2_module_effects.csv` | AQ2 card secondary metric: "module-specific risk differences from the sign × module terms" | Per sign and module: unadjusted and mutually adjusted risk difference and odds ratio |
| `aq2_model_coefficients.csv` | Section 3.2 model | All coefficients of the main model with HC1 robust SE, z, p and odds ratio |
| `aq2_sign_rates_by_run.csv` | AQ2 card validation ("task-based signs only in runs with a task due by day 27") | Prevalence of every sign, late CMA and the C10 rule per run |
| `aq2_binned_residuals.csv` | AQ2 card error analysis: "binned residuals by run and activity level" | Observed − predicted (pp) with ±2 SE band by run, by five activity levels and by predicted-risk decile |
| `aq2_sign_correlation.csv` | AQ2 card error analysis: "correlation among the click-based signs" | Pearson correlation (phi between two binary signs) of the five signs and three click measures |
| `aq2_sensitivity.csv` | AQ2 card error analysis: sensitivity runs | Mutually adjusted estimates under each variant (see below) |
| `aq2_subgroups.csv` | AQ2 card fairness / subgroup check: "associations by gender, disability and deprivation band, described, not adjusted away" | Per group and sign: non-completion rate, unadjusted risk difference, mutually adjusted risk difference from a within-group refit |
| `aq2_sensitivity_continuous.csv` | Post-hoc sensitivity (T14), not in the Milestone 4 plan; prompted by the binned-residual check (`aq2_binned_residuals.csv`, activity levels outside ±2 SE) | Main AQ2 model and the same model with log(1 + clicks on days 0–27) added: mutually adjusted average risk difference (pp, 95% CI), modules with the same direction and verdict per sign; the refit's residuals by the five activity levels all lie inside ±2 SE (`code/aq2_sensitivity_continuous.py`, `logs/T14_aq2_sensitivity.log`) |
| `aq_results.json` | – | Key numbers of all the above |
| `aq_summary.md` | – | The tables in Markdown, one line each on what they show |

## Methods as implemented

**Intervals.** Every proportion carries a 95% Wilson score interval; every difference of two proportions a 95%
Newcombe hybrid score interval (Wilson limits combined); a crude odds ratio a 95% Woolf (log) interval. Both
implementations match statsmodels to 8–10 decimals (`logs/T08_checks.log`).

**AQ2 signs at day 27** (from `features_d27`, 2013 rows):

| Sign | Definition | Defined in |
| :---- | :---- | :---- |
| `missed_task` | a TMA or CMA due by day 27 with no non-banked submission by day 27 (`tasks_missed_c ≥ 1`, equal to `rule_missed`) | 7 runs with a task due by day 27 |
| `late_tma` | a TMA due by day 27 submitted late by day 27 (`tma_late_c ≥ 1`, equal to `rule_tma_late`, C10) | same 7 runs |
| `inactive_last7` | no click on days 21–27 (C10) | all 9 runs |
| `low_relative_activity` | clicks on days 0–27 below the median of the same run (`activity_ratio_run < 1`) | all 9 runs |
| `no_pre_start_activity` | no click before day 0 (`clicks_pre = 0`) | all 9 runs |

**AQ2 model.** Logistic regression of non-completion on the five signs, a fixed effect per run (8 dummies),
previous attempts (linear) and credits studied (linear, per 30 credits), and sign × module terms coded as deviations
from the average module over the modules where the sign is defined (4 modules for the task signs, 6 for the click
signs); 37 parameters, 11,811 enrolments, converged (McFadden pseudo-R² 0.145). Covariance HC1 (heteroskedasticity-robust), no clustering, as
Section 3.2 fixes. In EEE 2013J and GGG 2013J the task signs are 0 by construction, so these runs inform only the
click signs and the background terms.

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

**Sensitivity runs** (`aq2_sensitivity.csv`, column `origin`):

| Variant | Origin | Change |
| :---- | :---- | :---- |
| `dedup_clicks` | AQ2 card | relative-activity sign recomputed from de-duplicated clicks (`clicks_0c_dedup`, run median of the same); inactivity and pre-start signs unchanged, since removing exact duplicate rows never empties an active day |
| `late_tma_or_cma` | AQ2 card | late sign counts late CMAs too (`tasks_late_c ≥ 1`); in 2013 a late CMA by day 27 occurs only in DDD 2013B (85.65% of its enrolments, `aq2_sign_rates_by_run.csv`) |
| `excl_flagged` | AQ2 card | without the 8 day-27 enrolments of 2013 flagged for an unknown withdrawal or registration day |
| `drop_no_task_runs` | AQ2 card | EEE 2013J and GGG 2013J removed (9,960 enrolments) |
| `below_half_median` | added | relative-activity sign at half the run median instead of the median |
| `no_interactions` | added | common sign effect across modules (no sign × module terms) |

## Deviations from the Milestone 4 plan and specification choices

1. **Threshold of the relative-activity sign.** The plan names the sign ("activity against the run's median") but
   fixes no cut. We use "below the run median" (`activity_ratio_run < 1`, the literal reading; by construction about
   half of each run), and add "below half the median" as a sensitivity run. Results: 13.36 pp against 14.70 pp
   (`aq2_sensitivity.csv`).
2. **Fifth sign "no activity before the start".** The AQ2 wording lists four kinds of sign; the AQ2 Modeling Brief
   (Milestone 4 Table 2.2) adds "activity before the start" to the inputs. It is included as a binary sign (no click
   before day 0); removing it would change the mutual adjustment of the other click signs.
3. **Functional form of the background terms.** The plan names "previous attempts and credits studied" without a
   form; both enter linearly (credits per 30).
4. **Robust covariance flavour.** The plan fixes robust standard errors without clustering; HC1 is used.
5. **Odds ratio with sign × module terms.** With module-specific terms there is no single odds ratio; the reported
   one is at the average module (deviation coding, the module coding Appendix III fixes for AQ3), with the module
   values beside it.
6. **AQ2 subgroup estimates.** The card asks for associations by gender, disability and deprivation band,
   described, not adjusted away. We report the unadjusted risk difference per group and a mutually adjusted one from
   a refit within the group without sign × module terms (too few enrolments per group and module), fitted only when
   the group holds at least 100 non-completers and 100 completers (the size Section 4.4 uses for a stable estimate);
   all 15 groups qualify. Age band is not in the AQ2 card and is not reported for AQ2 (it is for AQ1).
7. **Activity levels for binned residuals.** The card names "activity level" without levels; five are used: no
   click on days 0–27, below half the run median, half to the median, median to twice the median, twice the median
   or more. Residuals by predicted-risk decile are added. Residuals by run are zero by construction (run fixed
   effects with an intercept reproduce each run's rate) and are kept only to show this.
8. **Year comparison.** 2014 enters only as the outcome counts published by Milestone 3, all-enrolment denominator,
   and only at the levels year, module × year and start month × year (see Deferred items).
9. **Baselines on 2013 only.** The AQ1 card's "pooled rate over all runs" and "rate without the 138 flagged
   enrolments" are computed over the 9 runs of 2013 (21 flagged enrolments in 2013, 8 of them in the day-14
   population).
10. **Denominator-shift rule.** "Moves by more than its interval" is read as: the all-enrolment rate lies outside
    the 95% Wilson interval of the day-14 rate.

## Deferred items (not computed) and why

| Planned item | Reason |
| :---- | :---- |
| AQ2 replication on the 13 runs of 2014, including module CCC (AQ2 card validation strategy; Appendix III step 8) | C14: the 2014 outcomes stay unopened until the single AQ3 test |
| AQ1 for 2014 under the day-14 denominator, 2014 first missed week, 2014 subgroup rates | Needs 2014 rows; after the AQ3 test |
| AQ1 pooled baselines over all 22 runs (28,061 day-14 enrolments; 54.7% completion published by Milestone 3) | Needs 2014 rows; the published 22-run figures are quoted in `logs/T08_checks.log`, not recomputed |
| Concurrent runs as an AQ2 input (Milestone 3 readiness matrix, C12) | Defined for 2014 only |
| Module CCC in any AQ1 or AQ2 comparison | No 2013 run |

## Results in brief

- AQ1: 45.7% (44.8–46.6) of the 12,076 enrolments still registered at day 14 did not complete; 51.4% (50.6–52.3)
  of all 13,529 enrolments. By module (day 14) from AAA 24.9% (20.7–29.5, n = 370) to DDD 53.5% (51.7–55.3,
  n = 2,872); by run from AAA 2013J 24.9% to DDD 2013B 57.5% (54.7–60.2, n = 1,197). The rate moves outside its
  interval between the two denominators overall and in 7 of 9 runs (all but AAA 2013J and GGG 2013J), by up to
  9.9 pp (BBB 2013J). 2014 − 2013 (all enrolments, 2014 published): +2.3 pp (1.2–3.4). Of the day-14 non-completers,
  78.1% missed an assessed task (19.6% by week 4; median first missed week 9), against 21.9% of completers (0.5% by
  week 4; median week 24) (`aq1_*.csv`).
- AQ2 (mutually adjusted average risk difference, pp, 95% CI; unadjusted beside it): missed task 40.8 (37.7–43.9)
  vs 50.3; late TMA 20.2 (15.9–24.5) vs 18.5; inactive last 7 days 14.5 (11.3–17.6) vs 25.3; below run median
  13.4 (11.5–15.2) vs 27.3; no pre-start activity 10.6 (7.8–13.3) vs 21.2. All five meet the card's criterion
  "consistent association" (same direction in 4/4 or 6/6 modules), and every sensitivity run keeps each sign above
  5 pp with an interval excluding 0 (`aq2_associations.csv`, `aq2_sensitivity.csv`).
- Points for the write-up: binned residuals by activity level lie outside ±2 SE in all five levels (no-click
  enrolments 5.6 pp above prediction), so the binary activity signs do not capture the full activity gradient; by
  predicted-risk decile all residuals lie within the band (`aq2_binned_residuals.csv`). Late TMA reads larger
  adjusted than unadjusted because it is negatively correlated with the missed-task sign (phi −0.079,
  `aq2_sign_correlation.csv`). Module intervals include 0 for inactivity in AAA and GGG, for low relative activity
  in AAA and for no pre-start activity in AAA and GGG (`aq2_module_effects.csv`).
