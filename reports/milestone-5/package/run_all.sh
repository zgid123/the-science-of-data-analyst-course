#!/usr/bin/env bash
# Rebuild the Final Project Package from the published OULAD files: download and verify the raw tables, prepare the
# analytic-ready views, validate them, compare them with the published prepared dataset, run the AQ1/AQ2 analysis and
# its checks, and compare the results with the shipped ones.
# Each step writes logs/<step>.log: UTC timestamp, command, console output and exit status.
# Usage (from anywhere): bash run_all.sh      (Python 3.12 with requirements.txt installed; set PYTHON to choose one)
set -uo pipefail
PKG="$(cd "$(dirname "$0")" && pwd)"
PY="${PYTHON:-python3}"
cd "$PKG" || exit 1
mkdir -p logs data/raw data/processed results
FAILED_CHECKS=()

run() {  # $1 = step name, $2... = command (run from the package folder)
  local name="$1"; shift
  local shown=("$@"); shown[0]="python"   # the interpreter's path stays out of the log; its version is logged
  { date -u +%Y-%m-%dT%H:%M:%SZ; echo "\$ ${shown[*]}   ($("$PY" --version 2>&1))"; } > "logs/$name.log"
  "$@" >> "logs/$name.log" 2>&1
  local s=$?
  echo "exit $s" >> "logs/$name.log"
  return $s
}
step() {   # a build step: stop at the first failure
  local name="$1"
  if run "$@"; then echo "ok    $name"; else echo "FAILED: $name (see logs/$name.log)"; exit 1; fi
}
check() {  # a comparison step: record the failure, go on, and fail the whole run at the end
  local name="$1"
  if run "$@"; then echo "ok    $name"; else echo "DIFF  $name (see logs/$name.log)"; FAILED_CHECKS+=("$name"); fi
}

step  00_collect_raw     "$PY" src/link_raw.py                 # download the pinned archive, SHA-256 of archive and 7 tables
step  01_understand      "$PY" src/01_understand.py            # dataset understanding map
step  02_profile         "$PY" src/02_profile.py               # profile and quality evidence
step  03_tests           "$PY" -m unittest discover -s tests -v  # formula tests on synthetic fixtures
step  04_prepare         "$PY" src/prepare_data.py             # ten preparation steps -> data/processed
step  05_fit_transforms  "$PY" src/fit_transforms.py           # transforms fitted on the 2013 runs -> model_ready views
check 06_validate        "$PY" src/validate_prepared.py        # validation checks, data dictionary, lineage, manifest
check 07_check_prepared  "$PY" src/checks/check_rebuild.py prepared   # rebuilt views vs the published manifest
step  08_aq_analysis     "$PY" src/analysis/aq_analysis.py     # AQ1 and AQ2 on the 9 runs of 2013 -> results/
step  09_aq1_year_shared "$PY" src/analysis/aq1_year_shared_modules.py
step  10_aq2_sensitivity "$PY" src/analysis/aq2_sensitivity_continuous.py
check 11_aq_checks       "$PY" src/analysis/aq_checks.py       # consistency with Milestones 3 and 4 and statsmodels
check 12_check_results   "$PY" src/checks/check_rebuild.py results     # rebuilt results vs results/checksums.csv

if [ ${#FAILED_CHECKS[@]} -gt 0 ]; then
  echo "finished with differences in: ${FAILED_CHECKS[*]}"; exit 2
fi
echo "finished: every step ok, every check passed"
