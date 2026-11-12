"""AQ2 step 2 – how strongly each early sign goes with later non-completion (association only).

--scope 2013 (estimation) or 2014 (replication, after the AQ3 test).

Every risk difference is averaged over the support of its sign only (PROTOCOL.md P17) and printed with that n.

Outputs in results/, suffix _<scope>:
  associations            unadjusted and adjusted risk difference per sign, 95% intervals, n of the support, verdict
  associations_by_module  adjusted risk difference per sign and module, with a flag for intervals that include 0
  sign_support            per sign and module: rows where the sign is defined, with and without it, and how it is handled
  odds_ratios             odds ratios of the model without sign x module terms (reported beside the risk differences)
  sign_correlation        phi correlation between two signs on the rows where both are defined
  non_completion_by_sign_count   non-completion by number of signs present
  binned_residuals_by_run        observed minus predicted by run and three activity levels (the Level 1 card's check)
  binned_residuals_activity5     the same by five activity levels, main model and model with continuous activity (P21, P22)
  binned_residuals_decile        the same by tenth of the predicted risk
  sensitivity             adjusted risk differences, n and verdict under each variant, the post hoc variants included
  subgroups               risk differences by gender, disability and deprivation band (description), with n
  model_coefficients      every coefficient of the main model
"""

import argparse

import numpy as np
import polars as pl

from aq2_model import (ACTIVITY_LEVELS5, CONTINUOUS_ACTIVITY, EXTRACT, RESULTS, SIGNS, VARIANT_LABELS, AssociationModel, lib,
                       diff_proportions_ci, risk_deciles, unadjusted, verdicts)

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--scope", choices=["2013", "2014"], required=True)
scope = p.parse_args().scope
if scope == "2014":
    lib.open_test_outcomes("aq-2/code/02_associations.py", "AQ2 replication on the 2014 runs (Appendix III step 8)")
df = pl.read_csv(EXTRACT / f"aq2_signs_d27_{scope}.csv")
signs = list(SIGNS)
y = df["non_completion"].to_numpy()

lib.banner(f"AQ2 associations at day 27, scope = {scope}: {df.height:,} enrolments, {df['run'].n_unique()} runs, "
           f"{int(y.sum()):,} non-completers ({y.mean():.1%})")

# ---- main model --------------------------------------------------------------------------------------
un = unadjusted(df, signs)
model = AssociationModel(df, signs, interactions=True)
adj = model.table()
bym = model.by_module()
ver = verdicts(adj, bym)
assert (un["enrolments"] == adj["n_support"]).all(), "unadjusted and adjusted estimates must use the same rows"
main = un.join(adj.drop("n_with_sign"), on="sign").join(ver.drop("adjusted_rd"), on="sign").with_columns(
    pl.col("sign").replace_strict(SIGNS).alias("label"))
print("**Risk difference per sign (percentage points = value x 100); n = rows of the support, the only rows averaged over**\n")
print(lib.md_table(main.select("sign", pl.col("n_support").alias("n"), "support_modules", "rows_defined_outside_support", "with_sign",
                               "rate_with_sign", "rate_without_sign", "unadjusted_rd", "unadj_ci_low", "unadj_ci_high",
                               "adjusted_rd", "adj_ci_low", "adj_ci_high")))
print("\n**Verdict against the Level 1 criterion (verdict = direction of the module point estimates, as Level 1 words it; "
      "verdict_strict = only modules whose own interval excludes 0)**\n")
print(lib.md_table(ver))
lib.save_csv(main, RESULTS / f"associations_{scope}.csv")
print("\n**Adjusted risk difference by module (modules with their own slope: at least 20 enrolments with and 20 without the sign)**\n")
print(lib.md_table(bym))
lib.save_csv(bym, RESULTS / f"associations_by_module_{scope}.csv")
unclear = bym.filter(~pl.col("interval_excludes_0"))
print(f"\nmodule estimates whose 95% interval includes 0 (no detectable association in that module): {unclear.height} of {bym.height}")
if unclear.height:
    print("\n" + lib.md_table(unclear.select("sign", "code_module", "enrolments", "with_sign", "adjusted_rd", "adj_ci_low", "adj_ci_high")))
sup = model.support_table()
print("\n**Support of each sign: rows of each module where the sign is defined, and how the module is handled**\n\n" + lib.md_table(sup))
lib.save_csv(sup, RESULTS / f"sign_support_{scope}.csv")
out_of_support = sup.filter(pl.col("handling").str.contains("outside the support") & (pl.col("rows_defined") > 0))
print(f"\nmodules where a sign is defined by the calendar but does not vary (rows left out of that sign's average): {out_of_support.height}")
print(f"\nmodel: {len(model.names)} coefficients, converged = {model.fit.converged}, log-likelihood = {model.fit.llf:.1f}, "
      f"deviance = {model.fit.deviance:.1f}")
coef = pl.DataFrame({"term": model.names, "coefficient": model.beta, "robust_se": np.asarray(model.fit.bse), "p_value": np.asarray(model.fit.pvalues)})
lib.save_csv(coef, RESULTS / f"model_coefficients_{scope}.csv")

# ---- odds ratios from the model without interactions ---------------------------------------------------
simple = AssociationModel(df, signs, interactions=False)
orr = simple.odds_ratios().with_columns(pl.col("term").str.replace(":all", ""))
orr = orr.join(simple.table().select(pl.col("sign").alias("term"), pl.col("adjusted_rd").alias("adjusted_rd_no_interactions")), on="term")
print("\n**Odds ratios, model without sign x module terms (they read larger than risk ratios at a 44% base rate)**\n")
print(lib.md_table(orr))
lib.save_csv(orr, RESULTS / f"odds_ratios_{scope}.csv")

# ---- correlation among signs, on the rows where both signs are defined -----------------------------------
rows = []
for i, a in enumerate(signs):
    for b in signs[i + 1:]:
        both = model.support[a] & model.support[b]
        xa, xb = df[a].to_numpy().astype(float)[both], df[b].to_numpy().astype(float)[both]
        rows.append({"sign_a": a, "sign_b": b, "enrolments_both_defined": int(both.sum()), "phi": float(np.corrcoef(xa, xb)[0, 1]),
                     "with_both": int((xa * xb).sum())})
cm = pl.DataFrame(rows)
print("\n**Phi correlation between signs, on the rows where both are defined**\n\n" + lib.md_table(cm))
lib.save_csv(cm, RESULTS / f"sign_correlation_{scope}.csv")
S = df.select(signs).to_numpy().astype(int)
all5 = np.logical_and.reduce([model.support[s] for s in signs])
co = []
for name, mask in {"all enrolments (task signs cannot occur in runs without a task due)": np.ones(df.height, bool),
                   "runs where all five signs are defined": all5}.items():
    t = (pl.DataFrame({"signs_present": S[mask].sum(axis=1), "y": y[mask]}).group_by("signs_present")
         .agg(pl.len().alias("enrolments"), pl.col("y").mean().alias("non_completion_rate")).sort("signs_present"))
    co.append(t.with_columns(pl.lit(name).alias("population")).select("population", "signs_present", "enrolments", "non_completion_rate"))
co = pl.concat(co)
print("\n**Non-completion by number of signs present**\n\n" + lib.md_table(co))
lib.save_csv(co, RESULTS / f"non_completion_by_sign_count_{scope}.csv")

# ---- binned residuals (P21) ----------------------------------------------------------------------------
yf = y.astype(float)
run, lvl3, lvl5 = df["run"].to_numpy(), df["activity_level"].to_numpy(), df["activity_level5"].to_numpy()
cells = {f"{r} | {a}": (run == r) & (lvl3 == a) for r in sorted(set(run)) for a in ("none", "low", "normal")}
res = lib.binned_residuals(cells, yf, model.p).with_columns(
    pl.col("group").str.split(" | ").list.get(0).alias("run"), pl.col("group").str.split(" | ").list.get(1).alias("activity_level")).drop("group")
res = res.select("run", "activity_level", "enrolments", "observed", "predicted", "residual", "two_se", "outside_2se")
print("\n**(a) Binned residuals by run and three activity levels (the check named in the Level 1 card). The levels are cut at "
      "the low-activity sign's own threshold, so the model fits them almost by construction.**\n\n" + lib.md_table(res))
print(f"\ncells outside two standard errors: {int(res['outside_2se'].sum())} of {res.height}; largest |residual| = {float(res['residual'].abs().max()):.3f}")
lib.save_csv(res, RESULTS / f"binned_residuals_by_run_{scope}.csv")

signs_median = [s if s != "sign_low_activity" else "sign_low_activity_median" for s in signs]
models = {
    "main model (low activity = below half the run median)": model,
    "main model, low activity = below the run median": AssociationModel(df, signs_median, interactions=True),
    "post hoc: main model + log(1 + clicks on days 0-27)": AssociationModel(df, signs, interactions=True, extra=[CONTINUOUS_ACTIVITY]),
    "post hoc: low activity = below the run median, + log(1 + clicks on days 0-27)": AssociationModel(df, signs_median, interactions=True, extra=[CONTINUOUS_ACTIVITY]),
}
r5, rd = [], []
for name, m in models.items():
    t = lib.binned_residuals({a: lvl5 == a for a in ACTIVITY_LEVELS5}, yf, m.p)
    r5.append(t.with_columns(pl.lit(name).alias("model")).select("model", pl.col("group").alias("activity_level5"), "enrolments", "observed", "predicted", "residual", "two_se", "outside_2se"))
    dec = risk_deciles(m.p)
    t = lib.binned_residuals({f"{d:02d}": dec == d for d in range(1, 11)}, yf, m.p)
    rd.append(t.with_columns(pl.lit(name).alias("model")).select("model", pl.col("group").alias("risk_decile"), "enrolments", "observed", "predicted", "residual", "two_se", "outside_2se"))
r5, rd = pl.concat(r5), pl.concat(rd)
print("\n**(b) Binned residuals by five activity levels on days 0-27**\n\n" + lib.md_table(r5))
print("\n**(c) Binned residuals by tenth of the predicted risk**\n\n" + lib.md_table(rd))
for name in models:
    a, b = r5.filter(pl.col("model") == name), rd.filter(pl.col("model") == name)
    print(f"- {name}: activity levels outside two standard errors: {int(a['outside_2se'].sum())} of {a.height} "
          f"(largest |residual| {float(a['residual'].abs().max()):.3f}); risk tenths outside: {int(b['outside_2se'].sum())} of {b.height} "
          f"(largest {float(b['residual'].abs().max()):.3f})")
lib.save_csv(r5, RESULTS / f"binned_residuals_activity5_{scope}.csv")
lib.save_csv(rd, RESULTS / f"binned_residuals_decile_{scope}.csv")
cont = models["post hoc: main model + log(1 + clicks on days 0-27)"]
j = cont.names.index(CONTINUOUS_ACTIVITY)
print(f"\ncontinuous activity term: coefficient {cont.beta[j]:.4f} per unit of log(1 + clicks) (robust SE {np.sqrt(cont.V[j, j]):.4f}), "
      f"odds ratio {np.exp(cont.beta[j]):.3f}; deviance {cont.fit.deviance:.1f} against {model.fit.deviance:.1f} for the main model")

# ---- sensitivity ---------------------------------------------------------------------------------------
swap = lambda old, new: [s if s != old else new for s in signs]  # noqa: E731
variants = {
    "main": (df, signs, None, "planned"),
    "clicks de-duplicated (low-activity sign from de-duplicated clicks)": (df, swap("sign_low_activity", "sign_low_activity_dedup"), None, "planned"),
    "late CMAs also count as late": (df, swap("sign_tma_late", "sign_any_task_late"), None, "planned"),
    "without flagged enrolments": (df.filter(~pl.col("flagged")), signs, None, "planned"),
    "only runs with a task due by day 27": (df.filter(pl.col("run_has_task_due")), signs, None, "planned"),
    "low activity = below a quarter of the run median": (df, swap("sign_low_activity", "sign_low_activity_q25"), None, "planned"),
    "low activity = below the run median": (df, signs_median, None, "planned"),
    "post hoc: + log(1 + clicks on days 0-27)": (df, signs, [CONTINUOUS_ACTIVITY], "post hoc"),
    "post hoc: low activity = below the run median, + log(1 + clicks on days 0-27)": (df, signs_median, [CONTINUOUS_ACTIVITY], "post hoc"),
}
sens = []
for name, (d, sg, extra, status) in variants.items():
    m = AssociationModel(d, sg, interactions=True, extra=extra)
    t, v = m.table(), verdicts(m.table(), m.by_module())
    t = t.join(v.drop("adjusted_rd"), on="sign").with_columns(pl.lit(name).alias("variant"), pl.lit(status).alias("status"), pl.lit(d.height).alias("rows_in_model"))
    sens.append(t.select("variant", "status", "rows_in_model", "sign", pl.col("n_support").alias("n"), "n_with_sign", "support_modules", "adjusted_rd",
                         "adj_ci_low", "adj_ci_high", "at_least_5_points", "interval_excludes_0", "modules_defined", "modules_same_direction",
                         "modules_same_direction_interval_excludes_0", "modules_interval_includes_0", "verdict", "verdict_strict"))
sens = pl.concat(sens)
print("\n**Sensitivity of the adjusted risk differences (n = rows of the sign's support in that variant)**\n\n" + lib.md_table(sens))
weak = sens.filter(pl.col("verdict") != "consistent association")
print(f"\nsign x variant rows that do not meet the Level 1 criterion: {weak.height} of {sens.height}")
if weak.height:
    print("\n" + lib.md_table(weak.select("variant", "sign", "n", "adjusted_rd", "adj_ci_low", "adj_ci_high", "modules_defined", "modules_same_direction", "verdict")))
lib.save_csv(sens, RESULTS / f"sensitivity_{scope}.csv")

# ---- subgroups (description) ---------------------------------------------------------------------------
df2 = df.with_columns(pl.when(pl.col("imd_band") == "Missing").then(pl.lit("Missing"))
                      .when(pl.col("imd_band").is_in(["0-10%", "10-20%", "20-30%"])).then(pl.lit("0-30% (most deprived)"))
                      .when(pl.col("imd_band").is_in(["30-40%", "40-50%", "50-60%", "60-70%"])).then(pl.lit("30-70%"))
                      .otherwise(pl.lit("70-100% (least deprived)")).alias("imd_group"))
sub = []
yb = y.astype(bool)
for col in ["gender", "disability", "imd_group"]:
    for g in sorted(df2[col].unique().to_list()):
        rows_g = (df2[col] == g).to_numpy()
        for s in signs:
            r = model.risk_difference(s, rows_g)
            d = model.support[s] & rows_g                      # the same rows for the plain and the adjusted difference
            x = df[s].to_numpy().astype(bool)
            k1, n1, k0, n0 = int(yb[d & x].sum()), int((d & x).sum()), int(yb[d & ~x].sum()), int((d & ~x).sum())
            u = diff_proportions_ci(k1, n1, k0, n0) if n1 and n0 else (float("nan"),) * 3
            sub.append({"attribute": col, "group": g, "sign": s, "n": r["n"], "with_sign": r["with_sign"],
                        "unadjusted_rd": u[0], "unadj_ci_low": u[1], "unadj_ci_high": u[2],
                        "adjusted_rd": r["rd"], "adj_ci_low": r["ci_low"], "adj_ci_high": r["ci_high"]})
sub = pl.DataFrame(sub)
print("\n**Risk differences by audit group (description; the groups are not model inputs; n = rows of the support in the group)**\n\n" + lib.md_table(sub))
lib.save_csv(sub, RESULTS / f"subgroups_{scope}.csv")
print("\nlabels of the sensitivity signs: " + "; ".join(f"{k} = {v}" for k, v in VARIANT_LABELS.items()))
