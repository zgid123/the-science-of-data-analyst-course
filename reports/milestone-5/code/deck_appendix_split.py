"""Write the proposed main / appendix split of the full Milestone 5 deck as a readable table.

Usage: venv/bin/python reports/milestone-5/code/deck_appendix_split.py
Input:  the split as the deck builds it (build_slides_milestone5_full.py: SPLIT, order(), pointers()), the ensemble plan
        and the speaker notes (presentation/v2-full/ensemble-plan.md, speech-script.md), and REASON below (why each slide
        moves; edit it together with SPLIT).
Output: reports/milestone-5/presentation/v2-full/appendix-split.md (main slides with speaking time and their appendix
        pointers; appendix slides with the main slide that points to them and the reason they move).
Checks: every appendix slide has a reason; exit 1 otherwise.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import build_slides_milestone5_full as deck                 # noqa: E402
from slides_milestone5_full import common as c                # noqa: E402

WPM = 125
OUT = ROOT / "reports" / "milestone-5" / "presentation" / "v2-full" / "appendix-split.md"

REASON = {
    7: 'Regulatory detail; the stakes line on the main context slide states the caps.',
    8: 'Literature evidence; the main slides carry the timing message.',
    10: 'Interview method and themes; the stakeholder slide states the needs and that the interviews are simulated.',
    13: 'Worked check of the SMART target; the goal slide marks the values as assumptions.',
    17: 'Reading rules per level; restated on the findings slides where they apply.',
    18: 'Required AQ quality check, kept as evidence; the revision slide carries the status.',
    20: 'Change log detail; the revision slide states that every change traces to the data.',
    21: 'Question-to-decision map; the decision slides restate which questions they draw on.',
    23: 'Gate definitions; the requirements and screening slides name the gates.',
    25: 'Selection conditions; the screening slide gives the decision and its reason.',
    26: 'Provenance record; needed for reproduction, not for the story.',
    28: 'Table structure; the dataset slide states the grain and coverage.',
    29: 'Run grid; the dataset slide gives the runs per year.',
    30: 'Required data dictionary, kept as evidence.',
    32: 'Gap classes; the fit slide names the gaps and their handling.',
    34: 'Population table; each finding names its population on its own slide.',
    36: 'Medium and low issues; the main quality slide names how they are handled.',
    37: 'Coverage and representativeness; the scope condition is restated in the conclusions.',
    38: 'Sensitive fields; the fairness slide states that group attributes serve only the audit.',
    42: 'Required Preparation Decision Matrix, kept as evidence; the three-rules slide summarises it.',
    43: 'Pipeline steps; reproducibility detail.',
    44: 'Derived variables; the early-sign rule and leakage slides carry what the talk needs.',
    48: 'Required Method Selection Matrix (AQ1, AQ2); the task slide summarises the choice.',
    49: 'Required Method Selection Matrix (AQ3, AQ4); the task slide summarises the choice.',
    50: 'Selection criteria and tie-break; method rationale detail.',
    51: 'Why a ranking; the list-judging and D1 slides restate the capacity argument.',
    54: 'AQ2 criterion detail; the evaluation plan and the AQ2 result slides state it.',
    55: 'Validation design detail; the gate slide states the frozen 2013/2014 split.',
    58: 'Leakage and interpretability in evaluation; the leakage and fairness slides cover the core.',
    60: 'Frozen protocol detail of the Level 2 prototype that was not run.',
    61: 'Reading rules; the findings slides carry level and confidence.',
    67: 'Year-comparison detail; the denominator slide carries the message.',
    68: 'Group rates; descriptive context for the fairness audit.',
    70: 'AQ2 test set-up; the five-signs slide states the population, model and criterion.',
    72: 'Per-module robustness; the meaning slide states the confidence.',
    73: 'Sensitivity runs; robustness detail.',
    74: 'Activity gradient; robustness detail behind the moderate confidence.',
    82: 'Required limitation log, kept as evidence; the three-kinds slide summarises it.',
    83: 'Measurement and model limits; detail behind the limitation log.',
    85: 'University transfer step; the future-work slide names it.',
    86: 'Legal conditions; the future-work and pilot slides name the risk classification.',
    89: 'Required AI decision log, kept as evidence; the AI slide states the one rule.',
    90: 'What AI changed; detail behind the AI slide.',
}


def main():
    missing = [n for n in deck.SPLIT if n not in REASON]
    if missing:
        print(f"FAIL: appendix slides without a reason: {missing}")
        return 1
    words = {n: len(v.split()) for n, v in c.NOTES_FULL.items()}
    seq, labels = deck.order("split")
    pts = deck.pointers()
    owner = {d: m for m, ds in pts.items() for d in ds}
    main_ = [n for n in seq if n != "divider" and labels[n].startswith("Slide")]
    app = [n for n in seq if n != "divider" and labels[n].startswith("Appendix")]
    mw = sum(words[n] for n in main_)
    lines = ["# Proposed split of the full deck: main slides and appendix", "",
             "The full deck (`N04_Milestone5_Slides-Full_EN.pptx`) is the ensembled story with no slide limit. The split",
             "deck (`N04_Milestone5_Slides-Split_EN.pptx`) keeps the slides the spoken story needs in story order, closes with",
             f"the thank-you slide, then an Appendix divider with an index and the detail slides A1–A{len(app)}. Each main slide",
             "that has detail slides names them on its section-label line (\"Detail in the appendix: A12, A13\"); every",
             "cross-reference on a slide follows the layout.", "",
             "Rule of the split: a slide moves when it carries evidence a reader may want but the spoken story can point to;",
             "every part of the brief keeps at least one main slide; where the brief requires an evidence table (Data",
             "Requirement Matrix, AQ quality check, data dictionary, Preparation Decision Matrix, Method Selection Matrix,",
             "limitation log, AI decision log), the main line carries its summary and the appendix keeps the full table.", "",
             f"Main deck: {len(main_)} slides, {mw:,} words of speaker notes, about {round(mw / WPM)} minutes at {WPM} words a",
             f"minute. Appendix: {len(app)} slides. The main slide count for the talk is set by the team after review; slides",
             "cut further move to the appendix in the same way.", "",
             "## Main slides", "", "| Slide | Plan | Title | Part | About (s) | Detail in the appendix |",
             "| :- | :- | :---- | :---- | -: | :---- |"]
    for n in main_:
        det = ", ".join(labels[d].split()[-1] for d in pts.get(n, []))
        lines.append(f"| {labels[n].split()[-1]} | {n} | {c.PLAN[n]['title']} | {c.PLAN[n]['part']} | "
                     f"{round(words[n] / WPM * 60)} | {det} |")
    lines += ["", "## Appendix slides", "", "| Appendix | Plan | Title | Pointed to from | Why it moves |",
              "| :- | :- | :---- | :---- | :---- |"]
    for n in app:
        lines.append(f"| {labels[n].split()[-1]} | {n} | {c.PLAN[n]['title']} | {labels[owner[n]]} | {REASON[n]} |")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"PASS: {len(main_)} main and {len(app)} appendix slides → {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
