"""AQ2 step 2 – how strongly each early sign goes with later non-completion (association only).

--scope 2013 (estimation) or 2014 (replication, after the AQ3 test).

Outputs in results/, suffix _<scope>:
  associations          unadjusted and adjusted risk difference per sign, with 95% intervals, and the verdict
  associations_by_module  adjusted risk difference per sign and module
  odds_ratios           odds ratios of the model without sign x module terms (reported beside the risk differences)
  sign_correlation      phi correlation between signs, and co-occurrence
  binned_residuals      observed minus predicted rate by run and activity level
  sensitivity           the adjusted risk differences under each variant of Table 4.2
  subgroups             risk differences by gender, disability and deprivation band (description)
  model_coefficients    every coefficient of the main model
"""

import argparse

import numpy as np
import polars as pl

from aq2_model import EXTRACT, RESULTS, SIGNS, AssociationModel, lib, unadjusted, verdicts

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
main = un.join(adj.drop("enrolments_defined"), on="sign").join(ver.drop("adjusted_rd"), on="sign").with_columns(
    pl.col("sign").replace_strict(SIGNS).alias("label"))
print("**Risk difference per sign (percentage points = value x 100)**\n")
print(lib.md_table(main.select("sign", "enrolments_defined", "with_sign", "rate_with_sign", "rate_without_sign", "unadjusted_rd",
                               "unadj_ci_low", "unadj_ci_high", "adjusted_rd", "adj_ci_low", "adj_ci_high")))
print("\n**Verdict against the Level 1 criterion**\n")
print(lib.md_table(ver))
lib.save_csv(main, RESULTS / f"associations_{scope}.csv")
print("\n**Adjusted risk difference by module (modules with at least 20 enrolments with and without the sign)**\n")
print(lib.md_table(bym))
lib.save_csv(bym, RESULTS / f"associations_by_module_{scope}.csv")
if model.cell_notes:
    notes = pl.DataFrame(model.cell_notes)
    print("\n**Sign x module cells below the minimum size**\n\n" + lib.md_table(notes))
    lib.save_csv(notes, RESULTS / f"small_cells_{scope}.csv")
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

# ---- correlation among signs ---------------------------------------------------------------------------
S = df.select(signs).to_numpy().astype(float)
corr = np.corrcoef(S.T)
cm = pl.DataFrame({"sign": signs, **{s: corr[:, i] for i, s in enumerate(signs)}})
print("\n**Phi correlation between signs (all enrolments)**\n\n" + lib.md_table(cm))
lib.save_csv(cm, RESULTS / f"sign_correlation_{scope}.csv")
nsig = S.sum(axis=1).astype(int)
co = pl.DataFrame({"signs_present": nsig, "y": y}).group_by("signs_present").agg(pl.len().alias("enrolments"), pl.col("y").mean().alias("non_completion_rate")).sort("signs_present")
print("\n**Non-completion by number of signs present**\n\n" + lib.md_table(co))
lib.save_csv(co, RESULTS / f"non_completion_by_sign_count_{scope}.csv")

# ---- binned residuals ----------------------------------------------------------------------------------
res = (df.select("run", "activity_level").with_columns(pl.Series("y", y.astype(float)), pl.Series("p", model.p))
       .group_by("run", "activity_level").agg(pl.len().alias("enrolments"), pl.col("y").mean().alias("observed"), pl.col("p").mean().alias("predicted"))
       .with_columns((pl.col("observed") - pl.col("predicted")).alias("residual"),
                     (2 * (pl.col("predicted") * (1 - pl.col("predicted")) / pl.col("enrolments")).sqrt()).alias("two_se"))
       .with_columns((pl.col("residual").abs() > pl.col("two_se")).alias("outside_2se")).sort("run", "activity_level"))
print("\n**Binned residuals: observed minus predicted non-completion by run and activity level**\n\n" + lib.md_table(res))
print(f"\ncells outside two standard errors: {int(res['outside_2se'].sum())} of {res.height}; largest |residual| = {float(res['residual'].abs().max()):.3f}")
lib.save_csv(res, RESULTS / f"binned_residuals_{scope}.csv")

# ---- sensitivity ---------------------------------------------------------------------------------------
variants = {
    "main": (df, signs),
    "clicks de-duplicated (low-activity sign from de-duplicated clicks)": (df, [s if s != "sign_low_activity" else "sign_low_activity_dedup" for s in signs]),
    "late CMAs also count as late": (df, [s if s != "sign_tma_late" else "sign_any_task_late" for s in signs]),
    "without flagged enrolments": (df.filter(~pl.col("flagged")), signs),
    "only runs with a task due by day 27": (df.filter(pl.col("run_has_task_due")), signs),
    "low activity = below a quarter of the run median": (df, [s if s != "sign_low_activity" else "sign_low_activity_q25" for s in signs]),
    "low activity = below the run median": (df, [s if s != "sign_low_activity" else "sign_low_activity_median" for s in signs]),
}
sens = []
for name, (d, sg) in variants.items():
    m = AssociationModel(d, sg, interactions=True)
    t = m.table().with_columns(pl.lit(name).alias("variant"), pl.lit(d.height).alias("enrolments"))
    sens.append(t.select("variant", "enrolments", "sign", "adjusted_rd", "adj_ci_low", "adj_ci_high"))
sens = pl.concat(sens)
print("\n**Sensitivity of the adjusted risk differences**\n\n" + lib.md_table(sens))
lib.save_csv(sens, RESULTS / f"sensitivity_{scope}.csv")

# ---- subgroups (description) ---------------------------------------------------------------------------
df2 = df.with_columns(pl.when(pl.col("imd_band") == "Missing").then(pl.lit("Missing"))
                      .when(pl.col("imd_band").is_in(["0-10%", "10-20%", "20-30%"])).then(pl.lit("0-30% (most deprived)"))
                      .when(pl.col("imd_band").is_in(["30-40%", "40-50%", "50-60%", "60-70%"])).then(pl.lit("30-70%"))
                      .otherwise(pl.lit("70-100% (least deprived)")).alias("imd_group"))
sub = []
for col in ["gender", "disability", "imd_group"]:
    for g in sorted(df2[col].unique().to_list()):
        rows = (df2[col] == g).to_numpy()
        ug = unadjusted(df2.filter(pl.col(col) == g), signs)
        for s in signs:
            r = model.risk_difference(s, rows)
            u = ug.filter(pl.col("sign") == s).row(0, named=True)
            sub.append({"attribute": col, "group": g, "sign": s, "enrolments": r["n"], "with_sign": u["with_sign"],
                        "unadjusted_rd": u["unadjusted_rd"], "unadj_ci_low": u["unadj_ci_low"], "unadj_ci_high": u["unadj_ci_high"],
                        "adjusted_rd": r["rd"], "adj_ci_low": r["ci_low"], "adj_ci_high": r["ci_high"]})
sub = pl.DataFrame(sub)
print("\n**Risk differences by audit group (description; the groups are not model inputs)**\n\n" + lib.md_table(sub))
lib.save_csv(sub, RESULTS / f"subgroups_{scope}.csv")
