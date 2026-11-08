"""Copy the Milestone 2 changes C01–C08 verbatim into the Milestone 3 Controlled Change Log.

Milestone 3 continues the Change Log of Milestone 2 (brief section 3, input "Controlled Change Log"), so its rows
C01–C08 must equal Milestone 2's Appendix V, Table A.9, cell for cell; only the "Milestone" column (2) is added.
Rows C09 onwards belong to Milestone 3 and are left as they are. The script prints every row it changes.

Usage: venv/bin/python reports/milestone-3/code/sync_change_log.py [--check]
--check only reports differences (exit 1 if any) and writes nothing.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
M2_LOG = HERE.parents[1] / "milestone-2" / "report" / "11-05-change-log.md"
M3_LOG = HERE.parent / "package" / "data" / "metadata" / "change_log.md"


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def m2_rows():
    rows = {}
    for line in M2_LOG.read_text().split("\n"):
        if line.startswith("| C0"):
            c = cells(line)
            rows[c[0]] = c[1:]
    return rows


def main():
    check = "--check" in sys.argv
    src = m2_rows()
    lines = M3_LOG.read_text().split("\n")
    changed = 0
    for i, line in enumerate(lines):
        if not line.startswith("| C0"):
            continue
        c = cells(line)
        cid = c[0]
        if int(cid[1:]) > 8:
            continue
        if cid not in src:
            sys.exit(f"{cid} is not in {M2_LOG}")
        new = "| " + " | ".join([cid, c[1]] + src[cid]) + " |"
        if new != line:
            changed += 1
            print(f"{cid}: differs from Milestone 2")
            for old_cell, new_cell in zip(c[2:], src[cid]):
                if old_cell != new_cell:
                    print(f"  old: {old_cell}\n  new: {new_cell}")
            lines[i] = new
    missing = set(src) - {cells(l)[0] for l in lines if l.startswith("| C0")}  # noqa: E501
    if missing:
        sys.exit(f"rows missing in Milestone 3: {sorted(missing)}")
    print(f"C01–C08: {len(src)} rows compared, {changed} differ")
    if check:
        sys.exit(1 if changed else 0)
    if changed:
        M3_LOG.write_text("\n".join(lines))
        print(f"wrote {M3_LOG.relative_to(HERE.parents[2])}")


if __name__ == "__main__":
    main()
