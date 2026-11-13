"""Derived numbers quoted in the report, each computed from result tables with its formula written out, so that
every quoted number has its own cell (results/headlines.csv) for the report check."""

import _tools  # noqa: F401
import pandas as pd

import common as c

R = c.RESULTS
rows = []


def add(name, value, formula):
    rows.append({"name": name, "value": value, "formula": formula})


ex = pd.read_csv(R / "aq1_exit_timing.csv").set_index("band")["non_completers"]
total = ex.sum()
add("nc_all", total, "non-completers among all 32,593 enrolments")
add("share_gone_before_d14", (ex["Withdrew before the start (day < 0)"] + ex["Withdrew days 0–13 (before the week-3 list)"]) / total,
    "withdrew before day 14 / all non-completers")
add("share_gone_d14_27", ex["Withdrew days 14–27 (before the week-5 list)"] / total, "withdrew days 14–27 / all non-completers")
add("share_reachable_after_d27", (ex["Withdrew days 28–90"] + ex["Withdrew after day 90"] + ex["Failed at the end of the run"]) / total,
    "(withdrew after day 27 + failed) / all non-completers")
add("share_fail_of_nc", ex["Failed at the end of the run"] / total, "failed / all non-completers")

yc = pd.read_csv(R / "aq1_not_registered_d14.csv").set_index("year")
add("not_reg_d14_2013", yc.loc[2013, "share"], "share of 2013 enrolments (6 shared modules) not registered at day 14")
add("not_reg_d14_2014", yc.loc[2014, "share"], "share of 2014 enrolments (6 shared modules) not registered at day 14")

err = pd.read_csv(R / "aq3_errors_by_slice.csv")
act = err[err["slice"] == "activity"].set_index("level")
add("nc_normal_activity", act.loc["normal", "non_completers"], "2014 non-completers at day 27 with clicks >= half the run median")
add("share_nc_normal_activity", act.loc["normal", "non_completers"] / act["non_completers"].sum(),
    "normal-activity non-completers / all non-completers at day 27 (2014)")
add("recall_normal_model", act.loc["normal", "recall_model"], "model recall among normal-activity non-completers")
add("recall_normal_rule", act.loc["normal", "recall_rule"], "rule recall among normal-activity non-completers")
add("recall_none_model", act.loc["none", "recall_model"], "model recall among non-completers with no click by day 27")

who = pd.read_csv(R / "aq3_model_vs_rule.csv").set_index("group")
add("swap_size", who.loc["Model list only", "enrolments"], "students on the model list only (= rule list only)")
add("rate_model_only", who.loc["Model list only", "rate"], "non-completion of students on the model list only")
add("rate_rule_only", who.loc["Rule list only", "rate"], "non-completion of students on the rule list only")
add("model_only_with_sign", who.loc["Model list only", "share_with_rule_sign"], "share of model-only students with any rule sign")
add("model_only_prev_attempt", who.loc["Model list only", "share_previous_attempt"], "share of model-only students with a previous attempt")
add("rule_only_prev_attempt", who.loc["Rule list only", "share_previous_attempt"], "share of rule-only students with a previous attempt")

s1 = pd.read_csv(R / "aq3_s1.csv").iloc[0]
groups = s1["list_places"] / 5
add("tutor_groups", groups, "list places / 5 = tutor groups of 20 across the 13 test runs")
add("groups_per_extra_hit", groups / s1["extra_listed_noncompleters"], "tutor groups per extra non-completer listed by the model")
add("rule_share_of_model_hits", 1 - s1["extra_listed_noncompleters"] / (s1["norm_recall_a"] * s1["list_places"]),
    "rule hits / model hits at day 27, 5 per 20")

reach = pd.read_csv(R / "aq4_reach.csv").iloc[0]
add("listed_withdrew_28_34", reach["withdrew_days_28_34"], "listed non-completers who withdrew in days 28–34")
add("share_listed_nc_fail", reach["listed_fail"] / reach["listed_non_completers"], "listed non-completers who failed / listed non-completers")

rs = pd.read_csv(R / "aq4_reasons.csv").set_index("top_reason")
add("share_list_reason_education", rs.loc["Prior education", "share_of_list"], "share of the list whose main reason is prior education")
add("share_list_reason_behaviour", rs.loc[["Low activity", "Missed a task", "Late submission"], "share_of_list"].sum(),
    "share of the list whose main reason is low activity, a missed task or a late submission")

pooled = pd.read_csv(R / "aq3_test_pooled.csv")
p = pooled[(pooled["cutoff"] == 27) & (pooled["per20"] == 5)].set_index("method")
add("m1_recall", p.loc["M1", "recall"], "share of all 2014 non-completers on the model lists, day 27, 5 per 20")
add("m1_precision", p.loc["M1", "precision"], "share of listed students who did not complete")
add("m1_missed", p.loc["M1", "positives"] - p.loc["M1", "tp"], "non-completers not on the model lists")
d13 = pooled[(pooled["cutoff"] == 13) & (pooled["per20"] == 5)].set_index("method")
add("m1_recall_d13", d13.loc["M1", "recall"], "model recall at day 13, 5 per 20")

out = pd.DataFrame(rows)
c.write(out, "headlines.csv")
print(out.assign(value=out["value"].round(4)).to_string(index=False))
