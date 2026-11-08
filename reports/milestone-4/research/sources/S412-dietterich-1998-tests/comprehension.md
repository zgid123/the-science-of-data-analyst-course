# S412 – Approximate statistical tests for comparing supervised classification learning algorithms (Dietterich, Neural Computation 1998)

## Summary in my own words

Dietterich compares five tests for deciding whether one learning algorithm beats another on a task, measuring their type I error by simulation. The difference-of-proportions test and the resampled paired t test (many random train/test splits) have high type I error and should never be used; the 10-fold cross-validated paired t test is somewhat elevated. McNemar's test on a single held-out test set has low type I error and is the only acceptable choice when the algorithms can be run only once; the new 5x2cv test is recommended when they can be run ten times. McNemar's test does not capture variation due to the choice of training set, so it answers a question about the two trained classifiers on that test set.

## Key facts

- Bad tests – "Two widely used statistical tests are shown to have high probability of type I error in certain situations and should never be used: a test for difference of two proportions and a paired-differences t test based on taking several random train-test splits."
- 10-fold t test – "A third test, a paired-differences t test based on 10-fold cross-validation, exhibits somewhat elevated probability of type I error."
- McNemar – "A fourth test, McNemar's test, is shown to have low type I error."
- Single run – "For algorithms that can be executed only once, McNemar's test is the only test with acceptable type I error."
- 5x2cv – "For algorithms that can be executed 10 times, the 5 x 2 cv test is recommended, because it is slightly more powerful and because it directly measures variation due to the choice of training set."
- Choice depends on cost – "The choice of the best test is determined by the computational cost of running the learning algorithm."

## Used in

04-03-metrics-success.md

## Against reference.md

Extends the outline's metrics bullet "comparison with the rule, uncertainty": on a single frozen test set (the 2014 runs) a paired comparison on the same students (McNemar for flagged/not flagged decisions) is the classical choice; the paper's tests assume independent examples and do not handle students clustered in module runs or tutor groups, so a cluster-level (run-level) bootstrap is a condition the report must add. No contradiction.

## Reliability

Primary; peer-reviewed article by Dietterich T.G. (Oregon State University); Neural Computation 10(7):1895–1923 (1998). The author-hosted PDF converts with broken ligatures (partial), so quotes come from the abstract in the Crossref record (fetch block 2). Citation traction: 3050 Crossref / 3889 OpenAlex citations as of 2026-11-06. Classic reference, still current as of November 2026.

## Open questions

The body text is garbled in conversion; details of the McNemar computation and its assumptions are not quoted. No fetched source covers the cluster (run-level) bootstrap directly – a gap for the comparison-with-uncertainty question.
