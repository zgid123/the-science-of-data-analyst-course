#!/usr/bin/env bash
# Run one command from the repository root and save its record in reports/milestone-4/logs/<name>.log:
# UTC timestamp, the command, the full console output and the exit status (project rule "working out loud").
# Usage: bash reports/milestone-4/code/run_logged.sh <log-name> <command> [args...]
set -u
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
LOG="$ROOT/reports/milestone-4/logs/$1.log"; shift
cd "$ROOT"
{
  date -u +%Y-%m-%dT%H:%M:%SZ
  echo "\$ $*"
  "$@" 2>&1
  status=$?
  echo "exit $status"
} > "$LOG"
cat "$LOG"
exit "$(tail -1 "$LOG" | awk '{print $2}')"
