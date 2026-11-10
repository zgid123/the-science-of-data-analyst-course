## 6.1. Quality Findings

In Milestone 3 we turned the profile into a Data Quality Issue Log of nineteen issues, rated against the questions: High
when ignoring the issue would change a rate, the target or a feature, Medium when it would change a measure by a known
amount, and Low otherwise. Table 6.2 gives the log with the decision on each issue; Table A.15 (Appendix VI) adds the
evidence. The three High issues each change the method: exam results are missing in five modules, so tasks mean TMAs
and CMAs only (DQ08); no 2013 run has a task due by day 13 and 7 of 9 have one by day 27, so the early-sign rule has an
activity part (DQ18); and the narrow population limits every claim (DQ19). Two Medium issues
could move a conclusion by a known amount: counting late CMAs would raise the share the early-sign rule flags at day 27
from 28.8% to 41.2%, so the rule uses TMA lateness and late CMAs become a sensitivity run (DQ10), and the duplicate click rows, 7.39% of click rows, whose removal would drop 3.19% of all clicks, which a de-duplicated twin of each click feature tests (DQ01). These findings
produced the Change Log entries C09 to C13 (Table A.8), none of which alters the Business Goal or the decisions.

**Table 6.2. Data Quality Issue Log**

| ID | Issue | Severity | Decision |
| :---- | :---- | :---- | :---- |
| DQ01, DQ02 | Duplicate click rows (7.39% of rows); several rows per day | Medium | Keep rows; sum by day; de-duplicated twin |
| DQ03 | Activity after unregistration | Medium | Truncate at the unregistration day |
| DQ04–DQ06 | Status disagreements; 58 late registrants; early leavers | Low | Flag; population rule (C09) |
| DQ07 | Banked results dated −1 | Medium | Never timed |
| DQ08 | 18 of 24 exams without result rows | High | Tasks are TMA and CMA only |
| DQ09, DQ10 | Weights differ by module; late CMAs and TMAs | Medium | Unweighted tasks; TMA lateness in the rule |
| DQ11–DQ14 | Missing scores, deprivation band, registration day, planned weeks | Low–Medium | "Missing" group or indicator; no imputation |
| DQ15–DQ17 | Logging gap; outliers; enrolments without activity | Low–Medium | Missing, not zero; keep values; left joins |
| DQ18 | Few tasks due by the cut-offs | High | Rule with an activity part (C10) |
| DQ19 | Seven UK modules of 2013–2014 | High | Scope stated; comparisons within module |
