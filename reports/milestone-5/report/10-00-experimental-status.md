# 10. Experimental Implementation and Results

The project completed Level 1, the compulsory level: the modeling strategy of Section 8 and the evaluation design of
Section 9. It also ran the optional Level 2 prototype for AQ3 and AQ4: the protocol that Milestone 4 fixed (Appendix
X), implemented in Python with polars, scikit-learn and statsmodels as steps 19 to 23 of the final package. The models
were developed on the 9 runs of 2013 with leave-one-run-out folds, frozen with a hash of every fitted model, and
tested once on the 13 runs of 2014 (15,724 enrolments registered at day 27, 6,911 of them non-completers). The plan
named no measure for tuning the penalty, so the inner folds minimise log loss, a choice made after the tuning results
of both measures were known (C18). The AQ1 and AQ2 analyses of
Section 11 are descriptive and diagnostic analyses, not this prototype: they train no predictive model.

**Model choice.** In development no challenger met the margin fixed in advance: gradient-boosted trees and the
extended predictor set changed pooled normalised recall by −0.001 to −0.002 against the penalised logistic model, so
the primary approach of Level 1 stays. Table 10.1 gives every list on the test runs at the main operating point.

**Table 10.1. Lists of 5 per 20 students at day 27 on the 13 test runs of 2014**

| List | Non-completers listed | Share of all non-completers | Share of list not completing |
| :---- | :---- | :---- | :---- |
| Penalised logistic model (primary) | 2,868 | 41.5% | 72.5% |
| Early-sign rule, ranked (B2) | 2,786 | 40.3% | 70.4% |
| Background-only model (B3) | 2,244 | 32.5% | 56.7% |
| Random list (expected) | 1,738 | 25.1% | 43.9% |

**Gate S1 is met.** The model's pooled normalised recall is 0.725 against 0.704 for the rule-ranked list, a gain of
+0.021 (paired bootstrap interval +0.006 to +0.036, sign-flip p = 0.0035), and the model is ahead in 11 of 13 runs.
The gain is real and small: 82 more non-completers on 3,955 list places, so the rule alone delivers 97% of the
model's hits, as Level 1 expected a baseline might. Every sensitivity view keeps the same direction (Table A.37).

**Calibration and errors.** The pooled risks meet condition S3 (calibration-in-the-large 0.117, slope 0.886), but
only 5 of the 13 runs meet it on their own, so tutors see ranks and reasons, not probabilities. The error analysis
finds one blind spot: 4,193 of the 6,911 non-completers (60.7%) still had normal activity at day 27, and the lists
hold 19.1% of them; a list built at week 4 mostly confirms disengagement that has already begun. No fairness group is
flagged by rule FR1 (Section 11.4).

**Against the Level 1 expectation.** The prototype supports every Level 1 choice: the primary model, the baselines and
the single gate. Two qualifications follow: probabilities stay hidden, and the gain over the rule is small enough
that the rule is a sound fallback. An independent implementation of the same protocol, our Milestone 4 draft,
reached the same verdicts, with counts of listed non-completers differing by at most 4. The 2014 runs had been described for AQ1 and AQ2 before this
test (C15); because the predictors, candidates, choice rule and gate stayed as Milestone 4 fixed them on 2013, the
test confirms a fixed design rather than giving a first look. The package reruns every step from the published data
with one seed, and its result files are checked byte for byte.
