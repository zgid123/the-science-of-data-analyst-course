"""Example deck built with the slide kit: one slide per proven layout, to copy into a new deck script.

Usage: python .claude/skills/build-report/templates/deck/example_deck.py [--lang en|vi] [--out DIR]
Output: DIR/Example_EN.pptx (default DIR: build/.cache/example-deck in the project).

The content is a neutral example (a method that cleans data tables, with made-up numbers) so the layouts read as they
would in a real talk. Each slide function names its pattern; slides.md section 6 lists them. A real deck copies this
file to the project root as build_slides_taskN.py, keeps the patterns it needs and writes its own text, with the
Vietnamese strings in slides_taskN_vi.py (slides.md section 5). example_deck_vi.py shows that module's form.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import charts                                               # noqa: E402
import slidekit as kit                                       # noqa: E402
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN              # noqa: E402
from slidekit import (AGENT_FILL, CW, END, EMU, GREY, H, I, INK, LINE, MINUS,  # noqa: E402
                      MX, NAVY, OUT_FILL, PLUS, PT, SOFT, TOP, W, WARM, WHITE, D, T, arrow, bignum, cards_at, chart,
                      chip, flow_row, foot, label, lead, lh, node, path, panels, rect, side_cards, split,
                      table_at, text)

FOOTER_EN = "Example deck · built with the build-report slide kit"
K = {}
kit.use_strings("example_deck_vi")


def kickers():
    K.update(intro=T("Introduction"), method=T("Part 1 · Method"), results=T("Part 2 · Results"),
             end=T("Part 3 · Conclusions"))


# ----------------------------------------------------------------------------- opening
def s_title(prs):
    """Pattern: title slide with the authors and the context line."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    title, sub = "CleanFlow", T("Purpose-driven cleaning of data tables: an example deck")
    th, sh = lh(title, 11.8, PT["cover"], True), lh(sub, 11.8, PT["lead"])
    rect(s, I(0.7), I(0.9), I(0.9), I(0.06), fill=NAVY)
    text(s, I(0.7), I(1.1), I(11.8), I(th), title, size=PT["cover"], color=NAVY, bold=True, spacing=1.0)
    text(s, I(0.7), I(1.25 + th), I(11.8), I(sh), sub, size=PT["lead"], color=INK, spacing=1.0)
    text(s, I(0.7), I(6.15), I(11.8), I(0.4), T("Course name, Faculty, University, month year"), size=PT["small"],
         color=GREY, spacing=1.0)
    s.notes_slide.notes_text_frame.text = T("(~20 seconds) Good morning. This example deck shows the kit's layouts.")


def s_outline(prs):
    """Pattern: outline as a grid of cards (part label as head, one sentence as body)."""
    s = kit.base(prs, K["intro"], T("Presentation Outline"),
                 T("(~20 seconds) The talk has three parts: the method, the results and the conclusions."))
    cards_at(s, [(K["method"], T("How the method cleans a table, step by step.")),
                 (K["results"], T("What the method achieves against two baselines.")),
                 (K["end"], T("What the evidence shows and what remains open."))], 3, TOP / EMU + 0.2)


# ----------------------------------------------------------------------------- method
def s_pipeline(prs):
    """Pattern: lead line, a flow row of styled nodes with icons, then fact cards (a mechanism and its facts)."""
    s = kit.base(prs, K["method"], T("Pipeline"), T("(~45 seconds) A table and a question enter; agents plan, a tool "
                                                    "executes, and the cleaned table answers the question."))
    y = lead(s, T("Agents plan each step, a tool executes it, and the result answers the question"))
    flow_row(s, y, 1.9, [(T("Table and question"), None, "input", "table"),
                         (T("Plan a step"), T("an LLM agent"), "agent", "agent"),
                         (T("Execute"), T("a cleaning tool"), "system", "gear"),
                         (T("Cleaned table"), T("and its workflow"), "out", "check")])
    cards_at(s, [(T("One column at a time"), T("The agents clean the columns the question needs.")),
                 (T("A record of every step"), T("The workflow can be replayed and audited."))], 2, y + 2.3)


def s_loop(prs):
    """Pattern: a loop with a feedback arrow above the row and an exit arrow below it."""
    s = kit.base(prs, K["method"], T("The Cleaning Loop"),
                 T("(~45 seconds) After each step the column is inspected again, until nothing is left to fix."))
    y = lead(s, T("Each step is inspected again until the column passes"))
    n, gap, h = 4, 0.5, 1.5
    w = (CW / EMU - (n - 1) * gap) / n
    top = y + 0.45
    xs = [MX / EMU + k * (w + gap) for k in range(n)]
    for k, (head, body, style) in enumerate([(T("Column"), None, "input"), (T("Inspect"), T("rate four dimensions"), "agent"),
                                             (T("Operate"), T("one operation"), "agent"), (T("Tool"), T("runs it"), "system")]):
        node(s, xs[k], top, w, h, head, body, style)
        if k + 1 < n:
            arrow(s, xs[k] + w + 0.04, top + h / 2, xs[k + 1] - 0.04, top + h / 2)
    ly = top - 0.28
    path(s, [(xs[3] + w / 2, top), (xs[3] + w / 2, ly), (xs[1] + w / 2, ly), (xs[1] + w / 2, top)])
    mid = (xs[1] + xs[3] + w) / 2
    label(s, mid - 1.4, ly, 2.8, T("next pass: the updated column"))
    oy = top + h + 0.6
    path(s, [(xs[1] + w / 2, top + h), (xs[1] + w / 2, oy)])
    label(s, xs[0], top + h + 0.3, xs[2] + w - xs[0], T("all dimensions pass: the column is done"))
    node(s, xs[0], oy, xs[2] + w - xs[0], 0.55, T("Clean column"), None, "out")


# ----------------------------------------------------------------------------- results
MODELS = ["Model A", "Model B", "Model C"]
ONE_STEP, LOOP, RAW = [0.28, 0.30, 0.26], [0.52, 0.63, 0.35], 0.22


def bars(fig):
    """Grouped bars with a dashed reference line and value labels, drawn with charts.py (labels through T)."""
    ax = charts.axes(fig)
    charts.bars(ax, MODELS, {T("One step"): ONE_STEP, T("Loop"): LOOP}, ref=RAW, ref_label=T("No cleaning"),
                labels="all", limit=0.75)


def s_results(prs):
    """Pattern: a chart (charts.py) on the left of a split, reading cards on the right."""
    s = kit.base(prs, K["results"], T("Results"), T("(~50 seconds) The loop beats one-step generation for every model."))
    y = lead(s, T("The loop beats one-step generation for every model"))
    lw, rw, rx = split(0.62)
    chart(s, "example-bars", MX / EMU, y, lw, END - y - 0.3, bars)
    side_cards(s, rx, y, rw, [(T("Firm"), T("Every model gains from the loop."), PLUS),
                              (T("Caution"), T("The numbers come from small, synthetic tables."), MINUS)])
    foot(s, T("Example numbers, made up for this deck."))


def s_evidence(prs):
    """Pattern: a table, then large-number tiles that carry the headline."""
    s = kit.base(prs, K["results"], T("Strength of the Evidence"),
                 T("(~40 seconds) The gains are significant on the data; the answers depend on the model."))
    y = lead(s, T("Gains are significant on the data; answer gains depend on the model"))
    end = table_at(s, [[T("Dimension"), T("Significant gain"), T("Exceptions")],
                       [T("Data"), T("All models, at 99%"), T("none")],
                       [T("Answers"), T("Two of three models"), T("Model C")]], [0.25, 0.4, 0.35], y, size=PT["small"] + 2)
    w = (CW / EMU - 0.6) / 3
    for k, (v, b) in enumerate([(D(0.63), T("best answer score")), (D(0.79), T("best data score")),
                                (D(0.11), T("best exact match"))]):
        x = MX / EMU + k * (w + 0.3)
        rect(s, I(x), I(end + 0.4), I(w), I(1.6), fill=SOFT, line=LINE, radius=True)
        bignum(s, x, end + 0.55, w, v, b, color=WARM)


def s_matrix(prs):
    """Pattern: a small matrix of chips with a score column (a worked example of pairwise comparison)."""
    s = kit.base(prs, K["results"], T("Pairwise Comparison"),
                 T("(~40 seconds) Each candidate meets every other one; the winner of each cell earns a point."))
    y = lead(s, T("Every pair is compared; the most wins takes the question"))
    names, best = ["c1", "c2", "c3"], 1
    cs, x0, y0 = 0.7, MX / EMU + 1.0, y + 0.3
    score = [0, 0, 0]
    for j, n in enumerate(names):
        chip(s, x0 + j * cs, y0, cs - 0.05, cs - 0.05, n, bold=True)
    for i, n in enumerate(names):
        chip(s, x0 - cs, y0 + (i + 1) * cs, cs - 0.05, cs - 0.05, n, bold=True)
        for j in range(3):
            if i == j:
                continue
            win = i if i == best or (j != best and i < j) else j
            score[win] += 1
            chip(s, x0 + j * cs, y0 + (i + 1) * cs, cs - 0.05, cs - 0.05, names[win],
                 fill=OUT_FILL if win == best else AGENT_FILL, line_color=PLUS if win == best else WARM)
    for i in range(3):
        chip(s, x0 + 3 * cs + 0.2, y0 + (i + 1) * cs, 0.8, cs - 0.05, str(score[i]), bold=True)
    note_x = x0 + 3 * cs + 1.4
    side_cards(s, note_x, y, MX / EMU + CW / EMU - note_x, [(T("Both orders"), T("Each pair is compared twice."), NAVY)])


# ----------------------------------------------------------------------------- conclusions
def s_conclusions(prs):
    """Pattern: two contrasting panels."""
    s = kit.base(prs, K["end"], T("What the Evidence Shows"),
                 T("(~40 seconds) The loop helps; the size of the gain on real data is still open."))
    y = lead(s, T("The loop helps; its gain on real data is still open"))
    panels(s, y, (T("Firm"), [T("The loop beats one-step generation."), T("Every run leaves an auditable record.")], PLUS),
           (T("Open"), [T("Gains on naturally dirty data."), T("Cost per question.")], MINUS))


def s_takehome(prs):
    """Pattern: a table of open problems, then a navy take-home box."""
    s = kit.base(prs, K["end"], T("Open Problems"), T("(~30 seconds) Each open problem names the test that settles it."))
    y = lead(s, T("Each open problem comes with the test that would settle it"))
    end = table_at(s, [[T("Open problem"), T("Test that would settle it")],
                       [T("Real data"), T("Naturally dirty tables with independent answers.")],
                       [T("Cost"), T("Tokens and seconds per question, by budget.")]], [0.3, 0.7], y)
    msg = T("Take-home: plan, act and inspect again; keep the record of every step.")
    mh = lh(msg, CW / EMU - 0.6, PT["lead"], True) + 0.4
    rect(s, MX, I(end + 0.5), CW, I(mh), fill=NAVY, radius=True)
    text(s, MX + I(0.3), I(end + 0.5), CW - I(0.6), I(mh), msg, size=PT["lead"], color=WHITE, bold=True,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)


def s_thanks(prs):
    """Pattern: the closing slide."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, fill=NAVY)
    text(s, 0, I(2.9), W, I(0.9), T("Thank you"), size=PT["cover"], color=WHITE, bold=True, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    s.notes_slide.notes_text_frame.text = T("(~10 seconds) Thank you for listening.")


SLIDES = [s_title, s_outline, s_pipeline, s_loop, s_results, s_evidence, s_matrix, s_conclusions, s_takehome, s_thanks]


def build(lang, out_dir=None):
    out_dir = Path(out_dir) if out_dir else kit.ROOT / "build" / ".cache" / "example-deck"
    kit.build_deck(lang, SLIDES, out_dir / f"Example_{lang.upper()}.pptx", FOOTER_EN, cache=out_dir / "cache",
                   before=kickers)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", choices=["en", "vi"], default="en")
    ap.add_argument("--out", help="output folder (default: build/.cache/example-deck in the project)")
    args = ap.parse_args()
    sys.path.insert(0, str(Path(__file__).resolve().parent))   # example_deck_vi.py sits beside this file
    build(args.lang, args.out)
