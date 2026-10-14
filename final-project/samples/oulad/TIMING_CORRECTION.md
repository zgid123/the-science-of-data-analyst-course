# Final timing audit correction

One historical FFF/2013J enrollment has recorded withdrawal day 444 after scheduled day 268. Under the declared end-of-presentation follow-up definition, its eventual withdrawal label cannot be assumed known by the 2014J warning point. Raw records are preserved; the one outside-follow-up enrollment is excluded from analysis eligibility. A new historical event-time check passes.

The approved pre-correction OULAD artifacts (code, reports, results and screenshots) are preserved in `evidence/approved-baseline-before-timing-audit.zip`. All affected OULAD and FFF model fits, thresholds, uncertainty, sensitivity and presentation outputs were regenerated. The broad conclusions survive: behavior adds to scores, combined does not uniformly beat behavior across modules, and many adverse outcomes remain missed.

Reference combined-model results at validation 20% capacity:

| cutoff | model | capacity | split | n_before | ap_before | alerts_before | precision_before | recall_before | fn_before | n_after | ap_after | alerts_after | precision_after | recall_after | fn_after |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 | combined | 0.200 | test | 6102 | 0.447 | 1892 | 0.442 | 0.390 | 1307 | 6102 | 0.447 | 1892 | 0.442 | 0.390 | 1307 |
| 60 | combined | 0.200 | test | 5903 | 0.586 | 1359 | 0.595 | 0.416 | 1136 | 5903 | 0.586 | 1358 | 0.595 | 0.415 | 1137 |
| 90 | combined | 0.200 | test | 5746 | 0.676 | 1290 | 0.622 | 0.449 | 986 | 5746 | 0.676 | 1290 | 0.622 | 0.449 | 986 |
