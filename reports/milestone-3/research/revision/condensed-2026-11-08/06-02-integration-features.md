## 6.2. Integration and Feature Construction

Integration starts from the enrolment table and adds every other table through checked left joins; all 25 joins
kept their input rows. Clicks are summed by enrolment and day, then by week, as the OU itself summarises clicks by week
and content type for early warning [9]. Every feature uses only records dated on or before its cut-off, because a
legitimate model may only build on information from before its target [10] and records updated later without a time
stamp are a common route for leakage [10]. Table 6.1 defines the main derived variables; the data dictionary
(Appendix III) gives all 20 primary and 10 extended predictors.

**Table 6.1. Main derived variables**

| Variable | Formula | Source fields | Window / timing rule |
| :---- | :---- | :---- | :---- |
| non_completion (target) | final_result is Fail or Withdrawn | studentInfo | Run end; never a feature |
| clicks_0c, activity_ratio_run | Clicks from day 0 to the cut-off c; (clicks_0c + 1) ÷ (median clicks_0c of the run's enrolled students + 1) | studentVle | Same run, up to c, no outcome |
| inactive_last7 | No click in days c − 6 to c | studentVle | Seven days ending at c |
| tasks_missed_c | TMA or CMA due by c, after registration, not submitted by c | assessments, studentAssessment | Up to c; banked excluded |
| tma_late_c, cma_late_c | Tasks due by c submitted late but by c | assessments, studentAssessment | Up to c |
| early_sign_rule | A task missed, or a TMA late, or inactive in the last seven days | derived | At c (C10) |

Demographic attributes serve mainly the fairness audit, since earlier OU experiments found that adding them to
activity and assessment data did not significantly improve the prediction of students at risk [9].
