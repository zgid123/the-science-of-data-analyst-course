#!/usr/bin/env bash
# Rebuild the whole exploration, stage by stage, and keep each step's console output in logs/<step>.log.
# Run from anywhere: bash datasets/oulad/exploration/code/run_all.sh
# Optional: DATAVIZ_VALIDATOR=<path to dataviz skill's scripts/validate_palette.js> also records the palette check.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
PY="$REPO/venv/bin/python"
C="$HERE/code"
LOGS="$HERE/logs"
mkdir -p "$LOGS"

step() {  # step <name> <command...>: header with date and command, then output, into logs/<name>.log
  local name="$1"; shift
  { echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ)  \$ $*"; "$@"; echo "# exit 0"; } 2>&1 | tee "$LOGS/$name.log"
}

step 00_verify_dataset "$PY" "$REPO/scripts/fetch-datasets/fetch_datasets.py" --verify oulad
step 01_profile        "$PY" "$C/01_profile.py"
step 02_features       "$PY" "$C/02_features.py"
step 03_describe       "$PY" "$C/03_describe.py"
step 04_multivariate   "$PY" "$C/04_multivariate.py"
step 05_crosscheck     "$PY" "$C/05_crosscheck.py"
step 06_kdense_audits  bash "$C/06_kdense_audits.sh"
step 07_build_report   "$PY" "$C/07_build_report.py"
step 10_scope_feasibility "$PY" "$C/10_scope_feasibility.py"   # Milestone 1 proposal scope (reports/milestone-1)
if [[ -n "${DATAVIZ_VALIDATOR:-}" ]]; then
  # outcome palette (Withdrawn, Fail, Pass, Distinction) and trajectory-cluster palette, on the page surface #ffffff
  step 08_palette_check bash -c "node '$DATAVIZ_VALIDATOR' '#c23a3a,#ec7b70,#5598e7,#184f95' --mode light --surface '#ffffff' && node '$DATAVIZ_VALIDATOR' '#2a78d6,#eb6834,#1baf7a' --mode light --surface '#ffffff'"
fi
find "$HERE" -name __pycache__ -type d -exec rm -rf {} +
