# Milestone 5 code

Run from the repository root with the shared `venv` (dependencies: `reports/milestone-5/requirements.txt`).

| Script | Run command | Output |
| :---- | :---- | :---- |
| `freeze_baseline.py` | `venv/bin/python reports/milestone-5/code/freeze_baseline.py` | `research/baseline/m5-baseline.md` |
| `run_T08.sh` (T08 runner) | `bash reports/milestone-5/code/run_T08.sh` | runs the two scripts below; appends to `logs/T08_aq_analysis.log` and `logs/T08_checks.log` |
| `aq_analysis.py` (T08) | `venv/bin/python reports/milestone-5/code/aq_analysis.py` | `results/2013/aq1_*.csv`, `results/2013/aq2_*.csv`, `results/2013/aq_results.json`, `results/2013/aq_summary.md` (2013 runs only; methods in `results/README.md`) |
| `aq_checks.py` (T08) | `venv/bin/python reports/milestone-5/code/aq_checks.py` | consistency checks against Milestones 3–4; exit 1 on any FAIL |
| `aq2_sensitivity_continuous.py` (T14) | `venv/bin/python reports/milestone-5/code/aq2_sensitivity_continuous.py` | `results/2013/aq2_sensitivity_continuous.csv`; post-hoc AQ2 sensitivity with log(1 + clicks on days 0–27) added (log `logs/T14_aq2_sensitivity.log`) |
| `t15_move_to_appendix.py` (T15) | `venv/bin/python reports/milestone-5/code/t15_move_to_appendix.py` | writes `report/16-00-appendices.md` and `16-01 … 16-16` from the full draft (commit `a6a8d5a`) plus the facts in `RESTORED`; main-text files are written by hand |
| `t15_measure.sh` (T15) | `bash reports/milestone-5/code/t15_measure.sh "<label>"` | builds the English report and appends page measurements to `logs/T15_move_appendix.log` |
| `t15_loss_check.py` (T15) | `venv/bin/python reports/milestone-5/code/t15_loss_check.py` | lists full-draft sentences and table rows found nowhere in the current report (log and review `logs/T15_loss_check.log`) |
| `t16_abbreviation_fixes.py` (T16) | `venv/bin/python reports/milestone-5/code/t16_abbreviation_fixes.py` | puts each abbreviation's definition on its first-use line and removes repeated full forms in `report/`; idempotent (log `logs/T16_front_matter.log`) |
| `t19_number_sample.py` (T19) | `venv/bin/python reports/milestone-5/code/t19_number_sample.py > reports/milestone-5/results/t19/number_sample.md` | seeded sample (seed 20261109) of 25 main-text sentences and table rows with numbers, traced in `research/spot-check.md` (log `logs/T19_spot_check.log`) |
| `t19_trace_checks.py` (T19) | `venv/bin/python reports/milestone-5/code/t19_trace_checks.py` | recounts the runs with a TMA or CMA due by day 13 and day 27 from `datasets/oulad/assessments.csv` (log `logs/T19_spot_check.log`) |
| `deck_full_script.py` (T31) | `venv/bin/python reports/milestone-5/code/deck_full_script.py` | `presentation/v2-full/speech-script.md` from `presentation/v2-full/script-parts/part1–4.md` and the ensemble plan; exit 1 if a plan slide has no section or the order differs |
| `deck_appendix_split.py` (T31) | `venv/bin/python reports/milestone-5/code/deck_appendix_split.py` | `presentation/v2-full/appendix-split.md` from the split in `build_slides_milestone5_full.py`; exit 1 if an appendix slide has no reason |
