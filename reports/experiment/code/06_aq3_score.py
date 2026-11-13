"""Score the 13 runs of 2014 once with the frozen models (day 13 and day 27). Reruns read the saved scores.

Saved per enrolment: key, run, outcome, the rule-ranked score, the fixed tie-breaker and the probability of every
frozen configuration. No model is refitted and nothing is recalibrated on 2014 rows.
"""

import pickle
import sys

import _tools  # noqa: F401
from holdout_guard import open_holdout, scores_saved

import common as c
import models as m  # noqa: F401  (needed to unpickle the frozen models)

OUT = {cut: c.SCORES / f"test_scores_d{cut}.csv" for cut in (13, 27)}
if all(scores_saved(p) for p in OUT.values()):
    print("test scores already saved: nothing to do")
    sys.exit(0)

open_holdout(c.FREEZE, c.ACCESS, who="06_aq3_score.py", why="score the 13 runs of 2014 once with the frozen models")
c.SCORES.mkdir(exist_ok=True)
for cut, path in OUT.items():
    f = c.features(cut)
    test = f[f["year"] == 2014].copy()
    out = test[c.KEY + ["run", "y", "tiebreak_u"]].copy()
    out["rule"] = c.rule_score(test)
    for cfg in m.CONFIGS:
        with open(c.MODELS / f"{cfg}_d{cut}.pkl", "rb") as fh:
            out[cfg] = pickle.load(fh).predict(test)
    out.to_csv(path, index=False)
    print(f"day {cut}: {len(out)} test enrolments in {out['run'].nunique()} runs scored -> {path.name}")
