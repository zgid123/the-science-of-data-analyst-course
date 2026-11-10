## 7.2. Final Prepared Dataset and Reproducibility

The result is one versioned dataset, OULAD-N04-prepared-1.0. All 22 validation checks, under the fifteen identifiers V01–V15 (Section 7), pass: the 32,593 enrolments and
their outcome mix are unchanged, and six features recomputed from raw by separate code differ in none of the 55,604
feature rows (Table A.20, Appendix VII). A data dictionary documents each of the 88 prepared variables with its source,
transformation, role and sensitivity, following the practice that every dataset comes with a datasheet [9]. The
views are stored as Parquet files (Table A.21), and one command rebuilds them from the pinned figshare download with
byte-identical output; the CC BY 4.0 licence allows sharing them with attribution [5], so the Final Project Package
carries the access instructions, the pipeline and the data dictionary. Synthetic data appear only in unit tests and never
in a view, a statistic or a finding.
