"""Design facts for the Milestone 4 modeling and evaluation proposal, read from the Milestone 3 prepared views.

No model is fitted. Outcome-based facts (events, base rates, attainable recall, events per parameter) use the 2013
training runs only; for the 2014 test runs only row and group counts are read, so the test outcomes stay unseen
until the single final evaluation.

Facts: rows and events per cut-off and split; candidate parameters of the primary and extended predictor sets and
events per parameter; Riley et al. minimum sample size for a binary outcome (criteria i–iii) under stated anticipated
values; training base rate per run; list sizes per run for 3 and 5 contacts per tutor group of 20; attainable recall
of those lists on training runs; leave-one-run-out folds; students in several training runs; paired and unpaired test
runs; audit-group sizes per split and training events per group.

Usage: venv/bin/python reports/milestone-4/code/design_facts.py
Writes reports/milestone-4/results/design_facts.json and design_facts.md.
"""
import json
import math
from pathlib import Path

import polars as pl

ROOT = Path(__file__).resolve().parents[3]
PKG = ROOT / "reports" / "milestone-3" / "package" / "data"
OUT = ROOT / "reports" / "milestone-4" / "results"
CUTS = {"d13": 13, "d27": 27}
GROUPS = {"disability": ["Y"], "imd_band": ["Missing", "0-10%"], "age_band": ["55<="], "gender": ["F", "M"]}


def riley(p, prevalence, r2_share=0.15, shrink=0.9, delta=0.05, margin=0.05):
    """Riley et al. (2020) minimum sample size for a binary outcome with p candidate parameters.

    Anticipated Cox-Snell R2 = r2_share x its maximum for this prevalence (conservative default).
    (i) expected uniform shrinkage >= shrink; (ii) optimism in Nagelkerke R2 <= delta; (iii) overall risk within
    +/- margin at 95% confidence.
    """
    phi = prevalence
    ln_null = phi * math.log(phi) + (1 - phi) * math.log(1 - phi)  # mean log-likelihood of the null model
    max_r2 = 1 - math.exp(2 * ln_null)
    r2 = r2_share * max_r2
    n1 = p / ((shrink - 1) * math.log(1 - r2 / shrink))
    s_vh = r2 / (r2 + delta * max_r2)
    n2 = p / ((s_vh - 1) * math.log(1 - r2 / s_vh))
    n3 = (1.96 / margin) ** 2 * phi * (1 - phi)
    n = math.ceil(max(n1, n2, n3))
    return {"p": p, "prevalence": round(phi, 4), "max_r2_cs": round(max_r2, 4), "anticipated_r2_cs": round(r2, 4),
            "n_shrinkage": math.ceil(n1), "n_optimism": math.ceil(n2), "n_intercept": math.ceil(n3),
            "n_required": n, "events_required": math.ceil(n * phi), "epp_required": round(n * phi / p, 1)}


def n_params(cols, sets, cut):
    """Columns of the model-ready matrix that a predictor list expands to (one-hot dummies counted once each,
    minus one reference level per nominal variable), plus missing indicators present."""
    base = [c for c in sets if c != "cma_score_mean_c"]
    count = 0
    for v in base:
        dummies = [c for c in cols if c.startswith(v + "=")]
        count += (len(dummies) - 1) if dummies else 1
        count += sum(c == v + "_missing" for c in cols)
    return count


def main():
    sets = json.loads((PKG / "metadata" / "predictor_sets.json").read_text())
    cap = pl.read_parquet(PKG / "processed" / "capacity_by_run.parquet")
    courses = pl.read_csv(PKG / "raw" / "courses.csv")
    lengths = {p: sorted(courses.filter(pl.col("code_presentation") == p)["module_presentation_length"].to_list())
               for p in ("2013B", "2013J", "2014B", "2014J")}
    facts = {"source": "Milestone 3 prepared views, OULAD-N04-prepared-1.0", "run_length_days": lengths, "cutoffs": {}}
    for key, day in CUTS.items():
        f = pl.read_parquet(PKG / "processed" / f"features_{key}.parquet")
        mr_cols = pl.read_parquet(PKG / "processed" / f"model_ready_{key}.parquet").columns
        tr, te = f.filter(pl.col("split") == "train"), f.filter(pl.col("split") == "test")
        ev = int(tr["non_completion"].sum())
        prev = ev / tr.height
        p_primary = n_params(mr_cols, sets["primary"], key)
        p_full = p_primary + n_params(mr_cols, sets["extended"], key) + len(sets["weekly_clicks"][key])
        runs_tr = (tr.group_by(["code_module", "code_presentation"])
                   .agg(pl.len().alias("n"), pl.col("non_completion").sum().alias("events"))
                   .join(cap.filter(pl.col("cutoff_day") == day), on=["code_module", "code_presentation"])
                   .with_columns((pl.col("events") / pl.col("n")).alias("base_rate"),
                                 (pl.min_horizontal("list_tutor_3", "events") / pl.col("events")).alias("max_recall_3"),
                                 (pl.min_horizontal("list_tutor_5", "events") / pl.col("events")).alias("max_recall_5"),
                                 (pl.col("list_tutor_3") / pl.col("n")).alias("list_share_3"),
                                 (pl.col("list_tutor_5") / pl.col("n")).alias("list_share_5"))
                   .sort(["code_module", "code_presentation"]))
        runs_te = (te.group_by(["code_module", "code_presentation", "paired_run"]).agg(pl.len().alias("n"))
                   .join(cap.filter(pl.col("cutoff_day") == day), on=["code_module", "code_presentation"])
                   .sort(["code_module", "code_presentation"]))
        multi = (tr.group_by("id_student").agg(pl.col("code_presentation").n_unique().alias("k"),
                                               pl.len().alias("rows"))
                 .filter(pl.col("rows") > 1))
        groups = {}
        for g, levels in GROUPS.items():
            for lv in levels:
                gtr = tr.filter(pl.col(g) == lv)
                gte = te.filter(pl.col(g) == lv)
                groups[f"{g}={lv}"] = {"train_rows": gtr.height, "train_events": int(gtr["non_completion"].sum()),
                                       "test_rows": gte.height,
                                       "test_rows_min_per_run": int(gte.group_by(["code_module", "code_presentation"])
                                                                    .len()["len"].min() or 0)}
        facts["cutoffs"][key] = {
            "day": day,
            "train_rows": tr.height, "train_events": ev, "train_nonevents": tr.height - ev,
            "train_prevalence": round(prev, 4),
            "test_rows": te.height,
            "test_rows_paired": int(te["paired_run"].sum()), "test_rows_unpaired": int((~te["paired_run"]).sum()),
            "test_rows_student_in_training": int(te["student_in_training_runs"].sum()),
            "test_rows_withdrawal_day_unknown": int(te["eval_withdrawal_day_unknown"].sum()),
            "train_runs": runs_tr.height, "test_runs": runs_te.height,
            "test_runs_paired": int(runs_te["paired_run"].sum()),
            "params_primary": p_primary, "params_full": p_full,
            "epp_primary": round(min(ev, tr.height - ev) / p_primary, 1),
            "epp_full": round(min(ev, tr.height - ev) / p_full, 1),
            "riley_primary": riley(p_primary, prev), "riley_full": riley(p_full, prev),
            "train_base_rate_min": round(runs_tr["base_rate"].min(), 4),
            "train_base_rate_max": round(runs_tr["base_rate"].max(), 4),
            "train_run_rows_min": int(runs_tr["n"].min()), "train_run_rows_max": int(runs_tr["n"].max()),
            "train_run_events_min": int(runs_tr["events"].min()),
            "max_recall_3_min": round(runs_tr["max_recall_3"].min(), 4),
            "max_recall_3_max": round(runs_tr["max_recall_3"].max(), 4),
            "max_recall_5_min": round(runs_tr["max_recall_5"].min(), 4),
            "max_recall_5_max": round(runs_tr["max_recall_5"].max(), 4),
            "train_attainable_tp_k3": int(runs_tr.select(pl.min_horizontal("list_tutor_3", "events")).sum().item()),
            "train_attainable_tp_k5": int(runs_tr.select(pl.min_horizontal("list_tutor_5", "events")).sum().item()),
            "train_students_in_several_runs": multi.height,
            "train_rows_of_those_students": int(multi["rows"].sum()),
            "test_list3_total": int(runs_te["list_tutor_3"].sum()), "test_list5_total": int(runs_te["list_tutor_5"].sum()),
            "test_run_rows_min": int(runs_te["n"].min()), "test_run_rows_max": int(runs_te["n"].max()),
            "groups": groups,
            "train_runs_detail": runs_tr.select("code_module", "code_presentation", "n", "events", "base_rate",
                                                "list_tutor_3", "list_tutor_5", "max_recall_3", "max_recall_5")
                                         .with_columns(pl.col("base_rate", "max_recall_3", "max_recall_5").round(4))
                                         .to_dicts(),
            "test_runs_detail": runs_te.select("code_module", "code_presentation", "paired_run", "n",
                                               "list_tutor_3", "list_tutor_5").to_dicts(),
        }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "design_facts.json").write_text(json.dumps(facts, indent=1))
    lines = ["# Design facts (Milestone 3 prepared views; outcomes from 2013 training runs only)", "",
             "Run lengths in days by presentation: " + "; ".join(f"{p}: {v}" for p, v in lengths.items()), ""]
    for key, c in facts["cutoffs"].items():
        lines += [f"## Cut-off day {c['day']}", "",
                  "| Fact | Value |", "| :---- | :---- |"]
        for k, v in c.items():
            if k in ("groups", "train_runs_detail", "test_runs_detail", "riley_primary", "riley_full"):
                continue
            lines.append(f"| {k} | {v} |")
        for k in ("riley_primary", "riley_full"):
            lines.append(f"| {k} | " + ", ".join(f"{a}={b}" for a, b in c[k].items()) + " |")
        lines += ["", "| Audit group | Train rows | Train events | Test rows | Test rows, smallest run |",
                  "| :---- | :---- | :---- | :---- | :---- |"]
        lines += [f"| {g} | {v['train_rows']} | {v['train_events']} | {v['test_rows']} | {v['test_rows_min_per_run']} |"
                  for g, v in c["groups"].items()]
        lines += ["", "| Training run | Rows | Events | Base rate | List 3/20 | List 5/20 | Max recall 3 | Max recall 5 |",
                  "| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |"]
        lines += [f"| {r['code_module']}-{r['code_presentation']} | {r['n']} | {r['events']} | {r['base_rate']} | "
                  f"{r['list_tutor_3']} | {r['list_tutor_5']} | {r['max_recall_3']} | {r['max_recall_5']} |"
                  for r in c["train_runs_detail"]]
        lines.append("")
    (OUT / "design_facts.md").write_text("\n".join(lines))
    for key, c in facts["cutoffs"].items():
        print(f"{key}: train {c['train_rows']} rows, {c['train_events']} events ({c['train_prevalence']}); "
              f"test {c['test_rows']} rows ({c['test_runs']} runs, {c['test_runs_paired']} paired); "
              f"params primary {c['params_primary']} (EPP {c['epp_primary']}), full {c['params_full']} "
              f"(EPP {c['epp_full']}); Riley n primary {c['riley_primary']['n_required']}, full "
              f"{c['riley_full']['n_required']}; base rate {c['train_base_rate_min']}-{c['train_base_rate_max']}; "
              f"max recall@3 {c['max_recall_3_min']}-{c['max_recall_3_max']}, @5 {c['max_recall_5_min']}-"
              f"{c['max_recall_5_max']}")


if __name__ == "__main__":
    main()
