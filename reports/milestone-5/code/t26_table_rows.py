"""T26: Markdown rows of Tables A.33 and A.34 (Appendix XIII) for 2013 and 2014, from the result files, so the
report's numbers are copied by code. Rounding: half-up to one decimal from the two-decimal values in the CSV files
(three decimals for odds ratios, shown with two).
Usage (from the repository root): venv/bin/python reports/milestone-5/code/t26_table_rows.py
"""
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import polars as pl

RES = Path(__file__).resolve().parents[1] / "results"
NAME = {"missed_task": "Task due not submitted", "late_tma": "TMA submitted late",
        "inactive_last7": "No click on days 21–27", "low_relative_activity": "Clicks on days 0–27 below run median",
        "no_pre_start_activity": "No click before day 0"}
SHORT = {**NAME, "low_relative_activity": "Clicks below run median"}


def f(v, d=1) -> str:
    q = Decimal(str(v)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return str(q).replace("-", "−")


def n(v) -> str:
    return f"{int(v):,}"


def ci(x, a, b, d=1) -> str:
    return f"{f(x[a], d)} ({f(x[b + '_low' if not b.endswith('_') else b + 'low'], d)}–{f(x[b + '_high' if not b.endswith('_') else b + 'high'], d)})"


for year, d in [("2013", RES / "2013"), ("2014", RES / "2014")]:
    a = pl.read_csv(d / "aq2_associations.csv")
    for x in a.iter_rows(named=True):
        runs = x["population"].split(" in ")[-1].replace("the ", "").replace("all ", "")
        runs = runs.split(" runs")[0] + " runs"
        print(f"| {NAME[x['sign']]} | {year}: {runs}, n = {n(x['n'])} | {n(x['n_with'])} | "
              f"{f(100 * x['rate_with'])}% / {f(100 * x['rate_without'])}% | "
              f"{f(x['rd_unadj_pp'])} ({f(x['rd_unadj_ci_low'])}–{f(x['rd_unadj_ci_high'])}) | "
              f"{f(x['rd_adj_mutual_pp'])} ({f(x['rd_adj_mutual_ci_low'])}–{f(x['rd_adj_mutual_ci_high'])}) | "
              f"{f(x['or_adj_mutual'], 2)} ({f(x['or_adj_mutual_ci_low'], 2)}–{f(x['or_adj_mutual_ci_high'], 2)}) | "
              f"{x['modules_same_direction']} of {x['modules_defined']} | {x['verdict'].capitalize()} |")
print()
mods = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
for year, d in [("2013", RES / "2013"), ("2014", RES / "2014")]:
    m = pl.read_csv(d / "aq2_module_effects.csv")
    for s in NAME:
        cells = []
        for mo in mods:
            r = m.filter((pl.col("sign") == s) & (pl.col("module") == mo))
            if r.height:
                x = r.row(0, named=True)
                cells.append(f"{f(x['rd_adj_mutual_pp'])} ({f(x['rd_adj_mutual_ci_low'])}–{f(x['rd_adj_mutual_ci_high'])})")
            else:
                cells.append("–")
        print(f"| {SHORT[s]}, {year} | " + " | ".join(cells) + " |")
