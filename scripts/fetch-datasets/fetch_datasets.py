"""Download, extract, derive and verify the project's education datasets into datasets/.

Analysis focus: OULAD. The final project's deep-dive analysis uses OULAD, so a run without
dataset names fetches only the focus dataset(s) marked in datasets.toml. The six other
datasets come from the screening stage and are fetched with --all or by name.

Sources, target folders and expected files are in datasets.toml next to this script.
Every step is idempotent: finished downloads, extractions and derived files are kept,
interrupted downloads resume, and a final inventory checks every dataset.

Usage (from the repository root):
  venv/bin/python scripts/fetch-datasets/fetch_datasets.py               # OULAD (analysis focus)
  venv/bin/python scripts/fetch-datasets/fetch_datasets.py fff ednet     # named datasets
  venv/bin/python scripts/fetch-datasets/fetch_datasets.py --all         # all seven
  venv/bin/python scripts/fetch-datasets/fetch_datasets.py --verify      # inventory of the selection
Options: --root DIR (default datasets/ at the repository root), --workers N (parallel
range requests per large file, default 8), --force (re-download and re-derive).
Exit code 0 when every selected dataset passes its checks, 1 otherwise.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import ssl
import subprocess
import sys
import time
import tomllib
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "datasets.toml"
REPO = HERE.parents[1]
DEFAULT_ROOT = REPO / "datasets"
# earlier code and saved evidence in final-project/ read final-project/datasets/...
LEGACY_LINKS = [REPO / "final-project" / "datasets"]
UA = {"User-Agent": "Mozilla/5.0 (dataset fetcher for MTH045 final project)"}
PARALLEL_MIN_BYTES = 20 * 1024 * 1024  # split files larger than this into range requests
CHUNK = 1024 * 1024


def ssl_context() -> ssl.SSLContext:
    """CA certificates that work on any machine.

    python.org builds on macOS ship without a CA store until "Install
    Certificates.command" is run; fall back to certifi or the system bundle.
    """
    try:
        import certifi  # type: ignore

        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        ctx = ssl.create_default_context()
        if not ctx.cert_store_stats()["x509_ca"]:
            for bundle in ("/etc/ssl/cert.pem", "/etc/ssl/certs/ca-certificates.crt"):
                if Path(bundle).exists():
                    ctx.load_verify_locations(bundle)
                    break
        return ctx


SSL = ssl_context()


def log(msg: str) -> None:
    print(msg, flush=True)


def human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(CHUNK), b""):
            h.update(block)
    return h.hexdigest()


# ---------------------------------------------------------------- download


def probe(url: str) -> tuple[str, int | None, bool]:
    """Final URL after redirects, total size, and whether byte ranges work.

    Uses a 1-byte ranged GET because some hosts (figshare) reject HEAD.
    """
    req = urllib.request.Request(url, headers={**UA, "Range": "bytes=0-0"})
    with urllib.request.urlopen(req, timeout=60, context=SSL) as r:
        final = r.geturl()
        if r.status == 206 and "/" in (r.headers.get("Content-Range") or ""):
            return final, int(r.headers["Content-Range"].rsplit("/", 1)[1]), True
        length = r.headers.get("Content-Length")
        return final, int(length) if length else None, False


def fetch_range(url: str, start: int, end: int, dest: Path, retries: int = 5) -> None:
    """Download bytes [start, end] into dest, resuming from what dest already holds."""
    want = end - start + 1
    for attempt in range(retries):
        have = dest.stat().st_size if dest.exists() else 0
        if have >= want:
            return
        req = urllib.request.Request(url, headers={**UA, "Range": f"bytes={start + have}-{end}"})
        try:
            with urllib.request.urlopen(req, timeout=120, context=SSL) as r, dest.open("ab") as f:
                shutil.copyfileobj(r, f, CHUNK)
        except OSError as e:
            if attempt == retries - 1:
                raise
            log(f"    retry {attempt + 1}/{retries} for bytes {start}-{end}: {e}")
            time.sleep(2 * (attempt + 1))


def download(url: str, dest: Path, workers: int) -> None:
    """Resumable download; large files with range support go through parallel parts."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    final, size, ranges = probe(url)
    if size and ranges and size >= PARALLEL_MIN_BYTES and workers > 1:
        step = -(-size // workers)
        parts = [(i, i * step, min(size, (i + 1) * step) - 1) for i in range(workers) if i * step < size]
        log(f"    {human(size)} in {len(parts)} parallel parts")
        with ThreadPoolExecutor(len(parts)) as pool:
            futures = [pool.submit(fetch_range, final, a, b, dest.with_name(f"{dest.name}.part{i}")) for i, a, b in parts]
            for fut in futures:
                fut.result()
        tmp = dest.with_name(dest.name + ".part")
        with tmp.open("wb") as out:
            for i, _, _ in parts:
                piece = dest.with_name(f"{dest.name}.part{i}")
                with piece.open("rb") as f:
                    shutil.copyfileobj(f, out, CHUNK)
                piece.unlink()
    else:
        tmp = dest.with_name(dest.name + ".part")
        if ranges and size:
            log(f"    {human(size)} single stream (resumable)")
            fetch_range(final, 0, size - 1, tmp)
        else:
            log(f"    single stream{' ' + human(size) if size else ''}")
            req = urllib.request.Request(final, headers=UA)
            with urllib.request.urlopen(req, timeout=120, context=SSL) as r, tmp.open("wb") as f:
                shutil.copyfileobj(r, f, CHUNK)
    if size and tmp.stat().st_size != size:
        raise IOError(f"{dest.name}: got {tmp.stat().st_size} bytes, expected {size}")
    tmp.replace(dest)


def download_gdrive(file_id: str, dest: Path) -> None:
    try:
        import gdown  # type: ignore
    except ImportError:
        sys.exit("EdNet is on Google Drive and needs gdown: venv/bin/pip install -r "
                 f"{HERE.relative_to(Path.cwd()) if HERE.is_relative_to(Path.cwd()) else HERE}/requirements.txt")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + ".part")
    if not gdown.download(id=file_id, output=str(tmp), quiet=False, resume=True):
        raise IOError(f"Google Drive download failed for {file_id}")
    tmp.replace(dest)


def fetch_file(spec: dict, folder: Path, workers: int, force: bool) -> Path:
    dest = folder / spec["save_as"]
    if dest.exists() and not force:
        if spec.get("sha256") and sha256(dest) != spec["sha256"]:
            log(f"  {spec['save_as']}: checksum mismatch, downloading again")
        else:
            log(f"  {spec['save_as']}: present, skipped")
            return dest
    log(f"  {spec['save_as']}: downloading")
    if "gdrive_id" in spec:
        download_gdrive(spec["gdrive_id"], dest)
    else:
        download(spec["url"], dest, workers)
    if spec.get("bytes") and dest.stat().st_size != spec["bytes"]:
        raise IOError(f"{dest.name}: {dest.stat().st_size} bytes, expected {spec['bytes']}")
    if spec.get("sha256") and sha256(dest) != spec["sha256"]:
        raise IOError(f"{dest.name}: SHA-256 differs from the pinned value")
    return dest


def extract(archive: Path, target: Path, force: bool) -> None:
    """Unzip next to the archive (the archive is kept as raw evidence).

    A marker file records a completed extraction so reruns skip it.
    """
    marker = target / f".{archive.name}.extracted"
    if marker.exists() and not force:
        log(f"  {archive.name}: already extracted")
        return
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        bad = z.testzip()
        if bad:
            raise IOError(f"{archive.name}: corrupt member {bad}")
        members = [m for m in z.infolist() if not m.filename.startswith("__MACOSX/")]
        log(f"  {archive.name}: extracting {len(members)} entries")
        z.extractall(target, members)
    marker.write_text(time.strftime("%Y-%m-%dT%H:%M:%S"))


# ------------------------------------------------------------------ derive


def _filter_csv(src: Path, dest: Path, key: str, keep: set[str]) -> int:
    """Stream src to dest keeping rows whose `key` column is in `keep`; lines are copied verbatim."""
    tmp = dest.with_name(dest.name + ".part")
    kept = 0
    with src.open(newline="", encoding="utf-8") as fin, tmp.open("w", newline="", encoding="utf-8") as fout:
        header_line = fin.readline()
        col = next(csv.reader([header_line])).index(key)
        fout.write(header_line)
        for line in fin:
            fields = line.rstrip("\r\n").split(",") if '"' not in line else next(csv.reader([line]))
            if fields[col].strip('"') in keep:
                fout.write(line)
                kept += 1
    tmp.replace(dest)
    return kept


def _column(path: Path, key: str) -> set[str]:
    with path.open(newline="", encoding="utf-8") as f:
        return {row[key] for row in csv.DictReader(f)}


def derive_fff(root: Path, folder: Path, force: bool) -> None:
    """OULAD rows of module FFF, copied line for line from the OULAD CSVs.

    Six tables are filtered on code_module == FFF; studentAssessment is filtered
    on the assessment ids of FFF (it has no code_module column).
    """
    src = root / "oulad"
    tables = ["courses", "assessments", "vle", "studentInfo", "studentRegistration", "studentVle", "studentAssessment"]
    missing = [t for t in tables if not (src / f"{t}.csv").exists()]
    if missing:
        raise IOError(f"FFF needs OULAD first; missing {missing} in {src}")
    folder.mkdir(parents=True, exist_ok=True)
    for t in tables:
        out = folder / f"{t}.csv"
        if out.exists() and not force:
            log(f"  {t}.csv: present, skipped")
            continue
        if t == "studentAssessment":
            kept = _filter_csv(src / f"{t}.csv", out, "id_assessment", _column(folder / "assessments.csv", "id_assessment"))
        else:
            kept = _filter_csv(src / f"{t}.csv", out, "code_module", {"FFF"})
        log(f"  {t}.csv: {kept:,} rows")


DERIVERS = {"fff": derive_fff}


# ------------------------------------------------------------------ verify


def count_rows(path: Path) -> int:
    with path.open("rb") as f:
        return max(0, sum(chunk.count(b"\n") for chunk in iter(lambda: f.read(CHUNK), b"")) - 1)


def verify(ds: dict, folder: Path) -> dict:
    checks = []
    for exp in ds.get("expect", []):
        matches = sorted(p for p in folder.glob(exp["path"]) if p.is_file() and p.stat().st_size > 0)
        ok, note = bool(matches), f"{len(matches)} file(s)"
        if "min_count" in exp:
            ok = len(matches) >= exp["min_count"]
            note = f"{len(matches):,} files (need ≥ {exp['min_count']:,})"
        elif matches and "sha256" in exp:
            ok = sha256(matches[0]) == exp["sha256"]
            note = "sha256 ok" if ok else "sha256 MISMATCH"
        elif matches and "rows" in exp:
            n = count_rows(matches[0])
            ok, note = n == exp["rows"], f"{n:,} rows (expected {exp['rows']:,})"
        elif not matches:
            note = "missing or empty"
        checks.append({"path": exp["path"], "ok": ok, "note": note})
    files = [p for p in folder.rglob("*") if p.is_file() and ".git" not in p.parts] if folder.exists() else []
    return {
        "dataset": ds["name"],
        "path": folder.relative_to(REPO).as_posix() if folder.is_relative_to(REPO) else str(folder),
        "focus": bool(ds.get("focus")),
        "files": len(files),
        "bytes": sum(p.stat().st_size for p in files),
        "ok": folder.exists() and all(c["ok"] for c in checks),
        "checks": checks,
    }


# -------------------------------------------------------------------- main


def run(ds: dict, root: Path, workers: int, force: bool) -> None:
    folder = root / ds["dir"]
    if ds.get("git") and not (folder / ".git").exists():
        log(f"  cloning {ds['git']}")
        subprocess.run(["git", "clone", "--depth", "1", ds["git"], str(folder)], check=True)
    if ds.get("derive"):
        DERIVERS[ds["derive"]](root, folder, force)
    for spec in ds.get("files", []):
        path = fetch_file(spec, folder, workers, force)
        if spec.get("extract"):
            extract(path, folder / spec.get("extract_to", ""), force)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("datasets", nargs="*", help="dataset names from datasets.toml (default: the analysis focus, OULAD)")
    ap.add_argument("--all", action="store_true", help="all datasets in datasets.toml")
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--verify", action="store_true", help="only check what is on disk and print the inventory")
    ap.add_argument("--force", action="store_true", help="re-download, re-extract and re-derive")
    a = ap.parse_args()

    manifest = tomllib.loads(MANIFEST.read_text(encoding="utf-8"))["dataset"]
    names = [d["name"] for d in manifest]
    unknown = set(a.datasets) - set(names)
    if unknown:
        sys.exit(f"unknown dataset(s) {sorted(unknown)}; choose from {names}")
    if a.all:
        selected = manifest
    elif a.datasets:
        selected = [d for d in manifest if d["name"] in a.datasets]
    else:
        selected = [d for d in manifest if d.get("focus")]
        others = ", ".join(d["name"] for d in manifest if not d.get("focus"))
        log(f"Analysis focus: {', '.join(d['name'] for d in selected)}. Other datasets ({others}): name them or use --all.")
    a.root.mkdir(parents=True, exist_ok=True)
    if a.root.resolve() == DEFAULT_ROOT.resolve():
        for link in LEGACY_LINKS:
            if link.parent.exists() and not link.exists() and not link.is_symlink():
                link.symlink_to(Path("..") / DEFAULT_ROOT.name)
                log(f"linked {link.relative_to(REPO)} -> ../{DEFAULT_ROOT.name}")

    errors = {}
    if not a.verify:
        for ds in selected:
            log(f"== {ds['name']}: {ds['title']}")
            try:
                run(ds, a.root, a.workers, a.force)
            except (OSError, subprocess.CalledProcessError, zipfile.BadZipFile) as e:
                errors[ds["name"]] = str(e)
                log(f"  FAILED: {e}")

    # inventory.json always describes every dataset; the printed table and exit code cover the selection
    full = {ds["name"]: verify(ds, a.root / ds["dir"]) for ds in manifest}
    report = [full[ds["name"]] for ds in selected]
    log("\nInventory")
    log(f"{'dataset':18} {'status':6} {'files':>9} {'size':>10}  path")
    focus = {d["name"] for d in manifest if d.get("focus")}
    for r in report:
        status = "PASS" if r["ok"] and r["dataset"] not in errors else "FAIL"
        tag = " (analysis focus)" if r["dataset"] in focus else ""
        log(f"{r['dataset']:18} {status:6} {r['files']:>9,} {human(r['bytes']):>10}  {r['path']}{tag}")
        for c in r["checks"]:
            if not c["ok"]:
                log(f"    ✗ {c['path']}: {c['note']}")
        if r["dataset"] in errors:
            log(f"    ✗ {errors[r['dataset']]}")
    (a.root / "inventory.json").write_text(json.dumps(list(full.values()), indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"\nwrote {a.root / 'inventory.json'}")
    sys.exit(0 if all(r["ok"] for r in report) and not errors else 1)


if __name__ == "__main__":
    main()
