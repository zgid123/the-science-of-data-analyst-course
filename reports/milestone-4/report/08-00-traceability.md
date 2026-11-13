# 8. Updated Traceability Matrix

**The matrix of the brief.** Parts 1 to 7 give each question one chain from the Business Goal to the decision it
supports. Table 8.1 gives that chain in the columns that the brief sets for the end of Milestone 4 [1]: the analytics
level, the technical task, the baseline, the primary approach, the primary metric, the validation and the decision supported. The prepared data behind each row are the views of Milestone 3: the
enrolment and task views for AQ1, the day-27 feature view for AQ2, and both feature views with their model-ready
matrices for AQ3 and AQ4.

**Table 8.1. Updated Traceability Matrix**

| AQ | Analytics level | Technical task | Baseline | Primary approach | Primary metric | Validation | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Aggregation | Pooled rate; second denominator | Grouped rates with 95% intervals | Rate with interval and denominator | Two aggregation paths; known totals | D2, D3 |
| AQ2 | Diagnostic | Association within module run | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Risk difference with interval | 2013 runs; replication on 2014 after the AQ3 test | D2; signs for D1 |
| AQ3 | Predictive | Binary classification at day 13 and day 27 | Rule-ranked list; background-only model; random list | Penalised logistic regression on the primary predictors, unless gradient-boosted trees or the extended set win by the fixed margin | Normalised recall at capacity | Leave-one-run-out on 2013; single test on 2014 | D1 |
| AQ4 | Prescriptive (ranking) | Ranking under capacity | Random and rule-ranked lists | Top-k per run with reasons | Normalised recall at capacity | As AQ3; confirmatory fairness check | D1; choice of contact deferred |

**The full chain.** Every row serves the Business Goal of improving successful course completion by identifying
students who stop taking part early enough to support them within the semester, measured by the primary KPI, the
completion rate of students enrolled after the add-drop period. Appendix VII gives the full chain from that goal and its
KPIs to the decision supported (Table A.22) and Change Log entry C14 (Table A.23).

Every question keeps its link to the Business Goal and to the prepared views of Milestone 3, and the only change to how
a question is measured, C14, protects the independence of the AQ3 test.
