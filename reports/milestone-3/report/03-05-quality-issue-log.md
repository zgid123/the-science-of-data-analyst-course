## 3.5. Data Quality Issue Log

The findings of Sections 3.1 to 3.4 become nineteen issues, each with its evidence, its impact on the questions, a
severity and a decision, in the format of the brief's Data Quality Issue Log [1]. The severity is judged against the
questions: High marks an issue that would change a reported rate, the target or a feature at a cut-off if it were
ignored; Medium one that would change a measure by a known amount; and Low one that touches few records or a field
that no question uses. Table 3.1 gives all nineteen issues in order with their key evidence; Appendix I (Table A.4)
gives the evidence in full with the profile entry behind each number.

**Table 3.1. Data Quality Issue Log**

| ID | Variable / table | Evidence | Impact on AQ | Severity | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- |
| DQ01 | studentVle: exact duplicate rows | 787,170 rows (7.39%); 3.19% of clicks | Click measures (AQ2, AQ3) | Medium | Keep every row; de-duplicated twin of each click feature for sensitivity |
| DQ02 | studentVle: grain | 1,614,505 student-resource-days with several rows | Counts and joins at row level | Medium | Sum clicks by enrolment and day before any join; count active days, not rows |
| DQ03 | Activity after unregistration | 98,745 clicks and 588 submissions after unregistering | Engagement up to withdrawal (AQ1, AQ2) | Medium | Truncate engagement at the unregistration day |
| DQ04 | final_result and unregistration day | 93 Withdrawn without a day; 9 Fail with one | Populations at each day; time to withdrawal | Low | Keep both as recorded; flag the 93 and the 9 |
| DQ05 | Registration after day 14 | 58 registered on days 16–167 | KPI denominator; populations at the cut-offs | Low | Enrolled at day d requires registration by day d (C09) |
| DQ06 | Departures before teaching | 3,097 unregistered by day 0; one on day 444 of a 268-day run | KPI denominator | Low | Not an error; outside the day-14 population; the day-444 record kept with a flag |
| DQ07 | Banked results | 1,909 dated −1 | Timing and missed-task measures (AQ1–AQ3) | Medium | Never timed; counted as banked results, known at registration |
| DQ08 | Exams | 18 of 24 exams without a result row | First missed task (AQ1); task signs (AQ2, AQ3) | High | Tasks are TMA and CMA only; exam scores not used |
| DQ09 | Weights | Coursework weight 0 in GGG; two exams in CCC 2014 | Weighted score features | Medium | No weighted grade; tasks counted unweighted |
| DQ10 | Late submissions | 32,991 of 69,956 CMA and 16,320 of 97,088 TMA late | Late-task signs (AQ1, AQ2, early-sign rule) | Medium | Lateness kept by task type; the rule uses TMA lateness (C10) |
| DQ11 | Scores | 173 TMA scores missing | Score features | Low | Score left missing; only marks known at the cut-off used |
| DQ12 | imd_band | 1,111 missing; 65.7% against 46.6% success | Fairness audit (AQ4); background features | Medium | Label corrected; "Missing" kept as its own group; no imputation |
| DQ13 | Registration day | 45 missing, 39 Withdrawn | Registration-lead feature | Low | Kept missing with an indicator |
| DQ14 | Planned weeks of resources | Missing for 82.4% of resources | None | Low | Not used |
| DQ15 | Days without any click | Days 218–219 of all February 2014 runs | Daily series after week 30 | Low | Treated as missing, not zero |
| DQ16 | Outliers in clicks and credits | 2,503 beyond the fence; 655 credits | Scale-sensitive methods | Low | Every value kept; logarithm in model matrices |
| DQ17 | Enrolments without activity | 3,365 without clicks; 6,750 without submissions | Inner joins would drop them | Medium | Left joins from the enrolment table; zero counts |
| DQ18 | Tasks due by the cut-offs | Task due by day 13 in 1 run, by day 27 in 16 | AQ3 comparison rule; secondary KPI 1 | High | Rule restated on the tasks actually due (C10) |
| DQ19 | Representativeness | Seven UK modules of 2013–2014 | Every claim; group comparisons | High | Scope stated; comparisons within module; results checked on the university's data |

Three issues are rated High. The missing exam results (DQ08) would count the exam as missed for every student of the
five modules without exam results if exams were counted as tasks, so only TMA and CMA count as tasks. The few tasks due by the cut-offs (DQ18) would leave the
early-sign rule silent in most runs, so the rule is restated (Section 4.1). The narrow population (DQ19) limits every
claim, so the scope is stated with each result.
