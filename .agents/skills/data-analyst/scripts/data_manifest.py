"""Pin the input files of an analysis and refuse to read one that has changed.

    python data_manifest.py write  data/*.csv -o data-manifest.json     record SHA-256, size and data rows of each file
    python data_manifest.py verify data-manifest.json                   exit 1 if a file is missing or differs

In code, read every input through the manifest so a silently replaced file stops the run:

    from data_manifest import checked
    path = checked("data/enrolments.csv", "data-manifest.json")          # returns the path, or raises ValueError

Paths in the manifest are relative to the manifest file; an input kept outside the folder is recorded with a `../` path.
Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def describe(path: Path) -> dict:
    entry = {"sha256": sha256(path), "bytes": path.stat().st_size}
    if path.suffix.lower() in {".csv", ".tsv", ".txt"}:
        with open(path, "rb") as fh:
            entry["data_rows"] = max(sum(1 for _ in fh) - 1, 0)          # lines after the header
    return entry


def write(files: list[Path], manifest: Path) -> dict:
    base = manifest.resolve().parent
    record = {
        "created_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "files": {os.path.relpath(Path(f).resolve(), base): describe(Path(f)) for f in sorted(files)},
    }
    manifest.write_text(json.dumps(record, indent=2) + "\n")
    return record


def verify(manifest: Path) -> list[str]:
    """Return one message per problem; an empty list means every file matches."""
    manifest = Path(manifest)
    record, base = json.loads(manifest.read_text()), manifest.resolve().parent
    problems = []
    for rel, entry in record["files"].items():
        path = base / rel
        if not path.exists():
            problems.append(f"{rel}: missing")
        elif sha256(path) != entry["sha256"]:
            problems.append(f"{rel}: content differs from the manifest")
    return problems


def checked(path: str | Path, manifest: str | Path) -> Path:
    """Return `path` if it is listed in the manifest and its content is unchanged; raise ValueError otherwise."""
    manifest, path = Path(manifest), Path(path)
    record, base = json.loads(manifest.read_text()), manifest.resolve().parent
    # match by the file each entry points to, as verify() does, so a path through a symlinked folder still matches
    target = path.resolve()
    rel = next((r for r in record["files"] if (base / r).resolve() == target), None)
    if rel is None:
        raise ValueError(f"{path} is not listed in {manifest}")
    if sha256(path) != record["files"][rel]["sha256"]:
        raise ValueError(f"{path} differs from the content recorded in {manifest}")
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write or verify a manifest of input files.")
    sub = parser.add_subparsers(dest="command", required=True)
    w = sub.add_parser("write")
    w.add_argument("files", nargs="+", type=Path)
    w.add_argument("-o", "--output", default=Path("data-manifest.json"), type=Path)
    v = sub.add_parser("verify")
    v.add_argument("manifest", type=Path)
    args = parser.parse_args(argv)
    if args.command == "write":
        record = write(args.files, args.output)
        print(f"{len(record['files'])} files recorded in {args.output}")
        return 0
    problems = verify(args.manifest)
    for problem in problems:
        print("FAIL", problem)
    print("RESULT:", "PASS" if not problems else f"FAIL ({len(problems)} files)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
