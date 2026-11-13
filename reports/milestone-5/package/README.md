# Final Project Package – team N04 (MTH045, Milestone 5)

This package holds everything needed to trace and rebuild the results of team N04's final project on early
identification of students at risk of not completing a course. The project uses the Open University Learning
Analytics Dataset (OULAD) as an open stand-in for a university's own records. Four Analytical Questions (AQ) lead
from the Business Goal to the decisions: AQ1 (descriptive: who completes, by module, run and year, and when
non-completers first miss a task), AQ2 (diagnostic: which signs by the end of week 4 go with non-completion), AQ3
(predictive: an early-warning model built on 2013 and tested once on 2014) and AQ4 (ranking students for a list of
limited length). AQ1 and AQ2 are answered with real results on both years of OULAD, the 9 module runs of 2013, the
13 runs of 2014 and the 22 runs pooled, and have the final status Answered. AQ3 is answered by the Level 2 prototype:
a model developed and frozen on the 2013 runs and tested once on the 13 runs of 2014 (final status Answered); AQ4 ranks
the 2014 students on lists of fixed length from that model (final status Partial, because whether a contact helps
needs data that only the pilot can create) (`docs/traceability_matrix.md`).

The package does not contain the OULAD data. One command downloads the published files from a pinned public
address, checks them byte for byte, rebuilds the prepared dataset and the AQ1/AQ2 results for 2013, 2014 and the 22
runs, develops and tests the AQ3 model and builds the AQ4 lists, and compares everything with the published versions.

## Quick start

With Python 3.12 and an internet connection (the archive is 46.8 MB; the full run takes about five minutes on a 10-core laptop,
download included, of which steps 19–27 take three; set `JOBS` to limit the number of parallel processes):

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
  run_all.sh             the one command that rebuilds everything (steps 00-27)
  src/                   preparation pipeline (prepared dataset OULAD-N04-prepared-1.0)
    link_raw.py            step 00: download the pinned archive, check the SHA-256 of the archive and of each table
    01_understand.py       step 01: dataset understanding map (tables, keys, time fields, outcome)
    02_profile.py          step 02: profile and data-quality evidence
    prepare_data.py        step 04: ten preparation steps -> data/processed (views by enrolment, task, week, cut-off)
    fit_transforms.py      step 05: transforms fitted on the 2013 runs only -> model-ready views
    validate_prepared.py   step 06: validation checks; writes the data dictionary, lineage and version manifest
    common.py, dictionary.py  shared paths, keys, category orders and the definition of every prepared variable
    analysis/
      aq_analysis.py               steps 08, 12, 13: AQ1 and AQ2 on one scope (--scope 2013 | 2014 | all)
      aq1_year_shared_modules.py   step 09: 2013 against the published 2014 counts, six shared modules (cross-check)
      aq2_sensitivity_continuous.py  steps 10, 14, 15: AQ2 with a continuous activity adjustment, per scope
      aq_checks.py                 step 11: 2013 results against Milestones 3 and 4 and statsmodels
      aq_year_compare.py           step 16: 2013 against 2014 from the prepared views -> results/compare/
      aq_checks_years.py           step 17: 2014 and 22-run results against Milestone 3 (53 checks)
      aq34_common.py               AQ3/AQ4 loaders with a year guard, candidate models, list rules and metrics
      aq3_develop.py               step 19: AQ3 development on the 2013 runs, model choice, freeze
      aq3_test.py                  step 20: single test on the 13 runs of 2014 (gate S1, sensitivity)
      aq4_lists.py                 step 21: reasons per listed name, fairness rule FR1 (test)
      aq34_scopes.py               steps 22, 23, 24: AQ3/AQ4 views on one scope (--scope 2013 | 2014 | all)
      aq34_compare.py              step 25: 2013 development estimates against the 2014 test
      aq34_checks.py               step 26: AQ3/AQ4 checks (populations, order, second count, Milestone 4 draft)
    checks/check_rebuild.py  steps 07, 18 and 27: rebuilt prepared views and results against the published versions
  tests/                 step 03: 12 unit tests on labelled synthetic data
    test_features.py       formula tests of the feature code (9 tests)
    test_scope.py          scope guard and AQ2 module terms (3 tests)
  data/
    raw/                 the seven OULAD tables, downloaded by step 00 (read-only; not shipped)
    interim/             clicks by enrolment and day; aq3/: fitted models, freeze record, development and 2014 scores (rebuilt; not shipped)
    processed/           the eight prepared views as Parquet files (rebuilt; not shipped)
    metadata/            provenance, data dictionary, quality and change logs, specifications, manifests, checks
  results/               methods note (README.md) and the SHA-256 of every result file (checksums.csv)
    2013/                  AQ1 and AQ2 on the 9 runs of 2013 (CSV, aq_results.json, aq_summary.md)
    2014/                  the same files for the 13 runs of 2014
    all_runs/              the same files for all 22 runs
    compare/               2013 against 2014: rates, first missed task, registration at day 14, AQ2 signs, with
                           aq_summary.md; cross-checks on the 2014 counts published in Milestone 3 (*_published.csv)
                           AQ3 and AQ4 files carry the prefix aq3_ or aq4_ in the same four folders: 2013/ holds the
                           model choice and development estimates (each 2013 run scored by the leave-one-run-out model
                           that left it out), 2014/ the single test of the frozen model (the report's numbers),
                           all_runs/ the 22 runs each scored by a model that did not see it, compare/ development
                           against test (aggregated tables only; no student identifier)
  docs/                  Final Project Traceability Matrix, AI Decision Log
  logs/                  one log per step of the last run; clean_copy_test.md
```

## Steps of `run_all.sh`

Each step writes `logs/<step>.log`, named by its number and name in the table (for example `logs/12_aq_2014.log`).

| Step | Log name | Script | Output |
| :---- | :---- | :---- | :---- |
| 00 | `00_collect_raw` | `src/link_raw.py` | `data/raw/*.csv`, `data/metadata/raw_check.csv` |
| 01 | `01_understand` | `src/01_understand.py` | `data/metadata/understanding_map.md`, `understanding.json` |
| 02 | `02_profile` | `src/02_profile.py` | `data/metadata/profile.json`, `fig_outcome_by_run.csv`, `fig_weekly_activity.csv` |
| 03 | `03_tests` | `python -m unittest discover -s tests` | test outcome in the log (12 tests) |
| 04 | `04_prepare` | `src/prepare_data.py` | `data/processed/*.parquet`, `data/metadata/transformation_log.md` |
| 05 | `05_fit_transforms` | `src/fit_transforms.py` | `data/processed/model_ready_*.parquet`, `data/metadata/transform_params.json`, `predictor_sets.json` |
| 06 | `06_validate` | `src/validate_prepared.py` | `data/metadata/validation_summary.md`, `data_dictionary.md`, `lineage.md`, `rule_rates.csv`, `version_manifest.json` |
| 07 | `07_check_prepared` | `src/checks/check_rebuild.py prepared` | `data/metadata/rebuild_check_prepared.csv` |
| 08 | `08_aq_analysis` | `src/analysis/aq_analysis.py` | `results/2013/` (`aq1_*.csv`, `aq2_*.csv`, `aq_results.json`, `aq_summary.md`); `results/compare/aq1_year_comparison_published.csv`, `aq1_year_difference_published.csv` |
| 09 | `09_aq1_year_shared` | `src/analysis/aq1_year_shared_modules.py` | `results/compare/aq1_year_shared_modules_published.csv` |
| 10 | `10_aq2_sensitivity` | `src/analysis/aq2_sensitivity_continuous.py` | `results/2013/aq2_sensitivity_continuous.csv` |
| 11 | `11_aq_checks` | `src/analysis/aq_checks.py` | check outcome in the log (exit 1 on any failed check) |
| 12 | `12_aq_2014` | `src/analysis/aq_analysis.py --scope 2014` | `results/2014/` |
| 13 | `13_aq_all_runs` | `src/analysis/aq_analysis.py --scope all` | `results/all_runs/` |
| 14 | `14_aq2_sens_2014` | `src/analysis/aq2_sensitivity_continuous.py --scope 2014` | `results/2014/aq2_sensitivity_continuous.csv` |
| 15 | `15_aq2_sens_all` | `src/analysis/aq2_sensitivity_continuous.py --scope all` | `results/all_runs/aq2_sensitivity_continuous.csv` |
| 16 | `16_aq_year_compare` | `src/analysis/aq_year_compare.py` | `results/compare/*.csv`, `results/compare/aq_summary.md` |
| 17 | `17_aq_checks_years` | `src/analysis/aq_checks_years.py` | check outcome in the log (exit 1 on any failed check) |
| 18 | `18_check_results` | `src/checks/check_rebuild.py results` | `data/metadata/rebuild_check_results.csv` |
| 19 | `19_aq3_develop` | `src/analysis/aq3_develop.py` | `results/2013/aq3_dev_folds.csv`, `aq3_dev_choice.csv`, `aq3_final_tuning.csv`, `aq3_choice.json`; `data/interim/aq3/*.pkl`, `freeze.json`, `scores_dev_d27.csv` |
| 20 | `20_aq3_test` | `src/analysis/aq3_test.py` | `results/2014/aq3_s1_gate.csv`, `aq3_sensitivity.csv`, `aq3_calibration_bins.csv`, `aq3_lead_time.csv`; `data/interim/aq3/scores_d13.csv`, `scores_d27.csv` |
| 21 | `21_aq4_lists` | `src/analysis/aq4_lists.py` | `results/2014/aq4_reasons.csv`, `aq4_fairness_confirmatory.csv`; `results/2013/aq3_coefficients.csv` |
| 22 | `22_aq34_2013` | `src/analysis/aq34_scopes.py --scope 2013` | `results/2013/aq3_*.csv`, `aq4_*.csv`, `aq3_summary.md`, `aq4_summary.md` (development estimates) |
| 23 | `23_aq34_2014` | `src/analysis/aq34_scopes.py --scope 2014` | the same files in `results/2014/` (the test) |
| 24 | `24_aq34_all_runs` | `src/analysis/aq34_scopes.py --scope all` | the same files in `results/all_runs/` |
| 25 | `25_aq34_compare` | `src/analysis/aq34_compare.py` | `results/compare/aq3_dev_vs_test.csv`, `aq4_dev_vs_test.csv`, `aq3_summary.md` |
| 26 | `26_aq34_checks` | `src/analysis/aq34_checks.py` | `data/metadata/aq34_checks.csv` (exit 1 on any failed check) |
| 27 | `27_check_results_aq34` | `src/checks/check_rebuild.py results_aq34` | `data/metadata/rebuild_check_results_aq34.csv` |

## Reproducibility

- **Raw data.** Step 00 checks the archive and all seven tables against the SHA-256 values in
  `data/metadata/raw_pins.csv` and stops on any difference.
- **Prepared data.** Step 07 compares the SHA-256 and row count of each of the eight rebuilt views with the published
  manifest of OULAD-N04-prepared-1.0 (`data/metadata/version_manifest_published.json`); the manifest of the latest
  rebuild is `data/metadata/version_manifest.json`. Byte-identical Parquet files need the pinned polars version.
- **Results.** All result files are deterministic: the AQ1/AQ2 steps draw no random numbers, the AQ3/AQ4 steps draw
  them only from the fixed seed 20261112 (tie-breaker, bootstrap, boosted trees), model fits use fixed settings, and
  every value is rounded before it is written. Step 18 compares each of the 63 result files in `results/2013/`,
  `results/2014/`, `results/all_runs/` and `results/compare/` with its SHA-256 in `results/checksums.csv`; step 27 does
  the same for the AQ3/AQ4 files (`aq3_*` and `aq4_*` in the same four folders) with `results/checksums_aq34.csv`.
- **Clean-copy test.** `logs/clean_copy_test.md` records a run of this package copied to an empty folder outside the
  team's working environment, with a new Python environment built from `requirements.txt`.
- **Use of the 2013 and 2014 runs.** AQ1 and AQ2 describe both years: each scope reads only its own runs (filter
  pushed to the reader, then asserted), and step 17 checks that each results folder holds only its own runs. The AQ3
  test keeps the predictors, candidate configurations, selection rule and gate that Milestone 4 fixed on the 2013 runs
  alone, so no 2014 outcome enters any AQ3 choice; the transforms of step 05 are fitted on the 2013 runs only. Step
  19 reads only 2013 rows (filter pushed to the reader, then asserted) and writes a freeze record with the SHA-256 of
  every fitted model; step 20 refuses to read a 2014 outcome without it, and step 26 checks the order. The AQ3/AQ4
  files of `results/2013/` and `results/all_runs/` are development estimates: each 2013 run is scored by the
  leave-one-run-out model that left it out, which the plan uses to choose the model, not to state its performance. The tuning
  criterion of step 19 is the one choice made after 2014 results existed (Change Log C18, `results/README.md`).

## Dependencies

Python 3.12 and the packages in `requirements.txt`: polars 2.1.0 (all data work), statsmodels 0.15.0 with numpy,
scipy, pandas and patsy (AQ2 logistic regression, interval checks and AQ3 calibration), scikit-learn 1.9.1 with
joblib and threadpoolctl (AQ3 models and parallel tuning). The shell script needs `bash`; the download
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
| Controlled Change Log C01–C18 | `data/metadata/change_log.md` |
| Results, populations, methods and deviations from the analysis plan | `results/README.md`; `aq_summary.md` in `results/2013/`, `results/2014/`, `results/all_runs/` and `results/compare/`; `aq3_summary.md` and `aq4_summary.md` in the same four folders |
| Final Project Traceability Matrix | `docs/traceability_matrix.md` |
| AI Decision Log | `docs/ai_decision_log.md` |
