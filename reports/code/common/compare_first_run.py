"""Compare every regenerated result table with the first run of this folder (git commit 11f4aca; PROTOCOL.md P20, P23).

AQ3 and AQ4 are a reproduction of an unchanged design, so their tables must hold the same numbers; the script exits 1
when a number of an AQ3 or AQ4 table differs. AQ1 and AQ2 changed by design (P16-P18, P21, P22); their differences are
listed, with the headline numbers of both runs side by side.

Columns that record time or file hashes (`seconds`, `sha256`) are compared apart: they may differ without any number
changing. In text columns, UTC timestamps and the count of recorded test accesses are masked before the comparison,
because they describe when a run happened (the detail of verification check V6 quotes the freeze time).

    python common/compare_first_run.py     writes logs/compare_first_run.csv and logs/compare_first_run_headlines.csv
"""

import io
import re
import subprocess
import sys
from pathlib import Path

import polars as pl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib  # noqa: E402

ROOT, REPO, OLD = lib.CODE_ROOT, lib.REPO, lib.FIRST_RUN_COMMIT
NON_NUMERIC_RECORD = {"seconds", "sha256"}
RUN_TIME_TEXT = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z|\d+ accesses recorded")


def mask_run_time(col: pl.Series) -> list:
    return [None if v is None else RUN_TIME_TEXT.sub("<run time>", v) for v in col.cast(pl.Utf8).to_list()]


def old_bytes(rel: str) -> bytes | None:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"{OLD}:reports/code/{rel}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def old_csv(rel: str) -> pl.DataFrame:
    return pl.read_csv(io.BytesIO(old_bytes(rel)))


listed = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", OLD, "reports/code/"], capture_output=True, text=True).stdout.split("\n")
old_files = sorted(f[len("reports/code/"):] for f in listed if "/results/" in f and f.endswith(".csv"))
new_files = sorted(str(p.relative_to(ROOT)) for p in ROOT.glob("aq-*/results/*.csv"))
rows = []
for rel in sorted(set(old_files) | set(new_files)):
    aq = rel.split("/")[0]
    if rel not in new_files:
        rows.append({"aq": aq, "file": rel, "status": "only in the first run", "detail": ""}); continue
    if rel not in old_files:
        rows.append({"aq": aq, "file": rel, "status": "new in the rerun", "detail": ""}); continue
    ob, nb = old_bytes(rel), (ROOT / rel).read_bytes()
    if ob == nb:
        rows.append({"aq": aq, "file": rel, "status": "byte-identical", "detail": ""}); continue
    o, n = pl.read_csv(io.BytesIO(ob)), pl.read_csv(io.BytesIO(nb))
    if o.columns != n.columns or o.shape != n.shape:
        rows.append({"aq": aq, "file": rel, "status": "structure differs",
                     "detail": f"first run {o.shape[0]} rows x {o.shape[1]} columns; rerun {n.shape[0]} x {n.shape[1]}"}); continue
    diffs, record = [], []
    for c in o.columns:
        if o[c].dtype.is_numeric() and n[c].dtype.is_numeric():
            d = float((o[c].cast(pl.Float64) - n[c].cast(pl.Float64)).abs().max() or 0.0)
            unequal = d > 0 or o[c].null_count() != n[c].null_count()
            msg = f"{c}: largest absolute difference {d:.6g}"
        else:
            raw = int((~o[c].cast(pl.Utf8).eq_missing(n[c].cast(pl.Utf8))).sum())
            k = sum(x != y for x, y in zip(mask_run_time(o[c]), mask_run_time(n[c])))
            unequal, msg = raw > 0, f"{c}: {k} of {o.height} values differ" + (f" ({raw - k} more differ only in a quoted run time)" if raw > k else "")
            if raw > 0 and k == 0:
                record.append(f"{c}: {raw} of {o.height} values differ only in a quoted run time")
                continue
        if unequal:
            (record if c in NON_NUMERIC_RECORD else diffs).append(msg)
    if diffs:
        rows.append({"aq": aq, "file": rel, "status": "values differ", "detail": "; ".join(diffs)})
    else:
        rows.append({"aq": aq, "file": rel, "status": "same values (only time or hash columns differ)", "detail": "; ".join(record)})
cmp = pl.DataFrame(rows)
lib.banner(f"Result tables of the rerun against the first run (commit {OLD})")
summary = cmp.group_by("aq", "status").agg(pl.len().alias("files")).sort("aq", "status")
print(lib.md_table(summary))
for aq in ("aq-3", "aq-4"):
    t = cmp.filter(pl.col("aq") == aq)
    print(f"\n**{aq}: {t.height} result tables** – byte-identical: {t.filter(pl.col('status') == 'byte-identical').height}; "
          f"same values, only time or hash columns differ: {t.filter(pl.col('status').str.starts_with('same values')).height}; "
          f"other: {t.filter(~pl.col('status').is_in(['byte-identical']) & ~pl.col('status').str.starts_with('same values')).height}")
other = cmp.filter(pl.col("status") != "byte-identical")
print("\n**Every table that is not byte-identical**\n\n" + lib.md_table(other.with_columns(pl.col("detail").str.slice(0, 400))))
lib.save_csv(cmp, ROOT / "logs" / "compare_first_run.csv")

# ---- model files -------------------------------------------------------------------------------------------------
fz_old = old_csv("aq-3/results/frozen_models.csv").select("name", "cutoff", pl.col("hyperparameters").alias("hp_first_run"), pl.col("sha256").alias("sha_first_run"))
fz_new = pl.read_csv(ROOT / "aq-3/results/frozen_models.csv").select("name", "cutoff", "hyperparameters", "sha256")
fz = fz_new.join(fz_old, on=["name", "cutoff"]).with_columns((pl.col("hyperparameters") == pl.col("hp_first_run")).alias("same_hyperparameters"),
                                                             (pl.col("sha256") == pl.col("sha_first_run")).alias("same_file_hash"))
print(f"\n**Frozen models**: same hyperparameters in {int(fz['same_hyperparameters'].sum())} of {fz.height}; "
      f"model file byte-identical (SHA-256) in {int(fz['same_file_hash'].sum())} of {fz.height}\n\n" + lib.md_table(fz.select("name", "cutoff", "hyperparameters", "same_hyperparameters", "same_file_hash")))

# ---- headline numbers side by side ---------------------------------------------------------------------------------
H = []


def head(aq, quantity, old, new, note=""):
    same = (old == new) or (isinstance(old, float) and isinstance(new, float) and abs(old - new) < 5e-7)
    H.append({"aq": aq, "quantity": quantity, "first_run": f"{old:.4f}" if isinstance(old, float) else str(old),
              "rerun": f"{new:.4f}" if isinstance(new, float) else str(new), "same": bool(same), "note": note})


o, n = old_csv("aq-3/results/s1_gate.csv").row(0, named=True), pl.read_csv(ROOT / "aq-3/results/s1_gate.csv").row(0, named=True)
for k, lab in [("tp_a", "S1: non-completers on the model lists"), ("tp_b", "S1: non-completers on the rule lists"), ("max_attainable", "S1: most attainable"),
               ("pooled_nr_a", "S1: pooled normalised recall, model"), ("pooled_nr_b", "S1: pooled normalised recall, rule"), ("difference", "S1: difference"),
               ("boot_ci_low", "S1: bootstrap interval, low"), ("boot_ci_high", "S1: bootstrap interval, high"), ("signflip_p", "S1: sign-flip p"),
               ("wins", "S1: runs won"), ("losses", "S1: runs lost"), ("verdict", "S1: verdict")]:
    head("aq-3", lab, o[k], n[k])
mo = old_csv("aq-3/results/model_choice.csv").filter(pl.col("chosen"))["config"][0]
mn = pl.read_csv(ROOT / "aq-3/results/model_choice.csv").filter(pl.col("chosen"))["config"][0]
head("aq-3", "chosen configuration", mo, mn)
f = lambda d: d.filter((pl.col("cutoff") == 27) & (pl.col("model") == "M1")).row(0, named=True)  # noqa: E731
o, n = f(old_csv("aq-3/results/calibration.csv")), f(pl.read_csv(ROOT / "aq-3/results/calibration.csv"))
for k, lab in [("citl", "S3: calibration-in-the-large"), ("slope", "S3: calibration slope"), ("s3_bounds_met", "S3: pooled bounds met")]:
    head("aq-3", lab, o[k], n[k])
o, n = old_csv("aq-4/results/fairness_confirmatory.csv").filter(pl.col("ranking") == "model"), pl.read_csv(ROOT / "aq-4/results/fairness_confirmatory.csv").filter(pl.col("ranking") == "model")
for ro, rn in zip(o.iter_rows(named=True), n.iter_rows(named=True)):
    assert ro["group"] == rn["group"]
    for k in ("gap", "boot_ci95_low", "boot_ci95_high"):
        head("aq-4", f"FR1 {ro['group']}: {k}", ro[k], rn[k])
    flag_col = [c for c in o.columns if "flag" in c][0]
    head("aq-4", f"FR1 {ro['group']}: {flag_col}", ro[flag_col], rn[flag_col])
f = lambda d: d.filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5) & (pl.col("ranking") == "model")).row(0, named=True)  # noqa: E731
o, n = f(old_csv("aq-4/results/list_quality_pooled.csv")), f(pl.read_csv(ROOT / "aq-4/results/list_quality_pooled.csv"))
for k, lab in [("recall", "list recall, day 27, 5 per 20"), ("lift", "list lift")]:
    head("aq-4", lab, o[k], n[k])
o, n = old_csv("aq-2/results/associations_2013.csv"), pl.read_csv(ROOT / "aq-2/results/associations_2013.csv")
o14, n14 = old_csv("aq-2/results/associations_2014.csv"), pl.read_csv(ROOT / "aq-2/results/associations_2014.csv")
for (ro, rn, yr) in [(a, b, 2013) for a, b in zip(o.iter_rows(named=True), n.iter_rows(named=True))] + [(a, b, 2014) for a, b in zip(o14.iter_rows(named=True), n14.iter_rows(named=True))]:
    assert ro["sign"] == rn["sign"]
    note = "P16/P17: averaged over the runs with a TMA due only" if ro["sign"] == "sign_tma_late" else ""
    head("aq-2", f"{yr} {ro['sign']}: rows averaged over", ro["enrolments_defined"], rn["n_support"], note)
    head("aq-2", f"{yr} {ro['sign']}: adjusted risk difference", ro["adjusted_rd"], rn["adjusted_rd"], note)
    head("aq-2", f"{yr} {ro['sign']}: unadjusted risk difference", ro["unadjusted_rd"], rn["unadjusted_rd"], note)
    head("aq-2", f"{yr} {ro['sign']}: verdict", ro["verdict"], rn["verdict"])
o, n = old_csv("aq-1/results/rates_all.csv"), pl.read_csv(ROOT / "aq-1/results/rates_all.csv")
for lev, grp in [("pooled", "all runs"), ("year", "2013"), ("year", "2014")]:
    a = o.filter((pl.col("level") == lev) & (pl.col("group").cast(pl.Utf8) == grp)).row(0, named=True)
    b = n.filter((pl.col("level") == lev) & (pl.col("group").cast(pl.Utf8) == grp)).row(0, named=True)
    head("aq-1", f"non-completion rate, {lev} {grp}", a["rate"], b["rate"])
yc = pl.read_csv(ROOT / "aq-1/results/year_comparison_all.csv").filter((pl.col("level") == "overall") & pl.col("method").str.starts_with("pooled"))
for r in yc.iter_rows(named=True):
    H.append({"aq": "aq-1", "quantity": f"2014 - 2013, {r['scope']}, {r['denominator']}", "first_run": "not computed",
              "rerun": f"{r['difference_2014_minus_2013']:+.4f} ({r['ci_low']:+.4f} to {r['ci_high']:+.4f})", "same": False, "note": "P18: added"})
hd = pl.DataFrame(H)
print("\n**Headline numbers, first run beside the rerun**\n\n" + lib.md_table(hd))
lib.save_csv(hd, ROOT / "logs" / "compare_first_run_headlines.csv")
h34 = hd.filter(pl.col("aq").is_in(["aq-3", "aq-4"]))
print(f"\nAQ3 and AQ4 headline numbers equal to the first run: {int(h34['same'].sum())} of {h34.height}")
bad = cmp.filter(pl.col("aq").is_in(["aq-3", "aq-4"]) & pl.col("status").is_in(["values differ", "structure differs", "only in the first run", "new in the rerun"]))
print(f"AQ3 and AQ4 result tables whose numbers differ from the first run: {bad.height}")
ok = bad.height == 0 and bool(h34["same"].all())
print("\nRESULT:", "PASS (AQ3 and AQ4 reproduce the first run)" if ok else "FAIL (AQ3 or AQ4 differs from the first run)")
sys.exit(0 if ok else 1)
