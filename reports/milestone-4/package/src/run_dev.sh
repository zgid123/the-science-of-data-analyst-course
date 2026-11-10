#!/usr/bin/env bash
# Phase 1 of the Level 2 prototype: development on the 9 runs of 2013 and the second freeze.
# Runs the tests and steps 01-05; each step's console output goes to logs/<step>.log with its UTC time,
# command and exit status; one entry is appended to logs/experiment_log.md.
# Run from anywhere: bash reports/milestone-4/package/src/run_dev.sh   (PY=<python> to override the interpreter)
set -u
PKG="$(cd "$(dirname "$0")/.." && pwd)"
PY="${PY:-$PKG/../../../venv/bin/python}"
JOBS="${JOBS:--1}"
mkdir -p "$PKG/logs" "$PKG/results" "$PKG/models"
cd "$PKG"
STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
STATUS=""
FAILED=0

run_step() {  # name, command...
  local name="$1"; shift
  local log="logs/$name.log"
  { echo "# step: $name"; echo "# utc_start: $(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "# command: $*"; echo; } > "$log"
  "$@" >> "$log" 2>&1
  local rc=$?
  { echo; echo "# utc_end: $(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "# exit_status: $rc"; } >> "$log"
  echo "$name exit $rc"
  STATUS="$STATUS $name=$rc"
  return $rc
}

run_step tests "$PY" -m unittest discover -s tests -v || FAILED=1
[ $FAILED -eq 0 ] && { run_step 01_load_check "$PY" src/01_load_check.py || FAILED=1; }
[ $FAILED -eq 0 ] && { run_step 02_baselines "$PY" src/02_baselines.py --jobs "$JOBS" || FAILED=1; }
[ $FAILED -eq 0 ] && { run_step 03_dev_folds "$PY" src/03_dev_folds.py --jobs "$JOBS" || FAILED=1; }
[ $FAILED -eq 0 ] && { run_step 04_choose "$PY" src/04_choose.py || FAILED=1; }
[ $FAILED -eq 0 ] && { run_step 05_freeze "$PY" src/05_freeze.py || FAILED=1; }

"$PY" src/log_entry.py --command "bash src/run_dev.sh" --started "$STARTED" --steps "$STATUS" ${NOTE:+--note "$NOTE"}
exit $FAILED
