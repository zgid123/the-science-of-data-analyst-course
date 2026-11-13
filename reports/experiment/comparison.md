# Comparison with the Milestone 4 Level 2 experiment

*Team N04 · MTH045 · this experiment (`report.md`) set against the team's Milestone 4 Level 2 prototype, both on OULAD-N04-prepared-1.0 with the same Milestone 4 design*

## Summary

**The two experiments reach the same answer to every analytical question.** All five AQ2 signs pass in both years in both experiments, M1 is chosen in both, gate S1 is met in both, the rule's lists are identical in all 13 test runs, and no fairness group is flagged in either. The model lists 2,871 non-completers in the Milestone 4 experiment and 2,868 here.

Two results differ, and both trace to a choice the Milestone 4 design leaves open:

1. **Calibration S3.** The Milestone 4 design says the penalty of the logistic model is tuned by nested cross-validation but does not name the measure. The Milestone 4 experiment tuned on recall at capacity and chose a strong penalty (C = 0.001); this experiment tuned on log loss and chose almost none (C = 10). The strong penalty pulls risks towards the average, so the calibration slope is 1.311 and S3 fails; here the slope is 0.886 and S3 passes pooled, but only in 5 of 13 runs. Both lead to the same advice: show ranks and reasons, not probabilities.
2. **Strength of the S1 test.** The model wins 12 of 13 runs in the Milestone 4 experiment (sign-flip p = 0.0002) and 11 of 13 here (p = 0.0035), because one run, GGG-2014J, changes sides by about one point of normalised recall. Both are well below the 0.05 the gate requires.

AQ1 cannot be compared: the Milestone 4 experiment has no AQ1 results. This experiment adds AQ1, the exit timing, the swap between model and rule lists, the active non-completers both lists miss, the yield of each extra contact and the reasons shown to tutors.

## AQ2: associations of the five signs

The adjusted risk differences agree within 2.3 points; the ranking of the signs and every verdict are the same. The small shifts come from two implementation choices: the Milestone 4 experiment cuts low activity at the run median (here half the median, the design's primary cut), and this experiment averages each sign only over the rows where it is defined.

<!-- table: results/compare_m4.csv where=aq:AQ2 cols=item,milestone_4,new,difference "names=item:Sign and year,milestone_4:Milestone 4 (points),new:This experiment (points),difference:Difference" digits=1 -->
| Sign and year | Milestone 4 (points) | This experiment (points) | Difference |
| :---- | :---- | :---- | :---- |
| Missed a task due, 2013 | 40.8 | 40.7 | −0.2 |
| Missed a task due, 2014 | 39.3 | 39.6 | 0.4 |
| Submitted a TMA late, 2013 | 20.2 | 21.7 | 1.5 |
| Submitted a TMA late, 2014 | 20.3 | 22.5 | 2.3 |
| No activity in the last 7 days, 2013 | 14.5 | 13.5 | −1.0 |
| No activity in the last 7 days, 2014 | 15.8 | 15.4 | −0.4 |
| Clicks below half the run median, 2013 | 13.4 | 14.7 | 1.3 |
| Clicks below half the run median, 2014 | 14.6 | 14.8 | 0.2 |
| No activity before the start, 2013 | 10.6 | 11.3 | 0.7 |
| No activity before the start, 2014 | 8.7 | 9.2 | 0.5 |
<!-- /table -->

## AQ3: model choice and the 2014 test

Development on the 2013 runs agrees within 0.003 normalised recall for every configuration, and no challenger comes near the 0.03 margin in either experiment.

<!-- table: results/compare_m4.csv "where=aq:AQ3 development" cols=item,milestone_4,new,difference "names=item:Configuration,milestone_4:Milestone 4,new:This experiment,difference:Difference" digits=3 -->
| Configuration | Milestone 4 | This experiment | Difference |
| :---- | :---- | :---- | :---- |
| Development, M1 | 0.753 | 0.750 | −0.002 |
| Development, rule | 0.727 | 0.727 | 0.000 |
| Development, B3 | 0.571 | 0.568 | −0.003 |
| Development, M2 | 0.747 | 0.749 | 0.002 |
| Development, M3 | 0.750 | 0.749 | −0.001 |
| Development, M4 | 0.749 | 0.748 | −0.001 |
<!-- /table -->

The choices behind the frozen model:

<!-- table: results/compare_m4.csv "where=aq:AQ3 setup" cols=item,milestone_4,new,same_conclusion "names=item:Choice,milestone_4:Milestone 4,new:This experiment,same_conclusion:Same?" -->
| Choice | Milestone 4 | This experiment | Same? |
| :---- | :---- | :---- | :---- |
| Chosen configuration | M1 | M1 | yes |
| M1 penalty C at day 27 | 0.001 | 10 | no: tuning criterion differs |
<!-- /table -->

On the 13 test runs of 2014, every S1 quantity agrees within 0.003 except the sign-flip p, and only the calibration slope crosses an S3 bound.

<!-- table: results/compare_m4.csv "where=aq:AQ3 test" cols=item,milestone_4,new,difference,same_conclusion "names=item:Quantity,milestone_4:Milestone 4,new:This experiment,difference:Difference,same_conclusion:Same conclusion?" digits=4 -->
| Quantity | Milestone 4 | This experiment | Difference | Same conclusion? |
| :---- | :---- | :---- | :---- | :---- |
| S1 normalised recall, model | 0.7259 | 0.7252 | −0.0008 | yes |
| S1 normalised recall, rule | 0.7044 | 0.7044 | 0.0000 | yes |
| S1 difference | 0.0215 | 0.0207 | −0.0008 | yes |
| S1 interval, low | 0.0093 | 0.0063 | −0.0029 | yes |
| S1 interval, high | 0.0337 | 0.0361 | 0.0024 | yes |
| S1 sign-flip p | 0.0002 | 0.0035 | 0.0033 | yes |
| S1 runs won (of 13) | 12 | 11 | -1 | yes |
| Non-completers listed by the model, day 27, 5 per 20 | 2,871 | 2,868 | -3 | yes |
| Runs where the rule's list is identical (of 13) | 13 | 13 | 0 | yes |
| S3 calibration-in-the-large | 0.0580 | 0.1168 | 0.0588 | yes |
| S3 calibration slope | 1.3106 | 0.8857 | −0.4249 | no: S3 fails in M4, passes pooled here |
<!-- /table -->

Run by run, the two models pick the same winner in 12 of 13 runs; GGG-2014J is the exception.

<!-- table: results/compare_m4_runs.csv cols=run,m4_difference,new_difference,same_winner "names=run:Test run,m4_difference:Model − rule (Milestone 4),new_difference:Model − rule (this experiment),same_winner:Same winner" digits=3 -->
| Test run | Model − rule (Milestone 4) | Model − rule (this experiment) | Same winner |
| :---- | :---- | :---- | :---- |
| AAA-2014J | 0.033 | 0.022 | True |
| BBB-2014B | 0.028 | 0.012 | True |
| BBB-2014J | 0.031 | 0.036 | True |
| CCC-2014B | 0.029 | 0.029 | True |
| CCC-2014J | 0.008 | 0.010 | True |
| DDD-2014B | 0.019 | 0.023 | True |
| DDD-2014J | 0.030 | 0.038 | True |
| EEE-2014B | 0.013 | 0.026 | True |
| EEE-2014J | 0.063 | 0.067 | True |
| FFF-2014B | 0.022 | 0.018 | True |
| FFF-2014J | 0.006 | 0.006 | True |
| GGG-2014B | −0.005 | −0.020 | True |
| GGG-2014J | 0.006 | −0.011 | False |
<!-- /table -->

The sensitivity views, which cannot change the S1 verdict, move by at most 0.003 and keep their direction.

<!-- table: results/compare_m4.csv "where=aq:AQ3 sensitivity" cols=item,milestone_4,new,difference "names=item:View (model − rule),milestone_4:Milestone 4,new:This experiment,difference:Difference" digits=3 -->
| View (model − rule) | Milestone 4 | This experiment | Difference |
| :---- | :---- | :---- | :---- |
| Day 13, 5 per 20 | 0.021 | 0.021 | 0.000 |
| Day 27, 3 per 20 | 0.028 | 0.031 | 0.003 |
| 9 runs also run in 2013 | 0.025 | 0.024 | −0.001 |
| 4 runs not run in 2013 | 0.013 | 0.013 | 0.000 |
| Without module CCC | 0.023 | 0.021 | −0.001 |
| Module CCC only | 0.017 | 0.018 | 0.001 |
| Without students seen in 2013 | 0.023 | 0.020 | −0.002 |
| Without Withdrawn lacking a withdrawal day | 0.022 | 0.020 | −0.002 |
<!-- /table -->

## AQ4: fairness of the lists

The confirmatory gaps agree within 0.6 points and no group is flagged in either experiment; the descriptive recall of women and men is the same to 0.1 points.

<!-- table: results/compare_m4.csv where=aq:AQ4 cols=item,milestone_4,new,difference "names=item:Group (recall gap),milestone_4:Milestone 4 (points),new:This experiment (points),difference:Difference" digits=1 -->
| Group (recall gap) | Milestone 4 (points) | This experiment (points) | Difference |
| :---- | :---- | :---- | :---- |
| Recall gap: Declared disability | 5.4 | 5.5 | 0.0 |
| Recall gap: Most deprived band (0–10%) | 1.7 | 1.4 | −0.4 |
| Recall gap: Deprivation band missing | −8.1 | −7.4 | 0.6 |
<!-- /table -->

<!-- table: results/compare_m4.csv "where=aq:AQ4 descriptive" cols=item,milestone_4,new "names=item:Group,milestone_4:Milestone 4,new:This experiment" pct=milestone_4,new digits=1 -->
| Group | Milestone 4 | This experiment |
| :---- | :---- | :---- |
| Recall, women | 38.8% | 38.7% |
| Recall, men | 43.4% | 43.4% |
<!-- /table -->

## What to state in the Final Report

Name the tuning criterion of the penalty, because the S3 verdict depends on it: under recall-based tuning S3 fails, under log-loss tuning it passes pooled and fails in 8 of 13 runs. The rest of the experimental results can be cited from either experiment; their numbers differ by at most a few students on a list.

Source tables: `results/compare_m4.csv` and `results/compare_m4_runs.csv`, built by `code/16_compare_m4.py` from copies of the Milestone 4 result files kept in `evidence/milestone-4/`.
