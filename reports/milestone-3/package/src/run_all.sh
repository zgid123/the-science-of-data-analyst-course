#!/usr/bin/env bash
# Rebuild the Prepared Data Package from the raw OULAD files, step by step (brief section 10).
# Each step's command, UTC timestamp, console output and exit status go to package/logs/<step>.log.
# Usage (from anywhere): bash src/run_all.sh   (Python with requirements.txt installed; set PYTHON to choose one)
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
PKG="$(dirname "$SRC")"
PY="${PYTHON:-python3}"
if [ -z "${PYTHON:-}" ] && [ -x "$PKG/../../../venv/bin/python" ]; then PY="$PKG/../../../venv/bin/python"; fi
mkdir -p "$PKG/logs"
step() {
  local name="$1"; shift
  { date -u +%Y-%m-%dT%H:%M:%SZ; echo "\$ $*"; } > "$PKG/logs/$name.log"
  if (cd "$SRC" && "$@") >> "$PKG/logs/$name.log" 2>&1; then echo "exit 0" >> "$PKG/logs/$name.log"
  else s=$?; echo "exit $s" >> "$PKG/logs/$name.log"; echo "FAILED: $name (see logs/$name.log)"; exit $s; fi
  echo "ok  $name"
}
step 00_link_raw        "$PY" link_raw.py              # raw files: hard links, SHA-256 against the pinned published files
step 01_understand      "$PY" 01_understand.py         # Task 1: Dataset Understanding Map
step 02_profile         "$PY" 02_profile.py            # Task 2: profile and quality evidence
step 03_tests           "$PY" -m unittest discover -s ../tests -v   # formula tests on synthetic fixtures
step 04_prepare         "$PY" prepare_data.py          # Tasks 5-6: ten preparation steps -> data/processed
step 05_fit_transforms  "$PY" fit_transforms.py        # Task 6: train-only fitted transforms -> model_ready
if [ -f "$SRC/validate_prepared.py" ]; then
  step 06_validate      "$PY" validate_prepared.py     # Task 8: validation, dictionary, lineage, version
fi
if [ -f "$SRC/build_notebooks.py" ]; then
  step 07_notebooks     "$PY" build_notebooks.py       # executed notebooks 02 and 03
fi
