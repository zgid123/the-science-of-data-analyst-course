"""Renumber a finished report's citations [n] in order of first citation and rewrite its reference list to match.

Usage: python .claude/skills/build-report/scripts/renumber_refs.py --report DIR --lang CODE
                                                                               [--write] [--drop-unused] [--map FILE]

Use it after edits that move, add or remove citations in a numbered report, for example a reviewer who added new
references at the end of the list and cited them early in the text. Without --write it only prints what would change.

1. Reads the language's files in report order (the same order and citation forms as check_citations.py: [n], [n, m],
   [n–m], outside code, math and link targets) and the reference list (the file whose H1 is the pack's references
   heading, entries "[n] …").
2. Numbers the entries by first citation: the first source cited becomes [1], and so on.
3. Rewrites every citation with the new numbers (a group is sorted; three or more consecutive numbers become "a–b")
   and writes the list in the new order. Text before the first entry (heading, introduction) is kept.
4. An entry that is never cited stops the run; --drop-unused removes it from the list instead.
5. --map FILE writes the old → new table, the record a research trail needs to keep its reference map current.
Exit code 1 when a citation has no entry, when an entry is unused without --drop-unused, or on duplicate entries.
"""

from __future__ import annotations

import argparse
import re
import sys

from check_citations import CITATION, ENTRY, numbers
from common import CODE_SPAN, MATH, ROOT, language_packs, load_report, text_lines


def compress(nums: list[int]) -> str:
    nums, out, i = sorted(set(nums)), [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out += [f"{nums[i]}–{nums[j]}"] if j - i >= 2 else [str(n) for n in nums[i:j + 1]]
        i = j + 1
    return ", ".join(out)


def citations(line: str):
    """Citation matches outside inline code and math, skipping intervals such as [0, 1]."""
    masked = CODE_SPAN.sub(lambda m: " " * len(m.group(0)), MATH.sub(lambda m: " " * len(m.group(0)), line))
    return [m for m in CITATION.finditer(masked) if 0 not in numbers(m.group(1))]


def rewrite(text: str, mapping: dict[int, int]) -> str:
    out = []
    for _, line, code in text_lines(text):
        if not code:
            for m in reversed(citations(line)):
                line = line[:m.start()] + "[" + compress([mapping[k] for k in numbers(m.group(1))]) + "]" + line[m.end():]
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True)
    ap.add_argument("--lang", required=True)
    ap.add_argument("--write", action="store_true", help="apply the changes (default: report only)")
    ap.add_argument("--drop-unused", action="store_true", help="remove entries that are never cited")
    ap.add_argument("--map", help="write the old → new table to this markdown file")
    a = ap.parse_args(argv)
    packs = language_packs()
    rep = load_report((ROOT / a.report).resolve(), packs[a.lang], packs)
    if not rep.references_file:
        sys.exit(f"no reference list in {a.report} ({a.lang})")

    ref_text = rep.references_file.read_text(encoding="utf-8")
    head, entries, current = [], {}, None
    for line in ref_text.splitlines():
        m = ENTRY.match(line)
        if m:
            current = int(m.group(1))
            if current in entries:
                sys.exit(f"reference [{current}] is listed twice")
            entries[current] = [line[m.end():]]
        elif current is None:
            head.append(line)
        elif line.strip():
            entries[current].append(line)                  # an entry continued on the next line

    order, where, errors = [], {}, []
    for p in rep.files:
        if p == rep.references_file:
            continue
        for n, line, code in text_lines(p.read_text(encoding="utf-8")):
            for m in ([] if code else citations(line)):
                for k in numbers(m.group(1)):
                    if k not in entries:
                        errors.append(f"{p.name}:{n}: citation [{k}] has no entry in the reference list")
                    elif k not in where:
                        order.append(k)
                        where[k] = f"{p.name}:{n}"
    unused = [k for k in entries if k not in where]
    if unused and not a.drop_unused:
        errors.append(f"never cited: {', '.join(f'[{k}]' for k in unused)} (pass --drop-unused to remove them)")
    for e in errors:
        print("ERROR " + e)
    if errors:
        return 1

    mapping = {old: new for new, old in enumerate(order, 1)}
    moved = [(o, n) for o, n in mapping.items() if o != n]
    print(f"{len(entries)} entries, {len(order)} cited, {len(moved)} renumbered, {len(unused)} dropped"
          + ("" if a.write else " (dry run; pass --write to apply)"))
    for old, new in moved[:15]:
        print(f"  [{old}] → [{new}]  first cited {where[old]}")
    if len(moved) > 15:
        print(f"  … {len(moved) - 15} more")
    for k in unused:
        print(f"  [{k}] dropped: {entries[k][0][:70]}")

    if a.map:
        rows = [f"| {old} | {new} | {where[old]} | {entries[old][0][:80]} |" for old, new in sorted(mapping.items())]
        rows += [f"| {k} | – (dropped) | – | {entries[k][0][:80]} |" for k in unused]
        (ROOT / a.map).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / a.map).write_text("\n".join([f"# Reference renumbering of {a.report} ({a.lang})", "",
                                             "| Old | New | First cited | Entry |", "| :---- | :---- | :---- | :---- |",
                                             *rows, ""]), encoding="utf-8")
        print(f"map → {a.map}")
    if not a.write:
        return 0

    for p in rep.files:
        if p != rep.references_file:
            text = p.read_text(encoding="utf-8")
            new = rewrite(text, mapping)
            if new != text:
                p.write_text(new, encoding="utf-8")
    while head and not head[-1].strip():
        head.pop()
    body = ["\n".join([f"[{mapping[old]}] " + entries[old][0], *entries[old][1:]]) for old in order]
    rep.references_file.write_text("\n".join(head) + "\n\n" + "\n\n".join(body) + "\n", encoding="utf-8")
    print(f"written: {len(rep.files)} files checked, reference list {rep.references_file.name} rewritten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
