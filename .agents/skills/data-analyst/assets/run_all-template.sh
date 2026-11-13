#!/usr/bin/env bash
# Every step of the analysis, in order. Each step is run through tools/run_step.py, which stops the script when a
# step fails and writes logs/<step>.md and a row of logs/experiment-log.md.
#
#   python3 tools/setup_env.py    once: creates .venv with the packages of requirements.txt
#   bash run_all.sh               uses .venv/bin/python when it exists, python3 otherwise; set PYTHON to override
set -euo pipefail
cd "$(dirname "$0")"
if [ -z "${PYTHON:-}" ] && [ -x .venv/bin/python ]; then PY=.venv/bin/python; else PY="${PYTHON:-python3}"; fi
step() { "$PY" tools/run_step.py "$1" -- "$PY" "${@:2}"; }
"$PY" tools/run_step.py --new-run

# Stage 4 – inputs are the files recorded in data-manifest.json (write it once: tools/data_manifest.py write <files>)
step 00_verify_inputs  tools/data_manifest.py verify data-manifest.json

# Stage 5 – profile the inputs (all files in one call)
# step 01_profile      tools/profile_data.py data/<file>.csv -o results/profile.md

# Stage 6 – preparation: one script per prepared table, each reconciling its row counts
# step 02_prepare      code/02_prepare.py

# Stage 7 – analysis: each script saves its result tables under results/
# step 03_analyse      code/03_analyse.py

# Predictive work only – freeze before the holdout is read (tools/holdout_guard.py), then score once
# step 04a_freeze      tools/holdout_guard.py freeze --record results/freeze.json --choices code/choices.json code/model.py
# step 04b_test        code/04b_test.py         # open_holdout(...) first; exits at once if scores_saved(...) is true
# step 04c_describe    code/04c_describe.py     # whole-population description: after the freeze, calls open_holdout(...)

# Stage 8 – a second code path for the headline numbers, and the comparison with another implementation if one exists
# step 05_recompute    code/05_recompute.py
# step 06_compare      tools/compare_results.py results/<mine>.csv <theirs>.csv --keys <k> --cols <c> --tol 0.0005

# Stage 9 – tables written into the report from results/, then the report check
# step 98_fill_tables  tools/report_tables.py fill report.md
# step 99_check_report tools/check_report.py report.md --claims claims.json
