# Clean-copy test

The package was copied without any data (85 files, 856 KiB) to an empty folder outside the team's working
environment, a new Python 3.12.7 virtual environment was built from `requirements.txt` alone, and `run_all.sh` was
run once (9 November 2026, 15:07–15:09 UTC; 81 seconds including the download). The run ended with exit status 0:
every step ran and every check passed.

| Check | Reference | Result |
| :---- | :---- | :---- |
| Raw archive downloaded from the pinned figshare address | SHA-256 in `data/metadata/raw_pins.csv` | archive and 7 of 7 tables MATCH (`data/metadata/raw_check.csv`) |
| Formula tests on synthetic fixtures | `tests/test_features.py` | 9 of 9 tests OK |
| Validation of the prepared views | `src/validate_prepared.py` | 22 of 22 checks PASS (`data/metadata/validation_summary.md`) |
| Rebuilt prepared views | `data/metadata/version_manifest_published.json` (OULAD-N04-prepared-1.0) | 8 of 8 views identical in SHA-256 and row count; the 8 shipped pipeline scripts identical to those that built the published version (`data/metadata/rebuild_check_prepared.csv`) |
| AQ1/AQ2 consistency checks | numbers published in Milestones 3 and 4; statsmodels | 97 PASS, 0 FAIL, 3 INFO (`logs/11_aq_checks.log`) |
| Rebuilt results | `results/checksums.csv` | 21 of 21 files byte-identical (`data/metadata/rebuild_check_results.csv`) |
| Rebuilt results against the result files behind the Milestone 5 report | the analysis output the report quotes | 20 of 21 files byte-identical; in `aq1_year_comparison.csv` every number is equal and only the text of the `source` column of the 54 rows of 2013 names this package's check log (`logs/11_aq_checks.log`) |

Notes on the run: Python's certificate store rejected the download server, so `src/link_raw.py` fetched the archive
with `curl`, as designed, and its SHA-256 matched the pin. The notebook builder of the Milestone 3
pipeline is not part of this package (no notebooks are shipped), so the manifest comparison lists it as not shipped.
Disk use after the run: raw data 443 MB, interim data 61 MB, prepared views 7.6 MB, Python environment 460 MB.
