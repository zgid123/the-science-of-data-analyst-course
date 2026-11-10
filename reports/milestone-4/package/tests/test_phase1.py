"""Code-path tests on SYNTHETIC fixtures (labelled synthetic; never feed a result, contract rule 5).

Run: venv/bin/python -m unittest discover -s reports/milestone-4/package/tests -v
"""
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import polars as pl

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import common as C  # noqa: E402


def synthetic_view(n_per_run=60, seed=0, years=(2013,)) -> pd.DataFrame:
    """SYNTHETIC feature view with the columns the models read."""
    rng = np.random.default_rng(seed)
    runs = [("AAA", "J"), ("BBB", "B"), ("BBB", "J"), ("DDD", "B")]
    frames = []
    sid = 0
    for year in years:
        for mod, mon in runs:
            n = n_per_run
            d = pd.DataFrame({
                "code_module": mod, "code_presentation": f"{year}{mon}", "year": year, "start_month": mon,
                "id_student": np.arange(sid, sid + n), "highest_education": rng.choice(list(C.EDUCATION_ORDER), n),
                "num_of_prev_attempts": rng.integers(0, 3, n).astype(float),
                "studied_credits": rng.choice([30, 60, 120], n).astype(float),
                "registration_lead": rng.normal(50, 20, n), "clicks_0c": rng.poisson(80, n).astype(float),
                "activity_ratio_run": rng.gamma(2, 0.5, n), "inactive_last7": rng.random(n) < 0.2,
                "rule_missed": rng.random(n) < 0.2, "rule_tma_late": rng.random(n) < 0.1,
            })
            d.loc[d.index[:3], "registration_lead"] = np.nan
            d["y"] = (rng.random(n) < 0.45).astype(int)
            frames.append(d)
            sid += n
    df = pd.concat(frames, ignore_index=True)
    df[C.RUN] = df["code_module"] + "_" + df["code_presentation"]
    return df


COLS = ["code_module", "start_month", "highest_education", "num_of_prev_attempts", "studied_credits",
        "registration_lead", "clicks_0c", "activity_ratio_run", "inactive_last7"]


class TestMetrics(unittest.TestCase):
    def test_list_length_matches_capacity_formula(self):
        self.assertEqual(C.list_length(369, 5), 95)     # ceil(369/20)=19 groups
        self.assertEqual(C.list_length(369, 3), 57)
        self.assertEqual(C.list_length(10, 5), 5)
        self.assertEqual(C.list_length(3, 5), 3)        # never longer than the run

    def test_normalised_recall_and_attainable_max(self):
        # 10 enrolments, 2 non-completers, k = 4: max attainable = 2
        y = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        listed = np.array([1, 0, 1, 1, 1, 0, 0, 0, 0, 0], bool)
        m = C.run_metrics(y, listed, 4, None)
        self.assertEqual(m["max_attainable"], 2)
        self.assertAlmostEqual(m["normalised_recall"], 0.5)
        self.assertAlmostEqual(m["precision"], 0.25)
        self.assertAlmostEqual(m["lift"], 0.25 / 0.2)
        # |Y| >= k: normalised recall equals precision
        y2 = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
        listed2 = np.array([1, 1, 0, 0, 0, 1, 1, 0, 0, 0], bool)
        m2 = C.run_metrics(y2, listed2, 4, None)
        self.assertEqual(m2["max_attainable"], 4)
        self.assertAlmostEqual(m2["normalised_recall"], m2["precision"])
        # no non-completer: normalised recall does not apply -> empty
        self.assertIsNone(C.run_metrics(np.zeros(5, int), np.ones(5, bool), 2, None)["normalised_recall"])

    def test_pooled_normalised_recall(self):
        self.assertAlmostEqual(C.pooled_normalised_recall([2, 4], [2, 8]), 0.6)

    def test_model_ties_by_ascending_id(self):
        order = C.ranked_order(np.array([0.5, 0.9, 0.5, 0.5]), np.array([30, 10, 20, 5]))
        self.assertEqual(order.tolist(), [1, 3, 2, 0])

    def test_rule_ranking_signs_then_lower_activity_then_id(self):
        df = pd.DataFrame({"rule_missed": [1, 0, 1, 1, 0], "rule_tma_late": [1, 0, 0, 0, 0],
                           "inactive_last7": [0, 1, 0, 0, 0], "activity_ratio_run": [2.0, 0.1, 0.5, 0.5, 0.0],
                           "id_student": [1, 2, 9, 3, 4]})
        # signs 2,1,1,1,0; among signs=1: ratio 0.1 (id2), then ratio 0.5 ids 3 then 9
        self.assertEqual(C.b2_order(df).tolist(), [0, 1, 3, 2, 4])
        self.assertEqual(C.on_list(C.b2_order(df), 2).tolist(), [True, True, False, False, False])
        # rule_score keeps ties and the same order
        s = C.rule_score(df)
        self.assertEqual(s[2], s[3])
        self.assertTrue(s[0] > s[1] > s[2] > s[4])


class TestFoldLocalPreprocessing(unittest.TestCase):
    def test_deviation_coding_unseen_level_is_zeros(self):
        dc = C.DeviationCoder().fit(np.array(["AAA", "BBB", "DDD"]).reshape(-1, 1))
        out = dc.transform(np.array(["AAA", "DDD", "CCC"]).reshape(-1, 1))
        self.assertEqual(out.tolist(), [[1, 0], [-1, -1], [0, 0]])

    def test_median_and_indicator_from_training_only(self):
        tr = pd.DataFrame({"a": [1.0, np.nan, 3.0, 5.0], "b": [1.0, 2.0, 3.0, 4.0]})
        fn = C.FoldNumeric(log=True, indicator=True).fit(tr)
        self.assertEqual(fn.median_.tolist(), [3.0, 2.5])
        self.assertEqual(fn.missing_cols_.tolist(), [0])        # b had no nulls in training: no indicator
        va = pd.DataFrame({"a": [np.nan], "b": [np.nan]})
        out = fn.transform(va)
        self.assertTrue(np.allclose(out, [[np.log1p(3.0), np.log1p(2.5), 1.0]]))
        self.assertEqual(C.FoldNumeric(log=False, indicator=False).fit(tr).missing_cols_.tolist(), [])

    def test_primary_parameter_count(self):
        df = synthetic_view()
        pipe = C.fit_pipeline("M1", COLS, {"C": 1.0}, df)
        names = list(pipe.named_steps["prep"].named_steps["encode"].get_feature_names_out())
        # 3 modules -> 2 deviation columns, 2 months -> 1; registration_lead: median fill, no indicator
        self.assertIn("code_module=AAA", names)
        self.assertNotIn("registration_lead_missing", names)
        self.assertEqual(len(names), 2 + 1 + len(COLS) - 2)

    def test_altered_validation_rows_leave_fold_parameters_unchanged(self):
        df = synthetic_view()
        run, train, valid = next(f for f in C.loro_folds(df) if f[0] == "BBB_2013J")
        p1 = C.fit_pipeline("M1", COLS, {"C": 1.0}, train)
        altered = df.copy()
        m = altered[C.RUN] == "BBB_2013J"
        altered.loc[m, "clicks_0c"] = 1e6
        altered.loc[m, "registration_lead"] = np.nan
        altered.loc[m, "y"] = 1 - altered.loc[m, "y"]
        run2, train2, valid2 = next(f for f in C.loro_folds(altered) if f[0] == "BBB_2013J")
        p2 = C.fit_pipeline("M1", COLS, {"C": 1.0}, train2)
        s1, s2 = p1.named_steps["prep"].named_steps["scale"], p2.named_steps["prep"].named_steps["scale"]
        self.assertTrue(np.array_equal(s1.mean_, s2.mean_))
        self.assertTrue(np.array_equal(s1.scale_, s2.scale_))
        self.assertTrue(np.array_equal(p1.named_steps["model"].coef_, p2.named_steps["model"].coef_))
        # the scaler mean equals the training rows' own mean
        Xt = p1.named_steps["prep"].named_steps["encode"].transform(train[COLS].assign(
            inactive_last7=train["inactive_last7"].astype(float)))
        self.assertTrue(np.allclose(s1.mean_, Xt.mean(axis=0)))

    def test_overlapping_students_removed_from_training(self):
        df = synthetic_view()
        shared = df.loc[df[C.RUN] == "AAA_2013J", "id_student"].iloc[:5].tolist()
        idx = df.index[df[C.RUN] == "BBB_2013B"][:5]
        df.loc[idx, "id_student"] = shared
        _, train, valid = next(f for f in C.loro_folds(df) if f[0] == "AAA_2013J")
        self.assertFalse(set(train["id_student"]) & set(valid["id_student"]))
        self.assertEqual(len(train), len(df) - 60 - 5)

    def test_tree_unseen_module_handled(self):
        df = synthetic_view()
        _, train, valid = next(f for f in C.loro_folds(df) if f[0] == "AAA_2013J")   # AAA unseen in training
        pipe = C.fit_pipeline("M3", COLS, {"max_depth": 2, "max_iter": 10, "learning_rate": 0.1}, train)
        self.assertEqual(len(C.predict(pipe, COLS, valid)), len(valid))


class Test2013Guard(unittest.TestCase):
    def test_guard_rejects_2014_rows(self):
        df = synthetic_view(years=(2013, 2014))
        with self.assertRaises(AssertionError):
            C.assert_2013(df)
        with self.assertRaises(AssertionError):
            C.fit_pipeline("M1", COLS, {"C": 1.0}, df)
        bad = synthetic_view().assign(year=2013)
        bad.loc[0, "code_presentation"] = "2014J"
        with self.assertRaises(AssertionError):
            C.assert_2013(bad)

    def test_loader_filters_2014_while_scanning(self):
        df = synthetic_view(years=(2013, 2014)).drop(columns=[C.RUN, "y"])
        df["non_completion"] = True
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "data/processed"
            p.mkdir(parents=True)
            pl.from_dict({c: df[c].tolist() for c in df.columns}).write_parquet(p / "features_d27.parquet")
            got = C.load_view(27, Path(tmp))
        self.assertEqual(set(got["year"]), {2013})
        self.assertEqual(len(got), len(df[df["year"] == 2013]))


if __name__ == "__main__":
    unittest.main()
