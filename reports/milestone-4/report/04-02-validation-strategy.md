## 4.2. Validation Strategy

**Test on unseen runs.** The cards of Section 4.1 rest on one validation design, drawn in Appendix III (Figure A.2). Testing on data
not used in model development is the core requirement of TRIPOD+AI [21], and the 13 test runs of 2014 share no run with
development. Testing on a later period is in addition a form of external validation [27], and in predicting student
success only an evaluation on a future course gives an honest estimate of how a model will perform in use [23]. The
1,586 test enrolments at day 27 of students already seen in the 2013 development data stay in the test, as they would in use, and are
removed in a sensitivity analysis.


**Development folds.** Development uses only the 9 runs of 2013. Each run forms its own fold, so each model is
validated on a whole run it did not see, because ignoring the group structure of data seriously underestimates
prediction error [28]. Students who also appear in the held-out run are removed from that fold's training data, since
a validation fold must hold only groups that are absent from training [29]. Every step that learns from data, including
the filling of missing values, the scaling and the tuning of the model, is repeated inside each fold, because a tuned
cross-validation score is substantially optimistic [30], and over-fitting the criterion used to select a model can
bias results as much as the differences between algorithms [31].

**When a challenger wins.** Gradient-boosted trees, or the extended set of 10 further predictors with the weekly
clicks, replace the primary choice only with a gain of at least 0.03 in pooled normalised recall, about 89 more non-completers listed over the 9 runs, and a gain in at least 7 of the 9 folds; if the two were equal,
a gain in 7 or more folds would occur by chance with a probability of about 0.09. The margin is fixed now, before any
fold result exists, so that a small, chance improvement cannot change the choice.

**Two freezes and one test.** The protocol follows the two-step freeze proposed for predictive modeling: the
question, splits, metrics and baselines are fixed before training, and the final model is fixed, with access to the
test data recorded, before testing [26]. The chosen model is refitted on all 2013 runs and scored once on the 13 runs
of 2014. Results are also reported apart for the 9 paired runs, whose module and start month also ran in 2013, and for
the 4 unpaired runs.

**Two features of the run structure.** Module CCC has no run in 2013, so module terms are coded as deviations from the
average module, and an unseen module receives the average. Presentations coded B start in February and those coded J
in October [2]. The 2013 J runs start in October 2013 and last 261–268 days, ending around mid-2014, whereas the 2014 B
runs start in February 2014 and reach their cut-offs a few weeks later, when the 2013 J outcomes are not yet known; a
labels-available variant therefore also scores the 2014 B runs with a model trained only on the 2013
B runs, the only runs whose outcomes a university would hold at that time.

**The protocol step by step.** Appendix III (Table A.5) lists the eight steps of the protocol in order, with the data
each uses, what happens and why; the paragraphs above describe each of them.

**Uncertainty.** Uncertainty about the gate comes from a paired two-level bootstrap: runs are resampled, then
enrolments within each sampled run, each run's list is formed again from its resampled enrolments, and the difference
between model and rule is computed on the same resample, because treating nested observations as independent inflates
false positives [32]. With only 13 test runs such intervals can be too narrow, so the gate also requires a sign-flip
permutation test on the 13 per-run differences, which asks how often differences as favourable would appear if the sign
of each run's difference were random.

**Sample sizes.** Appendix III (Table A.6) gives the sample sizes behind these choices, computed from the prepared views without
fitting a model; outcome counts come from the 2013 runs only, so the 2014 outcomes stay unseen. The minimum development size follows the three criteria of Riley et al. [14]: expected shrinkage of at least 0.9,
meaning that the fitted effects need to be pulled back by no more than 10% on new data; optimism of at most 0.05 in
Nagelkerke R², a measure of how much of the variation in the outcome the model explains, between the development data
and new data; and the overall risk, the non-completion rate in the development data, estimated within 0.05.

**C14.** AQ2 is replicated on 2014 only after the single test, which is Change Log entry C14: it changes when AQ2 is
estimated on the test runs, not what AQ2 asks, and it protects the independence of the AQ3 test.
