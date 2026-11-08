## Appendix II – Preparation Pipeline and Prepared Data Package

Figure A.3 shows the five phases of the pipeline, from the read-only raw files to the validated package.

![Figure A.3. From the raw files to the prepared views](assets/figures/fig-6-1-pipeline.png)

Table A.7 maps the ten preparation steps of the brief to the function of `src/prepare_data.py` or the script that carries each out, with the row counts it produced.

**Table A.7. Pipeline steps, code and results**

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

The Prepared Data Package, submitted with this report, is laid out as the brief recommends: `data/raw/` (immutable inputs), `data/interim/`, `data/processed/`, `data/metadata/`, `notebooks/`, `src/`, `tests/` and `logs/`. One command, run from the package folder, rebuilds it from the raw files; when `data/raw/` is empty it first downloads the published archive and checks every table against its pinned SHA-256:

```
bash src/run_all.sh
```

Table A.8 lists the eight stages the command runs, each recording its command, time, output and exit status in `logs/`.

**Table A.8. Stages of run_all.sh**

| Stage | Script | Output |
| :---- | :---- | :---- |
| 00 | `link_raw.py` | raw files hard-linked, SHA-256 checked against the Milestone 2 pins |
| 01 | `01_understand.py` | Dataset Understanding Map (Section 2.1) |
| 02 | `02_profile.py` | profile and quality evidence (Section 3) |
| 03 | `unittest on tests/` | formula tests on synthetic fixtures |
| 04 | `prepare_data.py` | ten preparation steps, views and transformation log (Section 6) |
| 05 | `fit_transforms.py` | transforms fitted on 2013 runs, model-ready matrices (Section 6.3) |
| 06 | `validate_prepared.py` | 22 checks, dictionary, lineage, version manifest (Section 7) |
| 07 | `build_notebooks.py` | notebooks 02 and 03, executed |

The transformation log records every operation with its row counts, in the order the pipeline runs them; each raw table is loaded only after its SHA-256 matches the pin and its columns match the documentation. Table A.9 reproduces it.

**Table A.9. Transformation log**

| Step | Operation | Rows in | Rows out | Note |
| :---- | :---- | :---- | :---- | :---- |
| 1 load | courses.csv |  | 22 |  |
| 1 load | assessments.csv |  | 206 |  |
| 1 load | vle.csv |  | 6,364 |  |
| 1 load | studentInfo.csv |  | 32,593 |  |
| 1 load | studentRegistration.csv |  | 32,593 |  |
| 1 load | studentAssessment.csv |  | 173,912 |  |
| 1 load | studentVle.csv |  | 10,655,280 |  |
| 2 population | studentInfo + studentRegistration | 32,593 | 32,593 | left join, rows kept |
| 2 population | + courses (run length) | 32,593 | 32,593 | left join, rows kept |
| 2 population | flag enrolled_d13 | 32,593 | 28,069 | enrolled at the day (C09) |
| 2 population | flag enrolled_d14 | 32,593 | 28,061 | enrolled at the day (C09) |
| 2 population | flag enrolled_d27 | 32,593 | 27,535 | enrolled at the day (C09) |
| 3 standardise | imd_band label '10-20' → '10-20%' | 3,516 | 0 |  |
| 3 standardise | year, start_month, completed, non_completion, split derived | 32,593 | 32,593 |  |
| 3 standardise | tasks = TMA and CMA (exams excluded, DQ08) | 206 | 182 |  |
| 4 keys | studentVle rows → enrolment × day (records, clicks, clicks_dedup) | 10,655,280 | 1,808,119 | clicks 39,605,099, de-duplicated 38,343,063 |
| 4 keys | studentVle rows → distinct enrolment × site × day | 10,655,280 | 8,459,320 |  |
| 5 missing | imd_band missing → category 'Missing' (no imputation) | 1,111 | 1,111 |  |
| 5 missing | flag registration_missing | 32,593 | 45 |  |
| 5 missing | flag withdrawal_day_missing | 32,593 | 93 |  |
| 5 missing | flag unregistered_not_withdrawn | 32,593 | 9 |  |
| 5 missing | flag unregistered_after_run_end | 32,593 | 1 |  |
| 6 truncate | enrolment × day click records up to the unregistration day | 1,808,119 | 1,802,593 | clicks removed 98,745 |
| 6 truncate | enrolment × site × day records up to the unregistration day | 8,459,320 | 8,435,429 |  |
| 7 integrate | enrolment × task grid (TMA, CMA of the run) | 32,593 | 286,898 |  |
| 7 integrate | + submission (if any) | 286,898 | 286,898 | left join, rows kept |
| 7 integrate | TMA/CMA submissions placed in the grid | 168,953 | 168,953 |  |
| 9 views | + banked results | 32,593 | 32,593 | left join, rows kept |
| 9 views | + concurrent runs | 32,593 | 32,593 | left join, rows kept |
| 9 views | + student seen in training runs | 32,593 | 32,593 | left join, rows kept |
| 9 views | + paired run flag | 32,593 | 32,593 | left join, rows kept |
| 9 views | + first missed task week | 32,593 | 32,593 | left join, rows kept |
| 9 views | + tasks while enrolled | 32,593 | 32,593 | left join, rows kept |
| 9 views | + whole-run activity (truncated at withdrawal) | 32,593 | 32,593 | left join, rows kept |
| 9 views | student_week grid + weekly clicks | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | + weekly distinct resources | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | + logging-gap flag (DQ15) | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | student_week rows (weeks -3..run end, cut at withdrawal) |  | 1,052,344 | clicks before week -3 not in this view: 0 |
| 8 features d13 | + activity up to the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + distinct resources | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + tasks due by the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + CMA marks known by the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + tasks submitted before their due day (due after the cut-off) | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + run median of clicks up to the cut-off (same run, no outcome) | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | features built; max event day ≤ cut-off | 28,069 | 28,069 | early_sign_rule 5,673 |
| 8 features d27 | + activity up to the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + distinct resources | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + tasks due by the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + CMA marks known by the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + tasks submitted before their due day (due after the cut-off) | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + run median of clicks up to the cut-off (same run, no outcome) | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | features built; max event day ≤ cut-off | 27,535 | 27,535 | early_sign_rule 7,933 |
| 10 persist | processed/enrolment.parquet |  | 32,593 | 39 columns |
| 10 persist | processed/assessment_due.parquet |  | 286,898 | 14 columns |
| 10 persist | processed/student_week.parquet |  | 1,052,344 | 10 columns |
| 10 persist | processed/features_d13.parquet |  | 28,069 | 50 columns |
| 10 persist | processed/features_d27.parquet |  | 27,535 | 52 columns |
| 10 persist | processed/capacity_by_run.parquet |  | 44 | 9 columns |

The prepared files are identified by version OULAD-N04-prepared-1.0; Table A.10 gives their row counts and hashes from `version_manifest.json`, identical across two runs from the raw files.

**Table A.10. Prepared files**

| File | Rows | SHA-256 (first 16) |
| :---- | :---- | :---- |
| assessment_due.parquet | 286,898 | f67d7916dd95c2ab |
| capacity_by_run.parquet | 44 | 38f6868c2b74fcc7 |
| enrolment.parquet | 32,593 | 1d1e397ac67ce774 |
| features_d13.parquet | 28,069 | c58a44150e8c367c |
| features_d27.parquet | 27,535 | 4bf8a482b9ec7fa4 |
| model_ready_d13.parquet | 28,069 | 773d1e2fa0773564 |
| model_ready_d27.parquet | 27,535 | 3560a51594d4ad97 |
| student_week.parquet | 1,052,344 | 7526872e26e95da7 |
