## 3.5. Data Quality Issue Log

The findings of Sections 3.1 to 3.4 become nineteen issues, each with its evidence, impact on the questions, a
severity and a decision; the evidence is stated in Sections 3.1 to 3.4. High marks an issue that would change a reported rate, the target or a feature at a cut-off,
Medium one that would change a measure by a known amount, and Low one that touches few records or an unused field.
Table 3.1 lists the eleven High and Medium issues. The eight Low issues are inconsistent withdrawal records (DQ04),
late registration (DQ05), departures before teaching (DQ06), missing TMA scores (DQ11), missing registration days
(DQ13), unused planned weeks (DQ14), a logging gap (DQ15) and outliers (DQ16); Appendix I (Table A.4) gives all
nineteen with full evidence.

**Table 3.1. Data Quality Issue Log**

| ID | Variable / table | Impact on AQ | Severity | Decision |
| :---- | :---- | :---- | :---- | :---- |
| DQ01 | studentVle duplicates | Click measures (AQ2, AQ3) | Medium | Keep all rows; de-duplicated twin for sensitivity |
| DQ02 | studentVle grain | Counts and joins | Medium | Aggregate by enrolment × day before joins |
| DQ03 | Activity after withdrawal | AQ1–AQ2 measures | Medium | Truncate at the unregistration day |
| DQ07 | Banked results | Timing features | Medium | Never timed; counted as banked results |
| DQ08 | Exams | Task signs (AQ1–AQ3) | High | Tasks = TMA and CMA only |
| DQ09 | Weights | Weighted scores | Medium | No weighted grade; tasks counted unweighted |
| DQ10 | Late submissions | Late-task signs | Medium | Lateness kept by task type; rule uses TMA lateness (C10) |
| DQ12 | imd_band | Fairness audit (AQ4) | Medium | Label fixed; "Missing" kept as its own group |
| DQ17 | No activity rows | Inner joins drop them | Medium | Left joins; zero counts |
| DQ18 | Tasks due by cut-offs | AQ3 rule; secondary KPI 1 | High | Rule restated (C10) |
| DQ19 | Representativeness | Every claim | High | Scope stated; within-module comparisons |
