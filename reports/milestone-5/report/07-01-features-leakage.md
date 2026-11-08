## 7.1. Derived Variables, Encoding and Leakage Control

The pipeline of Section 7 integrates the tables at the enrolment grain; the variables derived from them are what the four questions actually use, and each must be built from information that existed at its cut-off. The timing rule, the derived variables, the predictor sets, the encoding and the controls against each form of leakage follow in turn.

**Timing rule.** Every feature uses only records dated on or before its cut-off c, which is day 13 or day 27. A legitimate model may build only on information that existed before its target was known, so activity after the cut-off, the withdrawal day and the final result never enter a feature. Activity before day 0 is kept as its own window, because it is known before teaching starts. Features that need a mark use only CMA marks for submissions made at least seven days before the cut-off, since a CMA score is expected within seven days, while a TMA mark has no release day in the data and is therefore never used as a feature.

**Derived variables.** Table 7.2 defines the main derived variables with their formula and timing rule; c stands for the cut-off day. The names are those of the data dictionary that travels with the Final Project Package.

**Table 7.2. Main derived variables**

| Variable | Formula | Timing rule | Used by |
| :---- | :---- | :---- | :---- |
| non_completion (target) | Final result is Fail or Withdrawn | Observed at the run end; never a feature | AQ1–AQ4 |
| enrolled_d13, enrolled_d14, enrolled_d27 | Registered by day d, or registration day unknown, and not unregistered by day d | Day d (rule C09) | Populations |
| clicks_pre | Clicks before day 0 | Before the start | AQ2 sign, AQ3 |
| clicks_0c, active_days_0c | Clicks, and days with at least one click, from day 0 to c | Days 0 to c | AQ3 |
| activity_ratio_run | (clicks_0c + 1) ÷ (median clicks_0c of the run's enrolled students + 1) | Same run, days 0 to c; no outcome used | AQ2 sign, AQ3 |
| inactive_last7 | No click on days c − 6 to c | Seven days ending at c | AQ2 sign, rule |
| tasks_missed_c | TMA or CMA due by c, due on or after the registration day, not submitted by c | Submissions up to c; banked results excluded | AQ2 sign, rule, AQ3 |
| tma_late_c, cma_late_c | Tasks due by c submitted after the due day but by c, by type | Submissions up to c | AQ2 sign, rule, AQ3 |
| cma_score_mean_c | Mean score of CMAs submitted by c − 7 | Marks known by c | Prepared, not used |
| early_sign_rule | A task missed, or a TMA late, or inactive in the last seven days | At c (rule C10) | AQ3 and AQ4 baseline; secondary KPI 1 |
| early_sign_rule_cma | The rule, or a CMA late | At c | Sensitivity variant |
| first_missed_week | Week of the earliest TMA or CMA not submitted that fell due while the student was enrolled | Whole run | AQ1 only |

A task counts as missed only if it fell due on or after the student's registration day, so a late registrant is not charged with tasks set before joining. The activity ratio compares a student with the median of the same run up to the same day and uses no outcome, so it is a cohort statistic that is still known at the cut-off. The early-sign rule (C10) flags an enrolment with a task due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off; it is the one early-sign rule of the project, on OULAD and in the pilot (Change Log C17, Section 3.2).

**Predictor sets.** The feature views hold 20 primary and 10 extended predictors plus the weekly click counts; every other column is an identifier, the target, a flag for evaluation, the rule or an audit attribute. The primary set covers module, start month, highest education, previous attempts, credits studied, registration lead, banked results, the click, activity and task measures and the mean CMA mark. Of these 20, the mean CMA mark is prepared but set aside, because marks known by the cut-off exist for only 1.4% of training rows at day 13 and 5.2% at day 27, below the 10% coverage required for a predictor. The final primary set therefore holds 19 usable predictors, which become 23 parameters once module and start month are coded (Section 8.1). Raw clicks are the declared primary measure, and the de-duplicated twin is a sensitivity variant that may be chosen only on the 2013 folds, before any 2014 evaluation; the duplicate share differs between the years, 6.82% of rows in 2013 against 7.87% in 2014, which makes this rule necessary. Only the columns of the declared predictor list may enter a model: identifier, split, evaluation, target, rule and audit columns never do.

**Encoding.** The prepared views keep original scales and labels, so the views show recorded values only. Milestone 3 also wrote model-ready matrices for linear models, with ordinal codes and a missing indicator for ordered categories, one-hot levels for nominal ones, and counts transformed by the logarithm of one plus the count, median-filled and standardised, all learned from the 2013 training rows. The final modeling protocol applies the same rule more strictly: every transform that learns a parameter is refitted inside each development fold and once on all 2013 runs before the test, and module terms are deviation-coded so that a module unseen in training receives the average effect (Section 9.1). The model-ready matrices therefore remain the reference encoding and the evidence that no test row informs a parameter, while models read the feature views and fit their own transforms. Tree models read the predictors untransformed. The AQ2 analysis reads the day-27 feature view of 2013 directly (Section 8.1).

**Leakage controls.** Leakage is the use of information about the target that would not be available at the moment of prediction, and it makes a model look better in evaluation than it can be in use. Table 7.3 matches each form of leakage named for education data to its case in OULAD and to the control applied.

**Table 7.3. Leakage risks and controls**

| Form | Case in OULAD | Control | Check |
| :---- | :---- | :---- | :---- |
| Target leakage | Final result, withdrawal day, activity or submissions after the cut-off, TMA marks, whole-run measures | Features built only from events dated up to the cut-off; CMA marks only, seven days after submission; target and whole-run measures outside the predictor lists | Features recomputed by separate code (V11); recount without the date filter (V13); column roles (V14) |
| Train–test contamination | Medians, scales and category levels computed on all runs | Learned from the 2013 runs only; refitted inside each fold | Parameters unchanged when test rows are altered (V12) |
| Student leakage | 1,962 of all enrolments in the 2014 runs belong to students who also enrolled in 2013, 1,586 of them registered at day 27 | Kept in the main test and flagged for a strict check; tuning folds keep each student on one side | Flags recomputed (V15) |
| Temporal leakage | A random split mixing the two years; tuning on 2014 | Training on the 9 runs of 2013, test on the 13 runs of 2014; tuning only inside 2013 | No run in both partitions (V15) |
| Augmentation leakage | None: no synthetic augmentation | – | – |
| Cohort statistic | The activity ratio uses the median of the same run | Only activity up to the cut-off of students enrolled at it; no outcome | Recount without the date filter (V13) |

The date-filter check (V13) is built so that it can fail: recounting the click features without any date filter changes them only for the enrolments that clicked after the cut-off, 26,755 at day 13 and 25,663 at day 27, which shows that the filter removes exactly the later clicks and nothing else.

**Split.** The data are split by year, following the OU practice of building at-risk models on previous runs of a module and applying them to the run in progress: the 9 runs of 2013 form the development data and the 13 runs of 2014 the test set. Of the 13 test runs, the 9 paired runs, BBB, DDD and FFF of February and AAA, BBB, DDD, EEE, FFF and GGG of October, test the claim directly, and the 4 unpaired runs, CCC of February and October, EEE of February and GGG of February, test transfer to a module or start month not seen in training and are reported apart (Change Log C16, Section 9.1). Tuning uses leave-one-run-out folds inside 2013, and students who also appear in the held-out run are removed from that fold's training data. The 2014 outcomes are not looked at while the data are prepared, nor in the AQ1 and AQ2 analyses (Change Log C14 and C15), and test results are to be reported also without the test enrolments that are Withdrawn without a withdrawal day, 89 at day 13 and 90 at day 27. Section 7.2 describes the prepared dataset these rules produce and how it is checked and rebuilt.
