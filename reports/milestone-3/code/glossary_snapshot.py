"""Snapshot the merged Vietnamese glossary that each milestone report sees, and compare two snapshots.

A reorganisation of the glossary files (splitting a topic file, grouping rows under headings, moving general rows to
the common layer) must not change what any report is checked against. This script records, for every task in
tasks.toml that uses the Vietnamese pack, the merged rows that build-report's glossary.load returns (English term,
Vietnamese form, usage note, replaced variants), independent of the file or layer that holds them.

Usage (from the repository root):
    venv/bin/python reports/milestone-3/code/glossary_snapshot.py save BEFORE.json
    venv/bin/python reports/milestone-3/code/glossary_snapshot.py compare BEFORE.json
compare prints every row added, removed or changed per task and exits 1 if any differs.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / ".agents" / "skills" / "build-report" / "scripts"))
import glossary  # noqa: E402
from common import language_packs, load_config, tasks  # noqa: E402

TASKS = ["milestone-1", "milestone-2", "milestone-3", "milestone-4"]


def snapshot() -> dict:
    pack = language_packs()["vi"]
    all_tasks = tasks(load_config())
    out = {}
    for name in TASKS:
        rows = glossary.load(pack, glossary.names_of(all_tasks[name], "vi"))
        out[name] = sorted([r["en"].lower(), r["vi"], r["usage"], sorted(r["replaces"])] for r in rows)
    return out


def main() -> int:
    mode, path = sys.argv[1], Path(sys.argv[2])
    now = snapshot()
    if mode == "save":
        path.write_text(json.dumps(now, ensure_ascii=False, indent=1))
        print(f"saved {path}: " + ", ".join(f"{t} {len(r)} rows" for t, r in now.items()))
        return 0
    before = json.loads(path.read_text())
    differ = 0
    for t in TASKS:
        a = {json.dumps(r, ensure_ascii=False) for r in before[t]}
        b = {json.dumps(r, ensure_ascii=False) for r in now[t]}
        for r in sorted(a - b):
            print(f"{t} REMOVED/CHANGED {r}")
        for r in sorted(b - a):
            print(f"{t} ADDED/CHANGED   {r}")
        differ += len(a ^ b)
        print(f"{t}: {len(before[t])} rows before, {len(now[t])} after, {len(a ^ b)} differences")
    return 1 if differ else 0


if __name__ == "__main__":
    sys.exit(main())
