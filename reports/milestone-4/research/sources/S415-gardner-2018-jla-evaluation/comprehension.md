# S415 – Evaluating predictive models of student success: Closing the methodological gap (Gardner & Brooks, Journal of Learning Analytics 2018)

## Summary in my own words

The paper surveys how learning analytics papers evaluate predictive models and finds that most use only the naïve average of performance or statistical tests unsuited to predictive models, while comparing many models without accounting for multiple comparisons and often without reporting hyperparameter tuning. It reviews null hypothesis significance testing (corrected t-tests, Friedman with Nemenyi post-hoc) and argues for Bayesian model evaluation (a hierarchical correlated t-test with a region of practical equivalence) that separates magnitude, uncertainty and sample size. On 96 dropout models over 48 MOOC sessions, the naïve best model beat the next one by less than 0.003 AUC, a difference the authors call small enough to be spurious or practically useless; the Bayesian method returned a family of practically equivalent best models instead of a single winner.

## Key facts

- Practice – "which overwhelmingly uses only naïve methods for model evaluation or statistical tests which are not appropriate for predictive model evaluation."
- Many comparisons – "Fewer than 20% of the works surveyed compare one or two models; the remainder compared more than two models"
- Tuning unreported (author-reported) – "in 20 out of 87 (23%) of the works surveyed, methods for hyperparameter tuning or selection were not reported or even mentioned"
- Naïve gap – "The difference in average AUC between"
- Spurious – "This difference is indeed small enough to be spurious, practically useless, or both."
- Separate magnitude and uncertainty – "The effects of the magnitude of observed differences, the uncertainty of estimates, and the number of data points should be separable in model evaluation."
- Bayesian case – "Together, these criteria collectively mount a strong imperative in favor of Bayesian model evaluation."
- Friedman and Nemenyi, after Demšar J. (JMLR 2006) – "The Friedman test, in particular, has gained increasing adoption across the field of machine learning for model evaluation"
- Bayesian hierarchical correlated t-test of Corani G. et al. (Machine Learning 2017) – "In the current work, we consider the Bayesian hierarchical correlated"

## Used in

04-03-metrics-success.md

## Against reference.md

Extends the outline's "comparison with the rule, uncertainty": a model should only be preferred over the rule or another model when the difference exceeds a pre-stated margin of practical equivalence and its uncertainty; small average gains are not evidence. The Bayesian machinery suits many-dataset comparisons; with one test year the report can apply the same logic through a pre-stated minimum gain and a confidence interval. No contradiction.

## Reliability

Primary; peer-reviewed article by Gardner J. and Brooks C. (University of Michigan); Journal of Learning Analytics 5(2):105–125 (2018), doi:10.18608/jla.2018.52.7; arXiv:1801.08494 (revised June 2018). Citation traction: 14 Crossref / 21 OpenAlex citations as of 2026-11-06 (low, so it supports the argument together with S414 and S409 rather than alone). Current as of November 2026.

## Open questions

The crawl's mathematical notation contains zero-width characters; quotes avoid formula text. The size of the region of practical equivalence the authors used was not extracted.
