## 9.1. Validation, Metrics and Success Criteria

The five-point threshold of AQ2 is the smallest gap we treat as worth staff attention, a convention fixed in Milestone
4 and lenient at a base rate near 44%, so the size of each estimate distinguishes the signs, and p-values take no part
in the verdict, because a p-value does not measure the size of an effect [12]. For AQ3, recall, precision, lift and
calibration would be reported beside the primary metric, because good discrimination does not guarantee reliable risk
estimates [13]; probabilities are shown only if calibration holds (S3), and gate S1 alone decides (Table A.23,
Appendix IX). Evaluation data should be distinct from the data used to train, tune or select the model [11]:
development uses leave-one-run-out folds on 2013, a challenger replaces the primary model only with a gain of at least
0.03 in pooled normalised recall and in 7 of 9 folds, and the frozen model is scored once on the 13 runs of 2014, with
the 9 paired and 4 unpaired runs also reported apart (C16).
