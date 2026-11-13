"""Stage 6: reconcile the populations every question uses, without reading any 2014 outcome.

Asserts the counts fixed in the Level 1 design (Table A.6 and the AQ1 card) and writes the population table.
Outcome counts are taken from the 2013 runs only; 2014 rows are counted, not their outcomes.
"""

import _tools  # noqa: F401
import pandas as pd

import common as c

e = c.enrolment()
f13, f27 = c.features(13), c.features(27)

rows = []
def add(name, value, expected=None):
    rows.append({"quantity": name, "value": int(value), "expected": "" if expected is None else int(expected),
                 "status": "" if expected is None else ("PASS" if int(value) == int(expected) else "FAIL")})

add("enrolments, all runs", len(e), 32593)
add("enrolment keys unique", e.duplicated(c.KEY).sum() == 0, 1)
add("runs", e["run"].nunique(), 22)
add("runs 2013", e.loc[e["year"] == 2013, "run"].nunique(), 9)
add("runs 2014", e.loc[e["year"] == 2014, "run"].nunique(), 13)
add("registered at day 14 (KPI population)", e["enrolled_d14"].sum(), 28061)
add("registered at day 13 = rows of features_d13", e["enrolled_d13"].sum(), len(f13))
add("registered at day 27 = rows of features_d27", e["enrolled_d27"].sum(), len(f27))
add("features_d27 keys unique", f27.duplicated(c.KEY).sum() == 0, 1)
add("features_d27 keys all registered at day 27",
    f27.merge(e[c.KEY + ["enrolled_d27"]], on=c.KEY, how="left")["enrolled_d27"].all(), 1)
add("training enrolments day 13 (2013)", (f13["year"] == 2013).sum(), 12080)
add("training enrolments day 27 (2013)", (f27["year"] == 2013).sum(), 11811)
add("training non-completers day 27 (2013)", f27.loc[f27["year"] == 2013, "y"].sum(), 5245)
add("test enrolments day 13 (2014)", (f13["year"] == 2014).sum(), 15989)
add("test enrolments day 27 (2014)", (f27["year"] == 2014).sum(), 15724)
add("test enrolments of students seen in 2013 (day 27)", f27["student_in_training_runs"].sum(), 1586)

signs = c.add_signs(f27)
add("runs with a task due by day 27", signs.loc[signs["any_task"], "run"].nunique(), 16)
add("rule flags at day 27, all runs", f27["early_sign_rule"].sum())
add("enrolments with nothing due by day 27 in a run with a task due",
    ((signs["any_task"]) & (signs["tasks_due_c"] == 0)).sum())

pop = pd.DataFrame(rows)
c.write(pop, "prep_reconciliation.csv")
print(pop.to_string(index=False))
assert (pop["status"] != "FAIL").all(), "a population count differs from the design"
