# 8. Updated Traceability Matrix

Parts 1 to 7 give each question one chain from the Business Goal to the decision it supports. Table 8.1 gives it in the columns the brief sets
for the end of Milestone 4 [1]; Appendix VIII (Tables A.21–A.22) adds the KPI and prepared data of each row and
the Change Log entry C14.

**Table 8.1. Updated Traceability Matrix**

| AQ | Analytics level | Technical task | Baseline | Primary approach | Primary metric | Validation | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Aggregation | Pooled rate; second denominator | Grouped rates with 95% intervals | Rate with interval and denominator | Two aggregation paths; known totals | D2, D3 |
| AQ2 | Diagnostic | Association within module run | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Risk difference with interval | 2013 runs; replication on 2014 after the AQ3 test | D2; signs for D1 |
| AQ3 | Predictive | Binary classification at day 13 and day 27 | Rule-ranked list; background-only model; random list | Penalised logistic regression | Normalised recall at capacity | Leave-one-run-out on 2013; single test on 2014 | D1 |
| AQ4 | Prescriptive (ranking) | Ranking under capacity | Random and rule-ranked lists | Top-k per run with reasons | Normalised recall at capacity | As AQ3; confirmatory fairness check | D1; contact deferred |

Every question keeps its link to the Business Goal and to the prepared views of Milestone 3, and the only change to
how a question is measured, Change Log entry C14, protects the independence of the AQ3 test.
