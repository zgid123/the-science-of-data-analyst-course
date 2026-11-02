"""Show, paragraph by paragraph, what a human reviewer changed in a translated report, to learn from it.

Usage: python .claude/skills/build-report/scripts/review_diff.py --before DIR --after DIR --lang CODE
                                                                              [--files GLOB] [--out FILE]

BEFORE is the report folder as translated (for example taskN/report), AFTER the reviewed version split into the same
file names (split_export.py). For each file matching GLOB (default: every twin of the language), paragraphs are
aligned in order and every changed pair is printed with a word-level diff: [-removed-]{+added+}. Unchanged paragraphs
are counted, not printed. Tables are compared row by row, headings and figure lines as single paragraphs.

The output is the evidence for a lessons file (for Vietnamese: languages/vi/lessons.md): read the pairs, name the
recurring kinds of change, and turn each kind into a guide rule, a review checklist item, a glossary row or a check.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

from common import ROOT, language_packs


def paragraphs(text: str) -> list[str]:
    """Blank-line separated blocks; table rows become one paragraph each."""
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = block.split("\n")
        if all(x.startswith("|") for x in lines):
            out += [x for x in lines if not re.match(r"^\|(\s*:?-{3,}:?\s*\|)+$", x)]
        else:
            out.append(" ".join(x.strip() for x in lines))
    return out


def word_diff(a: str, b: str) -> str:
    wa, wb = a.split(), b.split()
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes():
        if op == "equal":
            out.append(" ".join(wa[i1:i2]))
        if op in ("delete", "replace"):
            out.append("[-" + " ".join(wa[i1:i2]) + "-]")
        if op in ("insert", "replace"):
            out.append("{+" + " ".join(wb[j1:j2]) + "+}")
    return " ".join(out)


def pair_up(pa: list[str], pb: list[str]):
    """Yield (before, after) for changed paragraphs; unchanged pairs are skipped."""
    sm = difflib.SequenceMatcher(None, pa, pb, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        left, right = pa[i1:i2], pb[j1:j2]
        for k in range(max(len(left), len(right))):            # pair in order inside a changed block
            yield (left[k] if k < len(left) else ""), (right[k] if k < len(right) else "")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--before", required=True, type=Path)
    ap.add_argument("--after", required=True, type=Path)
    ap.add_argument("--lang", required=True)
    ap.add_argument("--files", default="*")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args(argv)
    suffix = language_packs()[a.lang].get("suffix", ".md")
    before, after = ROOT / a.before, ROOT / a.after
    lines = [f"# Human review of {a.before} ({a.lang}), files {a.files}", "",
             "Each changed paragraph: before (as translated) → after (as reviewed), word diff [-removed-]{+added+}.", ""]
    changed = total = 0
    for fa in sorted(before.glob(a.files + suffix)):
        fb = after / fa.name
        if not fb.exists():
            continue
        pa, pb = paragraphs(fa.read_text(encoding="utf-8")), paragraphs(fb.read_text(encoding="utf-8"))
        pairs = list(pair_up(pa, pb))
        total += max(len(pa), len(pb))
        if not pairs:
            continue
        lines += [f"## {fa.name}", "", f"{len(pairs)} of {len(pa)} paragraphs changed", ""]
        for n, (x, y) in enumerate(pairs, 1):
            changed += 1
            lines += [f"### {fa.name} – {n}", "", "**Before:** " + (x or "–"), "", "**After:** " + (y or "–"), "",
                      "**Diff:** " + word_diff(x, y), ""]
    lines.insert(4, f"{changed} changed paragraphs of {total}.\n")
    text = "\n".join(lines)
    if a.out:
        (ROOT / a.out).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / a.out).write_text(text, encoding="utf-8")
        print(f"{changed} changed paragraphs of {total} → {a.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
