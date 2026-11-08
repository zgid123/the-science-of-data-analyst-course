## 4.2. Validation Strategy

The cards of Section 4.1 rest on one validation design, shown in Figure 4.1. Testing on data not used in model development is the core requirement of TRIPOD+AI [21]; the 2014 test runs share no run with development, and the 1,586 test enrolments of students already seen in 2013 are removed in a sensitivity analysis. In addition, testing on a later period is a form of
external validation [25], and in student-success prediction only evaluation on a future course gives the honest
estimate [23].

![Figure 4.1. Validation and test protocol from the first freeze to the single test on the 2014 runs](assets/figures/fig-4-1-validation.png){width=100%}

Development uses only the 9 runs of 2013, each run forming its own fold, because ignoring group structure seriously
underestimates prediction error [26]; students who also appear in the held-out run are removed from that fold's
training data, since validation folds must hold only groups absent from training [27]. Every learned step, tuning included, is repeated inside each fold, because a tuned cross-validation score is substantially optimistic [28] and over-fitting the selection criterion can bias results as much as the differences between algorithms [29]. Gradient-boosted trees, or an extended set of 10 further predictors with the weekly clicks (Appendix I, Table A.3), replace the primary choice only with a gain of at least 0.03 in pooled normalised recall (about 89 more non-completers listed over the 9 runs) and in at least 7 of 9 folds.

The two-step freeze proposed for predictive modeling fixes question, splits, metrics and baselines before training,
and the final model, with test access recorded, before testing [30]; the chosen model is refitted on all 2013 runs and
scored once on the 13 runs of 2014, with results also reported apart for the 9 paired runs, whose module and start month also ran in 2013, and the 4 unpaired runs. Module CCC has no 2013 run, so module terms are coded as deviations from the
average module and an unseen module receives the average. Presentations coded B start in February and J in October
[2], and the 2013 J runs last 261–268 days, so their outcomes are not yet known when the 2014 B runs reach their cut-offs; a labels-available variant therefore scores the 2014 B runs with a model trained only on the 2013 B runs. Appendix IV gives the full protocol and sample sizes (Tables A.13–A.14); AQ2 is replicated
on 2014 only after this test (Change Log entry C14, Appendix VIII).
