"""Task 8 – validate the prepared views against the raw data and package them (brief section 13).

Runs checks V01–V15 named in the Preparation Decision Matrix. The activity and task features of every row of both
feature views are recomputed here from the raw CSV files by a separate code path (not the pipeline's functions), so a
formula or cut-off error in the pipeline shows as a mismatch. Then writes the data dictionary, the lineage table, the
version manifest and the validation summary; the rule firing rates, CMA-score coverage and the KPI with and without
the flagged enrolments are reported as the AI preparation critic asked (no test-run outcome is used for any choice).

Usage (from the package folder): python src/validate_prepared.py   (after prepare_data.py, fit_transforms.py)
Writes data/metadata/validation_summary.{md,json}, rule_rates.csv, data_dictionary.md, lineage.md,
version_manifest.json. Exit 1 if a check fails.
"""
from __future__ import annotations

import json
import platform
import subprocess
import sys

import polars as pl

from common import (AGE, CUTOFFS, EDU, ENROLMENT, IMD, META, OUTCOMES, PKG, PROCESSED, RAW, RUN, load, md_table,
                    now_utc, sha256, write_json)
from dictionary import C, FEATURE_VIEW_FORBIDDEN, VIEWS
from fit_transforms import fit
from prepare_data import EXTENDED, PREDICTORS

RESULTS: list[dict] = []


def check(cid, name, expected, observed, ok):
    RESULTS.append({"ID": cid, "Check": name, "Expected": str(expected), "Observed": str(observed),
                    "Status": "PASS" if ok else "FAIL"})
    print(f"{cid} {'PASS' if ok else 'FAIL'} {name}: expected {expected}; observed {observed}")


def main():
    v = {n: pl.read_parquet(PROCESSED / f"{n}.parquet") for n in VIEWS}
    prof = json.loads((META / "profile.json").read_text())
    info, reg, crs = load("studentInfo"), load("studentRegistration"), load("courses")
    sa, asm, sv = load("studentAssessment"), load("assessments"), load("studentVle")
    e = v["enrolment"]

    # V01 rows, entities and outcome distribution before and after
    before = info.group_by("final_result").len().sort("final_result").rows()
    after = e.group_by("final_result").len().sort("final_result").rows()
    check("V01a", "enrolment rows and outcome mix equal raw studentInfo", f"{info.height:,}; {before}",
          f"{e.height:,}; {after}", e.height == info.height and before == after)
    check("V01b", "students", f"{info['id_student'].n_unique():,}", f"{e['id_student'].n_unique():,}",
          info["id_student"].n_unique() == e["id_student"].n_unique())
    pops = {"d14": int(e["enrolled_d14"].sum()), **{k: v[f"features_{k}"].height for k in CUTOFFS}}
    exp = {"d14": prof["outcome"]["kpi_population_day14"],
           **{k: prof["outcome"]["population_at_cutoff"][k]["enrolments"] for k in CUTOFFS}}
    check("V01c", "population sizes equal the profile (C09)", exp, pops, exp == pops)
    nc = {k: int(v[f"features_{k}"]["non_completion"].sum()) for k in CUTOFFS}
    nce = {k: prof["outcome"]["population_at_cutoff"][k]["non_completion"] for k in CUTOFFS}
    check("V01d", "non-completion count per feature view equals the profile", nce, nc, nc == nce)

    # V02 missing values kept, not imputed
    m = {"imd_band Missing": int((e["imd_band"] == "Missing").sum()), "date_registration": e["date_registration"].null_count(),
         "TMA/CMA score null (submitted)": v["assessment_due"].filter(pl.col("date_submitted").is_not_null())["score"].null_count()}
    raw_m = {"imd_band Missing": info["imd_band"].null_count(), "date_registration": reg["date_registration"].null_count(),
             "TMA/CMA score null (submitted)": sa.join(asm.filter(pl.col("assessment_type") != "Exam"),
                                                       on="id_assessment")["score"].null_count()}
    check("V02", "missing values after = before (no imputation in views)", raw_m, m, raw_m == m)

    # V03 key uniqueness
    keys = {"enrolment": ENROLMENT, "assessment_due": [*ENROLMENT, "id_assessment"], "student_week": [*ENROLMENT, "week"],
            "features_d13": ENROLMENT, "features_d27": ENROLMENT, "capacity_by_run": [*RUN, "cutoff_day"]}
    dup = {n: v[n].height - v[n].unique(subset=k).height for n, k in keys.items()}
    check("V03", "key unique in every view", "0 duplicates", dup, all(x == 0 for x in dup.values()))

    # V04 click totals reconcile with the raw log
    truncated = prof["validity"]["clicks_after_unregistration"]
    tot = int(e["total_clicks"].sum())
    check("V04a", "enrolment clicks + clicks after withdrawal = raw clicks", f"{int(sv['sum_click'].sum()):,}",
          f"{tot:,} + {truncated:,} = {tot + truncated:,}", tot + truncated == int(sv["sum_click"].sum()))
    check("V04b", "student_week clicks = enrolment clicks", f"{tot:,}", f"{int(v['student_week']['clicks'].sum()):,}",
          tot == int(v["student_week"]["clicks"].sum()))
    check("V04c", "de-duplicated total ≤ raw total", "dedup ≤ raw",
          f"{int(e['total_clicks_dedup'].sum()):,} ≤ {tot:,}", int(e["total_clicks_dedup"].sum()) <= tot)

    # V05 categories in expected sets
    cats = {"imd_band": set(IMD) | {"Missing"}, "age_band": set(AGE), "highest_education": set(EDU),
            "final_result": set(OUTCOMES), "start_month": {"B", "J"}, "split": {"train", "test"}}
    bad = {c: sorted(set(e[c].unique().to_list()) - s) for c, s in cats.items()}
    check("V05", "every category in its expected set", "no other label", bad, not any(bad.values()))

    # V06 banked results never timed
    ad = v["assessment_due"]
    banked_timed = ad.filter((pl.col("status") == "banked") & pl.col("lateness_days").is_not_null()).height
    check("V06", "banked results carry no lateness and no missed status", "0", banked_timed, banked_timed == 0)

    # V07 ranges unchanged
    rng = {"score": [float(ad["score"].min()), float(ad["score"].max())],
           "studied_credits": [int(e["studied_credits"].min()), int(e["studied_credits"].max())]}
    check("V07", "ranges after = before (no capping)", "score [0, 100]; credits [30, 655]", rng,
          rng == {"score": [0.0, 100.0], "studied_credits": [30, 655]})

    # V08 nothing counted after withdrawal
    sw = v["student_week"].join(e.select([*ENROLMENT, "date_unregistration"]), on=ENROLMENT)
    late_weeks = sw.filter(pl.col("date_unregistration").is_not_null()
                           & (pl.col("week") > pl.col("date_unregistration") // 7 + 1)).height
    check("V08", "no student_week row after the withdrawal week", "0", late_weeks, late_weeks == 0)

    # V09 joins kept rows
    tl = json.loads((META / "transformation_log.json").read_text())["steps"]
    joins = [s for s in tl if s["note"].startswith("left join")]
    check("V09", "every logged join kept its rows", f"{len(joins)} joins, rows in = rows out",
          sum(s["rows_in"] == s["rows_out"] for s in joins), all(s["rows_in"] == s["rows_out"] for s in joins))

    # V10 enrolments without activity kept with zero
    no_act = info.join(sv.select(ENROLMENT).unique(), on=ENROLMENT, how="anti").height
    zero = int((e["total_clicks"] == 0).sum())
    check("V10", "enrolments without any click row kept with 0 clicks", f"≥ {no_act:,}", f"{zero:,}", zero >= no_act)

    # V11 + V13 independent recomputation of every feature row from the raw files
    regd = reg.select([*ENROLMENT, "date_registration", "date_unregistration"])
    for name, c in CUTOFFS.items():
        f = v[f"features_{name}"]
        pop = info.join(regd, on=ENROLMENT).filter(
            (pl.col("date_registration").is_null() | (pl.col("date_registration") <= c))
            & (pl.col("date_unregistration").is_null() | (pl.col("date_unregistration") > c))).select(
            [*ENROLMENT, "date_registration"])
        s_all = sv.join(pop.select(ENROLMENT), on=ENROLMENT)
        s = s_all.filter(pl.col("date") <= c)
        indep = pop.select(ENROLMENT).join(s.group_by(ENROLMENT).agg(
            pl.col("sum_click").filter(pl.col("date") >= 0).sum().alias("clicks_0c"),
            pl.col("sum_click").filter(pl.col("date") < 0).sum().alias("clicks_pre"),
            pl.col("date").filter(pl.col("date") >= 0).n_unique().alias("active_days_0c"),
            pl.col("id_site").filter(pl.col("date") >= 0).n_unique().alias("sites_0c")), on=ENROLMENT, how="left")
        t = asm.filter((pl.col("assessment_type") != "Exam") & (pl.col("date") <= c)).select([*RUN, "id_assessment", "assessment_type", "date"])
        t_reg = pop.join(t, on=RUN).filter(pl.col("date_registration").is_null()
                                           | (pl.col("date") >= pl.col("date_registration")))
        g = t_reg.join(sa.filter(pl.col("is_banked") == 0).select(["id_assessment", "id_student", "date_submitted"]),
                                     on=["id_assessment", "id_student"], how="left")
        tk = g.group_by(ENROLMENT).agg(
            (pl.col("date_submitted").is_null() | (pl.col("date_submitted") > c)).sum().alias("tasks_missed_c"),
            ((pl.col("date_submitted") > pl.col("date")) & (pl.col("date_submitted") <= c)).sum().alias("tasks_late_c"))
        indep = indep.join(tk, on=ENROLMENT, how="left").fill_null(0)
        # banked tasks due by c are neither missed nor late in the pipeline: remove them from the recount
        bk = t_reg.join(sa.filter(pl.col("is_banked") == 1).select(["id_assessment", "id_student"]),
                                      on=["id_assessment", "id_student"]).group_by(ENROLMENT).len("banked_due")
        indep = indep.join(bk, on=ENROLMENT, how="left").with_columns(
            (pl.col("tasks_missed_c") - pl.col("banked_due").fill_null(0)).alias("tasks_missed_c")).drop("banked_due")
        cols = ["clicks_0c", "clicks_pre", "active_days_0c", "sites_0c", "tasks_missed_c", "tasks_late_c"]
        cmp = f.select([*ENROLMENT, *cols]).join(indep.select([*ENROLMENT, *cols]), on=ENROLMENT, suffix="_raw")
        mism = {x: int((cmp[x].cast(pl.Int64) != cmp[f"{x}_raw"].cast(pl.Int64)).sum()) for x in cols}
        check(f"V11-{name}", f"{len(cols)} features recomputed from raw for all {f.height:,} rows (independent code)",
              "0 mismatches", mism, cmp.height == f.height and not any(mism.values()))
        trn = cmp.join(f.filter(pl.col("split") == "train").select(ENROLMENT), on=ENROLMENT)
        picks = [trn.filter(pl.col("tasks_missed_c") > 0), trn.filter(pl.col("tasks_late_c") > 0), trn]
        sample = pl.concat([d.sort(ENROLMENT).sample(min(k, d.height), seed=7) for d, k in zip(picks, (2, 2, 1))])
        (META / f"manual_check_{name}.csv").write_text(sample.write_csv())
        # V13: recount clicks with no cut-off at all; the pipeline must equal the cut-off recount on every row and
        # differ from the unfiltered recount exactly where the student has clicks after the cut-off
        later = pop.select(ENROLMENT).join(s_all.filter(pl.col("date") > c).group_by(ENROLMENT).agg(
            pl.col("sum_click").sum().alias("later")), on=ENROLMENT, how="left").fill_null(0)
        unf = pop.select(ENROLMENT).join(s_all.filter(pl.col("date") >= 0).group_by(ENROLMENT).agg(
            pl.col("sum_click").sum().alias("unfiltered")), on=ENROLMENT, how="left").fill_null(0)
        z = f.select([*ENROLMENT, "clicks_0c"]).join(later, on=ENROLMENT).join(unf, on=ENROLMENT)
        rows_later = int((z["later"] > 0).sum())
        differs = int((z["clicks_0c"] != z["unfiltered"]).sum())
        forbidden = [x for x in f.columns if C.get(x, ("?",))[0] in FEATURE_VIEW_FORBIDDEN]
        check(f"V13-{name}", "pipeline clicks differ from an unfiltered recount exactly for students with later clicks; "
              "no target-derived or whole-run column in the view",
              f"{rows_later:,} rows with later clicks; no forbidden column", f"{differs:,} rows differ; forbidden {forbidden}",
              differs == rows_later and rows_later > 0 and not forbidden)

    # V12 fitted transforms from training rows only (refit with test rows altered)
    tp = json.loads((META / "transform_params.json").read_text())
    same = []
    for name, c in CUTOFFS.items():
        f = v[f"features_{name}"]
        cols = [x for x in [*PREDICTORS, *EXTENDED] if x in f.columns] + sorted(x for x in f.columns if x.startswith("clicks_w"))
        p1 = fit(f, cols, c)
        p2 = fit(f.filter(pl.col("split") == "train"), cols, c)
        stored = {k: tp["cutoffs"][name][k] for k in p1}
        same.append(p1 == p2 and json.loads(json.dumps(p1)) == stored)
    check("V12", "transform parameters identical with and without test rows, equal to the stored ones", "identical",
          ", ".join(f"{n}: {'identical' if ok else 'DIFFERENT'}" for n, ok in zip(CUTOFFS, same)), all(same))

    # V14 roles
    undocumented = sorted({c for df in v.values() for c in df.columns} - set(C))
    # code_module is both a run key (role id) and a primary predictor
    roles_bad = ([x for x in PREDICTORS if C[x][0] != "predictor" and x != "code_module"]
                 + [x for x in EXTENDED if C[x][0] != "predictor_extended"])
    check("V14", "every column documented; predictor lists hold no audit, target or descriptive column", "none",
          {"undocumented": undocumented, "wrong role": roles_bad}, not undocumented and not roles_bad)

    # V15 split
    runs = e.group_by(RUN).agg(pl.col("split").n_unique().alias("n"), pl.col("split").first(), pl.col("year").first())
    tr_students = set(info.filter(pl.col("code_presentation").str.starts_with("2013"))["id_student"].to_list())
    test = e.filter(pl.col("split") == "test")
    flag_ok = test.with_columns(pl.col("id_student").is_in(list(tr_students)).alias("x")).filter(
        pl.col("x") != pl.col("student_in_training_runs")).height
    split_ok = runs.filter(pl.col("n") > 1).height == 0 and runs.filter((pl.col("year") == 2013) != (pl.col("split") == "train")).height == 0
    counts = {"train runs": runs.filter(pl.col("split") == "train").height, "test runs": runs.filter(pl.col("split") == "test").height,
              "test enrolments of students seen in 2013": int(test["student_in_training_runs"].sum())}
    check("V15", "no run in both partitions; 2013 = train; student flag recomputed", "9 train, 13 test runs; 0 flag mismatches",
          {**counts, "flag mismatches": flag_ok}, split_ok and flag_ok == 0 and counts["train runs"] == 9)

    # Reports asked for by the AI preparation critic (no test outcome used)
    rates = []
    for name, c in CUTOFFS.items():
        f = v[f"features_{name}"]
        rates.append(f.group_by([*RUN, "split"]).agg(pl.len().alias("enrolled"),
            *[pl.col(x).mean().round(4).alias(x) for x in ["early_sign_rule", "early_sign_rule_cma", "rule_missed",
                                                           "rule_tma_late", "inactive_last7"]],
            (pl.col("cma_marked_c") > 0).mean().round(4).alias("cma_score_coverage")).with_columns(pl.lit(c).alias("cutoff_day")))
    rr = pl.concat(rates).sort(["cutoff_day", *RUN])
    rr.write_csv(META / "rule_rates.csv")
    cov = {name: round(float((v[f"features_{name}"].filter(pl.col("split") == "train")["cma_marked_c"] > 0).mean()), 4) for name in CUTOFFS}
    k = e.filter(pl.col("enrolled_d14"))
    kk = k.filter(~pl.col("withdrawal_day_missing") & ~pl.col("registration_missing"))
    kpi = {"completion_day14": round(float(k["completed"].mean()), 4), "enrolled_day14": k.height,
           "completion_without_138_flagged": round(float(kk["completed"].mean()), 4), "enrolled_without_flagged": kk.height}
    extra = {"cma_score_coverage_training_rows": cov, "kpi_sensitivity": kpi,
             "rule_rate_overall": {name: round(float(v[f"features_{name}"]["early_sign_rule"].mean()), 4) for name in CUTOFFS},
             "rule_rate_cma_variant": {name: round(float(v[f"features_{name}"]["early_sign_rule_cma"].mean()), 4) for name in CUTOFFS},
             "runs_where_rule_exceeds_list_of_5_per_20": {c: int((rr.filter(pl.col("cutoff_day") == c)["early_sign_rule"] > 0.25).sum())
                                                           for c in CUTOFFS.values()},
             "runs_where_rule_exceeds_list_of_3_per_20": {c: int((rr.filter(pl.col("cutoff_day") == c)["early_sign_rule"] > 0.15).sum())
                                                           for c in CUTOFFS.values()},
             "rule_rate_by_run_range": {c: [float(rr.filter(pl.col("cutoff_day") == c)["early_sign_rule"].min()),
                                            float(rr.filter(pl.col("cutoff_day") == c)["early_sign_rule"].max())] for c in CUTOFFS.values()}}
    print("extra:", extra)

    # Data dictionary, lineage, version manifest
    dd = ["# Prepared data dictionary", f"Written by `src/validate_prepared.py` at {now_utc()} from the prepared files and "
          "`src/dictionary.py`. Roles: id, split, target, target_derived, predictor, predictor_extended, rule, audit, "
          "descriptive. Day fields are offsets from the start of the module run (day 0); week n = days 7(n−1) to 7n−1.", ""]
    for n, desc in VIEWS.items():
        df = v[n]
        dd += [f"## {n}.parquet", f"{desc}. Rows: {df.height:,}; columns: {df.width}.", "",
               md_table([{"Column": c, "Type": str(t), "Role": C[c][0], "Source": C[c][1], "Transformation": C[c][2],
                          "Sensitivity": C[c][5]} for c, t in df.schema.items()]), ""]
    dd += ["## model_ready_d13.parquet, model_ready_d27.parquet",
           "Linear-model matrices from `src/fit_transforms.py`: the identifier, split, target, rule and audit columns of the "
           "feature view unchanged, then every predictor and extended predictor encoded with training-run parameters "
           "(`transform_params.json`): `code_module=…`, `start_month=…` one-hot; highest_education ordinal 0–4; counts "
           "log1p; `<column>_missing` indicators where a training median fills a gap; all standardised with training "
           "mean and standard deviation.", ""]
    (META / "data_dictionary.md").write_text("\n".join(dd))
    lin = [r for r in ({"Prepared variable": c, "Source file / field": s[1], "Transformation": s[2], "Window / filter": s[3],
                        "Purpose / AQ": s[4], "Sensitivity": s[5]} for c, s in C.items())
           if C[r["Prepared variable"]][0] not in ("id",)]
    (META / "lineage.md").write_text("# Data lineage (brief section 13.1)\n\nOne row per prepared variable, from "
                                     "`src/dictionary.py`; the formulas are implemented in `src/prepare_data.py`.\n\n"
                                     + md_table(lin) + "\n")
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=PKG, capture_output=True, text=True).stdout.strip()
        dirty = bool(subprocess.run(["git", "status", "--porcelain", "--", "."], cwd=PKG, capture_output=True, text=True).stdout.strip())
    except OSError:
        commit, dirty = "unknown", True
    manifest = {"prepared_dataset_version": "OULAD-N04-prepared-1.0", "created": now_utc(),
                "raw_input": {f.name: sha256(f) for f in sorted(RAW.glob("*.csv"))},
                "raw_source": "OULAD, figshare DOI 10.6084/m9.figshare.5081998.v1 (Milestone 2 package, SHA-256 pinned)",
                "code": {f.name: sha256(f) for f in sorted((PKG / "src").glob("*.py"))},
                "git_commit": commit, "package_has_uncommitted_changes": dirty,
                "python": platform.python_version(), "polars": pl.__version__,
                "outputs": {f.name: {"sha256": sha256(f), "rows": pl.read_parquet(f).height}
                            for f in sorted(PROCESSED.glob("*.parquet"))}}
    write_json(META / "version_manifest.json", manifest)

    ok = all(r["Status"] == "PASS" for r in RESULTS)
    write_json(META / "validation_summary.json", {"generated": now_utc(), "checks": RESULTS, "extra": extra, "all_pass": ok})
    (META / "validation_summary.md").write_text(
        "# Validation summary (Task 8)\n\nWritten by `src/validate_prepared.py` at " + now_utc() +
        ". Each check names its expected and observed value.\n\n" + md_table(RESULTS) +
        "\n\n## Reports for the analysis plan\n\n" + "\n".join(f"- {k}: {json.dumps(x, ensure_ascii=False)}" for k, x in extra.items()) +
        "\n\nRule firing rates per run and cut-off (no outcome used): `rule_rates.csv`. Five training-run rows per cut-off (two with a missed task, two with a late task where the cut-off has one, one at "
        "random) recomputed from raw rows: `manual_check_d13.csv`, `manual_check_d27.csv`.\n")
    print(f"{sum(r['Status'] == 'PASS' for r in RESULTS)} of {len(RESULTS)} checks PASS")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
