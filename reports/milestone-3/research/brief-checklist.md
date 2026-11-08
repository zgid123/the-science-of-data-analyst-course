# Brief section 17 – checklist before submission (checked at T23, 2026-11-06)

| # | Checklist item (brief, translated) | Evidence | State |
| :---- | :---- | :---- | :---- |
| 1 | Raw data in data/raw unchanged, with provenance and version | `package/data/metadata/raw_check.csv` (7/7 SHA-256 match, read-only); Section 1.2 | done |
| 2 | Unit of analysis, keys, target and time semantics correct | Table 2.1, 2.2; `understanding.json` | done |
| 3 | Profiling evidence for missingness, duplicates, validity, outliers, target balance, time, joins | Sections 3.1–3.4; `profile.json` | done |
| 4 | Every quality issue has a decision and rationale | Table 3.1, Table 5.1; `quality_issue_log.md`, `decision_matrix.md` | done |
| 5 | Missing values distinguished from missing variables | Table 4.2 | done |
| 6 | No AQ saved with synthetic data | Section 4.2 | done |
| 7 | Synthetic data, if any, within policy and apart from real evidence | `package/tests/` level A fixtures only | done |
| 8 | Predictive AQ has prediction point, split strategy and leakage control | Sections 2.2, 6.3; V11–V13, V15 | done |
| 9 | Fitted transforms fitted on the training partition | `fit_transforms.py`; V12 | done |
| 10 | Derived features have formula, source field, time window and lineage | Table 6.2, `feature_spec.md`, `lineage.md` (Appendix III) | done |
| 11 | Prepared data rechecked for counts, target distribution, missingness, keys | Table 7.1; V01–V10 | done |
| 12 | Traceability updated to prepared variables and views | Appendix IV Table A.8; `traceability.md` | done |
| 13 | Data / Model Readiness Matrix for the four levels | Tables 8.1, 8.2 | done |
| 14 | AI suggestions verified and recorded in the AI Decision Log | Table 10.1; Appendix V Tables A.10–A.12 | done |
| 15 | Limitations and rewritten, dropped or deferred questions shown | Sections 4.1, 7.3, 8.2, 9 | done |
