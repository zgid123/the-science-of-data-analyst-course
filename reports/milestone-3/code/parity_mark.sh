#!/usr/bin/env bash
# Check each changed English/Vietnamese pair with check_parity.py and record it with translation_status.py --mark
# (docs/appendix-move-brief.md, rule 6). Logged in reports/milestone-3/logs/<tag>_parity_mark.log.
# Usage: bash reports/milestone-3/code/parity_mark.sh <tag> <section base name> ...   (e.g. M2 02-02-outcome-time-measures)
set -u
TAG="$1"; shift
HERE="$(cd "$(dirname "$0")" && pwd)"
D=reports/milestone-3/report
R=.claude/skills/build-report/scripts
FILES=()
for b in "$@"; do FILES+=("$D/$b.md"); done
bash "$HERE/run_logged.sh" "${TAG}_parity_mark" bash -c \
  "venv/bin/python $R/check_parity.py --report $D --lang vi ${FILES[*]} && venv/bin/python $R/translation_status.py --report $D --lang vi --mark ${FILES[*]}" \
  | grep -v "WARN  12-05" | tail -6
