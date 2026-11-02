"""Check the structure of a report: heading numbers, captions, cross-references, images and footnotes.

Usage: python .claude/skills/build-report/scripts/check_structure.py --report DIR [--lang CODE|all]

Each language is read in report order (front matter 00-*, numbered parts, then unnumbered back matter such as the
references and the appendices). Words come from the language pack (Figure/Hình, Section/Mục, …).
ERROR  headings: a part H1 that is not "N." in sequence; an H2+ in a part whose number does not continue its parent
       and previous sibling (1.2 → 1.3 or 1.2.1), or whose depth differs from its level; appendix H2s that are not
       "Appendix I, II, …" in sequence; numbered H3s inside an appendix that do not restart at 1.
ERROR  captions: "Figure P.n." / "Table P.n." whose P is not the current part (appendices use A, B, … in order) or
       whose n does not continue 1, 2, 3 within the part (appendix captions are A.1, A.2, … continuously across all
       appendices); a table caption not directly followed by a table.
ERROR  cross-references: "Section x.y", "Figure x.y", "Table x.y", "Part n", "Appendix I" (and lists such as
       "Sections 1.2 and 1.3", "Figures 2.1 to 2.3") that point to nothing in the report. Quotations and code are
       skipped; a reference preceded by an acronym or number ("(FATE) Part 10", "30107-3 Part 3") names another
       document and is skipped; [<task>.structure] ignore_refs in tasks.toml lists further exceptions.
ERROR  images whose file does not exist; footnote references without a definition, definitions never referenced.
WARN   a figure or table that the text never refers to.
Exit code 1 when any ERROR is found.
"""

import argparse
import re
import sys
from collections import defaultdict

from common import ROOT, language_packs, load_config, load_report, mask, roman, task_languages, tasks, text_lines

IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
FOOT_REF = re.compile(r"\[\^([^\]]+)\](?!:)")
FOOT_DEF = re.compile(r"^\[\^([^\]]+)\]:")
KINDS = {"section": r"\d+(?:\.\d+)*", "figure": r"(?:\d+|[A-Z])\.\d+", "table": r"(?:\d+|[A-Z])\.\d+",
         "part": r"\d+", "appendix": r"[IVXLC]+"}


def check_headings(rep):
    errors, part, stack, in_appendix, appendix_n, app_h3 = [], 0, [], False, 0, 0
    numbered_seen = False
    for h in rep.headings:
        where = f"{h.file}:{h.line}"
        if h.level == 1:
            if h.number:
                numbered_seen = True
                part += 1
                if h.number != str(part):
                    errors.append(f"{where}: part heading '{h.text[:40]}' should be numbered {part}.")
                stack, in_appendix = [part], False
            else:
                stack, in_appendix = [], numbered_seen and h.text in rep.pack["appendix"][1:] + rep.pack["appendix"][:1]
            continue
        if in_appendix and h.level == 2:
            appendix_n += 1
            if h.appendix != roman(appendix_n):
                errors.append(f"{where}: appendix heading '{h.text[:40]}' should be {rep.pack['appendix'][0]} "
                              f"{roman(appendix_n)}")
            app_h3 = 0
            continue
        if in_appendix and h.level >= 3 and h.number:
            if h.level == 3:
                app_h3 += 1
                if h.number != str(app_h3):
                    errors.append(f"{where}: appendix subheading '{h.text[:40]}' should be numbered {app_h3}.")
            continue
        if not stack:
            continue                                   # front matter or back matter without numbered parts
        if not h.number:
            errors.append(f"{where}: heading '{h.text[:40]}' in Part {stack[0]} has no number")
            continue
        parts = [int(x) for x in h.number.split(".")]
        if len(parts) != h.level:
            errors.append(f"{where}: heading {h.number} has depth {len(parts)} but level H{h.level}")
            continue
        parent = stack[:h.level - 1]
        expected_next = (stack[h.level - 1] + 1) if len(stack) >= h.level else 1
        if len(stack) < h.level - 1 or parts[:-1] != parent or parts[-1] != expected_next:
            want = ".".join(map(str, parent + [expected_next])) if len(stack) >= h.level - 1 else "a parent first"
            errors.append(f"{where}: heading {h.number} breaks the sequence (expected {want})")
        stack = parts
    return errors


def check_captions(rep):
    errors, counters = [], defaultdict(int)
    part = None
    events = sorted([(h.file, h.line, "h", h) for h in rep.headings] + [(c.file, c.line, "c", c) for c in rep.captions],
                    key=lambda e: ([p.name for p in rep.files].index(e[0]), e[1]))
    for _, _, kind, obj in events:
        if kind == "h":
            if obj.level == 1:
                part = obj.number or None
            elif obj.level == 2 and obj.appendix:
                part = "A"                             # appendix captions share A.1, A.2, … across appendices
            continue
        c, where = obj, f"{obj.file}:{obj.line}"
        word = rep.pack[c.kind][0]
        p, n = c.number.split(".")[0], c.number.split(".")[-1]
        if part is None or p != part:
            errors.append(f"{where}: {word} {c.number} is not in Part/Appendix {part}")
        counters[(c.kind, p)] += 1
        if int(n) != counters[(c.kind, p)]:
            errors.append(f"{where}: {word} {c.number} breaks the sequence (expected {p}.{counters[(c.kind, p)]})")
        if c.kind == "table" and not c.followed_by_table:
            errors.append(f"{where}: {word} {c.number} caption is not directly followed by a table")
    return errors


def ref_pattern(pack, kind, connectors):
    words = "|".join(map(re.escape, sorted(pack[kind], key=len, reverse=True)))
    num = KINDS[kind]
    conn = "|".join(map(re.escape, connectors))
    return re.compile(rf"(?<![\w-])(?:{words})\s+({num}(?:(?:{conn})(?:(?:{words})\s+)?{num})*)(?![\w.]*\d)")


def check_refs(rep, ignore):
    errors, warns = [], []
    targets = {
        "section": {h.number for h in rep.headings if h.number and not h.appendix},
        "part": {h.number for h in rep.headings if h.level == 1 and h.number},
        "appendix": {h.appendix for h in rep.headings if h.appendix},
        "figure": {c.number for c in rep.captions if c.kind == "figure"},
        "table": {c.number for c in rep.captions if c.kind == "table"},
    }
    cited = defaultdict(set)
    pats = {k: ref_pattern(rep.pack, k, rep.pack["connectors"]) for k in KINDS}
    for p in rep.body_files():
        for n, line, code in text_lines(p.read_text(encoding="utf-8")):
            if code or line.startswith("#"):
                continue
            own = None
            for c in rep.captions:
                if c.file == p.name and c.line == n:
                    own = (c.kind, c.number)
            text = mask(re.sub(r"\]\([^)]*\)", "]", line))
            for kind, pat in pats.items():
                for m in pat.finditer(text):
                    before = text[:m.start()].rstrip().split(" ")[-1].strip("()[],") if text[:m.start()].strip() else ""
                    if len(before) > 1 and not before.endswith((".", "!", "?", ";", ":")) \
                            and re.fullmatch(r"[A-Z0-9][A-Z0-9/.:-]*", before):
                        continue                       # "FATE Part 10", "30107-3 Part 3": another document
                                                       # ("… on CT. Table 3.1 …" ends a sentence: a reference)
                    for num in re.findall(KINDS[kind], m.group(1)):
                        if own == (kind, num):
                            continue
                        cited[kind].add(num)
                        label = f"{rep.pack[kind][0]} {num}"
                        if num not in targets[kind] and label not in ignore:
                            errors.append(f"{p.name}:{n}: '{label}' refers to nothing in the report")
    for c in rep.captions:
        if c.number not in cited[c.kind]:
            warns.append(f"{c.file}:{c.line}: {rep.pack[c.kind][0]} {c.number} is never referred to in the text")
    return errors, warns


def check_files(rep):
    errors, refs, defs = [], {}, defaultdict(list)
    for p in rep.files:
        for n, line, code in text_lines(p.read_text(encoding="utf-8")):
            if code:
                continue
            for target in IMAGE.findall(line):
                if not target.startswith(("http://", "https://")) and not (rep.folder / target).exists():
                    errors.append(f"{p.name}:{n}: image file '{target}' does not exist")
            m = FOOT_DEF.match(line)
            if m:
                defs[m.group(1)].append(f"{p.name}:{n}")
            for label in FOOT_REF.findall(mask(line, quotes=False)):
                refs.setdefault(label, f"{p.name}:{n}")
    for label, where in refs.items():
        if label not in defs:
            errors.append(f"{where}: footnote [^{label}] has no definition")
    for label, wheres in defs.items():
        if label not in refs:
            errors.append(f"{wheres[0]}: footnote [^{label}] is defined but never referenced")
        if len(wheres) > 1:
            errors.append(f"{wheres[1]}: footnote [^{label}] is defined twice (also {wheres[0]})")
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True, help="report folder, relative to the project root")
    ap.add_argument("--lang", default="all", help="language pack code, or all")
    args = ap.parse_args()
    packs = language_packs()
    folder = (ROOT / args.report).resolve()
    task = next((t for t in tasks(load_config()).values() if (ROOT / t["report"]).resolve() == folder), {})
    codes = (task_languages(task, packs) if task else list(packs)) if args.lang == "all" else [args.lang]
    ignore = set(task.get("structure", {}).get("ignore_refs", []))
    n_err = n_warn = 0
    for code in codes:
        rep = load_report(folder, packs[code], packs)
        if not rep.files:
            continue
        errors = check_headings(rep) + check_captions(rep) + check_files(rep)
        ref_err, warns = check_refs(rep, ignore)
        errors += ref_err
        n_fig = sum(c.kind == "figure" for c in rep.captions)
        print(f"===== {code.upper()}: {len(rep.files)} files, {len(rep.headings)} headings, {n_fig} figures, "
              f"{len(rep.captions) - n_fig} tables: {len(errors)} errors, {len(warns)} warnings")
        for e in errors:
            print("  ERROR " + e)
        for w in warns:
            print("  WARN  " + w)
        n_err, n_warn = n_err + len(errors), n_warn + len(warns)
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
