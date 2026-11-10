# Final Project Package – team N04 (MTH045, Milestone 5)

This package holds everything needed to trace and rebuild the results of team N04's final project on early
identification of students at risk of not completing a course. The project uses the Open University Learning
Analytics Dataset (OULAD) as an open stand-in for a university's own records. Four Analytical Questions (AQ) lead
from the Business Goal to the decisions: AQ1 (descriptive: who completes, by module, run and year, and when
non-completers first miss a task), AQ2 (diagnostic: which signs by the end of week 4 go with non-completion), AQ3
(predictive: an early-warning model built on 2013 and tested once on 2014) and AQ4 (ranking students for a list of
limited length). AQ1 and AQ2 are answered with real results on the 9 module runs of 2013 and have the final status
Partial, because their 2014 parts wait until the AQ3 test has opened the 2014 outcomes; AQ3 and AQ4 have a complete
evaluation design and no result yet, with the final status Deferred (`docs/traceability_matrix.md`).

The package does not contain the OULAD data. One command downloads the published files from a pinned public
address, checks them byte for byte, rebuilds the prepared dataset and the AQ1/AQ2 results, and compares both with
the published versions.

## Quick start

With Python 3.12 and an internet connection (the archive is 46.8 MB; the full run takes about one minute after the
download on a laptop):

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHON=.venv/bin/python bash run_all.sh
```

`run_all.sh` prints one line per step and writes each step's UTC time, command, output and exit status to
`logs/<step>.log`. It stops at the first failing build step; a comparison that finds a difference is reported, the
run goes on, and the script ends with exit status 2. Exit status 0 means every step ran and every check passed.

## Project structure

```
package/
  README.md              this file
  requirements.txt       pinned Python dependencies
  run_all.sh             the one command that rebuilds everything (steps 00-12)
  src/                   preparation pipeline (prepared dataset OULAD-N04-prepared-1.0)
    link_raw.py            step 00: download the pinned archive, check the SHA-256 of the archive and of each table
    01_understand.py       step 01: dataset understanding map (tables, keys, time fields, outcome)
    02_profile.py          step 02: profile and data-quality evidence
    prepare_data.py        step 04: ten preparation steps -> data/processed (views by enrolment, task, week, cut-off)
    fit_transforms.py      step 05: transforms fitted on the 2013 runs only -> model-ready views
    validate_prepared.py   step 06: validation checks; writes the data dictionary, lineage and version manifest
    common.py, dictionary.py  shared paths, keys, category orders and the definition of every prepared variable
    analysis/              steps 08-11: AQ1 and AQ2 analysis, the AQ1 shared-module year comparison, the
                           post-hoc AQ2 sensitivity run, and consistency checks
    checks/check_rebuild.py  steps 07 and 12: rebuilt prepared views and results against the published versions
  tests/test_features.py step 03: formula tests of the feature code on labelled synthetic data
  data/
    raw/                 the seven OULAD tables, downloaded by step 00 (read-only; not shipped)
    interim/             clicks by enrolment and day (rebuilt; not shipped)
    processed/           the eight prepared views as Parquet files (rebuilt; not shipped)
    metadata/            provenance, data dictionary, quality and change logs, specifications, manifests, checks
  results/               AQ1 and AQ2 result tables (CSV), key numbers (aq_results.json), summary, methods note
  docs/                  Final Project Traceability Matrix, AI Decision Log
  logs/                  one log per step of the last run; clean_copy_test.md
```

## Steps of `run_all.sh`

| Step | Script | Output |
| :---- | :---- | :---- |
| 00 | `src/link_raw.py` | `data/raw/*.csv`, `data/metadata/raw_check.csv` |
| 01 | `src/01_understand.py` | `data/metadata/understanding_map.md`, `understanding.json` |
| 02 | `src/02_profile.py` | `data/metadata/profile.json`, `fig_outcome_by_run.csv`, `fig_weekly_activity.csv` |
| 03 | `python -m unittest discover -s tests` | `logs/03_tests.log` |
| 04 | `src/prepare_data.py` | `data/processed/*.parquet`, `data/metadata/transformation_log.md` |
| 05 | `src/fit_transforms.py` | `data/processed/model_ready_*.parquet`, `data/metadata/transform_params.json`, `predictor_sets.json` |
| 06 | `src/validate_prepared.py` | `data/metadata/validation_summary.md`, `data_dictionary.md`, `lineage.md`, `rule_rates.csv`, `version_manifest.json` |
| 07 | `src/checks/check_rebuild.py prepared` | `data/metadata/rebuild_check_prepared.csv` |
| 08 | `src/analysis/aq_analysis.py` | `results/aq1_*.csv`, `results/aq2_*.csv`, `aq_results.json`, `aq_summary.md` |
| 09 | `src/analysis/aq1_year_shared_modules.py` | `results/aq1_year_shared_modules.csv` |
| 10 | `src/analysis/aq2_sensitivity_continuous.py` | `results/aq2_sensitivity_continuous.csv` |
| 11 | `src/analysis/aq_checks.py` | `logs/11_aq_checks.log` (exit 1 on any failed check) |
| 12 | `src/checks/check_rebuild.py results` | `data/metadata/rebuild_check_results.csv` |

## Reproducibility

- **Raw data.** Step 00 checks the archive and all seven tables against the SHA-256 values in
  `data/metadata/raw_pins.csv` and stops on any difference.
- **Prepared data.** Step 07 compares the SHA-256 and row count of each of the eight rebuilt views with the published
  manifest of OULAD-N04-prepared-1.0 (`data/metadata/version_manifest_published.json`); the manifest of the latest
  rebuild is `data/metadata/version_manifest.json`. Byte-identical Parquet files need the pinned polars version.
- **Results.** All result files are deterministic; step 12 compares each rebuilt file with `results/checksums.csv`.
- **Clean-copy test.** `logs/clean_copy_test.md` records a run of this package copied to an empty folder outside the
  team's working environment, with a new Python environment built from `requirements.txt`.
- **The 2013-only rule.** The analysis reads only the 2013 rows of every view (filter pushed to the reader, then
  asserted); the 2014 runs stay unopened for the single AQ3 test. The only 2014 information used is the outcome
  count per run in `data/metadata/fig_outcome_by_run.csv` (`results/README.md`).

## Dependencies

Python 3.12 and the packages in `requirements.txt`: polars 2.1.0 (all data work), statsmodels 0.15.0 with numpy,
scipy, pandas and patsy (AQ2 logistic regression and interval checks). The shell script needs `bash`; the download
uses Python's `urllib`, with `curl` as a fallback when Python's certificate store rejects the server. Tested on
macOS with Python 3.12.7.

## Data, licence and citation

OULAD is published by the Knowledge Media Institute of The Open University under the Creative Commons Attribution 4.0
International licence (CC BY 4.0). The copy used is version 1 of the figshare deposit
https://doi.org/10.6084/m9.figshare.5081998.v1 (file 8606371); the pinned hashes, the access date and other
distributions are in `data/metadata/provenance.md`. The data are anonymised by the provider; the package
redistributes no data file and attempts no re-identification. Please cite:

> Kuzilek, J., Hlosta, M. and Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4,
> 170171. https://doi.org/10.1038/sdata.2017.171

BibTeX entries: `data/metadata/citation.bib`.

## Documentation map

| Item | File |
| :---- | :---- |
| Dataset source, version, licence, citation, pinned hashes | `data/metadata/provenance.md`, `raw_pins.csv`, `citation.bib` |
| Prepared dataset and how to rebuild it | this README; `data/metadata/version_manifest_published.json` |
| Data dictionary of the prepared views (every column: type, role, source, transformation, sensitivity) | `data/metadata/data_dictionary.md` |
| Lineage of every prepared variable | `data/metadata/lineage.md` |
| Preparation steps, decisions and quality issues | `data/metadata/transformation_log.md`, `decision_matrix.md`, `quality_issue_log.md` |
| Views and derived variables; split and leakage controls | `data/metadata/feature_spec.md`, `split_spec.md` |
| Validation of the prepared data | `data/metadata/validation_summary.md` |
| Controlled Change Log C01–C17 | `data/metadata/change_log.md` |
| Results, populations, methods and deviations from the analysis plan | `results/README.md`, `results/aq_summary.md` |
| Final Project Traceability Matrix | `docs/traceability_matrix.md` |
| AI Decision Log | `docs/ai_decision_log.md` |
