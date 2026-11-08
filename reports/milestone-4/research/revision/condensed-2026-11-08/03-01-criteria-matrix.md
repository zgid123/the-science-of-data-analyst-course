## 3.1. Selection Criteria and Candidate Solution Matrix

Each candidate is judged on the brief's eight criteria: fit to the question, fit to the data, assumptions,
interpretability, complexity against the baseline, robustness and reproducibility, ethics and fairness, and
actionability [1]. Four findings on prediction systems settle most ties between candidates: a simple heuristic often delivers
much of the gain, so predictive questions start from a rule baseline and a simple first model [6]; when many models
reach about the same error, the simpler one can be chosen without loss [5]; complexity is costly to maintain [10];
and for high-stakes decisions about people an inherently interpretable model is preferable to a black box explained
afterwards [11].

Table 3.1 is the Candidate Solution Matrix. The comparison of every candidate against the eight criteria is in
Appendix II (Tables A.5–A.7).

**Table 3.1. Candidate Solution Matrix**

| AQ | Technical task | Baseline | Candidate 1 | Candidate 2 | Primary approach | Short rationale |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Aggregation | Pooled rate; second denominator | Grouped rates with 95% intervals | – | Grouped rates with intervals | Descriptive question; no model needed |
| AQ2 | Association within module run | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Mixed-effects logistic regression; shallow tree as supplement | Candidate 1 | All runs of the modules observed; effect sizes within module; no causal claim |
| AQ3 | Binary classification at day 13 and day 27 | Early-sign rule ranked by signs; background-only logistic model; random list | Penalised logistic regression | Gradient-boosted trees; discrete-time survival as extension | Candidate 1, unless Candidate 2 wins by a margin fixed in advance | Interpretable reasons for tutors; ample events per parameter; transfer to a later run |
| AQ4 | Ranking under capacity | Random list; rule-ranked list | Top-k per run from AQ3 scores | Risk tiers from capacity | Candidate 1 with reasons | Fixed capacity; no contact data, so no benefit ranking |
