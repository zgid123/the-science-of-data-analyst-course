"""Code-path tests of the AQ2 association model and of the AQ1 year-comparison helpers on SYNTHETIC inputs.

The rows below are generated toy values. They test the code only and are never used as evidence (Milestone 4 brief,
section 11: toy data must be labelled synthetic and kept out of the results).

The first group of tests is the one that would have caught the error of the first run: a sign that is absent from one
module must not enter that module's rows into its average as differences of 0.

    python common/tests/test_aq2_model.py
"""

import sys
from pathlib import Path

import numpy as np
import polars as pl

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "common"))
sys.path.insert(0, str(ROOT / "aq-2" / "code"))
sys.path.insert(0, str(ROOT / "aq-1" / "code"))
import lib  # noqa: E402
from aq2_model import AssociationModel, defined_rows, expit, support_rows, unadjusted, verdicts  # noqa: E402

checks = []


def ok(name, cond):
    checks.append((name, bool(cond)))
    print(f"- {'PASS' if cond else 'FAIL'}: {name}")


# ---- synthetic table: modules A and B have a TMA due; module C has only a CMA due, so nobody in C has a late TMA ----
rng = np.random.default_rng(7)
n_mod = 3000
rows = []
for module, has_tma in (("A", True), ("B", True), ("C", False)):
    late = (rng.random(n_mod) < 0.15) & has_tma
    low = rng.random(n_mod) < 0.3
    logit = -0.6 + 1.0 * late + 0.5 * low + (0.4 if module == "C" else 0.0)      # true late-TMA effect: 1.0 on the log-odds
    y = rng.random(n_mod) < expit(logit)
    prev, cred = rng.integers(0, 3, n_mod), rng.choice([30, 60, 120], n_mod)       # unrelated to the outcome
    for i in range(n_mod):
        rows.append({"code_module": module, "run": f"{module}-2014J", "non_completion": bool(y[i]), "sign_tma_late": bool(late[i]),
                     "sign_low_activity": bool(low[i]), "run_has_task_due": True, "run_has_tma_due": has_tma,
                     "num_of_prev_attempts": int(prev[i]), "studied_credits": int(cred[i])})
df = pl.DataFrame(rows)
in_ab = (df["code_module"] != "C").to_numpy()
signs = ["sign_tma_late", "sign_low_activity"]
m = AssociationModel(df, signs)
r = m.risk_difference("sign_tma_late")

ok("late TMA is defined only in the runs with a TMA due (6,000 of 9,000 synthetic rows)", int(defined_rows(df, "sign_tma_late").sum()) == 6000)
ok("support of the late-TMA sign excludes module C", np.array_equal(support_rows(df, "sign_tma_late"), in_ab) and np.array_equal(m.support["sign_tma_late"], in_ab))
ok("the average covers 6,000 rows, not 9,000, and reports that n", r["n"] == 6000 and r["support_modules"] == 2)
# the value the first run's code produced: C rows counted as differences of exactly 0
X1, X0 = m.X.copy(), m.X.copy()
for j, mask in m.sign_cols["sign_tma_late"]:
    X1[:, j], X0[:, j] = mask.astype(float), 0.0
per_row = expit(X1 @ m.beta) - expit(X0 @ m.beta)
diluted = float(per_row.mean())
ok("every module C row has a difference of exactly 0, which is why it must stay out of the average", np.all(per_row[~in_ab] == 0.0))
ok("estimate equals the mean over the support (about +0.24), not the diluted mean over all rows (two-thirds of it)",
   abs(r["rd"] - float(per_row[in_ab].mean())) < 1e-12 and abs(diluted - r["rd"] * 2 / 3) < 1e-12 and 0.18 < r["rd"] < 0.30)
t = m.table().filter(pl.col("sign") == "sign_tma_late").row(0, named=True)
ok("table() carries n_support = 6,000 and no row defined outside the support", t["n_support"] == 6000 and t["rows_defined_outside_support"] == 0)
u = unadjusted(df, signs).filter(pl.col("sign") == "sign_tma_late").row(0, named=True)
ok("the unadjusted difference uses the same 6,000 rows (module C is not the comparison group)", u["enrolments"] == 6000)
ok("a subgroup average is restricted to the support as well", m.risk_difference("sign_tma_late", np.ones(df.height, bool))["n"] == 6000
   and m.risk_difference("sign_tma_late", ~in_ab)["n"] == 0 and np.isnan(m.risk_difference("sign_tma_late", ~in_ab)["rd"]))
ok("the click sign keeps all 9,000 rows", m.risk_difference("sign_low_activity")["n"] == 9000)

# ---- a sign defined by the calendar but absent in one module (the generic guard, independent of the calendar flag) ----
df2 = df.with_columns(pl.lit(True).alias("run_has_tma_due"))
m2 = AssociationModel(df2, signs)
note = [x for x in m2.cell_notes if x["sign"] == "sign_tma_late" and x["code_module"] == "C"][0]
ok("module with no enrolment carrying the sign gets no term and stays outside the support", "outside the support" in note["handling"]
   and m2.risk_difference("sign_tma_late")["n"] == 6000 and m2.table().filter(pl.col("sign") == "sign_tma_late")["rows_defined_outside_support"][0] == 3000)
simple = AssociationModel(df2, signs, interactions=False)
ok("the model without sign x module terms excludes that module too", simple.risk_difference("sign_tma_late")["n"] == 6000)

# ---- small cells are pooled, not dropped ---------------------------------------------------------------------------
small = df.filter(pl.col("code_module") == "A").head(400).with_columns(pl.lit("D").alias("code_module"), pl.lit("D-2014J").alias("run"))
x = np.zeros(400, bool); x[:5] = True
small = small.with_columns(pl.Series("sign_tma_late", x), pl.Series("non_completion", (np.arange(400) % 2 == 0)))
m3 = AssociationModel(pl.concat([df, small]), signs)
note = [c for c in m3.cell_notes if c["sign"] == "sign_tma_late" and c["code_module"] == "D"][0]
ok("module with 5 enrolments carrying the sign shares a pooled slope and stays in the support", "pooled slope" in note["handling"]
   and m3.risk_difference("sign_tma_late")["n"] == 6400 and "D" not in m3.sign_modules["sign_tma_late"])

# ---- verdicts: a module estimate indistinguishable from 0 is not counted in the strict reading ---------------------------
overall = pl.DataFrame({"sign": ["s"], "adjusted_rd": [0.20], "adj_ci_low": [0.15], "adj_ci_high": [0.25]})
bym = pl.DataFrame({"sign": ["s"] * 3, "code_module": ["A", "B", "C"], "adjusted_rd": [0.25, 0.22, 0.002],
                    "adj_ci_low": [0.20, 0.15, -0.13], "adj_ci_high": [0.30, 0.29, 0.134]})
v = verdicts(overall, bym).row(0, named=True)
ok("direction count: 3 of 3 by point estimate, 2 of 3 with an interval excluding 0, module C named", v["modules_same_direction"] == 3
   and v["modules_same_direction_interval_excludes_0"] == 2 and v["modules_interval_includes_0"] == "C" and v["verdict_strict"] == "consistent association")
bym2 = bym.with_columns(pl.Series("adj_ci_low", [0.20, -0.01, -0.13]))
ok("strict reading fails when only 1 of 3 module intervals excludes 0, while the point-estimate reading still passes",
   verdicts(overall, bym2)["verdict_strict"][0] == "weak or inconsistent" and verdicts(overall, bym2)["verdict"][0] == "consistent association")

# ---- binned residuals and the stratified difference ------------------------------------------------------------------
p = np.array([0.2, 0.2, 0.8, 0.8]); yy = np.array([0, 1, 1, 1.0])
br = lib.binned_residuals({"low": np.array([True, True, False, False]), "high": np.array([False, False, True, True])}, yy, p)
ok("binned residuals: observed 0.5 against predicted 0.2; band = 2 x sqrt(2 x 0.16) / 2", abs(br["residual"][0] - 0.3) < 1e-12 and abs(br["two_se"][0] - 2 * np.sqrt(0.32) / 2) < 1e-12)
one = lib.mh_risk_difference([(30, 100, 20, 100)])
ok("stratified difference with one stratum = plain difference 0.10 with its Wald standard error", abs(one["rd"] - 0.10) < 1e-12
   and abs(one["se"] - np.sqrt(0.3 * 0.7 / 100 + 0.2 * 0.8 / 100)) < 1e-12)
# Simpson-type toy: within each stratum group 1 is 10 points lower, pooled it looks higher because of the mix
mh = lib.mh_risk_difference([(80, 100, 810, 900), (90, 900, 20, 100)])
pooled = (80 + 90) / 1000 - (810 + 20) / 1000
ok("stratified difference is -0.10 in a toy case where the mix of strata differs between the groups", abs(mh["rd"] + 0.10) < 1e-12 and pooled < -0.5)

from aq1_common import year_comparison, year_difference  # noqa: E402

toy = pl.DataFrame({"code_module": ["A"] * 400 + ["C"] * 100, "start_month": ["J"] * 500, "year": [2013] * 200 + [2014] * 300,
                    "run": ["A-2013J"] * 200 + ["A-2014J"] * 200 + ["C-2014J"] * 100,
                    "enrolled_d14": [True] * 180 + [False] * 20 + [True] * 150 + [False] * 50 + [True] * 100,
                    "non_completion": ([True] * 90 + [False] * 90 + [True] * 20) + ([True] * 60 + [False] * 90 + [True] * 50) + [True] * 80 + [False] * 20})
yc = year_comparison(toy)
kpi_shared = yc.filter(pl.col("denominator").str.starts_with("registered") & pl.col("scope").str.contains("modules run in both years")).row(0, named=True)
all_shared = yc.filter((pl.col("denominator") == "all enrolments") & pl.col("scope").str.contains("modules run in both years")).row(0, named=True)
kpi_all = yc.filter(pl.col("denominator").str.starts_with("registered") & pl.col("scope").str.starts_with("all runs")).row(0, named=True)
ok("year comparison, shared modules, day-14 denominator: 60/150 - 90/180 = -0.10", abs(kpi_shared["difference_2014_minus_2013"] + 0.10) < 1e-12 and kpi_shared["n_2014"] == 150)
ok("year comparison, shared modules, all enrolments: 110/200 - 110/200 = 0 (the sign changes with the denominator)", abs(all_shared["difference_2014_minus_2013"]) < 1e-12)
ok("year comparison over all runs includes the module that ran only in 2014: 140/250 - 90/180", abs(kpi_all["difference_2014_minus_2013"] - (140 / 250 - 0.5)) < 1e-12)
yd = year_difference(toy.filter(pl.col("year") == 2013), toy.filter(pl.col("year") == 2014))
ok("Newcombe interval contains the difference and is not symmetric Wald", yd["ci_low"] < yd["difference_2014_minus_2013"] < yd["ci_high"])

bad = [n for n, v in checks if not v]
print(f"\n{len(checks) - len(bad)} of {len(checks)} checks passed (synthetic inputs, code paths only)")
sys.exit(1 if bad else 0)
