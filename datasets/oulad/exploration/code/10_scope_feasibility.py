"""Stage 10: scope feasibility for the Milestone 1 proposal (reports/milestone-1), descriptive only.

The proposal plans a short review list made early in each module presentation. This stage measures, for the candidate
prediction points (days 14, 28 and 60, and each presentation's first assessment due day), how many enrolments are
still registered, what their outcomes are, how much withdrawal is still ahead, which assessments are already due, how
long capacity-limited lists would be, and how large the groups are that a fairness check compares. It also writes the
overall outcome shares and the withdrawn-by-day shares as values of their own, so the proposal can cite them.

No comparator rule, model or list is evaluated here: those belong to Milestone 3 and its held-out presentations.

Definitions (dates are day offsets from the presentation start; aligned with stage 03's survival population):
- registered at day d: date_registration <= d (missing: counted as registered from the start) and
  date_unregistration missing or > d, so an enrolment that leaves on day d is not available on day d;
- non-completion after d: final_result Fail or Withdrawn among those registered at day d;
- day-0 cohort: date_unregistration missing or > 0, without the Withdrawn enrolments that have no unregistration day
  (timing unknown), as in stage 03; withdrawn by day d: Withdrawn with date_unregistration <= d, so the shares equal
  stage 03's Kaplan-Meier values (no censoring happens before the presentation ends);
- first assessment due day: earliest due day of a TMA or CMA in the presentation (exams excluded).

Output: results/scope_feasibility.json.
"""

from __future__ import annotations

import math

import polars as pl

from common import ENROLMENT, IMD, PRESENTATION, load_all, write_json

DAYS = [14, 28, 60]
CAPACITY = [0.10, 0.15, 0.20]  # review-list capacity scenarios (Program Manager's estimate, an assumption)


def enrolments(t: dict[str, pl.DataFrame]) -> pl.DataFrame:
    first_due = (t["assessments"].filter(pl.col("assessment_type") != "Exam")
                 .group_by(PRESENTATION).agg(pl.col("date").min().alias("first_due")))
    return (t["studentInfo"].join(t["studentRegistration"], on=ENROLMENT, how="left")
            .join(first_due, on=PRESENTATION, how="left")
            .with_columns(pl.concat_str(PRESENTATION, separator="-").alias("presentation")))


def registered_at(day) -> pl.Expr:
    """Still registered at `day` (a number or an expression such as pl.col('first_due'))."""
    day = day if isinstance(day, pl.Expr) else pl.lit(day)
    return ((pl.col("date_registration").is_null() | (pl.col("date_registration") <= day))
            & (pl.col("date_unregistration").is_null() | (pl.col("date_unregistration") > day)))


def outcome_counts(df: pl.DataFrame) -> dict:
    n = df.height
    counts = {r: df.filter(pl.col("final_result") == r).height for r in ["Withdrawn", "Fail", "Pass", "Distinction"]}
    non = counts["Withdrawn"] + counts["Fail"]
    return {"n": n, **counts, "non_completion": non, "non_completion_rate": round(non / n, 4) if n else None,
            "success_rate": round((counts["Pass"] + counts["Distinction"]) / n, 4) if n else None}


def overall(e: pl.DataFrame) -> dict:
    n = e.height
    out = {r: {"n": e.filter(pl.col("final_result") == r).height} for r in ["Withdrawn", "Fail", "Pass", "Distinction"]}
    for r in out:
        out[r]["share"] = round(out[r]["n"] / n, 4)
    success = out["Pass"]["n"] + out["Distinction"]["n"]
    no_date = (pl.col("final_result") == "Withdrawn") & pl.col("date_unregistration").is_null()
    day0 = e.filter(~no_date & (pl.col("date_unregistration").is_null() | (pl.col("date_unregistration") > 0)))
    wd = day0.filter(pl.col("final_result") == "Withdrawn")
    withdrawn_by = {}
    for d in DAYS:
        k = wd.filter(pl.col("date_unregistration") <= d).height
        withdrawn_by[f"day_{d}"] = {"n": k, "share": round(k / day0.height, 4)}
    total = wd.height
    after = {f"day_{d}": round(wd.filter(pl.col("date_unregistration") > d).height / total, 4) for d in DAYS}
    return {
        "enrolments": n,
        "outcomes": out,
        "success": {"n": success, "share": round(success / n, 4)},
        "registered_day0": day0.height,
        "left_on_or_before_day0": e.filter(pl.col("date_unregistration") <= 0).height,
        "withdrawn_from_day0_cohort": {"n": total, "share": round(total / day0.height, 4)},
        "withdrawn_by_day": withdrawn_by,
        "share_of_day0_withdrawals_after_day": after,
        "anomalies": {
            "withdrawn_without_unregistration_day": e.filter((pl.col("final_result") == "Withdrawn")
                                                             & pl.col("date_unregistration").is_null()).height,
            "not_withdrawn_with_unregistration_day": e.filter((pl.col("final_result") != "Withdrawn")
                                                              & pl.col("date_unregistration").is_not_null()).height,
            "registration_day_missing": e.filter(pl.col("date_registration").is_null()).height,
        },
    }


def per_presentation(e: pl.DataFrame, t: dict[str, pl.DataFrame]) -> list[dict]:
    ass = t["assessments"].filter(pl.col("assessment_type") != "Exam")
    clicks = t["studentVle"]
    rows = []
    for (mod, pres), g in e.group_by(PRESENTATION, maintain_order=True):
        first_due = int(g["first_due"][0])
        row = {"presentation": f"{mod}-{pres}", "code_module": mod, "code_presentation": pres,
               "enrolments": g.height, "first_due_day": first_due,
               "first_assessment_before_day_28": first_due < 28}
        a = ass.filter((pl.col("code_module") == mod) & (pl.col("code_presentation") == pres))
        points = {f"day_{d}": d for d in DAYS} | {"at_first_due": first_due}
        for name, d in points.items():
            cohort = g.filter(registered_at(d))
            oc = outcome_counts(cohort)
            ids = cohort.select("id_student")
            active = (clicks.filter((pl.col("code_module") == mod) & (pl.col("code_presentation") == pres)
                                    & (pl.col("date") < d))
                      .select("id_student").unique().join(ids, on="id_student", how="inner").height)
            row[name] = {
                "day": d,
                **oc,
                "assessments_due_before": a.filter(pl.col("date") < d).height,
                "share_with_any_click_before": round(active / cohort.height, 4) if cohort.height else None,
                "list_size": {f"{int(c * 100)}%": math.ceil(c * cohort.height) for c in CAPACITY},
            }
        rows.append(row)
    return sorted(rows, key=lambda r: (r["code_module"], r["code_presentation"]))


def summary(rows: list[dict]) -> dict:
    out = {"presentations": len(rows),
           "first_due_day": {"min": min(r["first_due_day"] for r in rows), "max": max(r["first_due_day"] for r in rows),
                             "median": sorted(r["first_due_day"] for r in rows)[len(rows) // 2],
                         "presentations_due_before_day_28": sum(r["first_assessment_before_day_28"] for r in rows)}}
    for name in ["day_14", "day_28", "day_60", "at_first_due"]:
        n = [r[name]["n"] for r in rows]
        rate = [r[name]["non_completion_rate"] for r in rows]
        lists = [r[name]["list_size"]["15%"] for r in rows]
        success = sum(r[name]["Pass"] + r[name]["Distinction"] for r in rows)
        non = sum(r[name]["non_completion"] for r in rows)
        out[name] = {"cohort_min": min(n), "cohort_max": max(n), "cohort_total": sum(n),
                     "success_rate_pooled": round(success / sum(n), 4),
                     "non_completion_rate_pooled": round(non / sum(n), 4),
                     "non_completion_rate_min": min(rate), "non_completion_rate_max": max(rate),
                     "list_15pct_min": min(lists), "list_15pct_max": max(lists)}
    return out


def split_sizes(rows: list[dict]) -> dict:
    """Day-28 cohort and later non-completers per presentation code (the temporal split of the proposal)."""
    out = {}
    for code in ["2013B", "2013J", "2014B", "2014J"]:
        r = [x["day_28"] for x in rows if x["code_presentation"] == code]
        non = sum(x["non_completion"] for x in r)
        out[code] = {"presentations": len(r), "registered_day28": sum(x["n"] for x in r), "non_completion": non}
        # most a capacity-limited list can reach: a perfect list holds min(list length, non-completers) per presentation
        for c in CAPACITY:
            k = f"{int(c * 100)}%"
            hit = sum(min(x["list_size"][k], x["non_completion"]) for x in r)
            out[code][f"list_{k}"] = sum(x["list_size"][k] for x in r)
            out[code][f"coverage_ceiling_{k}"] = round(hit / non, 4) if non else None
    return out


def group_sizes(e: pl.DataFrame) -> dict:
    """Group sizes among enrolments registered at day 28, for the fairness KPI (S2)."""
    c = e.filter(registered_at(28))
    imd = {b: c.filter(pl.col("imd_band") == b).height for b in IMD}
    return {"registered_day28": c.height,
            "imd_band": imd,
            "imd_missing": c.filter(pl.col("imd_band").is_null()).height,
            "imd_most_deprived_20pct": imd["0-10%"] + imd["10-20%"],
            "imd_least_deprived_20pct": imd["80-90%"] + imd["90-100%"],
            "disability_yes": c.filter(pl.col("disability") == "Y").height,
            "disability_no": c.filter(pl.col("disability") == "N").height}


def main() -> None:
    t = load_all()
    e = enrolments(t)
    rows = per_presentation(e, t)
    result = {
        "definitions": __doc__.split("Definitions", 1)[1].split("Output:", 1)[0].strip(),
        "capacity_scenarios": CAPACITY,
        "overall": overall(e),
        "summary": summary(rows),
        "groups_day28": group_sizes(e),
        "split_day28": split_sizes(rows),
        "per_presentation": rows,
    }
    write_json("scope_feasibility.json", result)
    o, s = result["overall"], result["summary"]
    print(f"enrolments {o['enrolments']:,}; success {o['success']['share']:.1%}; "
          f"withdrawn {o['outcomes']['Withdrawn']['share']:.1%}; registered on day 0 {o['registered_day0']:,}")
    print("withdrawn by day (day-0 cohort): " + ", ".join(f"{k} {v['share']:.1%}" for k, v in o["withdrawn_by_day"].items())
          + f"; by the end {o['withdrawn_from_day0_cohort']['share']:.1%}")
    print("share of day-0-cohort withdrawals after: " + ", ".join(f"{k} {v:.1%}" for k, v in o["share_of_day0_withdrawals_after_day"].items()))
    print(f"first due day: {s['first_due_day']['min']}-{s['first_due_day']['max']} (median {s['first_due_day']['median']}); "
          f"{s['first_due_day']['presentations_due_before_day_28']} of {s['presentations']} presentations due before day 28")
    for name in ["day_14", "day_28", "day_60", "at_first_due"]:
        x = s[name]
        print(f"{name}: cohort {x['cohort_min']}-{x['cohort_max']} (total {x['cohort_total']:,}); non-completion "
              f"{x['non_completion_rate_min']:.1%}-{x['non_completion_rate_max']:.1%}; 15% list {x['list_15pct_min']}-{x['list_15pct_max']}")
    g = result["groups_day28"]
    print(f"day-28 groups: most deprived 20% {g['imd_most_deprived_20pct']:,}, least deprived 20% "
          f"{g['imd_least_deprived_20pct']:,}, IMD missing {g['imd_missing']:,}, disability {g['disability_yes']:,}")
    print("split (day-28 cohort / later non-completers): " + "; ".join(
        f"{k} {v['presentations']} pres. {v['registered_day28']:,}/{v['non_completion']:,}" for k, v in result["split_day28"].items()))
    print("written results/scope_feasibility.json")


if __name__ == "__main__":
    main()
