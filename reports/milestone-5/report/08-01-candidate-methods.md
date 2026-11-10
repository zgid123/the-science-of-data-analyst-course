## 8.1. Baselines, Candidate Methods and Primary Proposal

Each candidate is judged on the eight criteria of the course, from fit to the question and the data to fairness and
actionability, and ties go to the simpler and more interpretable method, because a simple heuristic often delivers much
of the gain and decisions about people call for an interpretable model. Table 8.1 is the Model and Method Selection
Matrix, with the reason for each primary proposal in its last column; Appendix VIII argues each choice against the
criteria, question by question.

**Table 8.1. Model and Method Selection Matrix**

| AQ | Analytics type | Technical task | Baseline | Candidate methods | Primary proposal | Rationale |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Aggregation and rate comparison | Pooled rate; rate over all enrolments (second denominator); rate without flagged enrolments | Grouped rates with 95% intervals | Grouped rates with Wilson intervals; cumulative first missed week by outcome; year difference with Newcombe interval | Descriptive question; no model needed; the denominator decides the rate |
| AQ2 | Diagnostic | Association within module run | Unadjusted rate difference per sign | (1) Logistic regression with run fixed effects and sign × module terms; (2) mixed-effects logistic regression, with a shallow tree as supplement | Candidate 1, with robust standard errors; effects as average risk differences, odds ratios beside them | Every run of the modules is observed, so fixed effects suit; 6 modules are too few for a random effect; effect sizes within module; no causal claim |
| AQ3 | Predictive | Binary classification at day 13 and day 27 | Early-sign rule ranked by its number of signs; background-only logistic model; random list | (1) Penalised logistic regression; (2) gradient-boosted trees; discrete-time survival as an extension | Candidate 1 on the 19 primary predictors (23 parameters), unless candidate 2 or the extended set wins by a margin fixed in advance | Interpretable reasons for staff; about 230 non-completers per parameter; classes close in size; transfer to a later run |
| AQ4 | Prescriptive (ranking under capacity) | Ranking under a fixed capacity | Random list; rule-ranked list of the same length | (1) Top-k per run from the AQ3 scores; (2) risk tiers from capacity | Candidate 1, with the signs behind each name | Capacity is fixed; no contact data, so no ranking by expected benefit; a member of staff decides; the list is a decision option, untested |
