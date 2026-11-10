"""Phase-2 code-path tests on SYNTHETIC fixtures (labelled synthetic; never feed a result, contract rule 5):
gate statistics (sign-flip, paired two-level bootstrap, S1 summary, Holm bounds, group recall gap) and the guards
that refuse a second test access and any 2014 read before the access is recorded.

Run: venv/bin/python -m unittest discover -s reports/milestone-4/package/tests -v
"""
import importlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import common as C  # noqa: E402
import gates as G  # noqa: E402

test06 = importlib.import_module("06_test")


def synthetic_runs(m=5, n=80, seed=0, perfect_a=True):
    """SYNTHETIC runs: ranker a scores by the outcome (perfect), ranker b by noise."""
    rng = np.random.default_rng(seed)
    runs = []
    for i in range(m):
        y = (rng.random(n) < 0.4).astype(int)
        ids = np.arange(n) + 1000 * i
        sa = y + 0.01 * rng.random(n) if perfect_a else rng.random(n)
        runs.append({"run": f"R{i}", "y": y, "a": [ids, -sa], "b": [ids, -rng.random(n)]})
    return runs


class TestSignFlip(unittest.TestCase):
    def test_all_positive_gives_smallest_p(self):
        self.assertAlmostEqual(G.sign_flip_p(np.ones(13) * 0.02), 1 / 2 ** 13)

    def test_all_zero_gives_p_one(self):
        self.assertEqual(G.sign_flip_p(np.zeros(4)), 1.0)

    def test_hand_computed(self):
        # d = (3, -1): assignments means 1, 2, -2, -1 -> observed 1; stats >= 1: {1, 2} -> p = 0.5
        self.assertAlmostEqual(G.sign_flip_p(np.array([3.0, -1.0])), 0.5)


class TestBootstrapAndS1(unittest.TestCase):
    def test_identical_rankers_give_zero_interval(self):
        runs = synthetic_runs()
        for r in runs:
            r["b"] = r["a"]
        s = G.s1_stats(runs, 5, B=50, seed=(1, 2))
        self.assertEqual((s["difference"], s["boot_ci_low"], s["boot_ci_high"]), (0.0, 0.0, 0.0))
        self.assertEqual((s["wins"], s["ties"], s["losses"]), (0, 5, 0))
        self.assertEqual(s["verdict"], "S1 not met")

    def test_perfect_ranker_beats_noise(self):
        s = G.s1_stats(synthetic_runs(), 5, B=200, seed=(1, 2))
        self.assertGreater(s["boot_ci_low"], 0)
        self.assertAlmostEqual(s["pooled_nr_model"], 1.0)
        self.assertEqual(s["wins"], 5)
        self.assertAlmostEqual(s["signflip_p"], 1 / 32)
        self.assertEqual(s["verdict"], "S1 met")

    def test_bootstrap_seeded_and_paired(self):
        runs = synthetic_runs(perfect_a=False)
        b1 = G.bootstrap_diff(runs, 5, 30, [7, 1])
        b2 = G.bootstrap_diff(runs, 5, 30, [7, 1])
        self.assertTrue(np.array_equal(b1, b2))
        self.assertFalse(np.array_equal(b1, G.bootstrap_diff(runs, 5, 30, [7, 2])))

    def test_run_counts_hand_computed(self):
        y = np.array([1, 0, 1, 0, 0, 0, 0, 0, 0, 0])
        ids = np.arange(10)
        r = {"y": y, "a": [ids, -np.array([9, 8, 7, 0, 0, 0, 0, 0, 0, 0.0])], "b": [ids, -np.arange(10.0)]}
        # n = 10, k = 5 per 20 -> 5 places; a lists ids 0,1,2,3,4 -> 2 non-completers; b lists 9..5 -> 0
        self.assertEqual(G.run_counts(r, 5), (2, 0, 2))


class TestFairnessStats(unittest.TestCase):
    def test_recall_gap_hand_computed(self):
        df = pd.DataFrame({"run": "R", "id_student": np.arange(8), "y": [1, 1, 1, 1, 0, 0, 0, 0],
                           "s": [8, 7, 1, 0, 6, 5, 4, 3]})
        g = np.array([1, 0, 1, 0, 0, 0, 0, 0], bool)    # group holds two non-completers
        runs = G.group_runs(df.rename(columns={"run": C.RUN}), "s", g)
        # n = 8 -> k = 5: listed ids 0,1,4,5,6 -> group recall 1/2, others 1/2
        rg, ro, diff = G.recall_gap(runs, 5)
        self.assertEqual((rg, ro, diff), (0.5, 0.5, 0.0))

    def test_holm_levels(self):
        rng = np.random.default_rng(0)
        boots = {"a": rng.normal(-0.2, 0.01, 500), "b": rng.normal(0.0, 0.05, 500), "c": rng.normal(0.2, 0.01, 500)}
        h = G.holm_upper_bounds(boots)
        self.assertAlmostEqual(h["a"][1], 0.05 / 3)
        self.assertAlmostEqual(h["b"][1], 0.05 / 2)
        self.assertAlmostEqual(h["c"][1], 0.05)
        self.assertLess(h["a"][0], 0)


class TestTestAccessGuards(unittest.TestCase):
    def _freeze(self, tmp, access):
        p = Path(tmp) / "freeze.csv"
        pd.DataFrame({"chosen_config": ["M1"], "spec": ["x cutoff=27 y"], "parameter_file": ["m"],
                      "model_sha256": ["h"], "first_test_access_utc": [access]}).to_csv(p, index=False)
        return p

    def test_second_access_refused(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(C, "FREEZE_CSV", self._freeze(tmp, "2026-11-10T00:00:00Z")):
            with self.assertRaises(SystemExit) as cm:
                test06.guard(reproduce=False)
            self.assertIn("REFUSED", str(cm.exception))
            self.assertEqual(test06.guard(reproduce=True), "2026-11-10T00:00:00Z")

    def test_first_access_allowed_and_reproduce_needs_access(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(C, "FREEZE_CSV", self._freeze(tmp, "")):
            self.assertEqual(test06.guard(reproduce=False), "")
            with self.assertRaises(SystemExit):
                test06.guard(reproduce=True)

    def test_2014_rows_refused_before_access(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(C, "FREEZE_CSV", self._freeze(tmp, "")):
            with self.assertRaises(PermissionError):
                C.load_test_view(27)


if __name__ == "__main__":
    unittest.main()
