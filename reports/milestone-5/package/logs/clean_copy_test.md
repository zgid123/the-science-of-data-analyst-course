# Clean-copy test

The package was copied without any data (117 files, 1.3 MiB: code, tests, `data/metadata/`, `results/`, `docs/`; no
`data/raw/`, `data/interim/`, `data/processed/` or `logs/`) to an empty folder outside the team's working environment,
a new Python 3.12.7 virtual environment was built from `requirements.txt` alone, and `run_all.sh` was run once
(10 November 2026, 17:58:40–18:00:17 UTC; 97 seconds including the download). The run ended with exit status 0:
every one of the 19 steps (00–18) printed "ok" and the script ended with "finished: every step ok, every check
passed".

```bash
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
PYTHON=.venv/bin/python bash run_all.sh
```

| Check | Reference | Result |
| :---- | :---- | :---- |
| Raw archive downloaded from the pinned figshare address (step 00) | SHA-256 in `data/metadata/raw_pins.csv` | archive and 7 of 7 tables MATCH (`data/metadata/raw_check.csv`) |
| Unit tests on synthetic fixtures (step 03) | `tests/test_features.py`, `tests/test_scope.py` | 12 of 12 tests OK (9 formula tests, 3 scope and module-term tests) |
| Validation of the prepared views (step 06) | `src/validate_prepared.py` | 22 of 22 checks PASS (`data/metadata/validation_summary.md`) |
| Rebuilt prepared views (step 07) | `data/metadata/version_manifest_published.json` (OULAD-N04-prepared-1.0) | 8 of 8 views identical in SHA-256 and row count, raw inputs all match; the 8 shipped pipeline scripts identical to those that built the published version (`data/metadata/rebuild_check_prepared.csv`) |
| AQ1/AQ2 consistency checks, 2013 (step 11) | numbers published in Milestones 3 and 4; statsmodels | 96 PASS, 0 FAIL, 3 INFO (`logs/11_aq_checks.log`) |
| AQ1 and AQ2 on 2014 and on all 22 runs, year comparison (steps 12–16) | – | each step exit 0; every AQ2 model converged |
| Checks of the 2014 and 22-run results (step 17) | 2014 counts and 22-run totals published in Milestone 3; two aggregation paths; scope purity; C12 concurrent count | 53 PASS, 0 FAIL (`logs/17_aq_checks_years.log`) |
| Rebuilt results (step 18) | `results/checksums.csv` | 63 of 63 files byte-identical in `results/2013/`, `results/2014/`, `results/all_runs/` and `results/compare/` (`data/metadata/rebuild_check_results.csv`) |
| Rebuilt results against the result files behind the Milestone 5 report | the analysis output the report quotes | 58 of 63 files byte-identical; in `compare/aq1_year_comparison_published.csv` every number is equal and only the text of the `source` column of the 54 rows of 2013 names this package's check log (`logs/11_aq_checks.log`); the four `aq_summary.md` files hold the same tables, with headings and the writer's name in this package's words |

| Step | Outcome | Step | Outcome |
| :---- | :---- | :---- | :---- |
| 00_collect_raw | ok | 10_aq2_sensitivity | ok |
| 01_understand | ok | 11_aq_checks | ok |
| 02_profile | ok | 12_aq_2014 | ok |
| 03_tests | ok | 13_aq_all_runs | ok |
| 04_prepare | ok | 14_aq2_sens_2014 | ok |
| 05_fit_transforms | ok | 15_aq2_sens_all | ok |
| 06_validate | ok | 16_aq_year_compare | ok |
| 07_check_prepared | ok | 17_aq_checks_years | ok |
| 08_aq_analysis | ok | 18_check_results | ok |
| 09_aq1_year_shared | ok | | |

Notes on the run: Python's certificate store rejected the download server, so `src/link_raw.py` fetched the archive
with `curl`, as designed, and its SHA-256 matched the pin. The notebook builder of the Milestone 3 pipeline is not
part of this package (no notebooks are shipped), so the manifest comparison lists it as not shipped. The metadata files
that steps 01–06 rewrite carry the time of the run; in addition, `data/metadata/fig_outcome_by_run.csv` was written
with its four outcome columns in a different order and `data/metadata/profile.json` with its list of regions in a
different order, the values being the same, and no result file changes, since every script reads these columns by
name. Disk use after the run: raw data 443 MB, interim data 61 MB, prepared views 7.6 MB, Python environment 460 MB.
