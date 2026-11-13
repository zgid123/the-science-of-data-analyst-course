#!/usr/bin/env bash
# One measurement cycle of an appendix move (docs/appendix-move-brief.md, rules 1 and 4): regenerate the English
# appendices from research/appendix/, rebuild both Word documents, then measure the pessimistic page count of each
# language. Every step is logged by run_logged.sh in reports/milestone-3/logs/<tag>_<step>.log.
# Usage: bash reports/milestone-3/code/move_cycle.sh <tag>        (for example M1 or M1b)
set -u
TAG="$1"
HERE="$(cd "$(dirname "$0")" && pwd)"
RUN="bash $HERE/run_logged.sh"
R=".claude/skills/build-report/scripts"
$RUN "${TAG}_appendices" venv/bin/python reports/milestone-3/code/build_appendices.py > /dev/null || exit 1
$RUN "${TAG}_build" venv/bin/python "$R/report.py" build milestone-3 > /dev/null || { tail -40 "$HERE/../logs/${TAG}_build.log"; exit 1; }
$RUN "${TAG}_pages" make pages TASK=milestone-3 BUDGET=12 | grep -E "^=====|main content:|last main-text page"
for L in EN VI; do
  $RUN "${TAG}_blocks_$L" venv/bin/python "$R/page_budget.py" "reports/milestone-3/build/N04_Milestone3_$L.docx" --blocks > /dev/null
done
