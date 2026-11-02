"""Check numbered citations [n] against the reference list.

Usage: python .claude/skills/build-report/scripts/check_citations.py --report DIR [--lang CODE|all]

The reference list is the section file whose H1 is a references heading of the language pack ("References",
"Tài liệu tham khảo"); its entries start with "[n] ". Citations are [n], [n, m] or [n–m] anywhere outside code,
footnote markers and link targets.
ERROR  a citation with no entry in the list; entries not numbered 1, 2, …, N without gaps or duplicates;
       an entry that is never cited (a WARN instead with [<task>.citations] unused = "warn"); with
       order = "first-citation", a first citation that is out of order ([1] must be cited first, then [2], …);
       order = "any" (default) skips that rule; with draft_ids = "<regex>" (for example "S\\d{3}"), a draft source
       ID such as [S101] still in the text. Brackets inside math and intervals such as [0, 1] are not citations.
Exit code 1 when any ERROR is found. A report without a reference list and without citations passes.
"""

import argparse
import re
import sys

from common import MATH, ROOT, language_packs, load_config, load_report, task_languages, tasks, text_lines

CITATION = re.compile(r"(?<!\])\[(\d+(?:\s*[,;–-]\s*\d+)*)\](?!\(|:\s*https?://)")
ENTRY = re.compile(r"^\[(\d+)\]\s")


def numbers(group):
    out = []
    for part in re.split(r"\s*[,;]\s*", group):
        if re.search(r"[–-]", part):
            a, b = map(int, re.split(r"\s*[–-]\s*", part))
            out += list(range(a, b + 1))
        else:
            out.append(int(part))
    return out


def check(rep, order, unused="error", draft_ids=""):
    errors, warns = [], []
    draft = re.compile(rf"\[(?:{draft_ids})(?:\s*[,;]\s*(?:{draft_ids}))*\]") if draft_ids else None
    entries = []
    if rep.references_file:
        for n, line, code in text_lines(rep.references_file.read_text(encoding="utf-8")):
            m = ENTRY.match(line)
            if m and not code:
                entries.append((int(m.group(1)), n))
    cites = []                                          # (n, file, line) in reading order
    for p in rep.files:
        if p == rep.references_file:
            continue
        for n, line, code in text_lines(p.read_text(encoding="utf-8")):
            if code:
                continue
            line = re.sub(r"`[^`]*`", " ", MATH.sub(" ", line))
            for m in (draft.finditer(line) if draft else []):
                errors.append(f"{p.name}:{n}: draft citation {m.group(0)} left in the text (finalize the references)")
            for m in CITATION.finditer(line):
                found = numbers(m.group(1))
                if 0 in found:
                    continue                            # an interval such as [0, 1], not a citation
                cites += [(k, p.name, n) for k in found]
    if not entries and not cites:
        return errors, warns, 0, 0                      # (draft citations are reported above even without a list)
    ref_name = rep.references_file.name if rep.references_file else "(no reference list)"
    nums = [k for k, _ in entries]
    defined = set(nums)
    for k, line in entries:
        if nums.count(k) > 1:
            errors.append(f"{ref_name}:{line}: reference [{k}] is listed more than once")
    if nums != list(range(1, len(nums) + 1)) and len(set(nums)) == len(nums):
        errors.append(f"{ref_name}: entries are not numbered 1 to {len(nums)} in order: {nums[:12]}…")
    for k, f, line in cites:
        if k not in defined:
            errors.append(f"{f}:{line}: citation [{k}] has no entry in the reference list")
    cited = {k for k, _, _ in cites}
    for k, line in entries:
        if k not in cited:
            (errors if unused == "error" else warns).append(f"{ref_name}:{line}: reference [{k}] is never cited")
    if order == "first-citation":
        expected = 1
        for k, f, line in cites:
            if k == expected:
                expected += 1
            elif k > expected:
                errors.append(f"{f}:{line}: [{k}] is cited before [{expected}] (order = first-citation)")
                break
    return errors, warns, len(entries), len(cited)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True, help="report folder, relative to the project root")
    ap.add_argument("--lang", default="all", help="language pack code, or all")
    args = ap.parse_args()
    packs = language_packs()
    folder = (ROOT / args.report).resolve()
    task = next((t for t in tasks(load_config()).values() if (ROOT / t["report"]).resolve() == folder), {})
    codes = (task_languages(task, packs) if task else list(packs)) if args.lang == "all" else [args.lang]
    order = task.get("citations", {}).get("order", "any")
    unused = task.get("citations", {}).get("unused", "error")
    draft_ids = task.get("citations", {}).get("draft_ids", "")
    failed = False
    for code in codes:
        rep = load_report(folder, packs[code], packs)
        if not rep.files:
            continue
        errors, warns, n_entries, n_cited = check(rep, order, unused, draft_ids)
        print(f"===== {code.upper()}: {n_entries} references, {n_cited} cited, order {order}: {len(errors)} errors, "
              f"{len(warns)} warnings")
        for e in errors:
            print("  ERROR " + e)
        for w in warns:
            print("  WARN  " + w)
        failed |= bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
