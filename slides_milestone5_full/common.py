"""Shared parts of the full Milestone 5 deck (no slide limit, then a main / appendix split).

The full deck reuses every helper of build_slides_milestone5_30.py (theme, layout blocks, charts, the Vietnamese string
table) and adds what a deck with an appendix needs:
- PLAN: the ensemble plan (reports/milestone-5/presentation/v2-full/ensemble-plan.md), one row per slide: number, title, part,
  line (main | detail);
- notes(n): the speaker notes of plan slide n, read from the full speech script (presentation/v2-full/speech-script.md);
- ref(n): how slide n is cited on another slide in the layout being built ("Slide 39" in the full order; "Slide 21"
  or "Appendix A12" in the split), so cross-references follow every reordering;
- the appendix label: in the split layout an appendix slide's section label reads "Appendix A12: <part>".

Slide modules (part1.py … part4.py) do `from slides_milestone5_full.common import *` and register their slide functions in a
dict SLIDES = {plan number: function}.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from build_slides_milestone5_30 import *                  # noqa: E402,F401,F403  helpers, kit, T, I, PT, colours …
import build_slides_milestone5_30 as base                 # noqa: E402

PRES = ROOT / "reports" / "milestone-5" / "presentation" / "v2-full"
PLAN_FILE = PRES / "ensemble-plan.md"
SCRIPT_FILE = PRES / "speech-script.md"

# Section labels by plan number (the kicker on each slide); K is filled per language by base.kickers().
PART_OF = [(1, "intro"), (6, "p1"), (22, "p2"), (39, "p3"), (47, "p4"), (59, "p5"), (78, "p6"), (91, "end")]


def part_key(n):
    key = PART_OF[0][1]
    for first, k in PART_OF:
        if n >= first:
            key = k
    return key


def kicker(n):
    """The section label of plan slide n in the current language."""
    return base.K[part_key(n)]


def _plan():
    rows = {}
    for line in PLAN_FILE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(main|detail)\s*\|", line)
        if m:
            rows[int(m.group(1))] = {"title": m.group(2), "part": m.group(3), "line": m.group(6)}
    return rows


PLAN = _plan()


def _notes():
    """Notes from the assembled script, or, while it is being written, from its range files in script-parts/."""
    files = [SCRIPT_FILE] if SCRIPT_FILE.exists() else sorted((PRES / "script-parts").glob("part*.md"))
    text = "\n".join(f.read_text(encoding="utf-8") for f in files)
    out = {}
    for block in re.split(r"(?m)^## Slide ", text)[1:]:
        m = re.match(r"(\d+)", block)
        if not m:
            continue
        nm = re.search(r"\*\*Speaker notes:\*\*\s*(.*?)(?=\n\*\*Sources:\*\*|\n## |\Z)", block, re.S)
        if nm:
            out[int(m.group(1))] = " ".join(nm.group(1).split())
    return out


NOTES_FULL = _notes()


def spoken_mark(words):
    """The spoken-time mark check_slides adds up, in the language being built: (~N seconds) or (~N giây)."""
    unit = "giây" if kit.LANG == "vi" else "seconds"
    return f"(~{round(words / 125 * 60)} {unit}) "


def num(s):
    """A number written in English form ("2,868", "41.5%") in the form of the language being built."""
    return s if kit.LANG == "en" else s.replace(",", "\0").replace(".", ",").replace("\0", ".")


def notes(n):
    """Speaker notes of plan slide n (English; the Vietnamese deck is built after the slide count is fixed), opened by
    the spoken-time mark that check_slides adds up: (~N seconds) at 125 words a minute."""
    text_ = NOTES_FULL.get(n, "")
    if not text_:
        return ""
    return spoken_mark(len(text_.split())) + T(text_)


# ----------------------------------------------------------------------------- layout state
STATE = {"labels": {}, "current": None}       # labels: plan number -> "Slide 12" | "Appendix A3"


def ref(n):
    """How plan slide n is cited from another slide in the layout being built."""
    return STATE["labels"].get(n, f"Slide {n}")


_base_kit_base = kit.base


def _base_with_label(prs, kick, title, notes_, presenter=None):
    label = STATE["labels"].get(STATE["current"], "")
    if label.startswith(("Appendix", T("Appendix"))):
        kick = f"{T('Appendix')} {label.split()[-1]}: {kick}"
    return _base_kit_base(prs, kick, title, notes_, presenter)


kit.base = _base_with_label


def placeholder(n):
    """A stand-in for a plan slide whose function is not written yet, so partial builds run."""
    def make(prs):
        s = kit.base(prs, kicker(n), T(PLAN[n]["title"]), notes(n))
        text(s, MX, I(1.3), CW, I(0.5), f"[slide {n} not built yet]", size=PT["body"], color=MINUS)
    return make
