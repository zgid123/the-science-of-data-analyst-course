## 7.2. Lineage, Dictionary and Version

**Dictionary.** Every prepared column is documented with its source field, its transformation, its data type, its role
and its sensitivity, as the brief requires [1]. The role says how a column may be used: identifier, target, predictor,
audit attribute, evaluation flag or descriptive measure. Validation fails if a column lacks an entry or if a predictor
list holds an audit, target or descriptive column (V14), so the documentation cannot drift from the data.

**Lineage.** The lineage table of the brief traces each prepared variable to its source file and field, with its
transformation, its window or filter, its purpose and its sensitivity [1]. Table 7.2 shows it for the variables that
carry the questions; the full table, with one row for each of the 88 prepared variables and the sensitive variables
marked in its purpose column, is Table A.12 in Appendix III.

**Table 7.2. Data lineage of the main prepared variables**

| Prepared variable | Source file / field | Transformation | Window / filter | Purpose / AQ | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| non_completion | studentInfo.final_result | Fail or Withdrawn | observed at the run end | AQ1–AQ3 target | none |
| enrolled_d14 | studentRegistration, registration days | enrolled at day 14 | day 14 | primary KPI denominator (C09) | none |
| clicks_0c | studentVle.sum_click, date | sum | days 0 to c | AQ2–AQ3 | none |
| tasks_missed_c | studentAssessment | due by c, no non-banked submission by c | submissions up to c | AQ2–AQ3; part of the rule | none |
| early_sign_rule | derived | missed task, late TMA or inactive | at c | AQ3 comparison rule; secondary KPI 1 (C10) | none |
| imd_band | studentInfo.imd_band | "10-20" → "10-20%"; missing → "Missing" | – | AQ4 fairness audit (C04) | sensitive |

**Version.** The version manifest names the prepared dataset OULAD-N04-prepared-1.0 and records the SHA-256 checksum
of every raw file, script and prepared file, the row counts of every view, the repository commit, the Python (3.12.7)
and polars (2.1.0) versions and the creation time in UTC. A reader can therefore tell which raw data and which code
produced a given prepared file, and the rerun check of Section 6.1 shows that the same inputs give the same outputs.
