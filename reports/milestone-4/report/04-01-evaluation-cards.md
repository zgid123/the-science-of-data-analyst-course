## 4.1. Evaluation Design Cards

**What a card holds.** The brief asks for an Evaluation Design Card for each question with seven items: the primary
and secondary metrics, the validation strategy, the baseline, the error analysis, the fairness or subgroup check and
the success criterion [1]. The metric follows the decision it supports: recall matters when a contact is cheap and
missing a struggling student is costly, precision when a contact is costly [23], and when only a limited number of
top-ranked cases can be acted on, performance among those cases is the practical measure [24].

**Capacity and the main operating point.** The capacity k of a run is 3 or 5 contacts per tutor group, with a group
assumed to hold 20 students, that is 15% or 25% of the enrolments registered at the cut-off. The main operating point
is 5 per 20 at day 27, because it serves the list delivered in week 5 and is close to the share of students the early-sign rule flags at day 27: 28.8% of the 27,535 enrolments registered then
across all 22 runs, a share computed without any outcome. A confusion matrix of listed and unlisted students against
their outcome is reported for each run; at a fixed list length its cells give recall, precision and lift, which
replace the F1 score, because the list length is set by capacity rather than chosen to balance the two kinds of error.

**The evaluation plan.** Table 4.1 gives the Evaluation Plan, the seven items of the card for each question side by side
in short form; Appendix II (Tables A.8–A.11) gives each card in full.

**Table 4.1. Evaluation Plan in summary**

| Item | AQ1 | AQ2 | AQ3 | AQ4 |
| :---- | :---- | :---- | :---- | :---- |
| Primary metric(s) | Non-completion rate and outcome shares with 95% intervals | Average risk difference of each sign within module run, with 95% interval | Normalised recall at capacity, pooled over runs (day 27, k = 5 per 20) | Normalised recall at capacity |
| Secondary metric(s) | Cumulative share of enrolments with a first missed task by week | Unadjusted rate difference; module-specific risk differences; odds ratios | Recall, precision and lift at capacity; ROC-AUC and PR-AUC within run; calibration; Brier score; net benefit as context only [25] | Lift; overlap with the rule list; Fail and Withdrawn on the list; recall at 3 and 5 per 20 |
| Validation strategy | Denominator checks; two independent aggregation paths | 9 runs of 2013; replication on 2014 after the AQ3 test (C14) | Leave-one-run-out folds on 2013; a single test on the 13 runs of 2014 after the second freeze [26] | As AQ3, with lists formed per test run |
| Baseline | Pooled rate; second denominator | Unadjusted rate difference per sign | Rule-ranked list; background-only model; random list | Random list; rule-ranked list |
| Error analysis | Runs whose rate moves between the two denominators | Binned residuals; correlated signs; sensitivity runs | Missed and wrongly listed students by run, module, activity, history and kind of non-completion; list stability | Runs whose list fills with completers; inactive students apart from active students at risk |
| Fairness / subgroup check | Rates by gender, disability, deprivation band and age band, as description | Associations by gender, disability and deprivation band, as description | Confirmatory check of recall at capacity by group; descriptive checks (Section 4.4) | Selection, recall and precision by deprivation band and disability, and by gender and age band |
| Success criterion | Both aggregation paths agree; every rate with its denominator and interval | Risk difference of at least 5 points with an interval excluding 0, same direction in two-thirds of modules | Gate S1; S3 before probabilities are shown (Table 4.2) | S1 met by the list; fairness flags reviewed before use; no claim about the effect of contact |

**Metric definitions.** The cards use metrics that are defined once here, for a run r with n enrolments, the set Y of
its non-completers, base rate b = |Y|/n, and a list L of the k highest scores. In words: recall at capacity is the
share of the run's non-completers who are on the list; attainable recall is the most a list of length k can reach,
which is below 1 when the run has more non-completers than places on the list; normalised recall divides recall by
that ceiling, so that 1 means the best list possible; precision is the share of the list who do not complete; and
lift divides precision by the base rate, so that 1 means no better than chance. Appendix II (Table A.12) gives the formula of every metric.

