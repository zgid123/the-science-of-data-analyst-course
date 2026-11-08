## 6.2. Integration and Feature Construction

**Integration.** Integration starts from the enrolment table, which holds one row for each of the 32,593 enrolments,
and adds every other table through left joins after summing it to the enrolment, so that no enrolment is lost and no
row is multiplied. Each join is checked: the pipeline asserts that the number of rows after the join equals the
number before it, and all 25 joins kept their input rows. Clicks are summed by enrolment and day, then by week, as
the OU itself summarises clicks by week and by type of content for its early-warning work [9].

**Timing rule.** Every feature uses only records dated on or before its cut-off. A legitimate model may only build on
information that existed before its target was known, and records that are updated later without a time stamp are a
common route for information from the future to reach a model [10]. Activity before day 0 is kept as its own window,
because it is known before teaching starts. Features that need a mark use only CMA marks, for submissions made at
least seven days before the cut-off, since a CMA score is expected within seven days [3] while a TMA mark has no
release day in the data.

**Derived variables.** Table 6.1 defines the main derived variables with their formula, source fields and timing rule;
c stands for the cut-off day, 13 or 27.

**Table 6.1. Main derived variables**

| Variable | Formula | Source fields | Window / timing rule |
| :---- | :---- | :---- | :---- |
| non_completion (target) | final_result is Fail or Withdrawn | studentInfo | Observed at the run end; never a feature |
| enrolled_d13, enrolled_d14, enrolled_d27 | Registered by day d, or registration day unknown, and not unregistered by day d | studentRegistration | Day d (C09) |
| clicks_pre | Clicks before day 0 | studentVle | Before the start |
| clicks_0c, active_days_0c | Clicks, and days with at least one click, from day 0 to c | studentVle | Days 0 to c |
| activity_ratio_run | (clicks_0c + 1) ÷ (median clicks_0c of the run's enrolled students + 1) | studentVle | Same run, days 0 to c; no outcome used |
| inactive_last7 | No click on days c − 6 to c | studentVle | Seven days ending at c |
| tasks_missed_c | TMA or CMA due by c, due on or after the registration day, not submitted by c | assessments, studentAssessment | Submissions up to c; banked results excluded |
| tma_late_c, cma_late_c | Tasks due by c submitted after the due day but by c, by type | assessments, studentAssessment | Submissions up to c |
| cma_score_mean_c | Mean score of CMAs submitted by c − 7; empty if none | studentAssessment | Marks known by c |
| early_sign_rule | A task missed, or a TMA late, or inactive in the last seven days | derived | At c (C10) |
| early_sign_rule_cma | early_sign_rule, or a CMA late | derived | At c; sensitivity variant |
| first_missed_week | Week of the earliest task not submitted that fell due while the student was enrolled | assessment_due view | Whole run (AQ1 only) |

Two of these definitions carry a choice. A task counts as missed only if it fell due on or after the student's
registration day, because a student who registers late cannot have missed a task that fell due before they joined.
The activity ratio compares a student with the median of the same run up to the same day, which stands for the "course
average" of the AQ2 sign; it adds one to both counts so that a run or a student with no clicks gives a defined value,
and it uses no outcome, so staff could compute it on the day of the cut-off.

**Predictor sets.** The feature views hold 20 primary predictors and 10 extended predictors, plus the weekly click
counts up to the cut-off, two at day 13 and four at day 27; every other column is an identifier, the target, a flag
for evaluation, the rule or an audit attribute. The primary set covers the module and start month, prior education,
previous attempts, study load, how early the student registered, banked results, activity before and after the start,
the activity ratio, inactivity, and the task counts and lateness. The extended set adds the de-duplicated clicks, the
days since the last click, the trend over the last week, tasks submitted early and clicks by resource type, for
comparison in Milestone 4. The CMA score falls below the coverage that a predictor needs, as Section 7.3 explains.
Demographic attributes serve mainly the fairness audit, because earlier experiments at the OU found that adding them
to activity and assessment data did not significantly improve the prediction of students at risk [9]; the data
dictionary (Appendix III) gives every prepared column with its role.
