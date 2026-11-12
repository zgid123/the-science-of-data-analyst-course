"""Assemble the full speech script of the Milestone 5 deck from its four range files.

Usage: venv/bin/python reports/milestone-5/code/deck_full_script.py
Input:  reports/milestone-5/presentation/v2-full/script-parts/part1.md … part4.md (one `## Slide N` section per plan
        slide; anything before a file's first `## Slide` heading is that file's own preamble and is dropped),
        presentation/v2-full/ensemble-plan.md (titles, parts, main / detail line).
Output: reports/milestone-5/presentation/v2-full/speech-script.md (a header with the big idea, SCQA, arc, length and
        coverage, then the 94 slide sections in plan order). The full deck reads its speaker notes from this file.
Checks: every plan slide has exactly one section, in plan order; exit 1 otherwise.
"""

import re
import sys
from pathlib import Path

FULL = Path(__file__).resolve().parents[1] / "presentation" / "v2-full"
WPM = 125


def plan():
    rows = {}
    for line in (FULL / "ensemble-plan.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(main|detail)\s*\|", line)
        if m:
            rows[int(m.group(1))] = {"title": m.group(2), "part": m.group(3), "line": m.group(6)}
    return rows


def sections():
    out = []
    for f in sorted((FULL / "script-parts").glob("part*.md")):
        text = f.read_text(encoding="utf-8")
        start = text.find("## Slide ")
        out += [s.strip() for s in re.split(r"(?m)^(?=## Slide )", text[start:]) if s.strip()]
    return out


def ranges(ns):
    out, start, prev = [], ns[0], ns[0]
    for n in ns[1:] + [None]:
        if n is not None and n == prev + 1:
            prev = n
            continue
        out.append(f"{start}" if start == prev else f"{start}–{prev}")
        if n is not None:
            start = prev = n
    return ", ".join(out)


def main():
    rows, secs = plan(), sections()
    nums = [int(re.match(r"## Slide (\d+)", s).group(1)) for s in secs]
    if nums != sorted(rows):
        print(f"FAIL: sections {nums[:5]}… do not match the plan's {len(rows)} slides in order")
        return 1
    words = {}
    for n, s in zip(nums, secs):
        m = re.search(r"\*\*Speaker notes:\*\*\s*(.*?)(?=\n\*\*Sources:\*\*|\Z)", s, re.S)
        words[n] = len(m.group(1).split()) if m else 0
    main_ = [n for n in rows if rows[n]["line"] == "main"]
    total, main_w = sum(words.values()), sum(words[n] for n in main_)
    cov = {}
    for n in sorted(rows):
        cov.setdefault(rows[n]["part"], []).append(n)
    header = f"""# Speech script, full version – Early Identification of Disengaging Students in Online Courses

Team N04 · MTH045 – The Science of Data Analytics · Milestone 5 final presentation · full deck, {len(rows)} slides, no
slide limit. The main / appendix split and the final slide count follow from this version (appendix-split.md).

**Big idea (core message).** Staff notice a drifting student only after the early weeks, when help is easiest, and the
obvious sign, a missed task, comes too late for most non-completers; on two years of open course data, an early-sign
rule that also counts inactivity gives staff a factual reason beside each name now, while a better ranking and the
effect of contact still need one designed test and a randomised pilot.

**SCQA.** Situation: a Vietnamese university expanding online and blended learning holds LMS, enrolment and result
records, and withdrawal is a regulated quality measure. Complication: staff notice late, can contact only a few
students, no open Vietnamese course data exist and no dataset records a contact. Question: can records dated by week 4
tell staff, in time and within capacity, whom to contact and why, and how much can the evidence honestly claim?
Answer: in part, each claim at its own level (Slide 4).

**Arc.** Hook and answer first (1–5) → introduction, business understanding and the questions (6–21) → the data:
requirements, selection, description, fit and quality (22–38) → preparation: the add-drop rule, the early-sign rule,
the pipeline and leakage control (39–46) → method and evaluation design (47–58) → status and evidence: what we ran,
the Traceability Matrix, AQ1 and AQ2, with the turning point that missed tasks come too late (59–75) → expected AQ3
and AQ4 outputs, answers and decision support (76–80) → limitations, future work and the pilot (81–87) → generative AI
(88–90) → conclusions firmest first, open problems, take-home, thank you (91–94).

**How it was ensembled.** Three full drafts (drafts/), each written independently from drafts/BRIEF.md with no slide limit by
one storytelling method (A Storytelling with Data; B SCQA and the pyramid principle; C the data-storytelling narrative
arc), were merged by the ensemble plan (ensemble-plan.md): the union of their topics in story order, one idea per
slide, each slide built from the clearest of its source slides, and the 30-slide deck's reviewed slides reused where
they match. Four range files (script-parts/) were written from script-parts/BRIEF.md and assembled into this file by
reports/milestone-5/code/deck_full_script.py.

**Length.** Speaker notes total {total:,} words, {min(words.values())}–{max(words.values())} a slide: about
{round(total / WPM)} minutes at {WPM} words a minute for the full deck, and about {round(main_w / WPM)} minutes for the
{len(main_)} slides marked main. The slide count for the talk is set after review; slides not presented move to the
appendix of the same deck.

**Coverage of the brief's report parts** (plan part labels → slides):

| Part | Slides |
| :---- | :---- |
""" + "\n".join(f"| {k} | {ranges(v)} |" for k, v in cov.items()) + """

**Format of each slide section.** Title with part label and line (main: the story needs it; detail: evidence the talk
can point to), then Lead, On the slide, Visual, Speaker notes (spoken, opening from the previous slide and handing over
to the next) and Sources (report sections behind every number).

"""
    (FULL / "speech-script.md").write_text(header + "\n\n".join(secs) + "\n", encoding="utf-8")
    print(f"PASS: {len(secs)} slide sections, {total:,} words of notes → {FULL / 'speech-script.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
