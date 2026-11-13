#!/usr/bin/env bash
# Rebuild both languages of the Milestone 2 report and measure its pages (pessimistic layout), logging each run.
# Usage (from the repository root): bash reports/milestone-2/code/measure_move.sh STEP [--blocks]
#   writes reports/milestone-2/logs/R22_<STEP>_build.log, R22_<STEP>_pages.log and, with --blocks,
#   R22_<STEP>_blocks_{EN,VI}.log; each log holds its UTC time, command, output and exit status.
set -u
STEP="$1"; BLOCKS="${2:-}"
LOGS="reports/milestone-2/logs"
run() {  # run LOGFILE CMD...
  local log="$1"; shift
  { echo "UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "CMD: $*"; "$@" 2>&1; echo "EXIT: $?"; } > "$log"
}
run "$LOGS/R22_${STEP}_build.log" make build TASK=milestone-2
run "$LOGS/R22_${STEP}_pages.log" make pages TASK=milestone-2 BUDGET=10
if [ "$BLOCKS" = "--blocks" ]; then
  for L in EN VI; do
    run "$LOGS/R22_${STEP}_blocks_${L}.log" venv/bin/python .claude/skills/build-report/scripts/page_budget.py \
      "reports/milestone-2/build/N04_Milestone2_${L}.docx" --blocks
  done
fi
grep -E "EXIT|FAIL" "$LOGS/R22_${STEP}_build.log"
grep -E "^main content|last main-text" "$LOGS/R22_${STEP}_pages.log"
