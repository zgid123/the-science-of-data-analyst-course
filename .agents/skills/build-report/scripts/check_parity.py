"""Check that every target-language twin mirrors its source file and follows the language's conventions.

Usage: python .claude/skills/build-report/scripts/check_parity.py --report DIR --lang CODE [FILE ...]
       (FILE: source-language section files to check; default: all of them)

ERROR  structure that breaks the shared layout, numbering or evidence: missing twin; heading levels or numbers;
       table shapes; image paths and attributes; footnote labels; code blocks; display and inline math (identical);
       list item counts; citation sequence ([n] or [Sxxx]: same numbers in the same order); em dash "—"; ordered
       lists written "1."; the pack's conventions (decimal style, glossary variants; see lang_rules.py).
WARN   a figure caption that does not start with the pack's figure word; the pack's style warnings; source-language
       references ("Figure 2.1"); lines that read as untranslated source text outside quotations; on the terms page
       ([translation] terms_page), a term cell that does not open with the source term, as "Acquirer – <target term>".
Pages listed in the pack's [translation] extra_files exist only in the target language and are skipped.
Exit code 1 when any ERROR is found.
"""

import argparse
import fnmatch
import re
import sys
from pathlib import Path

import glossary
from common import ROOT, is_extra, language_packs, section_files, source_language, task_for_report, twin
from lang_rules import DISPLAY_MATH, INLINE_MATH, Rules

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
NUMBER = re.compile(r"^((?:\d+\.)+|[IVX]+\.|\w+ [IVX]+\b)")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)(\{[^}]*\})?")
FOOTNOTE = re.compile(r"\[\^([^\]]+)\]")
CITATION = re.compile(r"\[((?:\d+|S\d{3})(?:\s*[,;–-]\s*(?:\d+|S\d{3}))*)\](?!\()")
LIST_ITEM = re.compile(r"^\s{0,3}(?:[-*+]|\(\d+\)|\d+\.)\s+\S")
NUMBERED_DOT = re.compile(r"^\s{0,3}\d+\.\s+\S")
CODE_SPAN = re.compile(r"`[^`]*`")


def strip_code(text):
    in_code = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            yield n, line


def blocks(text):
    """Structural facts of a markdown file, comparable across languages."""
    heads, tables, images, notes, lists, code = [], [], [], [], 0, text.count("\n```") + text.startswith("```")
    table = []
    for _, line in list(strip_code(text)) + [(0, "")]:
        if line.startswith("|"):
            table.append(line.count("|") - 1)
            continue
        if table:
            tables.append((len(table), max(table)))
            table = []
        m = HEADING.match(line)
        if m:
            num = re.match(r"^((?:\d+\.)+|[IVX]+\.)", m.group(2)) or re.search(r"\b([IVX]+)\b(?= –)", m.group(2))
            heads.append((len(m.group(1)), num.group(1) if num else ""))
        images += [(path, attrs or "") for _, path, attrs in IMAGE.findall(line)]
        notes += FOOTNOTE.findall(line)
        if LIST_ITEM.match(line):
            lists += 1
    body = "\n".join(line for _, line in strip_code(text))
    math = [re.sub(r"\s+", " ", m) for m in DISPLAY_MATH.findall(body)]
    math += INLINE_MATH.findall(DISPLAY_MATH.sub(" ", body))
    cites = [c for m in CITATION.finditer(IMAGE.sub(" ", body)) for c in re.split(r"\s*[,;]\s*", m.group(1))]
    return dict(heads=heads, tables=tables, images=images, notes=sorted(notes), code=code, math=math,
                lists=lists, cites=cites)


def first_cells(text):
    """First cell of every body row of the first table, and the table's column count."""
    rows = [x for x in text.splitlines() if x.startswith("|")]
    body = [r for r in rows[1:] if not re.match(r"^\|(\s*:?-{3,}:?\s*\|)+$", r)]
    cells = [r.strip("|").split("|")[0].replace("**", "").strip() for r in body]
    return cells, (rows[0].count("|") - 1 if rows else 0)


def check_terms_page(src_text, tgt_text):
    """The terms page lists terms in the source language's order, so each target cell opens with the source term
    and then names it in the target language: "Acquirer – Tổ chức thanh toán thẻ" (lessons F2)."""
    warns = []
    (a, cols), (b, _) = first_cells(src_text), first_cells(tgt_text)
    for n, (term, cell) in enumerate(zip(a, b), 1):
        if not cell.lower().startswith(term.lower()):
            warns.append(f"terms page row {n}: open with the source term, as '{term} – {cell[:40]}'")
        elif cell == term and cols == 2:
            warns.append(f"terms page row {n}: add the target-language name, as '{term} – …'")
    return warns


def check_pair(src: Path, tgt: Path, pack: dict, rules: Rules):
    errors, warns = [], []
    if not tgt.exists():
        return [f"missing translation {tgt.name}"], []
    a, b = blocks(src.read_text(encoding="utf-8")), blocks(tgt.read_text(encoding="utf-8"))
    if [h[0] for h in a["heads"]] != [h[0] for h in b["heads"]]:
        errors.append(f"heading levels differ: source={[h[0] for h in a['heads']]} target={[h[0] for h in b['heads']]}")
    for (_, na), (_, nb) in zip(a["heads"], b["heads"]):
        if na != nb:
            errors.append(f"heading number differs: source='{na}' target='{nb}'")
    for key, label in (("tables", "table shapes (rows, columns)"), ("images", "image paths or attributes"),
                       ("notes", "footnote labels"), ("code", "code fence count"), ("lists", "list item count")):
        if a[key] != b[key]:
            errors.append(f"{label} differ: source={a[key]} target={b[key]}")
    if a["math"] != b["math"]:
        diff = [m for m in a["math"] if m not in b["math"]] or [m for m in b["math"] if m not in a["math"]]
        errors.append(f"math differs (must be identical): {len(a['math'])} vs {len(b['math'])} formulas; "
                      f"first difference: {diff[0][:60] if diff else 'order'}")
    if a["cites"] != b["cites"]:
        missing = [c for c in a["cites"] if c not in b["cites"]]
        extra = [c for c in b["cites"] if c not in a["cites"]]
        errors.append(f"citation sequence differs: source has {len(a['cites'])}, target has {len(b['cites'])}"
                      + (f"; missing {sorted(set(missing))}" if missing else "")
                      + (f"; extra {sorted(set(extra))}" if extra else "")
                      + ("; same set, different order" if not missing and not extra else ""))

    text = tgt.read_text(encoding="utf-8")
    terms_page = pack.get("translation", {}).get("terms_page")
    if terms_page and fnmatch.fnmatch(src.name, terms_page):
        warns += check_terms_page(src.read_text(encoding="utf-8"), text)
    fig_word = pack["figure"][0]
    for m in IMAGE.finditer(text):
        if m.group(1) and not m.group(1).startswith((fig_word, "Logo")):
            warns.append(f"figure caption should start with '{fig_word}': '{m.group(1)[:50]}'")
    is_refs = re.search(r"^# (" + "|".join(map(re.escape, pack["references"])) + ")", text, re.M) is not None
    for n, line in strip_code(text):
        if not line.strip():
            continue
        line = CODE_SPAN.sub(" ", IMAGE.sub(lambda m: m.group(1), line))
        if "—" in line:
            errors.append(f"line {n}: em dash '—' (use '–')")
        if NUMBERED_DOT.match(line):
            errors.append(f"line {n}: ordered list written '1.' (use '(1)')")
        if re.match(r"^\[\d+\]\s", line) or is_refs:
            continue                                        # reference entries keep their original titles
        e, w = rules.check(line, heading=line.startswith("#"))
        errors += [f"line {n}: {x}" for x in e]
        warns += [f"line {n}: {x}" for x in w]
    return errors, warns


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="source-language section files to check (default: all)")
    ap.add_argument("--report", required=True)
    ap.add_argument("--lang", required=True, help="target language pack code")
    args = ap.parse_args()
    packs = language_packs()
    pack, source = packs[args.lang], packs[source_language(packs)]
    report = (ROOT / args.report).resolve()
    rules = Rules(pack, source, glossary.for_task(pack, task_for_report(report)))
    sources = [Path(f).resolve() for f in args.files] or section_files(report, source, packs)
    n_err = n_warn = 0
    for src in sources:
        tgt = twin(src, pack)
        errors, warns = check_pair(src, tgt, pack, rules)
        for e in errors:
            print(f"ERROR {src.name}: {e}")
        for w in warns:
            print(f"WARN  {tgt.name}: {w}")
        n_err, n_warn = n_err + len(errors), n_warn + len(warns)
    extras = [p.name for p in section_files(report, pack, packs) if is_extra(p.name, pack)]
    print(f"\nChecked {len(sources)} pairs ({args.lang}): {n_err} errors, {n_warn} warnings"
          + (f"; {len(extras)} {pack['name']}-only pages skipped" if extras else ""))
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
