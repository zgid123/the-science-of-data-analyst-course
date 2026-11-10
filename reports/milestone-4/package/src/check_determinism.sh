#!/usr/bin/env bash
# Runs run_dev.sh twice and compares the SHA-256 of every result CSV and frozen model file between the two runs.
# Output: logs/determinism.log (UTC time, command, both hash lists, verdict, exit status).
# Run: bash reports/milestone-4/package/src/check_determinism.sh
set -u
PKG="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PKG"
LOG=logs/determinism.log
mkdir -p logs
hashes() { (cd "$PKG" && shasum -a 256 results/*.csv models/*.joblib models/*.json | sort -k2); }
{
  echo "# utc_start: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "# command: bash src/check_determinism.sh (two runs of src/run_dev.sh)"
  NOTE="determinism check, run 1 of 2" bash src/run_dev.sh; rc1=$?
  hashes > logs/determinism_run1.sha256
  NOTE="determinism check, run 2 of 2" bash src/run_dev.sh; rc2=$?
  hashes > logs/determinism_run2.sha256
  echo "## run 1 (exit $rc1)"; cat logs/determinism_run1.sha256
  echo "## run 2 (exit $rc2)"; cat logs/determinism_run2.sha256
  if [ $rc1 -eq 0 ] && [ $rc2 -eq 0 ] && diff logs/determinism_run1.sha256 logs/determinism_run2.sha256; then
    echo "VERDICT: byte-identical results and models across two runs"; rc=0
  else
    echo "VERDICT: DIFFERENT"; rc=1
  fi
  echo "# utc_end: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "# exit_status: $rc"
} > "$LOG" 2>&1
tail -3 "$LOG"
exit $rc
