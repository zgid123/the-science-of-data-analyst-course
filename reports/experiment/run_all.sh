#!/usr/bin/env bash
# Every step of the analysis, in order. Each step runs through tools/run_step.py, which stops the script when a
# step fails and writes logs/<step>.md and a row of logs/experiment-log.md.
#
#   bash run_all.sh               uses the repository's shared venv (../../venv) when it exists; set PYTHON to override
#
# Order protects the 2014 test runs: AQ2 is estimated on 2013, AQ3 is developed on 2013 and frozen, and only then
# does any step read a 2014 outcome (each such step calls holdout_guard.open_holdout and is logged).
set -euo pipefail
cd "$(dirname "$0")"
if [ -n "${PYTHON:-}" ]; then PY="$PYTHON"; elif [ -x ../../venv/bin/python ]; then PY=../../venv/bin/python; else PY=python3; fi
step() { "$PY" tools/run_step.py "$1" -- "$PY" "${@:2}"; }
"$PY" tools/run_step.py --new-run

# Stage 4 – inputs: the prepared dataset OULAD-N04-prepared-1.0 and five raw OULAD tables, pinned by SHA-256
step 00_verify_inputs  tools/data_manifest.py verify data-manifest.json

# Stage 5 – profile the prepared views
P=../milestone-3/package/data/processed
step 01_profile        tools/profile_data.py $P/enrolment.parquet $P/features_d13.parquet $P/features_d27.parquet $P/assessment_due.parquet -o results/profile.md

# Stage 6 – populations reconcile with the design (no 2014 outcome read)
step 02_prepare        code/02_prepare.py

# Stage 7 – before the freeze: AQ2 on 2013, AQ3 development on 2013
step 03_aq2_2013       code/03_aq2.py 2013
step 04_aq3_dev        code/04_aq3_dev.py

# Freeze: choices, model code and the 10 fitted models, before any 2014 outcome is read
step 05_freeze         tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl

# After the freeze: score the 2014 runs once, then every view reads the saved scores
step 06_aq3_score      code/06_aq3_score.py
step 07_aq3_evaluate   code/07_aq3_evaluate.py
step 08_aq4_lists      code/08_aq4_lists.py
step 09_aq2_2014       code/03_aq2.py 2014
step 10_aq2_compare    code/10_aq2_compare.py
step 11_aq1            code/11_aq1.py

# Stage 8 – a second code path for the headline numbers, and the comparison with the earlier team implementation
step 12_recompute      code/12_recompute.py
step 13_compare_prior  code/13_compare_prior.py
step 13b_compare_m4    code/16_compare_m4.py
step 14_holdout_order  tools/holdout_guard.py status --record results/freeze.json --access logs/holdout-access.md
step 14b_headlines     code/14_headlines.py

# Stage 9 – figures, tables written into the report from results/, then the report check
step 15_figures        code/15_figures.py
step 98_fill_tables    tools/report_tables.py fill report.md
step 99_check_report   tools/check_report.py report.md --claims claims.json
step 99b_fill_comparison tools/report_tables.py fill comparison.md
step 99c_check_comparison tools/check_report.py comparison.md --claims comparison-claims.json
