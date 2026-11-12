# Log: logs / tests_aq2_model

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:48:08Z |
| Finished (UTC) | 2026-11-12T15:48:10Z |
| Duration | 1.5 s |
| Command | `python common/tests/test_aq2_model.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output

- PASS: late TMA is defined only in the runs with a TMA due (6,000 of 9,000 synthetic rows)
- PASS: support of the late-TMA sign excludes module C
- PASS: the average covers 6,000 rows, not 9,000, and reports that n
- PASS: every module C row has a difference of exactly 0, which is why it must stay out of the average
- PASS: estimate equals the mean over the support (about +0.24), not the diluted mean over all rows (two-thirds of it)
- PASS: table() carries n_support = 6,000 and no row defined outside the support
- PASS: the unadjusted difference uses the same 6,000 rows (module C is not the comparison group)
- PASS: a subgroup average is restricted to the support as well
- PASS: the click sign keeps all 9,000 rows
- PASS: module with no enrolment carrying the sign gets no term and stays outside the support
- PASS: the model without sign x module terms excludes that module too
- PASS: module with 5 enrolments carrying the sign shares a pooled slope and stays in the support
- PASS: direction count: 3 of 3 by point estimate, 2 of 3 with an interval excluding 0, module C named
- PASS: strict reading fails when only 1 of 3 module intervals excludes 0, while the point-estimate reading still passes
- PASS: binned residuals: observed 0.5 against predicted 0.2; band = 2 x sqrt(2 x 0.16) / 2
- PASS: stratified difference with one stratum = plain difference 0.10 with its Wald standard error
- PASS: stratified difference is -0.10 in a toy case where the mix of strata differs between the groups
- PASS: year comparison, shared modules, day-14 denominator: 60/150 - 90/180 = -0.10
- PASS: year comparison, shared modules, all enrolments: 110/200 - 110/200 = 0 (the sign changes with the denominator)
- PASS: year comparison over all runs includes the module that ran only in 2014: 140/250 - 90/180
- PASS: Newcombe interval contains the difference and is not symmetric Wald

21 of 21 checks passed (synthetic inputs, code paths only)

