"""15-slide Milestone 5 deck for a manager: the analytics lifecycle in 15 main slides, everything else in an appendix.

Usage: venv/bin/python build_slides_milestone5_15.py [--lang en|vi|all]
Output: reports/milestone-5/build/N04_Milestone5_Slides-15_EN.pptx and …_VI.pptx (SLIDES_OUT_DIR overrides the
folder). The Vietnamese strings, keyed by the English text, live in slides_milestone5_15_vi.py.

The main slides follow the lifecycle and the path the team took (MAIN below). They reuse the slide functions of the
full deck (slides_milestone5_full/part1.py … part4.py) and add one new slide, "What Changed Along the Way"
(slides_milestone5_15/path.py). The slide text carries the key information; the speaker notes of the 15 main slides
carry the full delivery and come from reports/milestone-5/presentation/v3-15/speech-script.md, as do the
notes of the closing slide. After the closing slide,
an Appendix index (two divider slides) lists the other slides of the full deck, in story order, with their full-deck
notes; each main slide names the appendix slides that hold its detail.
"""

import argparse
import re
from pathlib import Path

import build_slides_milestone5_full as full
from slides_milestone5_full import common
from slides_milestone5_full.common import (GREY, I, MX, NAVY, PLAN, PP_ALIGN, PT, STATE, T, W, H, WHITE, base, kit,
                                           rect, rich, text)
from slides_milestone5_15.path import PATH_ID, TITLE as PATH_TITLE, s_path

ROOT = Path(__file__).resolve().parent
DECK_TITLE = "15-slide Milestone 5 deck of team N04 for a manager: early identification of disengaging students on OULAD"
kit.use_strings("slides_milestone5_15_vi")
OUT = {"en": base.OUT_DIR / "N04_Milestone5_Slides-15_EN.pptx", "vi": base.OUT_DIR / "N04_Milestone5_Slides-15_VI.pptx"}
NOTES_FILE = ROOT / "reports" / "milestone-5" / "presentation" / "v3-15" / "speech-script.md"

# The 15 main slides in talk order (plan numbers of the full deck; PATH_ID is the new slide) and the closing slide.
MAIN = [1, 3, 12, 16, 24, 35, 40, 45, 52, 59, 64, 71, 76, PATH_ID, 93]
CLOSING = 94
APPENDIX = [n for n in sorted(PLAN) if n not in MAIN and n != CLOSING]
INDEX_PER_SLIDE = 42                               # appendix index: 3 columns of 14 rows per divider slide


def notes15():
    """{plan number: [paragraphs]} of the main slides, from the 15-slide speech script ('## Slide <k> – … [plan <n>]');
    a blank line in the script separates two paragraphs of a note."""
    out = {}
    if not NOTES_FILE.exists():
        return out
    for block in re.split(r"(?m)^## Slide ", NOTES_FILE.read_text(encoding="utf-8"))[1:]:
        m = re.search(r"\[plan (\d+)\]", block.splitlines()[0])
        nm = re.search(r"\*\*Speaker notes:\*\*\s*(.*?)(?=\n\*\*Sources:\*\*|\n## |\Z)", block, re.S)
        if m and nm:
            paras = [" ".join(p.split()) for p in re.split(r"\n\s*\n", nm.group(1))]
            out[int(m.group(1))] = [p for p in paras if p]
    return out


def timed(paras):
    """The note as the presenter reads it: the spoken time on its own line, then one paragraph per line, each
    paragraph translated on its own."""
    if not paras:
        return ""
    words = sum(len(p.split()) for p in paras)
    return "\n".join([common.spoken_mark(words).strip()] + [T(p) for p in paras])


def owners():
    """{main plan slide: [appendix plan slides]}: each appendix slide belongs to the last main slide before it in story
    order (slides before the first story slide go to it; the title slide has none)."""
    out = {}
    story_main = sorted(n for n in MAIN if n not in (PATH_ID, 1))   # the title slide carries no pointer
    for n in APPENDIX:
        before = [m for m in story_main if m < n]
        out.setdefault(before[-1] if before else story_main[0], []).append(n)
    return out


def ranges(labels):
    """['A3', 'A4', 'A5', 'A9'] -> 'A3–A5, A9'."""
    nums = sorted(int(x[1:]) for x in labels)
    parts, start = [], None
    for i, k in enumerate(nums):
        if start is None:
            start = k
        if i + 1 == len(nums) or nums[i + 1] != k + 1:
            parts.append(f"A{start}" if start == k else f"A{start}–A{k}")
            start = None
    return ", ".join(parts)


def pointer_line(s, details):
    label = T("Detail on appendix slides ") + ranges([STATE["labels"][d].split()[-1] for d in details])
    text(s, W - MX - I(6.2), I(0.14), I(5.0), I(0.28), label, size=PT["kicker"], color=GREY, bold=True,
         align=PP_ALIGN.RIGHT)


def divider(prs, chunk, first, part, parts):
    """An appendix divider: navy title and one page of the index of appendix slides."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, fill=NAVY)
    head = T("Appendix") + (f" ({part}/{parts})" if parts > 1 else "")
    text(s, I(0.7), I(0.6), W - I(1.4), I(0.8), head, size=PT["cover"], color=WHITE, bold=True, spacing=1.0)
    text(s, I(0.7), I(1.35), W - I(1.4), I(0.4), T("Detail slides the talk points to; not presented."),
         size=PT["lead"], color=WHITE, spacing=1.0)
    rows = [[(f"A{first + k}  ", WHITE, True), (T(PLAN[n]["title"]), WHITE, False)] for k, n in enumerate(chunk)]
    per = (len(rows) + 2) // 3
    for c in range(3):
        rich(s, 0.7 + c * 4.1, 2.0, 3.95, rows[c * per:(c + 1) * per], pt=PT["small"], color=WHITE)
    s.notes_slide.notes_text_frame.text = ""


def build(lang="en"):
    fns = full.functions()
    fns[PATH_ID] = None

    def set_labels():                                  # after build_deck has set the language
        base.kickers()
        labels = {n: f"{T('Slide')} {i}" for i, n in enumerate(MAIN + [CLOSING], 1)}
        labels.update({n: f"{T('Appendix')} A{k}" for k, n in enumerate(APPENDIX, 1)})
        STATE["labels"] = labels
    notes = notes15()
    points = owners()

    def main_slide(n):
        def make(prs):
            STATE["current"] = n
            if n == PATH_ID:
                s_path(prs, timed(notes.get(n, [])))
            else:
                fns[n](prs)
                if n in notes:                         # the 15-slide delivery replaces the full-deck notes
                    prs.slides[-1].notes_slide.notes_text_frame.text = timed(notes[n])
            if n in points:
                pointer_line(prs.slides[-1], points[n])
            STATE["current"] = None
        return make

    def other(n):
        def make(prs):
            STATE["current"] = n
            fns[n](prs)
            STATE["current"] = None
        return make

    chunks = [APPENDIX[i:i + INDEX_PER_SLIDE] for i in range(0, len(APPENDIX), INDEX_PER_SLIDE)]
    dividers = [(lambda prs, c=c, k=k: divider(prs, c, 1 + k * INDEX_PER_SLIDE, k + 1, len(chunks)))
                for k, c in enumerate(chunks)]
    seq = [main_slide(n) for n in MAIN + [CLOSING]] + dividers + [other(n) for n in APPENDIX]
    kit.build_deck(lang, seq, OUT[lang], base.FOOTER_EN, cache=base.CACHE, before=set_labels)
    missing = [n for n in MAIN if n != PATH_ID and n not in notes]
    if missing:
        print(f"main slides without 15-slide notes (full-deck notes used): {missing}")
    print(f"main slides: {len(MAIN)}; appendix slides: {len(APPENDIX)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", choices=["en", "vi", "all"], default="all")
    lang = ap.parse_args().lang
    for code in (["en", "vi"] if lang == "all" else [lang]):
        build(code)
