"""Final consistency check of the written reports.

1. Every file named in back-ticks or in a Markdown link inside the reports and notes exists.
2. The decision-critical numbers quoted in the reports equal the values in the result tables.

    python common/check_reports.py        (run through common/run_step.py: logs/check_reports.md)
"""

import re
import sys
from pathlib import Path

import polars as pl

ROOT = Path(__file__).resolve().parents[1]
bad = []
KNOWN_ABSENT = {"logs/logs/tests_lib.md"}      # named in the process log as a wrong path that was corrected

# ---- 1. referenced files exist --------------------------------------------------------------------------------
docs = [ROOT / "README.md", ROOT / "PROTOCOL.md", *sorted(ROOT.glob("aq-*/README.md")), *sorted(ROOT.glob("aq-*/NOTES.md")),
        ROOT / "logs" / "process-log.md", ROOT / "logs" / "ai-decision-log.md"]
n_refs = 0
for doc in docs:
    text = doc.read_text()
    refs = set(re.findall(r"\]\(([^)#]+?)\)", text)) | set(re.findall(r"`([\w./*-]+\.(?:csv|md|json|py|sh|png|sha256|txt|parquet))`", text))
    for ref in refs:
        if ref.startswith("http") or "<" in ref:
            continue
        n_refs += 1
        bases = [doc.parent, ROOT, doc.parent / "results", doc.parent / "extracted-datasets", doc.parent / "logs", doc.parent / "figures",
                 ROOT.parents[1], ROOT / "aq-3" / "results", ROOT / "logs", ROOT.parents[1] / "reports" / "milestone-3" / "package" / "data" / "processed",
                 ROOT.parents[1] / "reports" / "milestone-3" / "package" / "data" / "metadata", ROOT.parents[1] / "datasets" / "oulad",
                 ROOT.parents[1] / ".agents" / "skills" / "data-analyst", ROOT.parents[1] / ".agents" / "skills" / "data-analyst" / "scripts",
                 ROOT.parents[1] / "reports" / "milestone-4" / "package"]
        found = any(list(b.glob(ref)) if "*" in ref else (b / ref).exists() for b in bases)
        if not found and "*" not in ref:                       # bare file names in tables: search this folder and the Level 1 task
            name = Path(ref).name
            found = any(True for _ in ROOT.rglob(name)) or any(True for _ in (ROOT.parents[1] / "reports" / "milestone-4").rglob(name))
        if not found and ref not in KNOWN_ABSENT:
            bad.append(f"{doc.relative_to(ROOT)}: missing reference {ref}")
print(f"- file references checked: {n_refs}; missing: {len([b for b in bad if 'missing reference' in b])}")

# ---- 2. quoted numbers equal the result tables -------------------------------------------------------------------
def pct(x: float, digits: int = 1) -> str:
    """Percentage rounded half up on the decimal value (189 / 720 = 26.25% reads 26.3%)."""
    from decimal import ROUND_HALF_UP, Decimal
    return str((Decimal(repr(round(x * 100, 6)))).quantize(Decimal(10) ** -digits, rounding=ROUND_HALF_UP)) + "%"


def has(doc: str, text: str, what: str):
    body = (ROOT / doc).read_text().replace("\u2212", "-")        # the reports print a true minus sign
    if text.replace("\u2212", "-") not in body:
        bad.append(f"{doc}: expected '{text}' ({what})")


s1 = pl.read_csv(ROOT / "aq-3/results/s1_gate.csv").row(0, named=True)
has("aq-3/README.md", f"{s1['tp_a']:,} / {s1['max_attainable']:,} = {s1['pooled_nr_a']:.3f}", "S1 model")
has("aq-3/README.md", f"{s1['tp_b']:,} / {s1['max_attainable']:,} = {s1['pooled_nr_b']:.3f}", "S1 rule")
has("aq-3/README.md", f"+{s1['boot_ci_low']:.3f} to +{s1['boot_ci_high']:.3f}", "S1 interval")
has("aq-3/README.md", f"{s1['signflip_count']} of {s1['signflip_total']:,} sign assignments", "sign-flip count")
has("aq-3/README.md", f"{s1['wins']} / {s1['ties']} / {s1['losses']}", "wins/ties/losses")
has("README.md", f"{s1['pooled_nr_a']:.3f} against {s1['pooled_nr_b']:.3f}", "overview S1")
cal = pl.read_csv(ROOT / "aq-3/results/calibration.csv").filter((pl.col("cutoff") == 27) & (pl.col("model") == "M1")).row(0, named=True)
has("aq-3/README.md", f"| All 13 test runs (S3) | +{cal['citl']:.3f} | {cal['slope']:.3f} |", "S3")
tp = pl.read_csv(ROOT / "aq-3/results/test_pooled.csv").filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5))
for name, label in [("B3", "B3 background-only logistic model"), ("M3", "M3 gradient-boosted trees, primary set"), ("M4", "M4 gradient-boosted trees, extended set")]:
    v = tp.filter(pl.col("ranking") == name)["pooled_normalised_recall"][0]
    has("aq-3/README.md", f"| {label} | {v:.3f} |", f"test pooled {name}")
sens = pl.read_csv(ROOT / "aq-3/results/sensitivity.csv")
for r in sens.iter_rows(named=True):
    has("aq-3/README.md", f"| {r['runs']} | {r['model_nr']:.3f} | {r['rule_nr']:.3f} | {r['difference']:+.3f} ({r['boot_ci_low']:+.3f} to {r['boot_ci_high']:+.3f}) | {r['wins']} / {r['ties']} / {r['losses']} |", f"sensitivity {r['variant'][:30]}")
q = pl.read_csv(ROOT / "aq-4/results/list_quality_pooled.csv")
for r in q.filter(pl.col("ranking") != "random (expected)").iter_rows(named=True):
    has("aq-4/README.md", f"| {r['non_completers_on_list']:,.0f} | {r['recall']:.1%} | {r['attainable_recall']:.1%} | {r['normalised_recall']:.3f} | {r['precision']:.1%} | {r['lift']:.2f} |", f"AQ4 quality {r['cutoff']}/{r['per20']}/{r['ranking']}")
f = pl.read_csv(ROOT / "aq-4/results/fairness_confirmatory.csv").filter(pl.col("ranking") == "model")
for r in f.iter_rows(named=True):
    has("aq-4/README.md", f"| {r['test_enrolments']:,} | {r['group_non_completers']:,} | {r['recall_group']:.1%} | {r['recall_others']:.1%} | {r['gap'] * 100:+.1f} points ({r['boot_ci95_low'] * 100:+.1f} to {r['boot_ci95_high'] * 100:+.1f}) |".replace("+-", "−").replace("(-", "(−").replace("to -", "to −").replace("| -", "| −"), f"FR1 {r['group']}")
a13, a14 = pl.read_csv(ROOT / "aq-2/results/associations_2013.csv"), pl.read_csv(ROOT / "aq-2/results/associations_2014.csv")
for r13, r14 in zip(a13.iter_rows(named=True), a14.iter_rows(named=True)):
    has("aq-2/README.md", f"+{r13['adjusted_rd'] * 100:.1f} ({r13['adj_ci_low'] * 100:.1f} to {r13['adj_ci_high'] * 100:.1f}) | +{r14['adjusted_rd'] * 100:.1f} ({r14['adj_ci_low'] * 100:.1f} to {r14['adj_ci_high'] * 100:.1f})", f"AQ2 replication {r13['sign']}")
rt = pl.read_csv(ROOT / "aq-1/results/rates_all.csv")
for r in rt.filter(pl.col("level").is_in(["pooled", "year", "start_month", "module"])).iter_rows(named=True):
    has("aq-1/README.md", f"| {r['enrolments']:,} | {r['events']:,} | {pct(r['rate'])} | {r['ci_low'] * 100:.1f} to {r['ci_high'] * 100:.1f} |", f"AQ1 rate {r['level']} {r['group']}")
fm = pl.read_csv(ROOT / "aq-1/results/first_missed_task_by_outcome_all.csv")
for r in fm.filter(pl.col("group").is_in(["Fail", "Withdrawn"])).iter_rows(named=True):
    has("aq-1/README.md", f"| {r['enrolments']:,} | {r['share_ever_missed']:.1%} | {r['median_first_missed_week']:.0f} | {r['share_missed_by_week_4']:.1%} | {r['share_missed_by_week_8']:.1%} | {r['share_missed_by_week_12']:.1%} | {r['share_missed_by_week_20']:.1%} |", f"AQ1 first missed {r['group']}")

numeric = [b for b in bad if "expected" in b]
print(f"- quoted-number checks failed: {len(numeric)}")
for b in bad:
    print(f"  - FAIL {b}")
print("\nRESULT:", "PASS" if not bad else "FAIL")
sys.exit(1 if bad else 0)
