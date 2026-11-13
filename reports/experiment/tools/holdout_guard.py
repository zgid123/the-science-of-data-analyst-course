"""Freeze the choices of a predictive analysis before the holdout is read, and record every read.

    python holdout_guard.py freeze --record freeze.json --choices choices.json model.pkl ...
    python holdout_guard.py status --record freeze.json --access holdout-access.md

`freeze` writes the record once: UTC time, the choices (model, features, tuning values, capacities, success
criteria) and the SHA-256 of each frozen file. Repeating it with the same choices and unchanged files does nothing,
so the step can stay in `run_all.sh`. With different choices or files it stops: a second freeze is a second test,
and has to be a deliberate act (delete the record and say so in the notes).

Freeze files that do not change on a rerun: the choices, and the code that defines the model. If a fitted model
file is frozen, the fitting script must skip its work when that file exists, because a refit rarely reproduces a
file byte for byte. A shared code file that is frozen cannot be edited afterwards: put later helpers elsewhere.

In every script that reads holdout outcomes, call the guard first:

    from holdout_guard import open_holdout
    open_holdout("freeze.json", "holdout-access.md", who="05_test.py", why="score the frozen model")

It raises RuntimeError when no freeze record exists, and appends the read to the access log. The first row of
that log, set beside the freeze time, shows the order of freeze and first read. Score the holdout once: the
scoring script saves its scores and starts with `if scores_saved(path): sys.exit(0)`; reruns and added views read
the saved scores. Describing the whole population also reads holdout outcomes, so that script comes after the
freeze and calls `open_holdout` too. Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def freeze(record: str | Path, choices: dict, files: list[str | Path] = ()) -> dict:
    record = Path(record)
    hashes = {str(f): hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in files}
    if record.exists():
        old = json.loads(record.read_text())
        if old["choices"] == choices and old["files"] == hashes:
            return old                                              # a rerun of the pipeline: nothing changed, the freeze stands
        raise RuntimeError(f"{record} exists and the choices or frozen files differ from it. A new freeze is a new test: "
                           "delete the record deliberately and say so in the notes.")
    content = {"frozen_utc": now(), "choices": choices, "files": hashes}
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text(json.dumps(content, indent=2) + "\n")
    return content


def open_holdout(record: str | Path, access_log: str | Path, who: str, why: str) -> dict:
    """Allow a read of holdout outcomes only after the freeze, and log it. Returns the freeze record."""
    record, access_log = Path(record), Path(access_log)
    if not record.exists():
        raise RuntimeError(f"holdout outcomes requested by {who} before the freeze: {record} does not exist")
    content = json.loads(record.read_text())
    for name, digest in content["files"].items():
        if not Path(name).exists() or hashlib.sha256(Path(name).read_bytes()).hexdigest() != digest:
            raise RuntimeError(f"frozen file {name} is missing or has changed since the freeze")
    if not access_log.exists():
        access_log.parent.mkdir(parents=True, exist_ok=True)
        access_log.write_text("# Reads of holdout outcomes\n\n| Read (UTC) | Script | Purpose |\n| :---- | :---- | :---- |\n")
    with open(access_log, "a") as fh:
        fh.write(f"| {now()} | {who} | {why} |\n")
    return content


def scores_saved(scores: str | Path) -> bool:
    """True when the holdout was already scored. A scoring script starts with
    `if scores_saved("results/holdout_scores.csv"): sys.exit(0)` so that a rerun reads the saved scores."""
    return Path(scores).exists()


def status(record: str | Path, access_log: str | Path) -> dict:
    record, access_log = Path(record), Path(access_log)
    frozen = json.loads(record.read_text())["frozen_utc"] if record.exists() else None
    reads = []
    if access_log.exists():
        reads = [line.split("|")[1].strip() for line in access_log.read_text().splitlines() if line.startswith("| 2")]
    return {"frozen_utc": frozen, "reads": len(reads), "first_read_utc": reads[0] if reads else None,
            "order_ok": frozen is not None and (not reads or reads[0] >= frozen)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Freeze choices before a holdout is read; report the order of freeze and reads.")
    sub = parser.add_subparsers(dest="command", required=True)
    f = sub.add_parser("freeze")
    f.add_argument("--record", required=True)
    f.add_argument("--choices", required=True, help="JSON file with the frozen choices")
    f.add_argument("files", nargs="*")
    s = sub.add_parser("status")
    s.add_argument("--record", required=True)
    s.add_argument("--access", required=True)
    args = parser.parse_args(argv)
    if args.command == "freeze":
        content = freeze(args.record, json.loads(Path(args.choices).read_text()), args.files)
        print(f"frozen at {content['frozen_utc']}: {len(content['files'])} files, {len(content['choices'])} choices")
        return 0
    result = status(args.record, args.access)
    print(json.dumps(result, indent=2))
    return 0 if result["order_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
