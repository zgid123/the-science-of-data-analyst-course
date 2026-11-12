"""Final consistency check of the written reports.

1. Every file named in back-ticks or in a Markdown link inside the reports, notes and logs exists.
2. Every row of every report table equals the row built from the result tables by `common/report_tables.py`.
3. The decision-critical numbers quoted in the prose equal the values in the result tables.
4. Times and counts of this run quoted in the documents equal the freeze record, the test-access record, the unit-test
   logs and the experiment log.
5. No sentence of the first run that is untrue of this rerun is left in a document (PROTOCOL.md, "Status").

    python common/check_reports.py        (run through common/run_step.py: logs/check_reports.md)
"""

import json
import re
import sys
from pathlib import Path

import polars as pl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report_tables as rt  # noqa: E402
from report_tables import ci, pct, rnd, signed  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
bad: list[str] = []
counts = {"refs": 0, "table_rows": 0, "prose": 0, "run_facts": 0, "stale": 0}
KNOWN_ABSENT = {"logs/check_reports.md", "check_reports.md"}      # this check's own log, written by the runner after the check ends

# ---- 1. referenced files exist --------------------------------------------------------------------------------
docs = [ROOT / "README.md", ROOT / "PROTOCOL.md", *sorted(ROOT.glob("aq-*/README.md")), *sorted(ROOT.glob("aq-*/NOTES.md")),
        ROOT / "logs" / "process-log.md", ROOT / "logs" / "ai-decision-log.md"]
for doc in docs:
    if not doc.exists():
        bad.append(f"{doc.relative_to(ROOT)}: document missing")
docs = [d for d in docs if d.exists()]
for doc in docs:
    text = doc.read_text()
    refs = set(re.findall(r"\]\(([^)#]+?)\)", text)) | set(re.findall(r"`([\w./*-]+\.(?:csv|md|json|py|sh|png|sha256|txt|parquet))`", text))
    for ref in refs:
        if ref.startswith("http") or "<" in ref:
            continue
        counts["refs"] += 1
        bases = [doc.parent, ROOT, doc.parent / "results", doc.parent / "extracted-datasets", doc.parent / "logs", doc.parent / "figures", doc.parent / "code",
                 REPO, ROOT / "aq-3" / "results", ROOT / "logs", ROOT / "common", REPO / "reports" / "milestone-3" / "package" / "data" / "processed",
                 REPO / "reports" / "milestone-3" / "package" / "data" / "metadata", REPO / "datasets" / "oulad",
                 REPO / ".agents" / "skills" / "data-analyst", REPO / ".agents" / "skills" / "data-analyst" / "scripts",
                 REPO / "reports" / "milestone-4" / "package", REPO / "reports" / "milestone-5" / "report", REPO / "reports" / "milestone-5" / "code"]
        found = any(list(b.glob(ref)) if "*" in ref else (b / ref).exists() for b in bases)
        if not found and "*" not in ref:                       # bare file names in tables: search this folder and the Level 1 task
            name = Path(ref).name
            found = any(True for _ in ROOT.rglob(name)) or any(True for _ in (REPO / "reports" / "milestone-4").rglob(name))
        if not found and ref not in KNOWN_ABSENT:
            bad.append(f"{doc.relative_to(ROOT)}: missing reference {ref}")


def norm(s: str) -> str:
    return s.replace("−", "-").replace("–", "-")


def has(doc: str, text: str, what: str, kind: str = "prose"):
    counts[kind] += 1
    p = ROOT / doc
    if not p.exists() or norm(text) not in norm(p.read_text()):
        bad.append(f"{doc}: expected '{text}' ({what})")


# ---- 2. every table row of the reports equals the row built from the result tables ---------------------------------
for aq, fn in rt.ALL.items():
    for title, lines in fn().items():
        for line in lines:
            if set(line) <= set("|:- "):
                continue
            has(f"{aq}/README.md", line, f"row of '{title[:60]}'", "table_rows")

# ---- 3. numbers quoted in the prose ------------------------------------------------------------------------------
csv = rt.csv
s1 = csv("aq-3/results/s1_gate.csv").row(0, named=True)
has("aq-3/README.md", f"{s1['tp_a']:,} / {s1['max_attainable']:,} = {s1['pooled_nr_a']:.3f}", "S1 model")
has("aq-3/README.md", f"{s1['tp_b']:,} / {s1['max_attainable']:,} = {s1['pooled_nr_b']:.3f}", "S1 rule")
has("aq-3/README.md", f"+{s1['boot_ci_low']:.3f} to +{s1['boot_ci_high']:.3f}", "S1 interval")
has("aq-3/README.md", f"{s1['signflip_count']} of {s1['signflip_total']:,} sign assignments", "sign-flip count")
has("aq-3/README.md", f"{s1['wins']} / {s1['ties']} / {s1['losses']}", "wins/ties/losses")
has("aq-3/README.md", f"+{s1['tp_a'] - s1['tp_b']} non-completers", "S1 extra non-completers")
has("README.md", f"{s1['pooled_nr_a']:.3f} against {s1['pooled_nr_b']:.3f}", "overview S1")
has("README.md", f"+{s1['boot_ci_low']:.3f} to +{s1['boot_ci_high']:.3f}", "overview S1 interval")
cal = csv("aq-3/results/calibration.csv").filter((pl.col("cutoff") == 27) & (pl.col("model") == "M1")).row(0, named=True)
has("README.md", f"calibration-in-the-large {signed(cal['citl'], 3, 1.0)} and slope {rnd(cal['slope'], 3)}", "overview S3")
cc = csv("aq-3/results/crosscheck_earlier_run.csv")
old_slope = cc.filter(pl.col("quantity").str.contains("Calibration slope"))["earlier_run"][0]
has("aq-3/README.md", f"{rnd(cal['slope'], 3)} / met | {rnd(old_slope, 3)} / not met", "cross-check S3")
q = csv("aq-4/results/list_quality_pooled.csv").filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5))
qm = q.filter(pl.col("ranking") == "model").row(0, named=True)
qr = q.filter(pl.col("ranking").str.starts_with("random")).row(0, named=True)
has("README.md", f"{pct(qm['recall'])} of later non-completers against {pct(qr['recall'])} for a random list", "overview AQ4 recall")
has("aq-4/README.md", f"{float(qm['non_completers_on_list']):,.0f} of {qm['non_completers']:,}", "AQ4 recall counts")
fl = csv("aq-4/results/fairness_confirmatory.csv").filter((pl.col("ranking") == "model") & pl.col("confirmatory"))
has("README.md", f"{int(fl['flagged'].sum())} of {fl.height} groups flagged", "overview FR1")

# AQ2: headline estimates, the late-TMA correction, the replication and the post hoc result
a13, a14 = csv("aq-2/results/associations_2013.csv"), csv("aq-2/results/associations_2014.csv")
rep = csv("aq-2/results/replication.csv")
for s in rt.SIGN_ORDER:
    r = rep.filter(pl.col("sign") == s).row(0, named=True)
    has("README.md", f"{signed(r['adjusted_rd'])} / {signed(r['adjusted_rd_2014'])}", f"overview AQ2 {s}")
tma = rep.filter(pl.col("sign") == "sign_tma_late").row(0, named=True)
has("aq-2/README.md", f"{signed(tma['adjusted_rd_2014'])} points ({ci(tma['adj_ci_low_2014'], tma['adj_ci_high_2014'])}) over the {tma['n_support_2014']:,} enrolments", "AQ2 late TMA 2014 with n")
has("aq-2/NOTES.md", f"{signed(tma['adjusted_rd_2014'])} ({ci(tma['adj_ci_low_2014'], tma['adj_ci_high_2014'])}), n = {tma['n_support_2014']:,}", "AQ2 notes late TMA")
bm14 = csv("aq-2/results/associations_by_module_2014.csv")
aaa = bm14.filter((pl.col("sign") == "sign_tma_late") & (pl.col("code_module") == "AAA")).row(0, named=True)
has("aq-2/README.md", f"{signed(aaa['adjusted_rd'])} points ({ci(aaa['adj_ci_low'], aaa['adj_ci_high'], sign=True)}; {aaa['with_sign']} of {aaa['enrolments']} students with the sign)", "AQ2 late TMA in AAA-2014J")
n_incl = int((~bm14["interval_excludes_0"]).sum())
has("aq-2/README.md", f"{n_incl} of the {bm14.height} module estimates of 2014 have an interval that includes 0", "AQ2 module estimates including 0, 2014")
bm13 = csv("aq-2/results/associations_by_module_2013.csv")
has("aq-2/README.md", f"{int((~bm13['interval_excludes_0']).sum())} of the {bm13.height} module estimates of 2013", "AQ2 module estimates including 0, 2013")
ss = csv("aq-2/results/replication_sensitivity.csv")
for v, tag in (("post hoc: + log(1 + clicks on days 0-27)", "half"), ("post hoc: low activity = below the run median, + log(1 + clicks on days 0-27)", "median")):
    r = ss.filter((pl.col("variant") == v) & pl.col("sign").str.starts_with("sign_low_activity")).row(0, named=True)
    has("aq-2/README.md", f"{signed(r['adjusted_rd'])} points ({ci(r['adj_ci_low'], r['adj_ci_high'], sign=True)}) in 2013 and {signed(r['adjusted_rd_2014'])} ({ci(r['adj_ci_low_2014'], r['adj_ci_high_2014'], sign=True)}) in 2014", f"AQ2 post hoc low activity, {tag} cut")
has("aq-2/README.md", f"{int(rep['change_interval_includes_0'].sum())} of the 5 changes have an interval that includes 0", "AQ2 change intervals")
lt = csv("aq-2/results/late_tma_average_check.csv").row(0, named=True)
has("aq-2/README.md", f"give {signed(lt['average_if_those_rows_counted_as_0'])} points", "AQ2 diluted late-TMA average")

# AQ1: headline rate, the year comparison and the week-4 share
rates = csv("aq-1/results/rates_all.csv")
p = rates.filter(pl.col("level") == "pooled").row(0, named=True)
has("aq-1/README.md", f"{p['events']:,} ({pct(p['rate'])}, 95% interval {ci(p['ci_low'], p['ci_high'])})", "AQ1 pooled rate")
has("README.md", f"{pct(p['rate'])} of the {p['enrolments']:,} enrolments registered at day 14", "overview AQ1 rate")
yc = csv("aq-1/results/year_comparison_all.csv").filter((pl.col("level") == "overall") & pl.col("method").str.starts_with("pooled"))
for r in yc.iter_rows(named=True):
    txt = f"{signed(r['difference_2014_minus_2013'])} points ({ci(r['ci_low'], r['ci_high'], sign=True)})"
    has("aq-1/README.md", txt, f"AQ1 year difference {r['scope'][:20]} / {r['denominator'][:12]}")
    if "modules run in both years" in r["scope"]:
        has("README.md", txt, f"overview AQ1 year difference / {r['denominator'][:12]}")
        has("aq-1/NOTES.md", txt, f"AQ1 notes year difference / {r['denominator'][:12]}")
nr = csv("aq-1/results/not_registered_d14_by_year_all.csv").row(0, named=True)
has("aq-1/README.md", f"{pct(nr['share_not_registered_2014'])} of the 2014 enrolments against {pct(nr['share_not_registered_2013'])} of the 2013 enrolments", "AQ1 not registered at day 14")
w4 = csv("aq-1/results/first_missed_by_week4_all.csv").filter(pl.col("group").str.starts_with("Non-completers") & (pl.col("year").cast(pl.Utf8) == "both years"))
has("aq-1/README.md", f"{pct(w4.filter(pl.col('population') == 'all runs')['share'][0])} of non-completers", "AQ1 week-4 share, all runs")
has("aq-1/README.md", f"{pct(w4.filter(pl.col('population') != 'all runs')['share'][0])} in the", "AQ1 week-4 share, runs with a task due")
ck = csv("aq-1/results/checks_all.csv")
has("aq-1/NOTES.md", f"{int((ck['result'] == 'PASS').sum())} of {ck.height} checks pass", "AQ1 check count")

# ---- 4. facts of this run ------------------------------------------------------------------------------------------
fz = json.loads((ROOT / "aq-3/results/freeze.json").read_text())
acc = [l for l in (ROOT / "aq-3/logs/test-access.md").read_text().splitlines() if l.startswith("| 20")]
first_access = acc[0].split("|")[1].strip()
for doc in ("README.md", "aq-3/README.md", "aq-3/NOTES.md", "logs/process-log.md"):
    has(doc, fz["frozen_utc"], "freeze time of this rerun", "run_facts")
    has(doc, first_access, "first test access of this rerun", "run_facts")
for doc in ("README.md", "PROTOCOL.md", "logs/process-log.md", "aq-3/README.md"):
    has(doc, "2026-11-11T23:18:16Z", "freeze time of the first run kept as history", "run_facts")
for doc in ("README.md", "PROTOCOL.md", "logs/process-log.md", "aq-1/README.md", "aq-2/README.md", "aq-3/README.md", "aq-4/README.md"):
    has(doc, "rerun", "the document says that this is a rerun", "run_facts")
for log, docs_ in (("tests_lib.md", ("README.md", "logs/process-log.md")), ("tests_aq2_model.md", ("README.md", "logs/process-log.md", "aq-2/NOTES.md"))):
    m = re.search(r"(\d+) of (\d+) checks passed", (ROOT / "logs" / log).read_text())
    for doc in docs_:
        has(doc, f"{m.group(1)} of {m.group(2)}", f"unit-test count of logs/{log}", "run_facts")
ver = csv("aq-3/results/verification.csv")
has("aq-3/NOTES.md", f"{int((ver['result'] == 'PASS').sum())} of {ver.height} verification checks pass", "verification count", "run_facts")
cmp = csv("logs/compare_first_run.csv")
for aq in ("aq-3", "aq-4"):
    t = cmp.filter(pl.col("aq") == aq)
    ident = t.filter(pl.col("status") == "byte-identical").height
    has("logs/process-log.md", f"{aq}: {ident} of {t.height} result tables byte-identical", f"comparison with the first run, {aq}", "run_facts")
exp = (ROOT / "logs" / "experiment-log.md").read_text()
fails = [l for l in exp.splitlines() if l.startswith("| 20") and l.split("|")[5].strip() != "0"]
has("logs/process-log.md", f"{len(fails)} step{'s' if len(fails) != 1 else ''} with a non-zero exit status", "failed steps recorded in the experiment log", "run_facts")

# ---- 5. sentences of the first run that are untrue of this rerun ------------------------------------------------------
STALE = ["fixed before any result", "written before any result", "before any result existed", "built without reading", "without reading the earlier",
         "No choice in it was made after seeing a 2014 outcome", "not opened** until", "5 points smaller", "least stable of the five signs",
         "the year does not", "2013 and 2014 are alike", "independent second implementation", "run 11 November 2026"]
for doc in docs:
    body = doc.read_text()
    for phrase in STALE:
        counts["stale"] += 1
        if phrase in body:
            bad.append(f"{doc.relative_to(ROOT)}: sentence of the first run left in the document: '{phrase}'")

print(f"- file references checked: {counts['refs']}; missing: {len([b for b in bad if 'missing reference' in b])}")
print(f"- report table rows compared with the rows built from the result tables: {counts['table_rows']}")
print(f"- numbers quoted in the prose compared with the result tables: {counts['prose']}")
print(f"- facts of this run (freeze time, first test access, test counts, comparison with the first run): {counts['run_facts']}")
print(f"- searches for sentences of the first run that are untrue of this rerun: {counts['stale']}")
print(f"- checks failed: {len(bad)}")
for b in bad:
    print(f"  - FAIL {b}")
print("\nRESULT:", "PASS" if not bad else "FAIL")
sys.exit(1 if bad else 0)
