#!/usr/bin/env bash
# Phase 2 of the Level 2 prototype: the single test on 2014 and everything that follows it (steps 06-12).
# 06 runs with its guard: first time it records the test access and scores 2014; once the access is recorded it runs
# with --reproduce (same frozen models, no refit, no tuning, byte-identity check of test_runs.csv).
# Each step's console output goes to logs/<step>.log with UTC time, command and exit status; one experiment-log entry.
# Run: bash reports/milestone-4/package/src/run_test.sh   (PY=<python> to override the interpreter)
set -u
PKG="$(cd "$(dirname "$0")/.." && pwd)"
PY="${PY:-$PKG/../../../venv/bin/python}"
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

ACCESS="$("$PY" -c "import sys; sys.path.insert(0, 'src'); import common as C; print(C.test_access_time())")"
run_step tests "$PY" -m unittest discover -s tests -v || FAILED=1
if [ $FAILED -eq 0 ]; then
  if [ -n "$ACCESS" ]; then
    run_step 06_test_reproduce "$PY" src/06_test.py --reproduce || FAILED=1
  else
    run_step 06_test "$PY" src/06_test.py || FAILED=1
  fi
fi
for s in 07_gates 08_fairness 09_sensitivity 10_aq4_lists 11_aq2_replication 12_report; do
  [ $FAILED -eq 0 ] && { run_step "$s" "$PY" "src/$s.py" || FAILED=1; }
done

"$PY" src/log_entry.py --phase 2 --command "bash src/run_test.sh" --started "$STARTED" --steps "$STATUS" \
  ${NOTE:+--note "$NOTE"}
exit $FAILED
