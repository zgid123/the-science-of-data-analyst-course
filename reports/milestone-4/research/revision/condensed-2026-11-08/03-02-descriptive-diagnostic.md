## 3.2. Descriptive and Diagnostic Questions

Following the matrix of Section 3.1, AQ1 and AQ2 describe completed runs and make no forecast, so they are answered
by descriptive statistics and an association model rather than machine learning [1], [3]. AQ1 is answered by
rates and outcome shares per module, run, start month and year, each with its denominator and a 95% confidence
interval, and by the week of the first missed task by outcome; its baseline is the pooled rate together with a second denominator, all 32,593 enrolments instead of the 28,061 still registered at day 14, which exposes rates that depend on the denominator.

AQ2 asks how much more often students with a sign by day 27 fail to complete than comparable students without it.
Its baseline is the unadjusted rate difference for each sign. Its primary approach is a logistic regression of
non-completion on the signs with fixed effects for each module run, previous attempts and credits studied, plus
sign × module terms that give a module-specific difference. Fixed effects suit a design in which every run of the
studied modules is observed, and whether to cluster standard errors follows from how the data were sampled [12]; a
mixed-effects model is set aside, because 6 modules and 9 training runs are few for estimating a variance. The effect
reported is the average risk difference in percentage points, with odds ratios beside it, because odds
ratios read larger than risk ratios when 44–46% of students do not complete, and a p-value does not measure the size
or importance of an effect [13]. Mutually adjusted estimates are partial effects of signs that are correlated with
each other, so they are shown beside the unadjusted differences rather than read as each sign's own weight. AQ2 is
estimated on the 9 runs of 2013 and replicated on 2014 only after the AQ3 test (Change Log entry C14, Appendix VIII), so that no test outcome
influences the predictive model.
