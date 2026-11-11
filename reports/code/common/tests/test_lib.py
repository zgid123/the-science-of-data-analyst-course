"""Code-path tests of the shared metric functions on tiny SYNTHETIC inputs.

The numbers below are hand-made toy values. They test the code only and are never used as evidence
(Milestone 4 brief, section 11: toy data must be labelled synthetic and kept out of the results).

    python common/tests/test_lib.py
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lib  # noqa: E402

checks = []


def ok(name, cond):
    checks.append((name, bool(cond)))
    print(f"- {'PASS' if cond else 'FAIL'}: {name}")


# list length: 5 per group of 20, groups = ceil(n / 20)
ok("list_len(40, 5) = 10", lib.list_len(40, 5) == 10)
ok("list_len(41, 5) = 15", lib.list_len(41, 5) == 15)
ok("list_len(3, 5) capped at n = 3", lib.list_len(3, 5) == 3)

# ranking and ties
score = np.array([0.9, 0.5, 0.5, 0.1])
tie = np.array([0.3, 0.8, 0.2, 0.5])
ok("rank_desc: higher score first, tie by smaller tie-break", list(lib.rank_desc(score, tie)) == [0, 2, 1, 3])

# metrics on a hand-checked run: 10 enrolments, 4 non-completers, list of 3 holding 2 of them
y = np.array([1, 0, 1, 0, 0, 1, 0, 0, 1, 0], bool)
rank = np.arange(10)
m = lib.run_metrics(rank, y, 3)
ok("tp = 2, recall = 0.5, precision = 2/3", m["non_completers_on_list"] == 2 and m["recall"] == 0.5 and abs(m["precision"] - 2 / 3) < 1e-12)
ok("attainable recall = 3/4 and normalised recall = 2/3", m["attainable_recall"] == 0.75 and abs(m["normalised_recall"] - 2 / 3) < 1e-12)
ok("lift = precision / base rate = (2/3)/0.4", abs(m["lift"] - (2 / 3) / 0.4) < 1e-12)
ok("random list expects k x base rate = 1.2 non-completers", abs(m["random_expected_tp"] - 1.2) < 1e-12)
m2 = lib.run_metrics(rank, y, 6)           # more places than non-completers: ceiling = 4
ok("ceiling = all non-completers when the list is longer", m2["max_attainable"] == 4 and m2["attainable_recall"] == 1.0)

# expected true positives under random tie-breaking: scores 3,2,2,2,1 ; y = 1,1,0,0,1 ; k = 2 -> 1 + 1 x (1/3)
ok("expected_tp_with_ties = 4/3", abs(lib.expected_tp_with_ties(np.array([3, 2, 2, 2, 1.0]), np.array([1, 1, 0, 0, 1.0]), 2) - 4 / 3) < 1e-12)

# sign-flip test
p, c, t = lib.sign_flip_p(np.full(13, 0.01))
ok("13 positive differences: p = 1/8192", t == 8192 and c == 1)
p, c, t = lib.sign_flip_p(np.array([0.02, -0.02]))
ok("symmetric differences: p = 3/4 (sum >= 0 in 3 of 4 assignments)", (c, t) == (3, 4))
p, c, t = lib.sign_flip_p(np.array([1.0, 2.0, 3.0]))
ok("three positive differences: p = 1/8", (c, t) == (1, 8))

# paired bootstrap: identical rankings give a zero difference in every replicate; a perfect ranking beats a reversed one
rng = np.random.default_rng(0)
runs = []
for n in (60, 80, 100):
    yy = rng.random(n) < 0.4
    s = yy + rng.random(n) * 0.01
    runs.append({"y": yy, "rank_a": lib.rank_desc(s, np.arange(n)), "rank_b": lib.rank_desc(s, np.arange(n))})
b = lib.paired_bootstrap_nr(runs, 5, B=200)
ok("identical rankings: every bootstrap difference is 0", np.all(b["diff"] == 0))
for r in runs:
    r["rank_b"] = len(r["y"]) - 1 - r["rank_a"]
b = lib.paired_bootstrap_nr(runs, 5, B=200)
ok("perfect ranking: normalised recall 1 in every replicate, reversed ranking far below", np.all(b["boot_a"] == 1.0) and b["ci_diff"][0] > 0.5)

# calibration: outcomes drawn from the stated probabilities -> intercept near 0, slope near 1
pp = rng.uniform(0.05, 0.95, 20000)
yy = rng.random(20000) < pp
c = lib.calibration(yy, pp)
ok("well-calibrated synthetic risks: |citl| < 0.08 and |slope - 1| < 0.08", abs(c["citl"]) < 0.08 and abs(c["slope"] - 1) < 0.08)
c2 = lib.calibration(yy, np.clip(pp + 0.15, 0.01, 0.99))
ok("risks 15 points too high: citl clearly negative", c2["citl"] < -0.3)

bad = [n for n, v in checks if not v]
print(f"\n{len(checks) - len(bad)} of {len(checks)} checks passed (synthetic inputs, code paths only)")
sys.exit(1 if bad else 0)
