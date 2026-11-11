#!/usr/bin/env bash
# Milestone 4 Level 2 prototype – run every step in the order of the protocol (PROTOCOL.md, P02).
#
#   bash run_all.sh            from reports/code; uses ../../venv/bin/python
#
# Stage A reads only the 2013 runs. Stage B starts with the second freeze; from then on 2014 outcomes may be read and
# every read is appended to aq-3/logs/test-access.md. The freeze step refuses to run when aq-3/results/freeze.json
# exists: the results in this folder come from one freeze and one test. To REPRODUCE the whole run on a clean copy,
# remove aq-3/results/freeze.json and aq-3/logs/test-access.md first and say so in the log – that is a reproduction
# of this run, not a new test.
set -euo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-../../venv/bin/python}"
step() { "$PY" common/run_step.py "$1" "$2" -- python "${@:3}"; }

# ---- code-path tests on synthetic toy inputs (never evidence) -------------------------------------------------
step logs tests_lib common/tests/test_lib.py

# ---- Stage A: 2013 runs only ------------------------------------------------------------------------------------
step aq-1 01_extract_2013        aq-1/code/01_extract.py --scope 2013
step aq-1 02_analyse_2013        aq-1/code/02_analyse.py --scope 2013
step aq-1 03_checks_2013         aq-1/code/03_checks.py --scope 2013
step aq-2 01_extract_2013        aq-2/code/01_extract.py --scope 2013
step aq-2 02_associations_2013   aq-2/code/02_associations.py --scope 2013
step aq-3 01_extract             aq-3/code/01_extract.py
step aq-3 02_dev_folds           aq-3/code/02_dev_folds.py          # about 3-4 minutes on 10 cores
step aq-3 03_choose              aq-3/code/03_choose.py

# ---- Stage B: second freeze, then the single test -------------------------------------------------------------
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

# ---- verification, cross-check, figures -------------------------------------------------------------------------
step aq-3 09_verify              aq-3/code/09_verify.py
step aq-3 10_crosscheck_earlier_run aq-3/code/10_crosscheck_earlier_run.py
step aq-1 04_figures             aq-1/code/04_figures.py
step aq-2 04_figures             aq-2/code/04_figures.py
step aq-3 11_figures             aq-3/code/11_figures.py
step aq-4 04_figures             aq-4/code/04_figures.py
step logs check_reports           common/check_reports.py           # file references and quoted numbers of the reports
echo "all steps finished; see logs/experiment-log.md"
