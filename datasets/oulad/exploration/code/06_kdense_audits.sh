#!/usr/bin/env bash
# Independent audits with the exploratory-data-analysis skill (K-Dense) -> evidence/*.json.
# The skill scripts need absolute paths; studentVle (433 MB) is read up to its first 1,000,000 rows.
# Stage 6 - run from anywhere: bash datasets/oulad/exploration/code/06_kdense_audits.sh
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
D="$REPO/datasets/oulad"
K="$REPO/.agents/skills/exploratory-data-analysis/scripts"
E="$HERE/evidence"
BIG=(--max-bytes 536870912 --max-rows 1000000)
mkdir -p "$E"

run() {  # run <output name> <script> <args...>; prints the command, then a one-line result
  local out="$E/$1.json"; shift
  echo "\$ python3 $*"
  python3 "$K/$@" > "$out" 2>&1
  python3 -c "import json,sys;a=json.load(open(sys.argv[1])).get('analysis',{});print('  ->', sys.argv[1].rsplit('/',1)[-1], 'rows_scanned', a.get('rows_scanned'), 'row_limit_reached', a.get('row_limit_reached'))" "$out"
}

for t in courses assessments vle studentInfo studentRegistration; do
  run "kdense_profile_$t" tabular_profile.py "$D/$t.csv" --root "$D" --reveal-identifiers
done
run kdense_profile_studentAssessment tabular_profile.py "$D/studentAssessment.csv" --root "$D" --reveal-identifiers --max-rows 1000000
run kdense_profile_studentVle_first1M tabular_profile.py "$D/studentVle.csv" --root "$D" --reveal-identifiers "${BIG[@]}"
run kdense_leakage_studentInfo missingness_leakage_audit.py "$D/studentInfo.csv" --root "$D" \
  --entity-column id_student --group-column code_module --reveal-identifiers
run kdense_sensitivity_score distribution_sensitivity.py "$D/studentAssessment.csv" --root "$D" \
  --column score --max-rows 1000000 --reveal-identifiers
run kdense_sensitivity_sum_click_first1M distribution_sensitivity.py "$D/studentVle.csv" --root "$D" \
  --column sum_click "${BIG[@]}" --reveal-identifiers
find "$REPO/.agents/skills/exploratory-data-analysis" -name __pycache__ -type d -exec rm -rf {} +
