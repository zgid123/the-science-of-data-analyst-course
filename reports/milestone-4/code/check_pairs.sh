#!/usr/bin/env bash
# Check parity of every Vietnamese twin whose English source changed, then record the passing pairs as translated.
# Usage: bash reports/milestone-4/code/check_pairs.sh   (from any folder; logs via run_logged.sh when given a tag)
set -u -o pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"
R=reports/milestone-4/report
S=.claude/skills/build-report/scripts
stale=$(venv/bin/python $S/translation_status.py --report $R --lang vi | awk '/stale|missing/ {print $2}' | sed "s#^#$R/#")
if [ -z "$stale" ]; then echo "no stale pairs"; exit 0; fi
venv/bin/python $S/check_parity.py --report $R --lang vi $stale | tail -3 || exit 1
venv/bin/python $S/translation_status.py --report $R --lang vi --mark $stale | tail -1
