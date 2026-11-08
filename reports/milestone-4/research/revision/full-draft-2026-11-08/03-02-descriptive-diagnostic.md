## 3.2. Descriptive and Diagnostic Questions

**No machine learning.** Following the matrix of Section 3.1, AQ1 and AQ2 describe runs that have ended and make no
forecast, so they are answered with descriptive statistics and an association model rather than machine learning,
as the brief advises when simple statistics answer the question [1], [3].

**AQ1.** AQ1 is answered by completion and non-completion rates and outcome shares per module, run, start month and
year, each with its denominator and a 95% confidence interval, and by the week in which each enrolment first misses an
assessed task, compared by outcome. Its baseline is the pooled rate over all runs, together with a second denominator:
all 32,593 enrolments instead of the 28,061 still registered at day 14. Comparing the two denominators shows which
rates depend on how the population is defined, which is the main way a descriptive rate can mislead.

**AQ2: the question.** AQ2 asks how much more often students with a sign by day 27 fail to complete than comparable
students without it. Its baseline is the unadjusted rate difference for each sign: the non-completion rate of students
with the sign minus that of students without it. Its primary approach is a logistic regression of non-completion on
the signs, with a fixed effect for each module run, which compares students only within the same run, adjustment for
previous attempts and credits studied, and sign × module terms, which let the size of a sign's association differ by
module.

**AQ2: why this model.** Fixed effects suit a design in which every run of the studied modules is observed, and
whether to cluster standard errors follows from how the data were sampled, not from the grouping alone [12]. A
mixed-effects model, which treats modules as a sample from a larger population, is set aside, because 6 modules and 9
training runs are too few to estimate the variance between them. The effect is reported as the average risk
difference in percentage points, with odds ratios beside it. Odds ratios read larger than risk ratios when an outcome
is common, and 44–46% of students do not complete; a p-value, in turn, does not measure the size or importance of an
effect [13]. The signs are correlated with each other, so their mutually adjusted estimates are partial effects; they
are shown beside the unadjusted differences rather than read as each sign's own weight.

**AQ2: the data it uses.** AQ2 is estimated on the 9 runs of 2013 and replicated on the 13 runs of 2014 only after the
AQ3 test (C14), so that no test outcome is seen while the predictive model is chosen. Table 3.2 compares the AQ2
candidates against the eight criteria.

**Table 3.2. AQ2 candidates against the eight criteria**

| Criterion | Baseline: unadjusted rate difference per sign | Candidate 1: logistic regression with run fixed effects and sign × module terms (primary) | Candidate 2: mixed-effects logistic regression | Candidate 3: shallow classification tree (supplement) |
| :---- | :---- | :---- | :---- | :---- |
| Fit to question | Unadjusted rate difference per sign and module | Pooled within-run risk difference per sign, and module-specific differences from the interaction terms | Same, with module effects drawn from a population of modules | Shows which combinations of signs separate outcomes |
| Fit to data | 9 runs, 6 modules | Smallest run 369 enrolments and 91 non-completers; task signs only in runs with a task due by day 27 | 6 modules and 9 runs are few for estimating a variance | Many rows, but the splits change between samples |
| Assumptions | None beyond counting | Additive log-odds within module; all runs of these modules observed, so fixed effects suit the design [12] | Normal random effects; inference to unseen modules | None parametric; unstable splits |
| Interpretability | Highest | Risk differences in percentage points, with odds ratios beside them | Similar, plus variance terms | High for a depth of 2–3 |
| Complexity vs baseline | – | One model per cut-off with a few interaction terms | Adds a variance component for little gain within the observed modules | Low, but adds no effect size |
| Robustness and reproducibility | Exact | Deterministic; robust standard errors; sensitivity runs; signs correlated with each other checked | Convergence and few-cluster issues | Unstable across samples |
| Ethics and fairness | No sensitive attribute used | Sensitive attributes not used as signs | Same | Same |
| Actionability | Gives tutors the size of each sign's gap | Tells D2 which signs to look at; shown beside the unadjusted gap, because mutually adjusted estimates are partial effects | No extra action | Gives readable rules for tutors |
