| Step (brief) | Code | Result |
| :---- | :---- | :---- |
| 1 Load raw files, validate schema | `step1_load_validate` | 7 tables, SHA-256 equal to the pins, columns as documented |
| 2 Select in-scope population | `step2_population` | 32,593 enrolments; 28,069 / 28,061 / 27,535 enrolled at days 13 / 14 / 27 |
| 3 Standardise types, labels, identifiers | `step3_standardise` | 3,516 "10-20" labels fixed; 182 tasks (TMA, CMA) |
| 4 Resolve keys and duplicates | `step4_keys` | 10,655,280 click rows → 1,808,119 enrolment-day records |
| 5 Handle missing values | `step5_missing` | 1,111 "Missing" bands; 45, 93, 9 and 1 flagged records |
| 6 Handle invalid values | `step6_truncate` | 98,745 clicks after withdrawal left out |
| 7 Integrate tables | `step7_integrate` | 286,898 enrolment-task rows; 168,953 submissions placed |
| 8 Construct features | `cutoff_features` | 28,069 and 27,535 feature rows |
| 9 Analysis-ready tables | `step9_views` | 6 views, among them 1,052,344 enrolment-week rows |
| 10 Persist with log and metadata | `step10_persist`, `fit_transforms.py`, `validate_prepared.py` | 8 Parquet files, dictionary, lineage, validation summary, version manifest |
