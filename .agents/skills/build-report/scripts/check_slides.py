"""Check a slide deck (.pptx) in a target language against that language's conventions.

Usage: python .claude/skills/build-report/scripts/check_slides.py DECK.pptx --lang vi

Every slide's text, table cells and speaker notes go through the pack's rules (lang_rules.py): decimal style,
glossary variants and source-language references ("Figure 2.1") are errors on slides; style warnings and lines
that read as untranslated are warnings. The em dash is an error, as in the reports. Spoken time is summed from
notes that state "~N giây" or "~N seconds". Layout is checked without rendering: every shape stays on the slide,
and every text box holds its text when wrapped with the font's metrics, with no word wider than the box (Arial by default; skipped when the font
file is absent). Exit code 1 when any ERROR is found.
"""

import argparse
import os
import re
import sys

from pptx import Presentation
from PIL import ImageFont

import glossary
from common import ROOT, language_packs, load_config, source_language, tasks
from lang_rules import Rules
from slide_measure import walk



def text_runs(p):
    """A paragraph's text runs including fields (a slide number is an a:fld), each readable as a run."""
    from pptx.oxml.ns import qn
    from pptx.text.text import _Run
    return [_Run(el, p) for el in p._p if el.tag in (qn("a:r"), qn("a:fld"))]

def slide_texts(prs):
    for n, slide in enumerate(prs.slides, 1):
        parts = []
        for shape in walk(slide.shapes):
            if shape.has_text_frame:
                parts += [("slide", p.text) for p in shape.text_frame.paragraphs if p.text.strip()]
            if shape.has_table:
                parts += [("table", c.text) for row in shape.table.rows for c in row.cells if c.text.strip()]
        notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
        parts += [("notes", line) for line in notes.splitlines() if line.strip()]
        yield n, parts


FONT_DIRS = ["/System/Library/Fonts/Supplemental", "/Library/Fonts", "/usr/share/fonts/truetype/msttcorefonts",
             "C:/Windows/Fonts"]
_fonts = {}


def font(bold, size):
    """Arial (Bold) at `size` pt in tenths, so lengths come back in tenths of a point; None when unavailable."""
    key = (bold, size)
    if key not in _fonts:
        name = "Arial Bold.ttf" if bold else "Arial.ttf"
        _fonts[key] = next((ImageFont.truetype(f"{d}/{name}", int(size * 10)) for d in FONT_DIRS
                            if os.path.exists(f"{d}/{name}")), None)
    return _fonts[key]


def text_height(frame, width_pt):
    """Height in points that the paragraphs of a text frame need when wrapped to `width_pt`; None without fonts."""
    total = 0.0
    paragraphs = frame.paragraphs
    for i, p in enumerate(paragraphs):
        runs = [r for r in text_runs(p) if r.text]
        size = max((r.font.size.pt for r in runs if r.font.size), default=18)
        if not runs:
            total += size * 1.2
            continue
        lines, line = 1, 0.0
        for r in runs:
            f = font(bool(r.font.bold), r.font.size.pt if r.font.size else size)
            if f is None:
                return None
            for word in re.split(r"(\s+)", r.text):
                w = f.getlength(word) / 10
                if line + w > width_pt and line > 0 and word.strip():
                    lines, line = lines + 1, w
                else:
                    line += w
        spacing = p.line_spacing if isinstance(p.line_spacing, float) else 1.0
        after = p.space_after.pt if p.space_after is not None and i < len(paragraphs) - 1 else 0
        total += lines * size * 1.2 * spacing + after       # the last paragraph's spacing falls outside the text
    return total


def wide_words(frame, width_pt):
    """Words wider than the box's inner width: PowerPoint breaks them across lines ("200" / "2")."""
    found = []
    for p in frame.paragraphs:
        for r in text_runs(p):
            f = font(bool(r.font.bold), r.font.size.pt if r.font.size else 18)
            if f is None:
                return []
            found += [w for w in r.text.split() if f.getlength(w) / 10 > width_pt]
    return found


def layout_issues(prs):
    """Shapes that leave the slide, and text boxes whose wrapped text is taller than the box."""
    W, H = prs.slide_width, prs.slide_height
    for n, slide in enumerate(prs.slides, 1):
        for shape in walk(slide.shapes):
            if shape.left < 0 or shape.top < 0 or shape.left + shape.width > W + 1 or shape.top + shape.height > H + 1:
                yield n, f"shape off the slide: '{(shape.text_frame.text if shape.has_text_frame else shape.name)[:50]}'"
            if not shape.has_text_frame or not shape.text_frame.text.strip():
                continue
            tf = shape.text_frame
            margins = [m.pt if m is not None else d for m, d in ((tf.margin_left, 7.2), (tf.margin_right, 7.2),
                                                                  (tf.margin_top, 3.6), (tf.margin_bottom, 3.6))]
            inner = shape.width / 12700 - margins[0] - margins[1]
            for word in wide_words(tf, inner) if tf.word_wrap is not False else []:
                yield n, f"word wider than its box, broken across lines: '{word[:30]}' in {inner:.0f} pt"
            need = text_height(tf, inner)
            room = shape.height / 12700 - margins[2] - margins[3]
            if need is not None and need > room * 1.08 + 4:
                yield n, f"text taller than its box ({need:.0f} pt in {room:.0f} pt): '{tf.text.strip()[:50]}'"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck")
    ap.add_argument("--lang", required=True)
    ap.add_argument("--task", help="task in tasks.toml, for its glossaries' variants")
    args = ap.parse_args()
    packs = language_packs()
    task = tasks(load_config()).get(args.task, {}) if args.task else {}
    rules = Rules(packs[args.lang], packs[source_language(packs)], glossary.for_task(packs[args.lang], task), scope="slides")
    prs = Presentation(str(ROOT / args.deck))
    n_err = n_warn = 0
    for n, parts in slide_texts(prs):
        for where, text in parts:
            errors, warns = rules.check(text, ref_level="error")
            if "—" in text:
                errors.append("em dash '—' (use an en dash '–')")
            if where != "notes" and text.count(" · ") >= 2:
                warns.append("keyword fragments joined with '·'; write short complete clauses")
            for e in errors:
                print(f"ERROR slide {n:2d} ({where}): {e}")
            for w in warns:
                print(f"WARN  slide {n:2d} ({where}): {w}")
            n_err, n_warn = n_err + len(errors), n_warn + len(warns)
    for n, issue in layout_issues(prs):
        print(f"WARN  slide {n:2d} (layout): {issue}")
        n_warn += 1
    seconds = sum(int(s) for slide in prs.slides if slide.has_notes_slide
                  for s in re.findall(r"~(\d+) (?:giây|seconds?)", slide.notes_slide.notes_text_frame.text))
    print(f"\nChecked {len(prs.slides)} slides: {n_err} errors, {n_warn} warnings; "
          f"spoken time ≈ {seconds // 60} min {seconds % 60:02d} s")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
