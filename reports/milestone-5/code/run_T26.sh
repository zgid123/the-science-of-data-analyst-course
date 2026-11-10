#!/usr/bin/env bash
# T26 runner: AQ1 and AQ2 completed on the 2014 runs and on all 22 runs (Change Log C15), run with the Final Project
# Package scripts (package/src/analysis/, run_all.sh steps 12-18 and the unit tests), then the task-only cross-check
# against the local experiment. The package's results/{2013,2014,all_runs,compare} are copied to
# reports/milestone-5/results/, which mirrors the package layout.
# Each step appends to logs/T26_<step>.log: UTC timestamp, command, console output and exit status.
# Usage (from anywhere): bash reports/milestone-5/code/run_T26.sh
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
TASK="$(dirname "$HERE")"
ROOT="$(cd "$TASK/../.." && pwd)"
PY="$ROOT/venv/bin/python"
PKG="$TASK/package"
mkdir -p "$TASK/logs"
cd "$PKG" || exit 1

run_step() {  # $1 = step, $2... = command (run from the package folder)
  local log="$TASK/logs/T26_$1.log"; shift
  { echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="; echo "\$ (cd ${PWD#$ROOT/} && ${*#$ROOT/})"; } >> "$log"
  "$@" >> "$log" 2>&1
  local status=$?
  { echo "exit status: $status"; echo ""; } >> "$log"
  echo "T26_$(basename "$log" .log | sed 's/^T26_//'): exit status $status"
  return $status
}

run_step tests            "$PY" -m unittest discover -s tests -v || exit $?
run_step aq_2013          "$PY" src/analysis/aq_analysis.py --scope 2013 || exit $?
run_step aq1_published    "$PY" src/analysis/aq1_year_shared_modules.py || exit $?
run_step aq2_sens_2013    "$PY" src/analysis/aq2_sensitivity_continuous.py --scope 2013 || exit $?
run_step aq_2014          "$PY" src/analysis/aq_analysis.py --scope 2014 || exit $?
run_step aq_all_runs      "$PY" src/analysis/aq_analysis.py --scope all || exit $?
run_step aq2_sens_2014    "$PY" src/analysis/aq2_sensitivity_continuous.py --scope 2014 || exit $?
run_step aq2_sens_all     "$PY" src/analysis/aq2_sensitivity_continuous.py --scope all || exit $?
run_step aq_year_compare  "$PY" src/analysis/aq_year_compare.py || exit $?
run_step aq_checks_years  "$PY" src/analysis/aq_checks_years.py
run_step check_results    "$PY" src/checks/check_rebuild.py results
{ echo "SHA-256 of the new result folders after this run (determinism: compare with the previous run):"
  (cd "$PKG/results" && find 2013 2014 all_runs compare -type f | sort | xargs shasum -a 256); echo ""; } >> "$TASK/logs/T26_aq_year_compare.log"
for d in 2013 2014 all_runs compare; do rm -rf "$TASK/results/$d"; cp -R "$PKG/results/$d" "$TASK/results/$d"; done
echo "copied results/{2013,2014,all_runs,compare} to reports/milestone-5/results/"
cd "$ROOT" && run_step crosscheck_replication "$PY" reports/milestone-5/code/t26_crosscheck_replication.py
