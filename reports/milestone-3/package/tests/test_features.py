"""Unit tests of the feature formulas on SYNTHETIC fixtures (brief section 8.3, level A: pipeline test data).

The three enrolments below are invented, labelled synthetic, and never enter a prepared view or a finding. Each
expected value is worked out by hand from the formulas in data/metadata/feature_spec.md, so a change in a formula
that breaks the specification fails a test.

Usage (from the package folder): python -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

import polars as pl

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from prepare_data import assessment_status, cutoff_features  # noqa: E402

RUN = {"code_module": "SYN", "code_presentation": "2099J"}   # synthetic run, not an OULAD module


def enrolments():
    rows = [
        # S1: active, registered early, stays
        {"id_student": 1, "date_registration": -30, "date_unregistration": None},
        # S2: registered, leaves on day 20
        {"id_student": 2, "date_registration": -10, "date_unregistration": 20},
        # S3: registers late, on day 15 (after the day-13 cut-off)
        {"id_student": 3, "date_registration": 15, "date_unregistration": None},
    ]
    return pl.DataFrame([{**RUN, **r} for r in rows], schema_overrides={"date_unregistration": pl.Int64})


def daily():
    # enrolment x day clicks (records, clicks, clicks_dedup)
    rows = [(1, -5, 4, 4), (1, 0, 10, 8), (1, 6, 2, 2), (1, 13, 3, 3), (1, 14, 50, 50), (1, 27, 1, 1),
            (2, 2, 6, 6), (2, 25, 9, 9),
            (3, 16, 5, 5)]
    return pl.DataFrame([{**RUN, "id_student": s, "date": d, "records": 1, "clicks": c, "clicks_dedup": cd}
                         for s, d, c, cd in rows])


def site_days():
    rows = [(1, 10, 0), (1, 11, 0), (1, 10, 6), (1, 12, 13), (2, 10, 2), (3, 10, 16)]
    return pl.DataFrame([{**RUN, "id_student": s, "id_site": site, "date": d} for s, site, d in rows])


def assessment_grid():
    # two tasks of the run: CMA due day 10, TMA due day 24
    tasks = [(101, "CMA", 10), (102, "TMA", 24)]
    subs = {(1, 101): (5, 80.0), (1, 102): (26, 70.0),     # S1: CMA early, TMA two days late
            (2, 101): (12, 60.0),                          # S2: CMA two days late, TMA never
            (3, 101): None}
    rows = []
    for e in enrolments().iter_rows(named=True):
        for aid, typ, due in tasks:
            s = subs.get((e["id_student"], aid))
            rows.append({**RUN, "id_student": e["id_student"], "date_registration": e["date_registration"],
                         "date_unregistration": e["date_unregistration"], "id_assessment": aid,
                         "assessment_type": typ, "due_day": due, "weight": 0.0,
                         "date_submitted": s[0] if s else None, "is_banked": 0 if s else None,
                         "score": s[1] if s else None})
    return pl.DataFrame(rows, schema_overrides={"date_submitted": pl.Int64, "is_banked": pl.Int64,
                                                "score": pl.Float64, "date_unregistration": pl.Int64})


class FeatureFormulas(unittest.TestCase):
    def setUp(self):
        self.ad = assessment_status(assessment_grid())
        self.f13 = cutoff_features(enrolments(), self.ad, daily(), site_days(), 13).sort("id_student")
        self.f27 = cutoff_features(enrolments(), self.ad, daily(), site_days(), 27).sort("id_student")

    def row(self, f, s):
        return f.filter(pl.col("id_student") == s).row(0, named=True)

    def test_population_at_cutoff(self):
        self.assertEqual(self.f13["id_student"].to_list(), [1, 2])      # S3 not yet registered on day 13
        self.assertEqual(self.f27["id_student"].to_list(), [1, 3])      # S2 left on day 20

    def test_activity_windows(self):
        r = self.row(self.f13, 1)
        self.assertEqual(r["clicks_pre"], 4)                             # day -5
        self.assertEqual(r["clicks_0c"], 15)                             # days 0, 6, 13
        self.assertEqual(r["clicks_0c_dedup"], 13)
        self.assertEqual(r["active_days_0c"], 3)
        self.assertEqual((r["clicks_w1"], r["clicks_w2"]), (12, 3))     # week 1 = days 0-6, week 2 = 7-13
        self.assertEqual(r["clicks_last7"], 3)                           # days 7-13
        self.assertEqual(r["sites_0c"], 3)                               # sites 10, 11, 12 on days 0-13
        self.assertFalse(r["inactive_last7"])
        self.assertTrue(self.row(self.f13, 2)["inactive_last7"])         # S2: last click day 2

    def test_no_event_after_cutoff(self):
        self.assertEqual(self.row(self.f13, 1)["clicks_0c"], 15)          # the 50 clicks on day 14 are excluded

    def test_tasks_and_rule(self):
        r = self.row(self.f13, 2)                                        # CMA due 10, submitted day 12
        self.assertEqual((r["tasks_due_c"], r["tasks_missed_c"], r["tasks_late_c"], r["cma_late_c"]), (1, 0, 1, 1))
        self.assertTrue(r["early_sign_rule"])
        r = self.row(self.f27, 1)                                        # TMA due 24, submitted 26 (late, by 27)
        self.assertEqual((r["tasks_due_c"], r["tasks_missed_c"], r["tasks_late_c"], r["tma_late_c"]), (2, 0, 1, 1))
        r = self.row(self.f27, 3)                  # S3 registered day 15: the CMA due day 10 does not count (audit F5)
        self.assertEqual((r["tasks_due_c"], r["tasks_missed_c"]), (1, 1))
        self.assertEqual(self.row(self.f27, 3)["days_since_last_click"], 27 - 16)

    def test_cma_mark_lag(self):
        self.assertEqual(self.row(self.f13, 1)["cma_score_mean_c"], 80.0)   # submitted day 5 <= 13 - 7
        self.assertIsNone(self.row(self.f13, 2)["cma_score_mean_c"])        # submitted day 12 > 6: mark not yet known

    def test_run_relative_activity(self):
        # d13 population S1 (15 clicks) and S2 (6): median 10.5; ratio (clicks + 1) / (median + 1), zero-safe
        self.assertAlmostEqual(self.row(self.f13, 1)["activity_ratio_run"], 16 / 11.5)

    def test_extended_features(self):
        r = self.row(self.f13, 1)
        self.assertEqual(r["clicks_pre14"], 4)                           # day -5 lies in days -14..-1
        self.assertEqual(r["days_since_last_click"], 0)                  # last click on day 13
        self.assertEqual(r["trend_last_week"], 3 - 12)                   # week 2 minus week 1
        self.assertEqual(self.row(self.f13, 2)["days_since_last_click"], 11)   # last click day 2
        never = cutoff_features(enrolments(), self.ad, daily().filter(pl.col("id_student") != 2), site_days(), 13)
        self.assertEqual(never.filter(pl.col("id_student") == 2)["days_since_last_click"][0], 14)   # no click: c + 1
        self.assertEqual(r["cma_marked_c"], 1)
        self.assertEqual(r["tasks_submitted_early_c"], 0)
        # S1 at day 13 has not yet submitted the TMA due on day 24; at day 27 it is no longer early
        self.assertEqual(self.row(self.f27, 1)["tasks_submitted_early_c"], 0)

    def test_rule_components(self):
        r = self.row(self.f13, 2)          # CMA late only, inactive in days 7-13
        self.assertEqual((r["rule_missed"], r["rule_tma_late"], r["inactive_last7"]), (False, False, True))
        self.assertTrue(r["early_sign_rule"] and r["early_sign_rule_cma"])
        r = self.row(self.f27, 1)          # TMA late on day 26
        self.assertTrue(r["rule_tma_late"] and r["early_sign_rule"])

    def test_status(self):
        st = {(r["id_student"], r["id_assessment"]): r["status"] for r in self.ad.iter_rows(named=True)}
        self.assertEqual(st[(1, 102)], "late")
        self.assertEqual(st[(2, 102)], "not_submitted")
        due = {(r["id_student"], r["id_assessment"]): r["due_while_enrolled"] for r in self.ad.iter_rows(named=True)}
        self.assertFalse(due[(2, 102)])                                  # TMA due 24, S2 left on day 20
        self.assertFalse(due[(3, 101)])                                  # CMA due 10, S3 registered on day 15


if __name__ == "__main__":
    unittest.main()
