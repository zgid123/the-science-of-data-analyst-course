"""Apply reviewed text fixes, written as FIND/REPLACE blocks, to a report folder: each fix exactly once or not at all.

Usage: python .claude/skills/build-report/scripts/apply_fixes.py --report DIR --fixes FILE [FILE ...]
                                                                             [--skip ID,ID] [--write]

A fixes file (for example a drift audit or a source verification of a human review) holds blocks of the form

    ### Fix D1 – 01-01-3-attack-potential-levels.vi.md
    FIND: <exact text, unique in that file>
    REPLACE: <new text>

The heading names the fix ID (the word after "Fix", "Typo", "APA" …) and the file inside DIR. Each FIND must occur
exactly once in its file at the moment it is applied (write a line break as "\\n": it is read as one when the
literal text does not occur, so a formula such as \\nu stays intact); blocks apply in file order, so a later block may rely on an
earlier one. Without --write nothing is changed and every block is reported as it would be applied.
Exit code 1 when any block (not skipped) does not match exactly once.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from common import ROOT

BLOCK = re.compile(r"^###\s+\w+\s+(\S+)\s+[–-]\s+(\S+)[^\n]*\n(?:.*\n)*?FIND: (.*)\nREPLACE: (.*(?:\n(?!```|###|\s*$).*)*)",
                   re.M)                                 # REPLACE may run over several lines, up to a blank line or fence


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True)
    ap.add_argument("--fixes", required=True, nargs="+")
    ap.add_argument("--skip", default="", help="comma-separated fix IDs to leave out")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    skip = {s.strip() for s in a.skip.split(",") if s.strip()}
    report = ROOT / a.report
    texts: dict[Path, str] = {}
    failed = applied = 0
    for fixes in a.fixes:
        for fid, name, find, repl in BLOCK.findall((ROOT / fixes).read_text(encoding="utf-8")):
            if fid in skip:
                print(f"skip  {fid:5} {name}")
                continue
            path = report / name
            if not path.exists():
                print(f"FAIL  {fid:5} {name}: no such file")
                failed += 1
                continue
            text = texts.setdefault(path, path.read_text(encoding="utf-8"))
            if "\\n" in find and find not in text:          # "\n" stands for a line break when the text has none
                find = find.replace("\\n", "\n")
            if "\\n" in repl and "\\n" not in text:
                repl = repl.replace("\\n", "\n")
            count = text.count(find)
            if count != 1:
                print(f"FAIL  {fid:5} {name}: FIND occurs {count} times: {find[:70]}")
                failed += 1
                continue
            texts[path] = text.replace(find, repl, 1)
            applied += 1
            print(f"ok    {fid:5} {name}")
    if a.write:
        for path, text in texts.items():
            if text != path.read_text(encoding="utf-8"):
                path.write_text(text, encoding="utf-8")
    print(f"{applied} applied, {failed} failed, {len(skip)} skipped" + ("" if a.write else " (dry run; pass --write)"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
