#!/usr/bin/env bash
# Phase-2 determinism: runs run_test.sh twice (06 in --reproduce mode, then 07-12) and compares the SHA-256 of every
# result CSV, AQ4 list, report file and figure. freeze.csv is not rewritten by these runs, so its access time is
# excluded by construction (its hash is listed separately as a check that it did not change).
# Output: logs/determinism_test.log. Run: bash reports/milestone-4/package/src/check_determinism_test.sh
set -u
PKG="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PKG"
LOG=logs/determinism_test.log
hashes() { shasum -a 256 $(ls results/*.csv results/aq4_lists/*.csv report/*.md report/*.html report/figures/*.png \
  | grep -v '^results/freeze.csv$') | sort -k2; }
{
  echo "# utc_start: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "# command: bash src/check_determinism_test.sh (two runs of src/run_test.sh)"
  F0="$(shasum -a 256 results/freeze.csv)"
  NOTE="phase-2 determinism check, run 1 of 2" bash src/run_test.sh; rc1=$?
  hashes > logs/determinism_test_run1.sha256
  NOTE="phase-2 determinism check, run 2 of 2" bash src/run_test.sh; rc2=$?
  hashes > logs/determinism_test_run2.sha256
  F2="$(shasum -a 256 results/freeze.csv)"
  echo "## run 1 (exit $rc1)"; cat logs/determinism_test_run1.sha256
  echo "## run 2 (exit $rc2)"; cat logs/determinism_test_run2.sha256
  echo "## freeze.csv before / after: $F0 / $F2"
  if [ $rc1 -eq 0 ] && [ $rc2 -eq 0 ] && [ "$F0" = "$F2" ] && \
     diff logs/determinism_test_run1.sha256 logs/determinism_test_run2.sha256; then
    echo "VERDICT: byte-identical outputs of 06 (reproduce) to 12 across two runs; freeze.csv unchanged"; rc=0
  else
    echo "VERDICT: DIFFERENT"; rc=1
  fi
  echo "# utc_end: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "# exit_status: $rc"
} > "$LOG" 2>&1
tail -3 "$LOG"
exit $rc
