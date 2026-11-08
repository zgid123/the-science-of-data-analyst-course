## 8.2. Model Readiness Matrix

Table 8.1 gives, for each question, the prepared view, the target or measure, the feature set or dimensions, the
split or time rule and the readiness for Milestone 4.

**Table 8.1. Model Readiness Matrix**

| AQ | Analytics type | Prepared view | Target / measure | Feature set / dimensions | Split / time rule | Readiness |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | enrolment, assessment_due | Completion rate; first missed week | Module, run, start month, year | All runs; day-14 population | Ready |
| AQ2 | Diagnostic | features_d27, enrolment | non_completion | Task, lateness, inactivity and activity signs | Up to day 27 | Ready¹ |
| AQ3 | Predictive | features_d13, features_d27, model_ready | non_completion | 20 primary, 10 extended predictors, weekly clicks; rule as comparison | Train 2013, test 2014 | Ready² |
| AQ4 | Prescriptive | capacity_by_run + AQ3 scores | Gain over base rate; attainable recall | Lists of 3 or 5 per 20; audit by deprivation and disability | Per run, per cut-off | Revise³ |

¹ Association only. ² The day-13 list rests on activity only. ³ The choice of contact is deferred.

The early-sign rule flags 20.2% of enrolled students at day 13 and 28.8% at day 27, while lists of 3 or 5 per 20
students hold 15% or 25%; the rule names more students than a list of 5 per 20 can hold in 7 of 22 runs at day 13 and
10 at day 27, so staff need a ranking of whom to contact first, which is what AQ3 and AQ4 provide. The choice of contact and its effect, comparisons by year of study, mode and attendance, and the
follow-up rate of secondary KPI 2 need the pilot's own records. For AQ1 to AQ3 the entry conditions of Milestone 4
hold: prepared views with traceability, stable definitions, a defined split and leakage control, documented quality
issues, no synthetic evidence and data reproducible from raw [1].
