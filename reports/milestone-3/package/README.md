# Prepared Data Package – Milestone 3 (team N04)

The pipeline, prepared data and metadata that turn the raw Open University Learning Analytics Dataset (OULAD) into
analytic-ready views for Milestone 4 (brief section 16, deliverables C and D, with B, E and F in `data/metadata/`).
Prepared dataset version: `OULAD-N04-prepared-1.0` (`data/metadata/version_manifest.json`).

```
package/
  README.md
  requirements.txt
  data/
    raw/         the seven OULAD CSV tables, read-only, checked against the SHA-256 in metadata/raw_pins.csv
    interim/     clicks by enrolment and day, resources by enrolment and day (rebuilt)
    processed/   analytic-ready views (rebuilt): enrolment, assessment_due, student_week, features_d13,
                 features_d27, capacity_by_run, model_ready_d13, model_ready_d27 (Parquet)
    metadata/    understanding map, profile, quality issue log, decision matrix, feature and split specifications,
                 transformation log, transform parameters, predictor sets, data dictionary, lineage, validation
                 summary, version manifest, traceability (B), change log (E), AI decision log (F)
  notebooks/     02_data_understanding.ipynb, 03_data_preparation.ipynb (executed)
  src/           link_raw, 01_understand, 02_profile, prepare_data, fit_transforms, validate_prepared,
                 build_notebooks, common, dictionary; run_all.sh
  tests/         formula tests on labelled synthetic fixtures (brief section 8.3, level A)
  logs/          one log per step of the last run_all.sh (UTC time, command, output, exit status)
```

## Rebuild from raw

Run from this folder, with Python 3.12 or later:

```bash
python -m pip install -r requirements.txt
bash src/run_all.sh          # steps 00-07, about 15 seconds once the raw files are in place
```

Step 00 uses the raw files in `data/raw/` when they are present. Otherwise it downloads the OULAD archive from the
figshare deposit cited by the data descriptor (DOI 10.6084/m9.figshare.5081998.v1, 46.8 MB) and extracts the seven
tables. Every table is checked against the SHA-256 in `data/metadata/raw_pins.csv` before any step reads it.
`run_all.sh` uses `python3`, or the interpreter named in the `PYTHON` environment variable, and stops at the first
failing step. Two runs from raw write identical files: the SHA-256 of all eight views is equal across runs. The
hashes, row counts and code hashes of the prepared files are in `data/metadata/version_manifest.json`.

## Steps

| Step | Script | Brief | Output |
| :---- | :---- | :---- | :---- |
| 00 | `link_raw.py` | section 3 (raw immutable) | `metadata/raw_check.csv` |
| 01 | `01_understand.py` | Task 1 | `metadata/understanding_map.md`, `understanding.json` |
| 02 | `02_profile.py` | Task 2 | `metadata/profile.json`, `profile_crosscheck.csv`, figure data |
| 03 | `python -m unittest` on `tests/` | Task 8 (formula check) | `logs/03_tests.log` |
| 04 | `prepare_data.py` | Tasks 5–6 | `processed/*.parquet`, `metadata/transformation_log.md` |
| 05 | `fit_transforms.py` | Task 6 | `processed/model_ready_*.parquet`, `metadata/transform_params.json`, `predictor_sets.json` |
| 06 | `validate_prepared.py` | Task 8 | `metadata/validation_summary.md`, `data_dictionary.md`, `lineage.md`, `version_manifest.json` |
| 07 | `build_notebooks.py` | section 10.1 | `notebooks/*.ipynb` |

## Using the views in Milestone 4

- Model inputs are only the columns listed in `metadata/predictor_sets.json`; identifier, split, evaluation, target,
  rule and audit columns are never inputs.
- Train on `split = train` (2013 runs), test on `split = test` (2014 runs); tune with leave-one-run-out folds inside
  2013 that keep each student in one fold. Report test results for paired and unpaired runs separately, and with
  and without `eval_withdrawal_day_unknown` and `student_in_training_runs`.
- `early_sign_rule` is the comparison rule (C10); `capacity_by_run` gives the list sizes of the AQ4 scenarios.

License of the data: CC BY 4.0; cite Kuzilek, Hlosta and Zdrahal (2017), Scientific Data 4, 170171.
