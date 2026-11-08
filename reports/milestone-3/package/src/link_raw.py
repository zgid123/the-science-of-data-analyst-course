"""Place the raw OULAD files in data/raw and prove they are the published files (brief principle "raw is immutable").

The seven CSV tables are taken, in this order, from: data/raw itself when they are already there; the Milestone 2
Data Collection Package when it sits beside this package (hard links, no copy); or the figshare archive cited by the
OULAD data descriptor (DOI 10.6084/m9.figshare.5081998.v1), downloaded and checked against its pinned SHA-256.
Every table is checked against the SHA-256 pinned in data/metadata/raw_pins.csv and made read-only. The check result
is written to data/metadata/raw_check.csv.

Usage (from the package folder): python src/link_raw.py
Exit 1 when a file is missing or its SHA-256 differs from the pin.
"""
import csv
import hashlib
import os
import shutil
import stat
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
RAW = PKG / "data" / "raw"
META = PKG / "data" / "metadata"
PINS = META / "raw_pins.csv"
M2_RAW = PKG.parents[1] / "milestone-2" / "package" / "data" / "raw"   # optional, when both packages sit side by side
ARCHIVE = "anonymisedData.zip"
FIGSHARE_URL = "https://ndownloader.figshare.com/files/8606371"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url, dest):
    """Download with urllib; fall back to the system curl when Python's certificate store rejects the server."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (MTH045 data preparation)"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
            shutil.copyfileobj(r, f)
    except urllib.error.URLError as e:
        print(f"urllib failed ({e.reason!r}); retrying with curl")
        subprocess.run(["curl", "-fsSL", "--retry", "3", "-o", str(dest), url], check=True)


def fetch_archive(pins, missing):
    """Download the figshare archive, check its pinned SHA-256 and extract the missing tables."""
    arc = RAW / ARCHIVE
    if not (arc.exists() and sha256(arc) == pins[ARCHIVE]["sha256"]):
        print(f"downloading {FIGSHARE_URL}")
        download(FIGSHARE_URL, arc)
    if sha256(arc) != pins[ARCHIVE]["sha256"]:
        sys.exit(f"{ARCHIVE} does not match its pinned SHA-256")
    with zipfile.ZipFile(arc) as z:
        for member in z.namelist():
            name = Path(member).name
            if name in missing:
                with z.open(member) as src, open(RAW / name, "wb") as out:
                    shutil.copyfileobj(src, out)
    arc.unlink()


def main():
    all_pins = {r["file"]: r for r in csv.DictReader(PINS.open())}
    pins = {k: v for k, v in all_pins.items() if k.endswith(".csv")}
    RAW.mkdir(parents=True, exist_ok=True)
    for name in pins:
        if not (RAW / name).exists() and (M2_RAW / name).exists():
            os.link(M2_RAW / name, RAW / name)
    missing = [n for n in pins if not (RAW / n).exists()]
    if missing:
        fetch_archive(all_pins, missing)
    rows, bad = [], 0
    for name, pin in pins.items():
        dst = RAW / name
        if not dst.exists():
            print(f"MISSING {name}")
            bad += 1
            continue
        digest = sha256(dst)
        state = "MATCH" if digest == pin["sha256"] else "MISMATCH"
        bad += state != "MATCH"
        dst.chmod(dst.stat().st_mode & ~(stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))
        rows.append({"file": name, "bytes": dst.stat().st_size, "sha256": digest, "pinned_sha256": pin["sha256"],
                     "data_rows_m2": pin["data_rows"], "check": state, "read_only": "yes"})
        print(f"{state} {name} {dst.stat().st_size} bytes")
    with (META / "raw_check.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows) - bad} of {len(pins)} raw tables match the pinned SHA-256 -> data/metadata/raw_check.csv")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
