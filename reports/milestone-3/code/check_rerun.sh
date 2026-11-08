#!/usr/bin/env bash
# Reproducibility check (brief section 10): run the package twice from raw and compare SHA-256 of every processed file.
set -euo pipefail
PKG="$(cd "$(dirname "$0")/../package" && pwd)"
bash "$PKG/src/run_all.sh"
(cd "$PKG/data/processed" && shasum -a 256 *.parquet) > "$PKG"/logs/rerun1.sha
bash "$PKG/src/run_all.sh"
(cd "$PKG/data/processed" && shasum -a 256 *.parquet) > "$PKG"/logs/rerun2.sha
cat "$PKG"/logs/rerun2.sha
if diff "$PKG"/logs/rerun1.sha "$PKG"/logs/rerun2.sha; then echo "RERUN IDENTICAL: $(wc -l < "$PKG"/logs/rerun2.sha) files"; else echo "RERUN DIFFERS"; exit 1; fi
