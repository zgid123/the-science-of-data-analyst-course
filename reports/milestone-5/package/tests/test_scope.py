"""Unit tests of the scope guard and the AQ2 module terms on SYNTHETIC fixtures (Change Log C15).

The rows below are invented, labelled synthetic, and never enter a result. They check two rules the 2014 and all-run
analyses rely on: a loader keeps only the runs of its scope and stops on any other row, and a module in which a sign
never occurs gets no sign x module term, so the model stays estimable and that module takes the average-module effect.

Usage (from the package folder): python -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

import numpy as np
import polars as pl

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "analysis"))
import aq_analysis as A  # noqa: E402


class ScopeGuard(unittest.TestCase):
    def tearDown(self):
        A.set_scope("2013")

    def test_scope_accepts_own_runs_and_rejects_others(self):
        A.set_scope("2014")
        ok = pl.DataFrame({"code_presentation": ["2014B", "2014J"], "year": [2014, 2014], "split": ["test", "test"]})
        A.assert_scope(ok, "synthetic 2014")
        bad = pl.DataFrame({"code_presentation": ["2014B", "2013J"], "year": [2014, 2013], "split": ["test", "train"]})
        with self.assertRaises(AssertionError):
            A.assert_scope(bad, "synthetic mixed")

    def test_results_folder_follows_scope(self):
        A.set_scope("all")
        self.assertEqual(A.RES, A.ROOT / "results" / "all_runs")
        A.set_scope("2013")
        self.assertEqual(A.RES, A.ROOT / "results" / "2013")


class ModuleTerms(unittest.TestCase):
    def fixture(self) -> pl.DataFrame:
        rng = np.random.default_rng(7)
        rows = []
        for mod, run, late_possible in [("SYA", "SYA 2099B", True), ("SYB", "SYB 2099B", True),
                                        ("SYC", "SYC 2099B", False)]:
            for i in range(300):
                late = int(late_possible and rng.random() < 0.3)
                missed = int(rng.random() < 0.2)
                p = 1 / (1 + np.exp(-(-0.5 + 1.2 * late + 1.5 * missed)))
                rows.append(dict(code_module=mod, run=run, task_run=True, num_of_prev_attempts=int(rng.integers(0, 3)),
                                 studied_credits=int(rng.choice([30, 60, 90])),
                                 late_tma=late, missed_task=missed, y=int(rng.random() < p)))
        return pl.DataFrame(rows)

    def test_module_without_the_sign_gets_no_term(self):
        f = self.fixture()
        fit = A.Fit(f, ["missed_task", "late_tma"], interactions=True)
        self.assertTrue(fit.converged)
        self.assertEqual(fit.mods["late_tma"], ["SYA", "SYB"])            # SYC: sign never occurs
        self.assertEqual(fit.mods["missed_task"], ["SYA", "SYB", "SYC"])
        self.assertNotIn("late_tma:dev[SYC]", fit.names)
        est, lo, hi, _ = fit.ame("late_tma", np.arange(f.height))
        self.assertTrue(lo < est < hi)


if __name__ == "__main__":
    unittest.main()
