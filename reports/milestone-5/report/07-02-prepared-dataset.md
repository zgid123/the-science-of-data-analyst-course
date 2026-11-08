## 7.2. Final Prepared Dataset and Reproducibility

The decisions of Section 7 and the variables of Section 7.1 produce one versioned prepared dataset, which every analysis of this project reads; it must be shown to change nothing without a rule, to document every column, and to be rebuildable by anyone from the public download.

**Validation.** The validation script runs 22 checks under fifteen identifiers, V01 to V15, against the raw files and the profile of Section 6, and all 22 pass. Table 7.4 gives the main before-and-after comparisons, each with the value in the raw data and in the prepared data.

**Table 7.4. Before-and-after checks of the prepared data**

| Check | Before (raw) | After (prepared) | Result |
| :---- | :---- | :---- | :---- |
| Enrolments, students, outcome mix | 32,593 enrolments; 28,785 students; 12,361 Pass, 10,156 Withdrawn, 7,052 Fail, 3,024 Distinction | Identical; no row dropped | Pass |
| Populations (rule C09) | 32,593 enrolments | 28,061 at day 14; 28,069 at day 13; 27,535 at day 27, equal to the profile | Pass |
| Clicks | All click rows | 39,506,354 clicks kept plus 98,745 after withdrawal left out; the weekly view sums to the same total | Pass |
| De-duplicated clicks | – | 38,247,422, below the 39,506,354 kept clicks | Pass |
| Missing values | Deprivation band 1,111; registration day 45; TMA score 173 | Identical, not imputed | Pass |
| Joins | – | 25 joins, rows in equal rows out | Pass |
| Derived features | – | Six features recomputed from raw by separate code for all 55,604 feature rows: 0 differences | Pass |
| Leakage (date filter) | – | Recount without the filter differs only for the 26,755 (day 13) and 25,663 (day 27) enrolments that clicked after the cut-off | Pass |
| Repeat students | – | 1,962 enrolments of the 2014 runs (all enrolments, before any cut-off) of students seen in 2013, with 0 flag mismatches | Pass |

The comparisons show that preparation changed no outcome and no count except by a stated rule: clicks after withdrawal are left out by the truncation decision, and every other total is equal before and after.

**Documentation.** Every prepared column is documented in a data dictionary with its source field, transformation, type, role and sensitivity, and the lineage table gives one row for each of the 88 prepared variables. The dictionary is also a guard: validation fails if a column lacks an entry or if a predictor list holds an audit, target or descriptive column (V14), so the dictionary cannot drift from the data. Such documentation follows the practice that every dataset should come with a datasheet of its motivation and composition [S910], and that reusable data carry a clear licence and detailed provenance [S911].

**Version and views.** The prepared dataset is named OULAD-N04-prepared-1.0. Its version manifest records the SHA-256 checksum of every raw file, every script and every prepared file, the row counts, the code commit and the Python (3.12.7) and polars (2.1.0) versions. Table 7.5 gives the prepared views, stored as Parquet files, with the unit of each and the questions that read it.

**Table 7.5. Prepared views of OULAD-N04-prepared-1.0**

| View | Unit | Read by |
| :---- | :---- | :---- |
| enrolment | Enrolment, with outcome, population flags and audit attributes | AQ1; populations of every question |
| assessment_due | Enrolment and assessed task, with due day, submission and lateness | AQ1 first missed week |
| student_week | Enrolment and week, with clicks | Weekly activity series; source of the weekly click counts |
| features_d13, features_d27 | Enrolment registered at the cut-off, with predictors, rule, target and audit columns | AQ2 (day 27); AQ3 and AQ4 |
| capacity_by_run | Run and cut-off, with list lengths at 3 and 5 per 20 | AQ4 |
| model_ready_d13, model_ready_d27 | Reference encoding for linear models | Leakage evidence; not model input |

**Reproducibility.** The raw tables are read-only copies checked against their checksums at every run, so the raw data stay immutable. The package rebuilds the prepared data from raw with an install of its listed requirements and one command that runs the preparation stages in order, logs the command, the time in Coordinated Universal Time (UTC) and the exit status of each stage, and stops at the first failure. When the raw files are absent, the first stage downloads the OULAD archive from its figshare record (DOI 10.6084/m9.figshare.5081998.v1) and checks every table against its pinned SHA-256. Run twice from the raw files, the pipeline writes byte-identical outputs: the SHA-256 of all eight prepared files is equal across runs. The data are licensed under CC BY 4.0 [S002], which requires citing the dataset's descriptor by Kuzilek, Hlosta and Zdrahal and allows the prepared views to be shared with that attribution. The Final Project Package therefore carries the access instructions, the pinned download, the pipeline and the data dictionary, so that the prepared data can be rebuilt outside our repository.

**Sensitivity of the KPI to flagged records.** The 138 enrolments flagged for an unknown withdrawal day (93) or registration day (45) barely move the KPI: completion in the day-14 population is 54.74% on all 28,061 enrolments and 54.93% without the flagged ones. In the 9 runs of 2013, 21 enrolments carry such a flag, 8 of them in the day-14 population, so the AQ1 rate without them serves as a baseline check (Section 9.1). The early-sign rule, computed without any outcome, flags between 8.4% and 44.0% of enrolments per run at day 13 and between 17.9% and 54.8% at day 27, so its reach differs widely between runs.

**Synthetic data.** Synthetic data are used only at the lowest level: a few hand-made test enrolments check the feature formulas in unit tests, and they never enter a prepared view, a statistic or a finding. Every number in this report therefore comes from the recorded OULAD data. With the data prepared, versioned and reproducible, Section 8 maps each question to the analysis that answers it.
