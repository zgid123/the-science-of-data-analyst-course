"""AQ1 step 2 – completion and non-completion rates, outcome shares, and the week of the first missed task.

Population (Level 1 report, Table 2.1): enrolments still registered at day 14 (the KPI population).
Baselines (Table 4.1): pooled rate; the same rate over all enrolments (second denominator); the rate without the
enrolments flagged for a missing withdrawal or registration day.

Scope all adds the year comparison of PROTOCOL.md P18: the 2014 - 2013 difference with a Newcombe interval on both
denominators, overall, for the modules and the module x start-month pairs that ran in both years, per module and per
start month, and the share of enrolments not registered at day 14 in each year.

Writes results/*_<scope>.csv; prints every table to the Markdown log.
"""

import polars as pl

from aq1_common import EXTRACT, RESULTS, lib, paired_keys, rate_table, scope_args, year_comparison, year_difference

scope, years = scope_args(__doc__)
enr = pl.read_csv(EXTRACT / f"aq1_enrolments_{scope}.csv")
kpi = enr.filter(pl.col("enrolled_d14"))
flag = pl.col("registration_missing") | pl.col("withdrawal_day_missing")

lib.banner(f"Populations, scope = {scope}")
pops = pl.DataFrame({
    "population": ["all enrolments", "KPI: registered at day 14", "KPI without flagged enrolments", "flagged (missing withdrawal or registration day), all", "flagged, in the KPI population"],
    "enrolments": [enr.height, kpi.height, kpi.filter(~flag).height, enr.filter(flag).height, kpi.filter(flag).height],
})
print(lib.md_table(pops))
lib.save_csv(pops, RESULTS / f"populations_{scope}.csv")

# ---- rates by level -------------------------------------------------------------------------------
lib.banner("Non-completion rate (Fail or Withdrawn) with Wilson 95% intervals, KPI population")
levels = {"pooled": [], "year": ["year"], "start_month": ["start_month"], "year_start": ["year", "start_month"],
          "module": ["code_module"], "run": ["code_module", "code_presentation", "run"]}
frames = []
for name, by in levels.items():
    t = rate_table(kpi, by).with_columns(pl.lit(name).alias("level"))
    label = pl.lit("all runs") if not by else pl.concat_str([pl.col(c).cast(pl.Utf8) for c in (["run"] if name == "run" else by)], separator="-")
    t = t.with_columns(label.alias("group")).select("level", "group", "enrolments", "events", "rate", "ci_low", "ci_high")
    frames.append(t)
    print(f"**By {name}**\n\n{lib.md_table(t.drop('level'))}\n")
rates = pl.concat(frames)
lib.save_csv(rates, RESULTS / f"rates_{scope}.csv", "non-completion rate by level, KPI population")

# ---- module by start month: does the February gap hold inside each module? -------------------------------
ms = rate_table(kpi, ["code_module", "start_month"]).pivot(on="start_month", index="code_module", values=["enrolments", "rate"]).sort("code_module")
if "rate_B" in ms.columns and "rate_J" in ms.columns:
    ms = ms.with_columns((pl.col("rate_B") - pl.col("rate_J")).alias("february_minus_october"))
    both = ms.filter(pl.col("february_minus_october").is_not_null())
    print("**Module by start month (B = February, J = October)**\n\n" + lib.md_table(ms))
    print(f"\nmodules with both start months: {both.height}; February rate higher in {int((both['february_minus_october'] > 0).sum())} of them "
          f"(gap {float(both['february_minus_october'].min()):.3f} to {float(both['february_minus_october'].max()):.3f})\n")
    lib.save_csv(ms, RESULTS / f"rates_module_by_start_month_{scope}.csv")

# ---- year comparison (scope all only; PROTOCOL.md P18) -------------------------------------------------
if scope == "all":
    lib.banner("Year comparison: 2014 minus 2013 non-completion, Newcombe 95% interval, two denominators")
    yc = year_comparison(enr)
    show = ["denominator", "level", "scope", "method", "n_2013", "rate_2013", "n_2014", "rate_2014", "difference_2014_minus_2013", "ci_low", "ci_high", "interval_excludes_0"]
    print("**Overall scopes**\n\n" + lib.md_table(yc.filter(pl.col("level") == "overall").select(show), digits=4))
    print("\n**By module (the six modules run in both years)**\n\n" + lib.md_table(yc.filter(pl.col("level") == "module").select(show), digits=4))
    print("\n**By start month**\n\n" + lib.md_table(yc.filter(pl.col("level").str.starts_with("start month")).select(show), digits=4))
    print("\n**By module x start-month pair run in both years**\n\n" + lib.md_table(yc.filter(pl.col("level") == "pair").select(show), digits=4))
    lib.save_csv(yc, RESULTS / f"year_comparison_{scope}.csv")
    ov = yc.filter((pl.col("level") == "overall") & pl.col("method").str.starts_with("pooled"))
    flips = ov.pivot(on="denominator", index="scope", values="difference_2014_minus_2013")
    print("\n**Sign of the year difference under each denominator**\n\n" + lib.md_table(flips, digits=4))
    mods = yc.filter(pl.col("level") == "module")
    for den in mods["denominator"].unique(maintain_order=True).to_list():
        t = mods.filter(pl.col("denominator") == den)
        print(f"- {den}: 2014 lower in {int((t['difference_2014_minus_2013'] < 0).sum())} of {t.height} shared modules; "
              f"interval excludes 0 in {int(t['interval_excludes_0'].sum())} (lower: {int(((t['ci_high'] < 0)).sum())}, higher: {int((t['ci_low'] > 0).sum())})")

    # share of enrolments not registered at day 14, and how those enrolments ended
    shared = sorted(set(enr.filter(pl.col("year") == 2013)["code_module"]) & set(enr.filter(pl.col("year") == 2014)["code_module"]))
    paired = enr.join(paired_keys(enr), on=["code_module", "start_month"], how="inner")
    out_rows = []
    for label, d in [("all runs", enr), (f"{len(shared)} modules run in both years", enr.filter(pl.col("code_module").is_in(shared))),
                     (f"{paired_keys(enr).height} module x start-month pairs run in both years", paired)]:
        d = d.with_columns((~pl.col("enrolled_d14")).alias("not_registered_d14"))
        r = year_difference(d.filter(pl.col("year") == 2013), d.filter(pl.col("year") == 2014), "not_registered_d14")
        nr = d.filter(pl.col("not_registered_d14"))
        rn = year_difference(nr.filter(pl.col("year") == 2013), nr.filter(pl.col("year") == 2014), "non_completion")
        out_rows.append({"scope": label, "enrolments_2013": r["n_2013"], "not_registered_2013": r["events_2013"], "share_not_registered_2013": r["rate_2013"],
                         "enrolments_2014": r["n_2014"], "not_registered_2014": r["events_2014"], "share_not_registered_2014": r["rate_2014"],
                         "difference_2014_minus_2013": r["difference_2014_minus_2013"], "ci_low": r["ci_low"], "ci_high": r["ci_high"],
                         "non_completion_among_not_registered_2013": rn["rate_2013"], "non_completion_among_not_registered_2014": rn["rate_2014"]})
    nreg = pl.DataFrame(out_rows)
    print("\n**Share of enrolments not registered at day 14, by year (they are outside the KPI population and nearly all end in Fail or Withdrawn)**\n\n" + lib.md_table(nreg, digits=4))
    lib.save_csv(nreg, RESULTS / f"not_registered_d14_by_year_{scope}.csv")

# ---- the three denominators per run ------------------------------------------------------------------
lib.banner("Three denominators per run: KPI population, all enrolments, KPI without flagged enrolments")
by = ["code_module", "code_presentation", "run"]
a = rate_table(kpi, by).select("run", pl.col("enrolments").alias("n_kpi"), pl.col("rate").alias("rate_kpi"), "ci_low", "ci_high")
b = rate_table(enr, by).select("run", pl.col("enrolments").alias("n_all"), pl.col("rate").alias("rate_all"))
c = rate_table(kpi.filter(~flag), by).select("run", pl.col("enrolments").alias("n_unflagged"), pl.col("rate").alias("rate_unflagged"))
den = a.join(b, on="run").join(c, on="run").with_columns(
    (pl.col("rate_all") - pl.col("rate_kpi")).alias("shift_all_minus_kpi"),
    ((pl.col("rate_all") < pl.col("ci_low")) | (pl.col("rate_all") > pl.col("ci_high"))).alias("all_outside_kpi_interval"),
    (pl.col("rate_unflagged") - pl.col("rate_kpi")).alias("shift_unflagged_minus_kpi"),
    ((pl.col("rate_unflagged") < pl.col("ci_low")) | (pl.col("rate_unflagged") > pl.col("ci_high"))).alias("unflagged_outside_kpi_interval"),
).sort("run")
print(lib.md_table(den))
lib.save_csv(den, RESULTS / f"denominators_by_run_{scope}.csv")
pooled = pl.DataFrame({
    "denominator": ["KPI (registered at day 14)", "all enrolments", "KPI without flagged"],
    "enrolments": [kpi.height, enr.height, kpi.filter(~flag).height],
    "non_completers": [int(kpi["non_completion"].sum()), int(enr["non_completion"].sum()), int(kpi.filter(~flag)["non_completion"].sum())],
}).with_columns((pl.col("non_completers") / pl.col("enrolments")).alias("rate"))
print("\n**Pooled**\n\n" + lib.md_table(pooled))
lib.save_csv(pooled, RESULTS / f"denominators_pooled_{scope}.csv")

# ---- outcome shares ------------------------------------------------------------------------------------
lib.banner("Outcome shares (Pass, Distinction, Fail, Withdrawn), KPI population")
shares = []
for name, by in {"pooled": [], "module": ["code_module"], "run": ["run"], "year": ["year"], "start_month": ["start_month"]}.items():
    for res in ["Distinction", "Pass", "Fail", "Withdrawn"]:
        t = rate_table(kpi.with_columns((pl.col("final_result") == res).alias("ev")), by, "ev")
        label = pl.lit("all runs") if not by else pl.col(by[0]).cast(pl.Utf8)
        shares.append(t.with_columns(pl.lit(name).alias("level"), label.alias("group"), pl.lit(res).alias("final_result"))
                      .select("level", "group", "final_result", "enrolments", "events", "rate", "ci_low", "ci_high"))
shares = pl.concat(shares)
lib.save_csv(shares, RESULTS / f"outcome_shares_{scope}.csv")
wide = shares.filter(pl.col("level").is_in(["pooled", "module"])).pivot(on="final_result", index=["level", "group", "enrolments"], values="rate")
print(lib.md_table(wide))

# ---- subgroup description -----------------------------------------------------------------------------
lib.banner("Non-completion by audit attribute (description only; no model reads these columns)")
sub = []
for col in ["gender", "disability", "imd_band", "age_band"]:
    t = rate_table(kpi, [col]).with_columns(pl.lit(col).alias("attribute"), pl.col(col).cast(pl.Utf8).alias("group"))
    sub.append(t.select("attribute", "group", "enrolments", "events", "rate", "ci_low", "ci_high"))
sub = pl.concat(sub)
print(lib.md_table(sub))
lib.save_csv(sub, RESULTS / f"rates_by_audit_group_{scope}.csv")

# ---- first missed task ---------------------------------------------------------------------------------
lib.banner("Week of the first assessed task (TMA or CMA) due while enrolled and not submitted, KPI population")
sched = pl.read_csv(EXTRACT / f"aq1_task_schedule_{scope}.csv")
first_due = sched.group_by("run").agg(pl.col("due_day").min().alias("first_task_due_day"), pl.col("due_week").min().alias("first_task_due_week"),
                                      (pl.col("due_day") <= 27).sum().alias("tasks_due_by_day27"), pl.len().alias("tasks_in_run")).sort("run")
print("**Task calendar per run**\n\n" + lib.md_table(first_due))
lib.save_csv(first_due, RESULTS / f"task_calendar_by_run_{scope}.csv")
no_task = first_due.filter(pl.col("tasks_due_by_day27") == 0)["run"].to_list()
print(f"\nRuns with no task due by day 27: {len(no_task)} of {first_due.height}: {', '.join(no_task)}")

kpi2 = kpi.with_columns(pl.when(pl.col("non_completion")).then(pl.lit("Non-completers (Fail or Withdrawn)")).otherwise(pl.lit("Completers (Pass or Distinction)")).alias("group"))
rows = []
for grp_col in ["group", "final_result"]:
    for (g,), d in kpi2.group_by([grp_col]):
        n = d.height
        ever = d.filter(pl.col("first_missed_week").is_not_null())
        row = {"group": g, "enrolments": n, "ever_missed": ever.height, "share_ever_missed": ever.height / n,
               "median_first_missed_week": ever["first_missed_week"].median(),
               "p25_week": ever["first_missed_week"].quantile(0.25), "p75_week": ever["first_missed_week"].quantile(0.75)}
        for w in (4, 8, 12, 16, 20):
            row[f"share_missed_by_week_{w}"] = ever.filter(pl.col("first_missed_week") <= w).height / n
        rows.append(row)
fm = pl.DataFrame(rows).sort("group")
print("\n**First missed task by outcome**\n\n" + lib.md_table(fm))
lib.save_csv(fm, RESULTS / f"first_missed_task_by_outcome_{scope}.csv")

# Missed by week 4, with the runs that have a task due by day 27 shown apart: a student with nothing due has an
# undefined missed-task status, not "no missed task" (PROTOCOL.md P18).
with_task = first_due.filter(pl.col("tasks_due_by_day27") > 0)["run"].to_list()
w4 = []
for pop, dpop in [("all runs", kpi2), ("runs with a task due by day 27", kpi2.filter(pl.col("run").is_in(with_task)))]:
    for yr in ["both years"] + sorted(dpop["year"].unique().to_list()):
        dy = dpop if yr == "both years" else dpop.filter(pl.col("year") == yr)
        for (g,), d in dy.group_by(["group"]):
            t = rate_table(d.with_columns((pl.col("first_missed_week") <= 4).fill_null(False).alias("ev")), [], "ev").row(0, named=True)
            w4.append({"population": pop, "runs": dy["run"].n_unique(), "year": str(yr), "group": g, "enrolments": t["enrolments"], "missed_by_week_4": t["events"],
                       "share": t["rate"], "ci_low": t["ci_low"], "ci_high": t["ci_high"]})
w4 = pl.DataFrame(w4).sort("population", "year", "group")
print("\n**Share with a first missed task by the end of week 4 (day 27), Wilson 95% interval**\n\n" + lib.md_table(w4))
lib.save_csv(w4, RESULTS / f"first_missed_by_week4_{scope}.csv")
if scope == "all":
    nc2 = kpi2.filter(pl.col("non_completion")).with_columns((pl.col("first_missed_week") <= 4).fill_null(False).alias("missed_w4"))
    yd = []
    for pop, dpop in [("all runs", nc2), ("runs with a task due by day 27", nc2.filter(pl.col("run").is_in(with_task)))]:
        yd.append({"population": pop, "group": "non-completers", **year_difference(dpop.filter(pl.col("year") == 2013), dpop.filter(pl.col("year") == 2014), "missed_w4")})
    yd = pl.DataFrame(yd)
    print("\n**Non-completers with a missed task by week 4: 2014 minus 2013**\n\n" + lib.md_table(yd, digits=4))
    lib.save_csv(yd, RESULTS / f"first_missed_by_week4_year_difference_{scope}.csv")

cum = []
maxw = int(kpi2["first_missed_week"].max())
for (g,), d in kpi2.group_by(["group"]):
    n = d.height
    wk = d["first_missed_week"].drop_nulls().to_numpy()
    for w in range(1, maxw + 1):
        cum.append({"group": g, "week": w, "enrolments": n, "first_missed_in_week": int((wk == w).sum()), "cumulative_share": float((wk <= w).sum() / n)})
cum = pl.DataFrame(cum).sort("group", "week")
lib.save_csv(cum, RESULTS / f"first_missed_task_cumulative_{scope}.csv")

by_mod = []
nc = kpi2.filter(pl.col("non_completion"))
for (m,), d in nc.group_by(["code_module"]):
    ever = d.filter(pl.col("first_missed_week").is_not_null())
    by_mod.append({"code_module": m, "non_completers": d.height, "share_ever_missed": ever.height / d.height,
                   "median_first_missed_week": ever["first_missed_week"].median(),
                   "share_missed_by_week_4": ever.filter(pl.col("first_missed_week") <= 4).height / d.height,
                   "share_missed_by_week_8": ever.filter(pl.col("first_missed_week") <= 8).height / d.height})
by_mod = pl.DataFrame(by_mod).sort("code_module")
print("\n**Non-completers: first missed task by module**\n\n" + lib.md_table(by_mod))
lib.save_csv(by_mod, RESULTS / f"first_missed_task_by_module_{scope}.csv")
