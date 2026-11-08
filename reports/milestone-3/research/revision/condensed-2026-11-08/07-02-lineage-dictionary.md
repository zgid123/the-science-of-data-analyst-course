## 7.2. Lineage, Dictionary and Version

Every prepared column is documented with its source field, transformation, data type, role and sensitivity, as the
brief requires [1], and validation fails if a column lacks an entry or a predictor list holds an audit, target or
descriptive column (V14). The lineage table of the brief, one row per prepared variable, is Table A.12 in Appendix III.
The version manifest names the prepared dataset OULAD-N04-prepared-1.0 and records the SHA-256 of every raw file,
script and prepared file, the row counts, the repository commit, the Python (3.12.7) and polars (2.1.0) versions and
the creation time in Coordinated Universal Time (UTC).
