"""AQ2 replication: 2014 − 2013 change of each adjusted risk difference, with a 95% interval from the two
independent standard errors (each recovered from its own delta-method interval)."""

import _tools  # noqa: F401
import numpy as np
import pandas as pd
from holdout_guard import open_holdout

import common as c

open_holdout(c.FREEZE, c.ACCESS, who="10_aq2_compare.py", why="compare AQ2 associations of 2013 and 2014")
a = pd.read_csv(c.RESULTS / "aq2_associations_2013.csv").set_index("sign")
b = pd.read_csv(c.RESULTS / "aq2_associations_2014.csv").set_index("sign")
rows = []
for s in c.SIGNS:
    se13 = (a.loc[s, "adj_high"] - a.loc[s, "adj_low"]) / (2 * 1.959964)
    se14 = (b.loc[s, "adj_high"] - b.loc[s, "adj_low"]) / (2 * 1.959964)
    diff = b.loc[s, "adj_rd"] - a.loc[s, "adj_rd"]
    half = 1.959964 * np.hypot(se13, se14)
    rows.append({"sign": s, "label": c.SIGN_LABEL[s], "rd_2013": a.loc[s, "adj_rd"], "low_2013": a.loc[s, "adj_low"],
                 "high_2013": a.loc[s, "adj_high"], "n_2013": a.loc[s, "n_support"],
                 "rd_2014": b.loc[s, "adj_rd"], "low_2014": b.loc[s, "adj_low"], "high_2014": b.loc[s, "adj_high"],
                 "n_2014": b.loc[s, "n_support"], "change": diff, "change_low": diff - half, "change_high": diff + half,
                 "criterion_2013": bool(a.loc[s, "meets_criterion"]), "criterion_2014": bool(b.loc[s, "meets_criterion"]),
                 "unadj_2013": a.loc[s, "unadj_rd"], "unadj_2014": b.loc[s, "unadj_rd"],
                 "modules_positive_2014": f"{b.loc[s, 'modules_positive']} of {b.loc[s, 'modules']}"})
out = pd.DataFrame(rows)
c.write(out, "aq2_replication.csv")
print(out[["sign", "rd_2013", "rd_2014", "change", "change_low", "change_high", "criterion_2013", "criterion_2014"]]
      .round(3).to_string(index=False))
