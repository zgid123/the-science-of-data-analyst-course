"""Check the markdown sources of a report against the house formatting rules and pandoc's parsing rules.

Usage: python .claude/skills/build-report/scripts/check_format.py --report DIR   (every *.md, all languages)

ERROR  house style: an em dash "—" (use the en dash "–"); an ordered list written "1." (use "(1)").
ERROR  pandoc traps, each of which silently changes the Word output:
       a heading, list or table that does not follow a blank line (pandoc reads it as part of the paragraph above);
       an image that does not stand alone between blank lines (it loses its figure caption);
       a table without its separator row, or with rows of different column counts (cells shift or merge);
       an unclosed code fence or display formula (the rest of the file turns into code or math).
WARN   a line with an odd number of "**" (bold that never closes); trailing double space (hard line break); a bulleted
       list item "- " or "* " (the house style numbers every list "(1)", "(2)" …); a display formula wider than a
       portrait text column (estimated from its TeX: fractions count their wider part, text its letters).
Code blocks and inline code are ignored. The build applies the house style through report_format.lua as well,
so these checks keep the markdown sources themselves consistent. Exit code 1 when any ERROR is found.
"""

import argparse
import re
import sys

from common import ROOT, text_lines

NUMBERED = re.compile(r"^\s{0,3}\d+\.\s+\S")
LIST_ITEM = re.compile(r"^\s{0,3}(?:[-*+]|\(\d+\)|\d+\.)\s+\S")
SEPARATOR = re.compile(r"^\|(\s*:?-{3,}:?\s*\|)+\s*$")


MATH_WIDTH = 70        # a display formula wider than about 70 letters runs past a portrait text column in Word


def _group(s, i):
    """Return (content, end) of the {...} group starting at s[i] == '{'."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{": depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0: return s[i + 1:j], j + 1
    return s[i + 1:], len(s)

def math_width(tex):
    """Rough rendered width of a TeX formula in average-character units (a letter = 1)."""
    tex = tex.strip()
    m = re.search(r"\\begin\{(cases|aligned|array|matrix|pmatrix|bmatrix)\}(.*?)\\end\{\1\}", tex, re.S)
    if m:
        rows = [r for r in re.split(r"\\\\", m.group(2))]
        inner = max(sum(math_width(c) for c in r.split("&")) + 2 * r.count("&") for r in rows)
        return math_width(tex[:m.start()]) + 1.5 + inner + math_width(tex[m.end():])
    w, i = 0.0, 0
    while i < len(tex):
        c = tex[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", tex[i:]); cmd = m.group(1); i += len(m.group(0))
            if cmd in ("frac", "dfrac", "tfrac"):
                a, i = _group(tex, tex.index("{", i)); b, i = _group(tex, tex.index("{", i))
                w += max(math_width(a), math_width(b)) + 0.5
            elif cmd in ("text", "mathrm", "mathbf", "mathit", "operatorname", "textbf"):
                a, i = _group(tex, tex.index("{", i)); w += len(a) * (0.9 if cmd.startswith("text") else 1)
            elif cmd in ("xrightarrow", "xleftarrow"):
                a, i = _group(tex, tex.index("{", i)); w += max(math_width(a) * 0.7, 2) + 1
            elif cmd == "qquad": w += 4
            elif cmd == "quad": w += 2
            elif cmd in (",", ";", ":", "!", " "): w += 0.3
            elif cmd in ("left", "right", "big", "Big", "bigg", "Bigg"): pass
            else: w += 1.3                                   # \sum, \delta, \cap, \cdots …
        elif c in "_^":
            i += 1
            if i < len(tex) and tex[i] == "{": a, i = _group(tex, i); w += math_width(a) * 0.65
            elif i < len(tex): w += 0.65; i += 1
        elif c in "{}": i += 1
        elif c.isspace(): i += 1
        elif c in "=+-<>,": w += 1.6; i += 1                 # operators carry spacing
        else: w += 1; i += 1
    return w


def cells(row):
    return len(re.split(r"(?<!\\)\|", row.strip().strip("|")))


def check(path):
    errors, warns = [], []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    fences = 0
    table_start = None
    prev = ""                                         # previous non-code line ("" = blank)
    for n, line, code in text_lines(text):
        if line.startswith("```"):
            fences += 1
        if code:
            prev = "code"
            continue
        clean = re.sub(r"`[^`]*`", " ", line)
        where = f"{path.name}:{n}"
        if "—" in clean:
            i = clean.find("—")
            errors.append(f"{where}: em dash '—' (use '–'): …{clean[max(0, i - 40):i + 30]}…")
        if NUMBERED.match(clean):
            errors.append(f"{where}: numbered list item '{clean.strip()[:40]}' (use '(1)', '(2)' …)")
        if re.match(r"^[-*] \S", line) and not line.startswith("**"):
            warns.append(f"{where}: bulleted list item '{clean.strip()[:40]}' (the house style numbers lists '(1)', '(2)' …)")
        if line.startswith("#") and prev.strip():
            errors.append(f"{where}: heading without a blank line before it (pandoc keeps it as paragraph text)")
        if LIST_ITEM.match(line) and prev.strip() and not LIST_ITEM.match(prev) and not prev.startswith("  "):
            errors.append(f"{where}: list starts without a blank line before it (pandoc joins it to the paragraph)")
        if line.startswith("|"):
            if table_start is None:
                table_start = n
                if prev.strip():
                    errors.append(f"{where}: table without a blank line before it (pandoc reads it as text)")
                nxt = lines[n] if n < len(lines) else ""
                if not SEPARATOR.match(nxt.strip()):
                    errors.append(f"{where}: table header without a separator row '| :---- |' below it")
                width = cells(line)
            elif cells(line) != width:
                errors.append(f"{where}: table row has {cells(line)} cells, header has {width}")
        else:
            table_start = None
        if line.startswith("!["):
            after = lines[n] if n < len(lines) else ""
            if prev.strip() or after.strip():
                errors.append(f"{where}: image not alone between blank lines (pandoc drops its figure caption)")
        if clean.count("**") % 2:
            warns.append(f"{where}: odd number of '**' (bold that never closes)")
        if line.endswith("  ") and line.strip():
            warns.append(f"{where}: trailing double space (hard line break)")
        prev = line
    if fences % 2:
        errors.append(f"{path.name}: unclosed code fence")
    if len(re.findall(r"\$\$", text)) % 2:
        errors.append(f"{path.name}: unclosed display formula '$$'")
    for m in re.finditer(r"\$\$(.+?)\$\$", text, re.S):
        w = math_width(m.group(1))
        if w > MATH_WIDTH:
            n = text.count("\n", 0, m.start()) + 1
            warns.append(f"{path.name}:{n}: display formula about {w:.0f} letters wide (over {MATH_WIDTH}) runs past "
                         "the page in Word; give each equation or each case its own '$$' line")
    return errors, warns


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True, help="report folder, relative to the project root")
    args = ap.parse_args()
    files = sorted((ROOT / args.report).glob("*.md"))
    n_err = n_warn = 0
    for f in files:
        errors, warns = check(f)
        for e in errors:
            print("ERROR " + e)
        for w in warns:
            print("WARN  " + w)
        n_err, n_warn = n_err + len(errors), n_warn + len(warns)
    print(f"\nChecked {len(files)} files in {args.report}: {n_err} errors, {n_warn} warnings")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
