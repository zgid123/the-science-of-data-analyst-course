#!/usr/bin/env bash
# Check and record Vietnamese twins after an edit, then run the pre-checks, logging to logs/R22_<STEP>_checks.log.
# Usage (from the repository root): bash reports/milestone-2/code/check_pair.sh STEP FILE.md [FILE.md ...]
set -u
STEP="$1"; shift
R=reports/milestone-2/report; P=.claude/skills/build-report/scripts
FILES=(); for f in "$@"; do FILES+=("$R/$f"); done
LOG="reports/milestone-2/logs/R22_${STEP}_checks.log"
{
  echo "UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "CMD: check_parity.py --report $R --lang vi $*"; venv/bin/python $P/check_parity.py --report $R --lang vi "${FILES[@]}" 2>&1; echo "EXIT: $?"
  echo "CMD: translation_status.py --report $R --lang vi --mark $*"; venv/bin/python $P/translation_status.py --report $R --lang vi --mark "${FILES[@]}" 2>&1; echo "EXIT: $?"
  echo "CMD: make precheck TASK=milestone-2"; make precheck TASK=milestone-2 2>&1; echo "EXIT: $?"
} > "$LOG"
grep -E "Checked|recorded|FAIL|ERROR|steps passed|EXIT" "$LOG"
