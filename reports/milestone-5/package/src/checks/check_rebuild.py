"""Compare a rebuild of this package with the published versions it must reproduce.

Usage (from the package folder):
    python src/checks/check_rebuild.py prepared   # run_all.sh step 07
    python src/checks/check_rebuild.py results    # run_all.sh step 18
    python src/checks/check_rebuild.py results --write   # record the reference checksums (package maintainers only)
    python src/checks/check_rebuild.py results_aq34          # run_all.sh step 27 (AQ3 and AQ4)
    python src/checks/check_rebuild.py results_aq34 --write  # record the AQ3/AQ4 reference checksums (maintainers only)

prepared: compares the SHA-256 and row count of every rebuilt view in data/processed/ with the published manifest of
the prepared dataset OULAD-N04-prepared-1.0 (data/metadata/version_manifest_published.json); also reports the raw
inputs and the pipeline scripts in src/ against the same manifest. Writes data/metadata/rebuild_check_prepared.csv.

results: compares the SHA-256 of every result file in results/2013/, 2014/, all_runs/ and compare/
with results/checksums.csv. Writes
data/metadata/rebuild_check_results.csv.

results_aq34: the same comparison for the AQ3/AQ4 files (aq3_* and aq4_* in results/2013/, 2014/, all_runs/ and
compare/) against results/checksums_aq34.csv. Writes
data/metadata/rebuild_check_results_aq34.csv.

Prints one line per file and exits 1 if a rebuilt prepared view or result file differs from its reference.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[2]
META = PKG / "data" / "metadata"
RESULTS = PKG / "results"
RESULT_FILES = [f"{d}{pat}" for d in ("2013/", "2014/", "all_runs/")
                for pat in ("aq1_*.csv", "aq2_*.csv", "aq_results.json", "aq_summary.md")] + ["compare/aq1_*.csv", "compare/aq2_*.csv", "compare/aq_summary.md"]
RESULT_FILES_AQ34 = [f"{d}/{p}" for d in ("2013", "2014", "all_runs", "compare") for p in ("aq3_*", "aq4_*")]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write(rows: list[dict], name: str) -> None:
    with (META / name).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def prepared() -> int:
    import polars as pl

    ref = json.loads((META / "version_manifest_published.json").read_text())
    rows = []
    for name, x in sorted(ref["outputs"].items()):
        p = PKG / "data" / "processed" / name
        if not p.exists():
            rows.append(dict(kind="prepared view", file=name, reference_sha256=x["sha256"], rebuilt_sha256="",
                             reference_rows=x["rows"], rebuilt_rows="", status="MISSING"))
            continue
        digest, n = sha256(p), pl.read_parquet(p).height
        status = "MATCH" if digest == x["sha256"] and n == x["rows"] else "MISMATCH"
        rows.append(dict(kind="prepared view", file=name, reference_sha256=x["sha256"], rebuilt_sha256=digest,
                         reference_rows=x["rows"], rebuilt_rows=n, status=status))
    for name, ref_sha in sorted(ref["raw_input"].items()):
        p = PKG / "data" / "raw" / name
        digest = sha256(p) if p.exists() else ""
        rows.append(dict(kind="raw input", file=name, reference_sha256=ref_sha, rebuilt_sha256=digest,
                         reference_rows="", rebuilt_rows="", status="MATCH" if digest == ref_sha else "MISMATCH"))
    for name, ref_sha in sorted(ref["code"].items()):
        p = PKG / "src" / name
        digest = sha256(p) if p.exists() else ""
        status = "MATCH" if digest == ref_sha else ("NOT SHIPPED" if not p.exists() else "DIFFERENT")
        rows.append(dict(kind="pipeline script", file=name, reference_sha256=ref_sha, rebuilt_sha256=digest,
                         reference_rows="", rebuilt_rows="", status=status))
    write(rows, "rebuild_check_prepared.csv")
    for r in rows:
        print(f"{r['status']:<11} {r['kind']:<15} {r['file']}"
              + (f"  rows {r['rebuilt_rows']} (published {r['reference_rows']})" if r["kind"] == "prepared view" else ""))
    views = [r for r in rows if r["kind"] == "prepared view"]
    ok = sum(r["status"] == "MATCH" for r in views)
    raw_ok = all(r["status"] == "MATCH" for r in rows if r["kind"] == "raw input")
    print(f"{ok} of {len(views)} prepared views identical to {ref['prepared_dataset_version']} "
          f"(SHA-256 and rows); raw inputs {'all match' if raw_ok else 'DIFFER'}")
    return 0 if ok == len(views) and raw_ok else 1


def rel(p: Path) -> str:
    """Path of a result file inside results/, with forward slashes (the key in checksums.csv)."""
    return p.relative_to(RESULTS).as_posix()


def result_files(patterns: list[str] = RESULT_FILES) -> list[Path]:
    return sorted({p for pat in patterns for p in RESULTS.glob(pat)})


def results(write_reference: bool, patterns: list[str] = RESULT_FILES, reference: str = "checksums.csv",
            out: str = "rebuild_check_results.csv") -> int:
    ref_path = RESULTS / reference
    if write_reference:
        with ref_path.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["file", "sha256"])
            w.writerows([rel(p), sha256(p)] for p in result_files(patterns))
        print(f"reference checksums of {len(result_files(patterns))} result files written to results/{reference}")
        return 0
    ref = {r["file"]: r["sha256"] for r in csv.DictReader(ref_path.open())}
    rows = []
    for name, ref_sha in sorted(ref.items()):
        p = RESULTS / name
        digest = sha256(p) if p.exists() else ""
        rows.append(dict(file=name, reference_sha256=ref_sha, rebuilt_sha256=digest,
                         status="MATCH" if digest == ref_sha else ("MISSING" if not p.exists() else "MISMATCH")))
    extra = [rel(p) for p in result_files(patterns) if rel(p) not in ref]
    write(rows, out)
    for r in rows:
        print(f"{r['status']:<8} {r['file']}")
    ok = sum(r["status"] == "MATCH" for r in rows)
    print(f"{ok} of {len(rows)} result files byte-identical to results/{reference}"
          + (f"; files without a reference: {', '.join(extra)}" if extra else ""))
    return 0 if ok == len(rows) and not extra else 1


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else ""
    if what == "prepared":
        sys.exit(prepared())
    if what == "results":
        sys.exit(results("--write" in sys.argv[2:]))
    if what == "results_aq34":
        sys.exit(results("--write" in sys.argv[2:], RESULT_FILES_AQ34, "checksums_aq34.csv",
                         "rebuild_check_results_aq34.csv"))
    sys.exit(__doc__)
