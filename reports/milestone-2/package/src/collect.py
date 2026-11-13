"""Collect the OULAD raw files reproducibly for the Milestone 2 Data Collection Package (brief section 9, Task 5).

Usage (from the package folder):
    python src/collect.py [--compare-mirror]

What it does, in order:
1. Takes the archive anonymisedData.zip from the figshare deposit cited by the OULAD data descriptor
   (DOI 10.6084/m9.figshare.5081998.v1, file 8606371). If the repository's dataset folder (datasets/oulad/, created
   by scripts/fetch-datasets/fetch_datasets.py) already holds an archive with the pinned SHA-256, it is hard-linked
   instead of downloaded again.
2. Verifies the archive's size and SHA-256 against the pins below, then extracts the seven CSV tables into
   package/data/raw/ without changing them, and verifies each table's SHA-256.
3. Writes package/data/metadata/raw_manifest.csv (file, bytes, SHA-256, MD5, data rows) and logs every step with a UTC
   timestamp to package/data/metadata/collection_log.txt.
4. With --compare-mirror, also downloads the archive linked from the provider's page (OU Analyse) and records
   whether its SHA-256 equals the figshare archive's.

Nothing is cleaned, filtered or converted: data/raw holds the files exactly as published.
"""
import argparse
import csv
import hashlib
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
ROOT = PKG.parents[2]
RAW = PKG / "data" / "raw"
META = PKG / "data" / "metadata"
ARCHIVE = "anonymisedData.zip"
FIGSHARE_URL = "https://ndownloader.figshare.com/files/8606371"
MIRROR_URL = "http://schools.stem.open.ac.uk/cdn/files/anonymisedData.zip"
ARCHIVE_BYTES = 46750706
ARCHIVE_SHA256 = "90dda45037939953f979072fa70a809ebe07e90ec783c408762af7698a3825ec"
TABLES = {
    "courses.csv": "4f16eee7454b15e109b0a21a0e43be820e6846ed6f9301bb7feb5ab5ad737a75",
    "assessments.csv": "8cc738fb88ad760571d6f2a23059bfee0ffcae3bcd830514c9cbd5c6d5a046f1",
    "vle.csv": "d1b28303dea802ad87b4484e1196e878e06824850b9a4fe8aa34693439fe87e9",
    "studentInfo.csv": "7e6f3e474a5eee00639d2a414a6c7e928745823c2d2c2563ca1780145f99b0d6",
    "studentRegistration.csv": "0d32676285372aaf2e7a80304e5b274b4fba24313e2ca4c04317225e1ec90170",
    "studentAssessment.csv": "fd5320786328d05af841ee7dd4b5871b9dada3b9fe9d6a3642b2f42635510a6e",
    "studentVle.csv": "52668253d876c5becbcb72185977152700cecab2942aca807fecc3dd54b937f0",
}
LOG = []


def log(msg):
    line = f"{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ}  {msg}"
    LOG.append(line)
    print(line)


def digest(path, algo):
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url, dest):
    """Download with urllib; fall back to the system curl when Python's certificate store rejects the server."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (MTH045 data collection)"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
            shutil.copyfileobj(r, f)
    except urllib.error.URLError as e:
        log(f"urllib failed ({e.reason!r}); retrying with curl")
        subprocess.run(["curl", "-fsSL", "--retry", "3", "-o", str(dest), url], check=True)


def get_archive():
    dest = RAW / ARCHIVE
    local = ROOT / "datasets" / "oulad" / ARCHIVE
    if dest.exists() and digest(dest, "sha256") == ARCHIVE_SHA256:
        log(f"archive already in data/raw with the pinned SHA-256")
        return dest
    if local.exists() and digest(local, "sha256") == ARCHIVE_SHA256:
        if dest.exists():
            dest.unlink()
        os.link(local, dest)
        log(f"archive hard-linked from {local.relative_to(ROOT)} (identical bytes, pinned SHA-256)")
    else:
        log(f"downloading {FIGSHARE_URL}")
        download(FIGSHARE_URL, dest)
    return dest


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--compare-mirror", action="store_true", help="also fetch the provider page's archive and compare")
    args = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    META.mkdir(parents=True, exist_ok=True)
    log("source: figshare deposit DOI 10.6084/m9.figshare.5081998.v1, file 8606371 (" + FIGSHARE_URL + ")")
    arc = get_archive()
    size, sha = arc.stat().st_size, digest(arc, "sha256")
    ok = size == ARCHIVE_BYTES and sha == ARCHIVE_SHA256
    log(f"archive {ARCHIVE}: {size} bytes, SHA-256 {sha} -> {'MATCH' if ok else 'MISMATCH'}")
    if not ok:
        sys.exit("archive does not match the pinned size or SHA-256")
    with zipfile.ZipFile(arc) as z:
        names = [n for n in z.namelist() if n.endswith(".csv")]
        log(f"archive members: {', '.join(sorted(names))}")
        for n in names:
            target = RAW / Path(n).name
            if not (target.exists() and digest(target, "sha256") == TABLES.get(target.name)):
                with z.open(n) as src, open(target, "wb") as out:
                    shutil.copyfileobj(src, out)
    rows, bad = [], 0
    for name, pin in TABLES.items():
        p = RAW / name
        sha = digest(p, "sha256")
        with open(p, "rb") as f:
            n = sum(1 for _ in f) - 1
        match = sha == pin
        bad += not match
        rows.append([name, p.stat().st_size, sha, digest(p, "md5"), n, "MATCH" if match else "MISMATCH"])
        log(f"{name}: {p.stat().st_size} bytes, {n} data rows, SHA-256 {'MATCH' if match else 'MISMATCH'}")
    rows.insert(0, [ARCHIVE, size, ARCHIVE_SHA256, digest(arc, "md5"), "", "MATCH"])
    with open(META / "raw_manifest.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file", "bytes", "sha256", "md5", "data_rows", "pin_check"])
        w.writerows(rows)
    if args.compare_mirror:
        tmp = RAW.parent / "mirror_anonymisedData.zip"
        try:
            log(f"downloading provider-page mirror {MIRROR_URL}")
            download(MIRROR_URL, tmp)
            msha = digest(tmp, "sha256")
            log(f"mirror archive: {tmp.stat().st_size} bytes, SHA-256 {msha} -> "
                f"{'IDENTICAL to figshare' if msha == ARCHIVE_SHA256 else 'DIFFERENT from figshare'}")
        except Exception as e:  # network failures are recorded, not fatal
            log(f"mirror download failed: {e!r}")
        finally:
            if tmp.exists():
                tmp.unlink()
    log(f"done: 1 archive + 7 tables, {7 - bad} matching their pinned SHA-256")
    (META / "collection_log.txt").write_text("\n".join(LOG) + "\n")
    if bad:
        sys.exit(f"{bad} table(s) do not match their pinned SHA-256")


if __name__ == "__main__":
    main()
