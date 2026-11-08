# 7. Prepared Data Validation

The brief asks the team to show that the prepared data serve the analysis better while staying correct and
traceable: row, entity and outcome counts compared before and after preparation, missingness, keys, joins, ranges and
time order checked again, derived features checked against their formulas and by hand, no leakage against the
prediction point, an updated data dictionary and a recorded version [1]. The validation script,
`src/validate_prepared.py`, runs 22 checks under fifteen identifiers, V01 to V15, against the raw files and the
profile, and all 22 pass; each check states its expected and observed value (Appendix VI). Section 7.1 reports the
comparisons, Section 7.2 the lineage, dictionary and version, and Section 7.3 the risks that remain in the data on
purpose.
