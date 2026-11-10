#!/usr/bin/env bash
# T08 runner: AQ1/AQ2 analysis on the 2013 runs, then the consistency checks.
# Each step appends to its log: UTC timestamp, command, console output and exit status.
# Usage (from anywhere): bash reports/milestone-5/code/run_T08.sh
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
TASK="$(dirname "$HERE")"
ROOT="$(cd "$TASK/../.." && pwd)"
PY="$ROOT/venv/bin/python"
mkdir -p "$TASK/logs" "$TASK/results"
cd "$ROOT" || exit 1

run_step() {  # $1 = log file, $2... = command
  local log="$1"; shift
  {
    echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    echo "\$ ${*#$ROOT/}"
  } >> "$log"
  "$@" >> "$log" 2>&1
  local status=$?
  echo "exit status: $status" >> "$log"
  echo "" >> "$log"
  echo "$(basename "$log"): exit status $status"
  return $status
}

run_step "$TASK/logs/T08_aq_analysis.log" "$PY" reports/milestone-5/code/aq_analysis.py || exit $?
{ echo "SHA-256 of results after this run (determinism: compare with the previous run):"
  (cd "$TASK/results" && shasum -a 256 2013/aq1_*.csv 2013/aq2_*.csv 2013/aq_results.json 2013/aq_summary.md compare/aq1_year_*_published.csv); echo ""; } >> "$TASK/logs/T08_aq_analysis.log"
run_step "$TASK/logs/T08_checks.log" "$PY" reports/milestone-5/code/aq_checks.py
