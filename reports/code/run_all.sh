#!/usr/bin/env bash
# Milestone 4 Level 2 prototype – run every step in the order of the protocol (PROTOCOL.md, P02 and P23).
#
#   bash run_all.sh                    from reports/code; uses ../../venv/bin/python
#   REPORT_CHECK=0 bash run_all.sh     the same without the last three steps (build the report tables, write them into
#                                      the reports, check the reports), for a run whose prose is written afterwards
#
# Stage A reads only the 2013 runs. Stage B starts with the second freeze; from then on 2014 outcomes may be read and
# every read is appended to aq-3/logs/test-access.md. The freeze step refuses to run when aq-3/results/freeze.json
# exists. To run the whole pipeline again, remove aq-3/results/freeze.json and aq-3/logs/test-access.md first and say
# so in logs/process-log.md: that is a reproduction, not a new test. The results in this folder come from such a
# rerun (PROTOCOL.md, "Status of this protocol").
set -euo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-../../venv/bin/python}"
step() { "$PY" common/run_step.py "$1" "$2" -- python "${@:3}"; }

# ---- code-path tests on synthetic toy inputs (never evidence) -------------------------------------------------
step logs tests_lib common/tests/test_lib.py
step logs tests_aq2_model common/tests/test_aq2_model.py

# ---- Stage A: 2013 runs only ------------------------------------------------------------------------------------
step aq-1 01_extract_2013        aq-1/code/01_extract.py --scope 2013
step aq-1 02_analyse_2013        aq-1/code/02_analyse.py --scope 2013
step aq-1 03_checks_2013         aq-1/code/03_checks.py --scope 2013
step aq-2 01_extract_2013        aq-2/code/01_extract.py --scope 2013
step aq-2 02_associations_2013   aq-2/code/02_associations.py --scope 2013
step aq-3 01_extract             aq-3/code/01_extract.py
step aq-3 02_dev_folds           aq-3/code/02_dev_folds.py          # about 3-4 minutes on 10 cores
step aq-3 03_choose              aq-3/code/03_choose.py

# ---- Stage B: second freeze, then the test ----------------------------------------------------------------------
step aq-3 04_freeze              aq-3/code/04_freeze.py             # about 12 minutes; stops if a freeze exists
step aq-3 05_test                aq-3/code/05_test.py
step aq-3 06_secondary           aq-3/code/06_secondary.py
step aq-3 07_error_analysis      aq-3/code/07_error_analysis.py
step aq-3 08_sensitivity         aq-3/code/08_sensitivity.py
step aq-4 01_lists               aq-4/code/01_lists.py
step aq-4 02_evaluate            aq-4/code/02_evaluate.py
step aq-4 03_fairness            aq-4/code/03_fairness.py
step aq-2 01_extract_2014        aq-2/code/01_extract.py --scope 2014
step aq-2 02_associations_2014   aq-2/code/02_associations.py --scope 2014
step aq-2 03_replication         aq-2/code/03_replication.py
step aq-1 01_extract_all         aq-1/code/01_extract.py --scope all
step aq-1 02_analyse_all         aq-1/code/02_analyse.py --scope all
step aq-1 03_checks_all          aq-1/code/03_checks.py --scope all

# ---- verification, comparison with the earlier runs, determinism, figures -----------------------------------------
step aq-3 09_verify              aq-3/code/09_verify.py
step aq-3 10_crosscheck_earlier_run aq-3/code/10_crosscheck_earlier_run.py
step logs compare_first_run      common/compare_first_run.py        # AQ3 and AQ4 must equal commit 11f4aca
step logs determinism_before     common/hash_outputs.py before
step aq-3 02_dev_folds_rerun     aq-3/code/02_dev_folds.py          # full rerun of the development folds
step logs determinism_after      common/hash_outputs.py after      # exits 1 if a file changed
step aq-1 04_figures             aq-1/code/04_figures.py
step aq-2 04_figures             aq-2/code/04_figures.py
step aq-3 11_figures             aq-3/code/11_figures.py
step aq-4 04_figures             aq-4/code/04_figures.py
if [ "${REPORT_CHECK:-1}" = "1" ]; then
  step logs report_tables        common/report_tables.py            # every report table, built from the result tables
  step logs fill_report_tables   common/fill_report_tables.py       # writes those tables into aq-*/README.md
  step logs check_reports        common/check_reports.py            # file references, table rows, quoted numbers, run facts
else
  echo "REPORT_CHECK=0: the three report steps were not run; run them after the prose of the reports is written"
fi
echo "all steps finished; see logs/experiment-log.md"
