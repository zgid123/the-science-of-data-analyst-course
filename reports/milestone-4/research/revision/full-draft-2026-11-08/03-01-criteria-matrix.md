## 3.1. Selection Criteria and Candidate Solution Matrix

**Criteria.** Each candidate is judged on the eight criteria that the brief makes compulsory [1]: fit to the
question, whether the method directly produces the output the question needs; fit to the data, whether sample size,
feature types, sparsity, imbalance, time structure and granularity suit it; assumptions, what the method requires of
the data and whether the data roughly meet it; interpretability, how much of the logic the users need to understand;
complexity against the baseline, what a more complex method is expected to add; robustness and reproducibility,
whether the method can be evaluated stably, rerun and kept free of leakage; ethics and fairness, whether its errors
could harm a group of students and whether it uses a sensitive attribute; and actionability, whether its output
supports the decision named in Milestone 1.

**Findings that settle ties.** Four findings on prediction systems settle most ties between candidates. A simple
heuristic often delivers much of the gain, so predictive work should start from a rule baseline and a simple first
model [6]. When many models reach about the same error, the simpler one can be chosen without loss [5]. Complexity is
costly to maintain over time [10]. And for high-stakes decisions about people, an inherently interpretable model is
preferable to a black box explained afterwards [11].

**The matrix.** Table 3.1 is the Candidate Solution Matrix of the brief: for each question, its technical task, its
baseline, its candidate families, the primary approach chosen and a short rationale. Sections 3.2 to 3.4 give the
reasoning behind each row.

**Table 3.1. Candidate Solution Matrix**

| AQ | Technical task | Baseline | Candidate 1 | Candidate 2 | Primary approach | Short rationale |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Aggregation | Pooled rate; second denominator | Grouped rates with 95% intervals | – | Grouped rates with intervals | Descriptive question; no model needed |
| AQ2 | Association within module run | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Mixed-effects logistic regression; shallow tree as supplement | Candidate 1 | All runs of the modules observed; effect sizes within module; no causal claim |
| AQ3 | Binary classification at day 13 and day 27 | Early-sign rule ranked by signs; background-only logistic model; random list | Penalised logistic regression | Gradient-boosted trees; discrete-time survival as extension | Candidate 1, unless Candidate 2 wins by a margin fixed in advance | Interpretable reasons for tutors; ample events per parameter; transfer to a later run |
| AQ4 | Ranking under capacity | Random list; rule-ranked list | Top-k per run from AQ3 scores | Risk tiers from capacity | Candidate 1 with reasons | Fixed capacity; no contact data, so no benefit ranking |
