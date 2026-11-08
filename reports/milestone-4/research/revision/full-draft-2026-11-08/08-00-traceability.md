# 8. Updated Traceability Matrix

**The matrix of the brief.** Parts 1 to 7 give each question one chain from the Business Goal to the decision it
supports. Table 8.1 gives that chain in the columns that the brief sets for the end of Milestone 4 [1]: the analytics
level, the technical task, the baseline, the primary approach, the primary metric, the validation and the decision
supported.

**Table 8.1. Updated Traceability Matrix**

| AQ | Analytics level | Technical task | Baseline | Primary approach | Primary metric | Validation | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Aggregation | Pooled rate; second denominator | Grouped rates with 95% intervals | Rate with interval and denominator | Two aggregation paths; known totals | D2, D3 |
| AQ2 | Diagnostic | Association within module run | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Risk difference with interval | 2013 runs; replication on 2014 after the AQ3 test | D2; signs for D1 |
| AQ3 | Predictive | Binary classification at day 13 and day 27 | Rule-ranked list; background-only model; random list | Penalised logistic regression | Normalised recall at capacity | Leave-one-run-out on 2013; single test on 2014 | D1 |
| AQ4 | Prescriptive (ranking) | Ranking under capacity | Random and rule-ranked lists | Top-k per run with reasons | Normalised recall at capacity | As AQ3; confirmatory fairness check | D1; contact deferred |

**The full chain.** Table 8.2 extends the traceability of Milestone 3 to the modeling and evaluation choices, so that
each row runs from the Business Goal and its KPI, through the question, its level and task, to the prepared data, the
baseline and primary approach, the primary metric, the validation and the decision supported. The Business Goal is to
improve successful course completion by identifying students who stop taking part early enough to support them within
the semester, and the primary KPI is the completion rate of students enrolled after the add-drop period.

**Table 8.2. Full traceability from goal to decision**

| AQ | KPI | Level | Technical task | Prepared data | Baseline | Primary approach | Primary metric | Validation | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Primary KPI | Descriptive | Aggregation and rate comparison | enrolment, assessment_due; population enrolled at day 14 | Pooled rate; second denominator | Grouped rates with 95% intervals; first missed week by outcome | Non-completion rate with interval | Two aggregation paths agree; known totals | D2, D3 |
| AQ2 | Primary KPI; secondary KPI 1 | Diagnostic | Association within module run | features_d27, enrolment; 2013 runs, then 2014 | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Risk difference with interval (odds ratio beside it) | Sensitivity runs; 2014 replication after the AQ3 test | D2; reasons on D1 |
| AQ3 | Secondary KPI 1 | Predictive | Binary classification at day 13 and day 27 | features_d13, features_d27, model_ready; 19 primary predictors | Rule-ranked list; background-only model; random list | Penalised logistic regression; boosted trees only by the pre-set margin | Normalised recall at capacity (day 27, 5 per 20) | Leave-one-run-out in 2013; single test on 2014 | D1 |
| AQ4 | Secondary KPIs 1 and 2 | Prescriptive (ranking) | Ranking under capacity | AQ3 scores; capacity_by_run | Random list; rule-ranked list | Top-k per run from AQ3 scores with reasons | Normalised recall at capacity | As AQ3; audit by deprivation band and disability | D1; contact deferred |

**The change of this milestone.** Table 8.3 gives Change Log entry C14 in the format of the Controlled Change Log.

**Table 8.3. Controlled Change Log entry C14**

| ID | Milestone | Before | After | Reason | Effect |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C14 | 4 | AQ2 associations estimated on all 22 runs | AQ2 estimated on the 9 runs of 2013; replicated on the 13 runs of 2014 only after the AQ3 model is frozen and scored | Looking at 2014 outcomes while choosing AQ3 predictors would leak test information into the model [39] | AQ2 results on 2014 are a replication; AQ3's test stays independent |

Every question keeps its link to the Business Goal and to the prepared views of Milestone 3, and the only change to how
a question is measured, C14, protects the independence of the AQ3 test.
