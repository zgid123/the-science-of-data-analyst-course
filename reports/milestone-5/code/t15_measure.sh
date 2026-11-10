#!/usr/bin/env bash
# T15: build the English report and measure its main-text pages; appends to logs/T15_move_appendix.log.
# Usage: bash reports/milestone-5/code/t15_measure.sh "<label>"
cd "$(dirname "$0")/../../.." || exit 1
LOG=reports/milestone-5/logs/T15_move_appendix.log
{
  echo "## $(date -u +%Y-%m-%dT%H:%M:%SZ) $1"
  echo '$ venv/bin/python .claude/skills/build-report/scripts/report.py build milestone-5 --lang en --force'
  venv/bin/python .claude/skills/build-report/scripts/report.py build milestone-5 --lang en --force 2>&1 | tail -3
  echo "exit ${PIPESTATUS[0]}"
  echo '$ venv/bin/python .claude/skills/build-report/scripts/page_budget.py reports/milestone-5/build/N04_Milestone5_EN.docx --budget 25'
  venv/bin/python .claude/skills/build-report/scripts/page_budget.py reports/milestone-5/build/N04_Milestone5_EN.docx --budget 25 2>&1
  echo "exit ${PIPESTATUS[0]}"
  echo '$ venv/bin/python .claude/skills/build-report/scripts/page_budget.py reports/milestone-5/build/N04_Milestone5_EN.docx --budget 25 --blocks'
  venv/bin/python .claude/skills/build-report/scripts/page_budget.py reports/milestone-5/build/N04_Milestone5_EN.docx --budget 25 --blocks 2>&1
  echo "exit ${PIPESTATUS[0]}"
} >> "$LOG" 2>&1
