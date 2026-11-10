"""Code-path dry run of phase 2 (steps 06-12) BEFORE the real test access, on a throwaway copy of the package in a
temporary directory, with the 2013 rows standing in for the test year (common.TEST_YEAR patched to 2013).
No 2014 row is read; the real package's results, models and logs are untouched. The numbers it produces are
meaningless (the 'test' rows are the training rows) and are deleted with the temporary directory.

Run: venv/bin/python reports/milestone-4/package/tests/dry_run_phase2.py
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
STEPS = ["06_test.py", "07_gates.py", "08_fairness.py", "09_sensitivity.py", "10_aq4_lists.py",
         "11_aq2_replication.py", "12_report.py"]
WRAP = ("import sys, runpy; sys.path.insert(0, 'src'); import common as C; C.TEST_YEAR = 2013; "
        "sys.argv = [sys.argv[1]]; runpy.run_path('src/' + sys.argv[0], run_name='__main__')")


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        reports = Path(tmp) / "reports"
        pkg = reports / "milestone-4" / "package"
        pkg.mkdir(parents=True)
        for d in ("src", "results", "models"):
            shutil.copytree(PKG / d, pkg / d, ignore=shutil.ignore_patterns("__pycache__"))
        (pkg / "logs").mkdir()
        for m in ("milestone-3", "milestone-5"):
            (reports / m).symlink_to(PKG.parents[1] / m)
        for step in STEPS:
            rc = subprocess.run([sys.executable, "-c", WRAP, step], cwd=pkg, capture_output=True, text=True)
            print(f"== {step}: exit {rc.returncode}")
            print(rc.stdout[-1500:])
            if rc.returncode:
                print(rc.stderr[-3000:])
                return rc.returncode
        print("== guard: second run of 06 without --reproduce")
        rc = subprocess.run([sys.executable, "-c", WRAP, "06_test.py"], cwd=pkg, capture_output=True, text=True)
        print(f"exit {rc.returncode}: {(rc.stderr or rc.stdout).strip().splitlines()[-1]}")
        if rc.returncode == 0:
            return 1
    print("DRY RUN OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
