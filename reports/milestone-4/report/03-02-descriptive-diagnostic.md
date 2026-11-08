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
whether to cluster standard errors follows from how the data were sampled, not from the grouping alone [12]; since
every run is observed rather than sampled, the model uses robust standard errors without clustering. A
mixed-effects model, which treats modules as a sample from a larger population, is set aside, because 6 modules and 9
training runs are too few to estimate the variance between them. The effect is reported as the average risk
difference in percentage points, with odds ratios beside it. Odds ratios read larger than risk ratios when an outcome
is common, and 44–46% of students do not complete; a p-value, in turn, does not measure the size or importance of an
effect [13]. The signs are correlated with each other, so their mutually adjusted estimates are partial effects: each shows the gap linked to one sign when the other signs
are held equal, which is smaller than the gap the sign shows on its own and is not the share of non-completion that the
sign explains. Both are therefore shown side by side. On the remaining criteria,
the model assumes that signs add up on the log-odds scale within a module, which the sign × module terms relax; it fits
the data, since even the smallest training run holds 369 enrolments with 91 non-completers; it is deterministic, giving the same result on
every rerun, and is checked with robust standard errors and sensitivity runs; and it uses no sensitive attribute as a sign.

**AQ2: the data it uses.** AQ2 is estimated on the 9 runs of 2013 and replicated on the 13 runs of 2014 only after the
AQ3 test (C14), so that no test outcome is seen while the predictive model is chosen. Appendix I (Table A.1) compares the AQ2
candidates cell by cell against the eight criteria.

