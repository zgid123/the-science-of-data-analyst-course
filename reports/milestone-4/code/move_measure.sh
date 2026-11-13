#!/usr/bin/env bash
# Rebuild both languages of the Milestone 4 report and measure the main-text pages after one appendix move.
# Writes logs/<tag>_build.log and logs/<tag>_pages.log (UTC time, command, output, exit status) through run_logged.sh,
# then prints the pessimistic ("laid out") main-content pages of each language on one line.
# Usage: bash reports/milestone-4/code/move_measure.sh <tag>      (for example AM01_context)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../.." && pwd)"
TAG="$1"
cd "$ROOT"
bash "$HERE/run_logged.sh" "${TAG}_build" venv/bin/python .claude/skills/build-report/scripts/report.py build milestone-4 --no-figures > /dev/null
b=$?
bash "$HERE/run_logged.sh" "${TAG}_pages" make pages TASK=milestone-4 BUDGET=12 > /dev/null
grep -E "PASS|FAIL" "reports/milestone-4/logs/${TAG}_build.log" | cut -c1-110
grep -E "^=====|^main content:|^last main-text page" "reports/milestone-4/logs/${TAG}_pages.log"
exit $b
