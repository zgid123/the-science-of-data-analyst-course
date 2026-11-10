"""T26: exact (unrounded) values behind the two-year rows of Tables A.29-A.34 and the numbers of Sections 11.2-11.3,
recomputed from the prepared views with the package's own functions, rounded once (half-up, one decimal), and
checked against the report's Markdown: every generated row must appear verbatim in its appendix file.
The result CSVs store values already rounded to 4 (rates) or 2 (points) decimals, so a value such as 20.25 can round
either way; this script settles each such tie from the unrounded number.
Usage (from the repository root): venv/bin/python reports/milestone-5/code/t26_exact_rows.py
"""
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import numpy as np
import polars as pl

TASK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TASK / "package" / "src" / "analysis"))
import aq_analysis as A  # noqa: E402

REPORT = TASK / "report"


def f(v, d=1):
    return str(Decimal(repr(float(v))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)).replace("-", "−")


def pct(e, n):
    p, lo, hi = A.wilson(e, n)
    return f"{f(100 * p)}% ({f(100 * lo)}–{f(100 * hi)})"


enr = pl.read_parquet(A.PROC / "enrolment.parquet")
rows = {"16-12-aq1-results.md": [], "16-13-aq2-results.md": []}
# Table A.29
for label, cond in [("2013", pl.col("year") == 2013), ("2014", pl.col("year") == 2014), ("22 runs", pl.lit(True))]:
    for den, dcond, kpi in [("registered at day 14 (KPI population)", pl.col("enrolled_d14"), True),
                            ("all enrolments", pl.lit(True), False)]:
        d = enr.filter(cond & dcond)
        cells = [pct(int(d["non_completion"].sum()), d.height)]
        cells += [pct(int((d["final_result"] == o).sum()), d.height) for o in ["Pass", "Distinction", "Fail", "Withdrawn"]]
        rows["16-12-aq1-results.md"].append(f"| {label}, {den} | {d.height:,} | " + " | ".join(cells) + " |")
# Table A.30
d14 = enr.filter(pl.col("enrolled_d14")).with_columns(pl.col("code_presentation").str.slice(4, 1).alias("sm"))
for g, cond in [(m, pl.col("code_module") == m) for m in ["AAA", "BBB", "DDD", "EEE", "FFF", "GGG"]] + [
        ("February start (B runs)", pl.col("sm") == "B"), ("October start (J runs)", pl.col("sm") == "J")]:
    c = []
    for y in (2013, 2014):
        s = d14.filter(cond & (pl.col("year") == y))
        c += [f"{s.height:,}", pct(int(s["non_completion"].sum()), s.height)]
    rows["16-12-aq1-results.md"].append(f"| {g} | " + " | ".join(c) + " |")
# Table A.31
OUT = ["Distinction", "Pass", "Fail", "Withdrawn"]
for y in (2013, 2014):
    s = d14.filter(pl.col("year") == y)
    for g, cond in [(o, pl.col("final_result") == o) for o in OUT] + [
            ("Completed (Pass or Distinction)", pl.col("completed")), ("Not completed (Fail or Withdrawn)", pl.col("non_completion"))]:
        t = s.filter(cond)
        miss = t["first_missed_week"].drop_nulls()
        q = [int(miss.quantile(x, "lower")) for x in (0.25, 0.5, 0.75)]
        rows["16-12-aq1-results.md"].append(
            f"| {y} | {g} | {t.height:,} | {pct(miss.len(), t.height)} | {pct(int((t['first_missed_week'] <= 4).sum()), t.height)} | "
            f"{q[1]} ({q[0]}–{q[2]}) |")
# Table A.32
def ratecell(s):
    return f"{f(100 * s['non_completion'].sum() / s.height)}% ({s.height:,})"
def diffcell(a, b):
    d, lo, hi = A.newcombe(int(b["non_completion"].sum()), b.height, int(a["non_completion"].sum()), a.height)
    sign = "+" if d > 0 else ""
    return f"{sign}{f(100 * d)} ({f(100 * lo)} to {f(100 * hi)})"
shared = ["AAA", "BBB", "DDD", "EEE", "FFF", "GGG"]
allr = enr.with_columns(pl.col("code_presentation").str.slice(4, 1).alias("sm"))
for g, cond in [("All runs", pl.lit(True)), ("Six modules run in both years", pl.col("code_module").is_in(shared))] + [
        (m, pl.col("code_module") == m) for m in shared] + [("February start", pl.col("sm") == "B"), ("October start", pl.col("sm") == "J")]:
    c = []
    for dcond in [pl.col("enrolled_d14"), pl.lit(True)]:
        a_ = allr.filter(cond & dcond & (pl.col("year") == 2013)); b_ = allr.filter(cond & dcond & (pl.col("year") == 2014))
        c += [ratecell(a_), ratecell(b_), diffcell(a_, b_)]
    rows["16-12-aq1-results.md"].append(f"| {g} | " + " | ".join(c) + " |")
# Table A.33 / A.34 mutually adjusted values (exact)
NAME = {"missed_task": "Task due not submitted", "late_tma": "TMA submitted late", "inactive_last7": "No click on days 21–27",
        "low_relative_activity": "Clicks below run median", "no_pre_start_activity": "No click before day 0"}
mods = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
A33 = {"missed_task": "Task due not submitted", "late_tma": "TMA submitted late", "inactive_last7": "No click on days 21–27",
       "low_relative_activity": "Clicks on days 0–27 below run median", "no_pre_start_activity": "No click before day 0"}
exact = {}
for scope in ["2013", "2014"]:
    A.set_scope(scope)
    fr = A.build_signs(A.load_view("features_d27"))
    m = A.Fit(fr, list(A.SIGNS))
    for s in A.SIGNS:
        mask = A.defined_mask(fr, s)
        e, lo, hi, _ = m.ame(s, np.where(mask)[0])
        exact[(scope, s)] = f"{f(100 * e)} ({f(100 * lo)}–{f(100 * hi)})"
        d = fr.filter(pl.Series(mask))
        a_ = int(((d[s] == 1) & (d["y"] == 1)).sum()); n1 = int((d[s] == 1).sum())
        c_ = int(((d[s] == 0) & (d["y"] == 1)).sum()); n0 = int((d[s] == 0).sum())
        rd, rlo, rhi = A.newcombe(a_, n1, c_, n0)
        lo_, se_ = m.log_or(s); o = A.or_ci(lo_, se_)
        same = sum(1 for mo in m.mods[s] if np.sign(m.ame(s, np.where(mask & (m.mod == mo))[0])[0]) == np.sign(e))
        runs = d["run"].n_unique()
        rows["16-13-aq2-results.md"].append(
            f"| {A33[s]} | {scope}: {runs} runs, n = {d.height:,} | {n1:,} | {f(100 * a_ / n1)}% / {f(100 * c_ / n0)}% | "
            f"{f(100 * rd)} ({f(100 * rlo)}–{f(100 * rhi)}) | {exact[(scope, s)]} | {f(o[0], 2)} ({f(o[1], 2)}–{f(o[2], 2)}) | "
            f"{same} of {len(m.mods[s])} | ")
        cells = []
        for mo in mods:
            if mo in m.mods[s]:
                e, lo, hi, _ = m.ame(s, np.where(mask & (m.mod == mo))[0])
                cells.append(f"{f(100 * e)} ({f(100 * lo)}–{f(100 * hi)})")
            else:
                cells.append("–")
        rows["16-13-aq2-results.md"].append(f"| {NAME[s]}, {scope} | " + " | ".join(cells) + " |")
A.set_scope("2013")
bad = 0
for fn, rs in rows.items():
    text = (REPORT / fn).read_text()
    for r in rs:
        ok = r in text
        bad += not ok
        print(("OK    " if ok else "DIFF  ") + fn + "  " + r)
print("exact mutually adjusted differences (for Table A.33 and Sections 11.3):")
for k, v in exact.items():
    print(f"  {k[0]} {k[1]}: {v}")
print(f"SUMMARY: {sum(len(v) for v in rows.values()) - bad} of {sum(len(v) for v in rows.values())} rows match the report")
