"""AQ1 step 2 – completion and non-completion rates, outcome shares, and the week of the first missed task.

Population (Level 1 report, Table 2.1): enrolments still registered at day 14 (the KPI population).
Baselines (Table 4.1): pooled rate; the same rate over all enrolments (second denominator); the rate without the
enrolments flagged for a missing withdrawal or registration day.

Writes results/*_<scope>.csv; prints every table to the Markdown log.
"""

import polars as pl

from aq1_common import EXTRACT, RESULTS, lib, rate_table, scope_args

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
