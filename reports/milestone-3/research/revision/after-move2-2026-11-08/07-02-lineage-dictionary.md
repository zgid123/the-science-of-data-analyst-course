## 7.2. Lineage, Dictionary and Version

**Dictionary.** Every prepared column is documented with its source field, its transformation, its data type, its role
and its sensitivity, as the brief requires [1]. The role says how a column may be used: identifier, target, predictor,
audit attribute, evaluation flag or descriptive measure. Validation fails if a column lacks an entry or if a predictor
list holds an audit, target or descriptive column (V14), so the documentation cannot drift from the data.

**Lineage.** The lineage table of the brief traces each prepared variable to its source file and field, with its
transformation, its window or filter, its purpose and its sensitivity [1]. The table holds one row for each of the 88
prepared variables and is Table A.12 in Appendix III; the formulas of the main derived variables are in Table 6.1,
and the lineage of the target, for example, runs from studentInfo.final_result, through the rule "Fail or
Withdrawn", observed at the run end, to non_completion, the target of AQ1 to AQ3, with no sensitivity.

**Version.** The version manifest names the prepared dataset OULAD-N04-prepared-1.0 and records the SHA-256 checksum
of every raw file, script and prepared file, the row counts of every view, the repository commit, the Python (3.12.7)
and polars (2.1.0) versions and the creation time in UTC. A reader can therefore tell which raw data and which code
produced a given prepared file, and the rerun check of Section 6.1 shows that the same inputs give the same outputs.
