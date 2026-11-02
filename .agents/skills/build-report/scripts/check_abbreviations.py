"""Check that every abbreviation in the report follows the first-use convention.

Usage: python .claude/skills/build-report/scripts/check_abbreviations.py --report DIR [--lang CODE|all]

For each abbreviation listed in the report's abbreviation table (front matter file 00-*abbreviations*, one file per
language), reading the body sections in report order:
  DEFINE   its first occurrence must be a definition: the full form appears beside it (within 160 characters);
  BEFORE   it must not be used anywhere before that definition (implied by the first-occurrence check);
  REPEAT   after the definition, the full form must not appear again; only the abbreviation is used.
Exceptions (by convention): headings, the reference list, front matter (00-* files), inline code, verbatim
quotations ("…" of 8 characters or more). Abbreviations that occur only in front matter or references are reported
as notes. Full forms that cannot be read from the table's second column (grouped rows such as "Q1, Q2, Q3") come
from [<task>.abbreviations.aliases.<lang>] in tasks.toml, matched by the task's report folder. Official titles that
contain a full form by name (a law such as "Luật Phòng, chống rửa tiền") are listed in [<task>.abbreviations.titles]
<lang> = [...] and do not count as a repeated full form.
With --candidates it lists, for the front-matter task, every token that looks like an abbreviation (two or more
capitals, digits or hyphens allowed) in the body text with its count and first use, marking those missing from the
table (except the names a task lists in [<task>.abbreviations] names), and every table row the body never uses. Exit code 1 when any violation is found.
"""

import argparse
import re
import sys

from common import ROOT, language_packs, load_config, load_report, mask, task_languages, tasks, text_lines

WINDOW = 160  # characters around the first occurrence searched for the full form


def load_list(rep, aliases):
    path = next((p for p in rep.files if p.name.startswith("00-") and "abbreviation" in p.name), None)
    entries = {}
    if path is None:
        return entries
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or set(cells[0]) <= set("-: ") or cells[0] in rep.pack["abbreviation_header"]:
            continue
        fulls = [f.strip() for f in re.split(r"\s+–\s+", cells[1]) if f.strip()]
        for token in (t.strip() for t in cells[0].split(",")):
            entries[token] = aliases.get(token, fulls)
    return entries


def body_lines(rep):
    """(file, line_no, text) for body text in report order: no front matter, references, headings or code."""
    for p in rep.body_files():
        for n, line, code in text_lines(p.read_text(encoding="utf-8")):
            if code or line.startswith("#"):
                continue
            yield p.name, n, mask(line.replace("$", " "))


def norm(s):
    return re.sub(r"[\s\-–]+", " ", s.lower())


def check(rep, aliases, titles=()):
    entries = load_list(rep, aliases)
    lines = list(body_lines(rep))
    if titles:                                    # official titles keep their words; blank them for the REPEAT test
        title_re = re.compile("|".join(re.escape(t) for t in titles), re.I)
        lines = [(f, n, title_re.sub(lambda m: " " * len(m.group(0)), t)) for f, n, t in lines]
    problems, notes = [], []
    for abbr, fulls in entries.items():
        pat = re.compile(r"(?<![\w-])" + re.escape(abbr.rstrip(".")) + (r"\." if abbr.endswith(".") else r"(?![\w])"))
        first = next(((i, f, n, m.start(), text) for i, (f, n, text) in enumerate(lines)
                      for m in [pat.search(text)] if m), None)
        if first is None:
            notes.append(f"{abbr}: used only in front matter or references")
            continue
        i, f, n, pos, text = first
        window = norm(text[max(0, pos - WINDOW): pos + WINDOW])
        if not any(norm(full) in window for full in fulls):
            problems.append(f"DEFINE  {abbr}: first use at {f}:{n} has no full form beside it: "
                            f"…{text[max(0, pos - 60): pos + 60].strip()}…")
        for j, (f2, n2, t2) in enumerate(lines[i:], start=i):
            for full in fulls:
                for m2 in re.finditer(re.escape(full), t2, re.I):
                    if j == i and abs(m2.start() - pos) <= WINDOW:
                        continue
                    problems.append(f"REPEAT  {abbr}: full form '{full}' again at {f2}:{n2}: "
                                    f"…{t2[max(0, m2.start() - 50): m2.end() + 40].strip()}…")
    return entries, problems, notes


TOKEN = re.compile(r"(?<![\w-])[A-Z][A-Za-z0-9+-]*[A-Z0-9][A-Za-z0-9+-]*(?![\w-])")


def candidates(rep, entries):
    """(token, count, first use) of abbreviation-like tokens in the body, and table rows never used."""
    seen = {}
    for f, n, text in body_lines(rep):
        for m in TOKEN.finditer(text):
            tok = m.group(0)
            if sum(c.isupper() for c in tok) >= 2 and not tok.isdigit():
                count, first = seen.get(tok, (0, f"{f}:{n}"))
                seen[tok] = (count + 1, first)
    unused = [a for a in entries if a.rstrip(".") not in seen and not any(a in t for t in seen)]
    return sorted(seen.items(), key=lambda kv: (-kv[1][0], kv[0])), unused


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True, help="report folder, relative to the project root")
    ap.add_argument("--lang", default="all", help="language pack code, or all (every language with section files)")
    ap.add_argument("--candidates", action="store_true", help="list abbreviation-like tokens and unused rows")
    args = ap.parse_args()
    packs = language_packs()
    folder = (ROOT / args.report).resolve()
    task = next((t for t in tasks(load_config()).values() if (ROOT / t["report"]).resolve() == folder), {})
    codes = (task_languages(task, packs) if task else list(packs)) if args.lang == "all" else [args.lang]
    failed = False
    for code in codes:
        rep = load_report(folder, packs[code], packs)
        if not rep.files:
            continue
        aliases = task.get("abbreviations", {}).get("aliases", {}).get(code, {})
        titles = task.get("abbreviations", {}).get("titles", {}).get(code, [])
        entries, problems, notes = check(rep, aliases, titles)
        if args.candidates:
            found, unused = candidates(rep, entries)
            names = set(task.get("abbreviations", {}).get("names", []))      # decided: names, not abbreviations
            missing = [(tok, c, first) for tok, (c, first) in found if tok not in entries and tok not in names]
            print(f"===== {code.upper()}: {len(found)} abbreviation-like tokens, {len(missing)} not in the table, "
                  f"{len(unused)} table rows unused")
            for tok, c, first in missing:
                print(f"  not in table  {tok:<14} {c:>4}×  first {first}")
            for a in unused:
                print(f"  unused row    {a}")
            continue
        print(f"===== {code.upper()}: {len(entries)} abbreviations, {len(problems)} violations")
        for p in problems:
            print("  " + p)
        for nt in notes:
            print("  note    " + nt)
        failed |= bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
