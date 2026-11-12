"""Full presentation deck of team N04's Milestone 5 final project: every slide of the ensembled script (no slide
limit), in two layouts built from the same slide functions.

Usage: venv/bin/python build_slides_milestone5_full.py [--layout full|split|both] [--lang en]
  full   every slide in story order (reports/milestone-5/presentation/v2-full/ensemble-plan.md)
  split  the main slides in story order, the closing slide, then an Appendix divider with an index and the appendix
         slides (A1, A2 …); which slides go to the appendix is set in SPLIT below
Output: reports/milestone-5/build/N04_Milestone5_Slides-Full_EN.pptx and N04_Milestone5_Slides-Split_EN.pptx
(SLIDES_OUT_DIR overrides the folder). Slide functions live in slides_milestone5_full/part1.py … part4.py; plan slides
without a function yet are built as placeholders. Speaker notes come from
reports/milestone-5/presentation/v2-full/speech-script.md. The Vietnamese deck follows once the main slide count is fixed.
"""

import argparse
import importlib

from slides_milestone5_full import common
from slides_milestone5_full.common import (END, I, NAVY, PLAN, PT, STATE, T, W, H, WHITE, base, kit, placeholder, rect,
                                  rich, text)

PARTS = ["slides_milestone5_full.part1", "slides_milestone5_full.part2", "slides_milestone5_full.part3", "slides_milestone5_full.part4"]
CLOSING = 94                                      # the thank-you slide closes the main deck, before the appendix

# Proposed split: plan slides that move to the appendix. Starts from the plan's "detail" line; edited after reading
# the full deck (each move and its reason is recorded in the ledger).
SPLIT = sorted(n for n, r in PLAN.items() if r["line"] == "detail")


# Detail slides belong to the main slide before them in story order (overrides: a detail slide that prepares the
# next main slide). In the split layout each main slide names its detail slides on the section-label line.
OWNER_OVERRIDE = {61: 62, 70: 71}


def pointers():
    """{main plan slide: [detail plan slides it points to]} for the split layout."""
    out, owner = {}, None
    for n in sorted(PLAN):
        if n not in SPLIT:
            owner = n
            continue
        out.setdefault(OWNER_OVERRIDE.get(n, owner), []).append(n)
    return out


def pointer_line(s, details):
    """'Detail in the appendix: A3, A4' at the right end of the section-label line, left of the slide number."""
    from slides_milestone5_full.common import GREY, PP_ALIGN, MX
    label = T("Detail in the appendix: ") + ", ".join(STATE["labels"][d].split()[-1] for d in details)
    text(s, W - MX - I(6.2), I(0.14), I(5.0), I(0.28), label, size=PT["kicker"], color=GREY, bold=True,
         align=PP_ALIGN.RIGHT)


def functions():
    fns = {}
    for name in PARTS:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError as e:
            if e.name != name:
                raise
            continue
        fns.update(getattr(mod, "SLIDES", {}))
    return {n: fns.get(n) or placeholder(n) for n in PLAN}


def order(layout):
    """(plan numbers in deck order, labels) for the layout."""
    if layout == "full":
        seq = sorted(PLAN)
        return seq, {n: f"Slide {i}" for i, n in enumerate(seq, 1)}
    main = [n for n in sorted(PLAN) if n not in SPLIT and n != CLOSING] + [CLOSING]
    labels = {n: f"Slide {i}" for i, n in enumerate(main, 1)}
    labels.update({n: f"Appendix A{k}" for k, n in enumerate(SPLIT, 1)})
    return main + ["divider"] + SPLIT, labels


def divider(prs):
    """The appendix divider: a navy title and the index of appendix slides with their titles."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, fill=NAVY)
    text(s, I(0.7), I(0.6), W - I(1.4), I(0.8), T("Appendix"), size=PT["cover"], color=WHITE, bold=True,
         spacing=1.0)
    text(s, I(0.7), I(1.35), W - I(1.4), I(0.4), T("Detail slides the talk points to; not presented."),
         size=PT["lead"], color=WHITE, spacing=1.0)
    rows = [[(f"A{k}  ", WHITE, True), (T(PLAN[n]["title"]), WHITE, False)] for k, n in enumerate(SPLIT, 1)]
    per = (len(rows) + 2) // 3
    for c in range(3):
        rich(s, 0.7 + c * 4.1, 2.0, 3.95, rows[c * per:(c + 1) * per], pt=PT["small"], color=WHITE)
    s.notes_slide.notes_text_frame.text = ""


def build(layout, lang="en"):
    fns = functions()
    seq, labels = order(layout)
    STATE["labels"] = labels

    points = pointers() if layout == "split" else {}

    def wrap(n):
        def make(prs):
            STATE["current"] = n
            (divider if n == "divider" else fns[n])(prs)
            if n in points:
                pointer_line(prs.slides[-1], points[n])
            STATE["current"] = None
        return make

    out = base.OUT_DIR / f"N04_Milestone5_Slides-{layout.capitalize()}_{lang.upper()}.pptx"
    kit.build_deck(lang, [wrap(n) for n in seq], out, base.FOOTER_EN, cache=base.CACHE, before=base.kickers)
    missing = [n for n in PLAN if fns[n].__name__ == "make" and fns[n].__qualname__.startswith("placeholder")]
    if missing:
        print(f"[{layout}] {len(missing)} plan slides are placeholders: {missing}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--layout", choices=["full", "split", "both"], default="both")
    ap.add_argument("--lang", choices=["en"], default="en")
    args = ap.parse_args()
    for layout in (["full", "split"] if args.layout == "both" else [args.layout]):
        build(layout, args.lang)
