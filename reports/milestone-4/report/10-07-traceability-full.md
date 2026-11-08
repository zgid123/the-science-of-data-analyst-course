## Appendix VII – Full Traceability and Change Log

Table A.12 extends the traceability of Milestone 3 to the modeling and evaluation choices: each row runs from the
Business Goal and its KPI through the question, its analytics level and technical task to the prepared data, the
baseline and primary approach, the primary metric, the validation and the decision supported. The Business Goal is to
improve successful course completion by identifying students who stop taking part early enough to support them within
the semester; the primary KPI is the completion rate of students enrolled after the add-drop period.

**Table A.12. Full traceability from goal to decision**

| AQ | KPI | Level | Technical task | Prepared data | Baseline | Primary approach | Primary metric | Validation | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Primary KPI | Descriptive | Aggregation and rate comparison | enrolment and assessed-task views (enrolment, assessment_due); population enrolled at day 14 | Pooled rate; second denominator | Grouped rates with 95% intervals; first missed week by outcome | Non-completion rate with interval | Two aggregation paths agree; known totals | D2, D3 |
| AQ2 | Primary KPI; secondary KPI 1 | Diagnostic | Association within module run | features_d27, enrolment; 2013 runs, then 2014 | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Risk difference with interval (odds ratio beside it) | Sensitivity runs; 2014 replication after the AQ3 test | D2; reasons on D1 |
| AQ3 | Secondary KPI 1 | Predictive | Binary classification at day 13 and day 27 | the two feature views (features_d13, features_d27) and the model-ready matrix (model_ready); 19 primary predictors | Rule-ranked list; background-only model; random list | Penalised logistic regression; boosted trees only by the pre-set margin | Normalised recall at capacity (day 27, 5 per 20) | Leave-one-run-out in 2013; single test on 2014 | D1 |
| AQ4 | Secondary KPIs 1 and 2 | Prescriptive (ranking) | Ranking under capacity | AQ3 scores; list lengths by capacity for each run (capacity_by_run) | Random list; rule-ranked list | Top-k per run from AQ3 scores with reasons | Normalised recall at capacity | As AQ3; audit by deprivation band and disability | D1; contact deferred |

Table A.13 records the one change to how a question is measured that the evaluation design introduces; it continues
the Controlled Change Log C01–C13 of Milestones 2 and 3.

**Table A.13. Controlled Change Log entry C14**

| ID | Milestone | Before | After | Reason | Effect |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C14 | 4 | AQ2 associations estimated on all 22 runs | AQ2 estimated on the 9 runs of 2013; replicated on the 13 runs of 2014 only after the AQ3 model is frozen and scored | Looking at 2014 outcomes while choosing AQ3 predictors would leak test information into the model [40] | AQ2 results on 2014 are a replication; AQ3's test stays independent |
