# Milestone 5 code

Run from the repository root with the shared `venv` (dependencies: `reports/milestone-5/requirements.txt`).

| Script | Run command | Output |
| :---- | :---- | :---- |
| `freeze_baseline.py` | `venv/bin/python reports/milestone-5/code/freeze_baseline.py` | `research/baseline/m5-baseline.md` |
| `run_T08.sh` (T08 runner) | `bash reports/milestone-5/code/run_T08.sh` | runs the two scripts below; appends to `logs/T08_aq_analysis.log` and `logs/T08_checks.log` |
| `aq_analysis.py` (T08) | `venv/bin/python reports/milestone-5/code/aq_analysis.py` | `results/aq1_*.csv`, `results/aq2_*.csv`, `results/aq_results.json`, `results/aq_summary.md` (2013 runs only; methods in `results/README.md`) |
| `aq_checks.py` (T08) | `venv/bin/python reports/milestone-5/code/aq_checks.py` | consistency checks against Milestones 3–4; exit 1 on any FAIL |
| `aq2_sensitivity_continuous.py` (T14) | `venv/bin/python reports/milestone-5/code/aq2_sensitivity_continuous.py` | `results/aq2_sensitivity_continuous.csv`; post-hoc AQ2 sensitivity with log(1 + clicks on days 0–27) added (log `logs/T14_aq2_sensitivity.log`) |
