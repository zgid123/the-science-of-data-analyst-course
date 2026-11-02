"""Render every visual of the kit with neutral example content: the palette, the icons, each chart form and each
diagram type, in English or Vietnamese number style, plus one contact sheet to review them at a glance.

Usage: python .claude/skills/build-report/scripts/gallery.py [OUT_DIR] [--lang en|vi]
Output: OUT_DIR/<name>.png for each visual, OUT_DIR/gallery.png, and OUT_DIR/gallery-native.pptx with every diagram
as native PowerPoint shapes and every native chart (default OUT_DIR: build/.cache/gallery).

Each visual passes the layout check (figqa); the script prints every finding and exits 1 when there is one, so the
self-test keeps the whole kit drawing cleanly. Copy a call from here into a figure builder to start a new figure.
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

import charts as ch  # noqa: E402
import diagrams as dg  # noqa: E402
import figqa  # noqa: E402
import icons  # noqa: E402
import palette as P  # noqa: E402
from c4kit import Canvas  # noqa: E402
from common import ROOT  # noqa: E402


def swatches(out):
    """The palette: series slots in order, state colours, text and structure, ramps."""
    cv = Canvas(6.5, 3.05)
    rows = [("Series (fixed order)", [(c, f"{k + 1}  {c}") for k, c in enumerate(P.SERIES)] + [(P.OTHER, "Other")]),
            ("State (with an icon)", [(P.GOOD, "good"), (P.WARNING, "warning"), (P.CRITICAL, "critical")]),
            ("Text and structure", [(P.INK, "ink"), (P.MUTED, "muted"), (P.NAVY, "navy"), (P.CONNECTOR, "connector"),
                                    (P.LINE, "line"), (P.SOFT, "soft")]),
            ("Sequential", [(c, "") for c in P.sequential(7)]),
            ("Diverging", [(c, "") for c in P.diverging(9)])]
    y = 0.1
    for label, items in rows:
        cv.ax.text(0.1, y + 0.2, label, fontsize=7.5, fontweight="bold", color=P.INK, va="center")
        x = 1.45
        w = min(0.68, (6.4 - x) / len(items) - 0.04)
        for c, name in items:
            cv.ax.add_patch(FancyBboxPatch((x, y + 0.02), w, 0.36, boxstyle="round,pad=0,rounding_size=0.04", fc=c,
                                           ec=P.LINE if c in (P.SOFT, P.SURFACE) else c, lw=0.6, zorder=3))
            if name:
                cv.ax.text(x + w / 2, y + 0.2, name.split("  ")[0] if len(name) > 9 else name, fontsize=6.5,
                           color=P.text_on(c), ha="center", va="center", zorder=4)
            x += w + 0.04
        y += 0.58
    return cv.save(out)


def chart_set(out_dir, lang):
    res = {}
    fig, ax = ch.figure(6.5, 2.8, lang=lang)
    ch.bars(ax, ["Model A", "Model B", "Model C", "Model D"],
            {"Baseline": [0.28, 0.30, 0.26, 0.22], "Method": [0.52, 0.63, 0.35, 0.41]}, ref=0.22, ref_label="No cleaning")
    res["chart-bars"] = ch.save(fig, out_dir / "chart-bars.png")
    fig, ax = ch.figure(6.5, 2.3, lang=lang)
    ch.bars(ax, ["Schema linking", "Join errors", "Aggregation", "Nested queries", "Value lookup"],
            {"Errors": [31, 24, 18, 12, 9]}, horizontal=True)
    res["chart-hbars"] = ch.save(fig, out_dir / "chart-hbars.png")
    fig, ax = ch.figure(6.5, 2.0, lang=lang)
    ch.stacked(ax, ["Model A", "Model B", "Model C"], {"Correct": [62, 55, 40], "Wrong join": [18, 20, 25],
                                                      "Wrong value": [12, 15, 20], "Other": [8, 10, 15]},
               colors=[P.TEAL, P.ORANGE, P.VIOLET, P.OTHER])
    res["chart-stacked"] = ch.save(fig, out_dir / "chart-stacked.png")
    fig, ax = ch.figure(6.5, 2.4, lang=lang)
    ch.dots(ax, ["Benchmark 1", "Benchmark 2", "Benchmark 3", "Benchmark 4"],
            {"Best single": [79.1, 68.2, 70.1, 72.5], "Selector": [85.3, 73.0, 74.8, 78.0]})
    res["chart-dots"] = ch.save(fig, out_dir / "chart-dots.png")
    fig, ax = ch.figure(6.5, 2.5, lang=lang)
    ch.lines(ax, [1, 3, 5, 10, 20, 30], {"Upper bound": [68, 74, 78, 82, 84, 85],
                                         "Selector": [68, 71, 72, 73.5, 74, 74.4],
                                         "Majority vote": [68, 69, 69.5, 70, 70.2, 70.3]})
    res["chart-lines"] = ch.save(fig, out_dir / "chart-lines.png")
    fig, ax = ch.figure(3.2, 2.5, lang=lang)
    ch.slope(ax, "Before", "After", {"Answer F1": (0.31, 0.52), "Workflow F1": (0.22, 0.48), "Column F1": (0.40, 0.44)})
    res["chart-slope"] = ch.save(fig, out_dir / "chart-slope.png")
    fig, ax = ch.figure(4.0, 2.9, lang=lang)
    ch.scatter(ax, {"Open models": [(7, 52), (13, 58), (34, 63), (70, 68)], "Closed models": [(100, 72), (200, 76)]},
               xlabel="Parameters (billions)", ylabel="Accuracy (%)", labels={(70, 68): "Model 70B"})
    res["chart-scatter"] = ch.save(fig, out_dir / "chart-scatter.png")
    fig, ax = ch.figure(4.6, 2.5, lang=lang)
    ch.heatmap(ax, ["Component A", "Component B", "Component C"], ["Set 1", "Set 2", "Set 3", "Set 4"],
               [[1.2, 2.5, 0.8, -0.4], [0.9, 3.1, 1.5, 0.6], [0.2, 1.8, -0.9, 1.1]], ramp="diverging", digits=1)
    res["chart-heatmap"] = ch.save(fig, out_dir / "chart-heatmap.png")
    fig, ax = ch.figure(3.4, 3.0, lang=lang)
    ch.venn(ax, ["Generator A", "Generator B", "Generator C"],
            {"A": 112, "B": 95, "C": 88, "AB": 140, "AC": 121, "BC": 133, "ABC": 1012})
    res["chart-venn"] = ch.save(fig, out_dir / "chart-venn.png")
    random.seed(1)
    fig, ax = ch.figure(4.0, 2.3, lang=lang)
    ch.hist(ax, [random.gauss(12.5, 3) for _ in range(400)], ref=12.5, ref_label="mean", xlabel="Steps per workflow")
    res["chart-hist"] = ch.save(fig, out_dir / "chart-hist.png")
    return res


def diagram_set(out_dir):
    res = {}
    res["diagram-sequence"] = dg.sequence(
        [("Client", "person", "laptop"), ("Gateway", "system", "shield"), ("Service", "system", "gear"),
         ("Database", "store", "database")],
        [("call", 0, 1, "request with a token"), ("call", 1, 2, "forward the checked request"),
         ("call", 2, 3, "read the record"), ("reply", 3, 2, "record"), ("self", 2, "apply the business rule"),
         ("note", 1, 2, "the gateway keeps the session open"), ("divider", "Later"),
         ("event", 3, 2, "change notification"), ("reply", 1, 0, "response")],
        legend={"call": "call", "reply": "reply", "event": "notification"}).save(out_dir / "diagram-sequence.png")
    res["diagram-timeline"] = dg.timeline(
        [("2016", "First standard", "Vocabulary and framework"), ("2017", "Two more parts", "Formats and testing"),
         ("2020", "Mobile profile", "Testing on phones"), ("2023", "Second edition", "Revised methods"),
         ("2024", "National rule", "Checks for large transfers", P.ORANGE),
         ("2025", "Mandate", "Required in banking apps", P.ORANGE)]).save(out_dir / "diagram-timeline.png")
    res["diagram-state"] = dg.state_machine(
        {"Requested": (0, 0), "Active": (1, 0), "Revoked": (2, 0), "Denied": (0, 1), "Ended": (1, 1)},
        [("Requested", "Active", "check passes"), ("Requested", "Denied", "check fails"),
         ("Active", "Revoked", "condition fails"), ("Active", "Ended", "user stops"), ("Active", "Active", "update"),
         ("Revoked", "Active", "granted again")], start="Requested", ends=("Denied", "Ended", "Revoked"),
        roles={"Denied": "critical", "Revoked": "critical", "Ended": "lake"}).save(out_dir / "diagram-state.png")
    res["diagram-process"] = dg.process(
        [("Profile", "Inspect the input", "search"), ("Plan", "Choose one step", "agent"),
         ("Execute", "A tool runs it", "gear"), ("Verify", "Inspect again", "check"),
         ("Answer", "Use the result", "table")]).save(out_dir / "diagram-process.png")
    res["diagram-cycle"] = dg.cycle(
        [("Inspect", "rate the column"), ("Plan", "one operation"), ("Execute", "a tool runs it"),
         ("Re-check", "until it passes")], centre="clean column").save(out_dir / "diagram-cycle.png")
    res["diagram-matrix"] = dg.matrix(
        ["Method A", "Method B", "Method C"], ["Several generators", "Pairwise selection", "Repair step", "Training"],
        [[True, True, True, False], [False, False, True, "examples only"], [True, False, "partial", False]],
        legend={True: "yes", "partial": "partly", False: "no"}).save(out_dir / "diagram-matrix.png")
    res["diagram-layers"] = dg.layers(
        [("Presentation", ["Web pages", "Player", "Admin console"], "warehouse"),
         ("Enforcement", ["Routes", "Middleware", "Event stream"], "system"),
         ("Decision", ["Decision point", "Information point", "Updater", "Scheduler"], "agent"),
         ("Data", ["Relational store", "Time series", "Notifications"], "store")]).save(out_dir / "diagram-layers.png")
    res["diagram-compare"] = dg.compare(
        ("Static control", ["Decides once, at log-in", "Ignores changes during use"]),
        ("Continuous control", ["Decides before and during use", "Revokes when an attribute changes"]),
        arrow_label="becomes").save(out_dir / "diagram-compare.png")
    img = out_dir / "_screen.png"
    import numpy as np
    a = np.ones((300, 480, 3))
    a[:40] = [0.16, 0.44, 0.73]
    a[60:280, 20:300] = 0.93
    a[60:120, 320:460] = [0.78, 0.37, 0.09]
    plt.imsave(img, a)
    res["diagram-screenshot"] = dg.screenshot(img, [(0.5, 0.07, "The header names the signed-in user."),
                                                    (0.33, 0.55, "The player starts after the check."),
                                                    (0.8, 0.3, "The card shows the time left.")]
                                              ).save(out_dir / "diagram-screenshot.png")
    img.unlink()
    res.update({f"diagram-{k}": sc.save(out_dir / f"diagram-{k}.png") for k, sc in more_diagrams("report").items()})
    cv = Canvas(6.5, 1.5)
    cv.box(0.1, 0.15, 2.0, 0.9, "Web app", "React", "pages and forms", role="system", icon="laptop")
    cv.box(2.3, 0.15, 2.0, 0.9, "Agent", "LLM", "plans each step", role="agent", light=True, icon="agent")
    cv.database(4.5, 0.1, 1.9, 1.0, "Store", "PostgreSQL", "records", role="store")
    res["diagram-c4-icons"] = cv.save(out_dir / "diagram-c4-icons.png")
    return res


def more_diagrams(medium):
    """The structure, time, grid and card diagrams, with neutral example content."""
    return {
        "tree": dg.tree(("Attacks", "at the sensor", "system"),
                        [("Artefact", "warehouse", [("Print", "paper photo"), ("Replay", "screen video"), ("Mask", "3D")]),
                         ("Human", "agent", [("Coerced", "a real user"), ("Look-alike", "a twin")])], medium=medium),
        "branches": dg.branches(
            [("Capture", "sensor", "system"), ("Check", "quality", "system"), ("Detect", "liveness", "agent"),
             ("Decide", "accept or reject", "system")],
            above=[(0, "Physical attack", "a printed photo", "critical", "at the sensor", False),
                   (1, "Injected stream", "a virtual camera", "critical", "after capture", True)],
            below=[(2, "Rejected", "attack detected", "lake", "detected", False)], medium=medium),
        "loop": dg.loop_flow([("Generate", "a candidate", "agent"), ("Run", "on the data", "system"),
                              ("Check", "error or empty?", "agent")], back=(2, 0, "retry with the error"),
                             exit=(2, "Answer", "the candidate that ran", "lake", "passes"), medium=medium),
        "ladder": dg.decision_ladder(("Request", "system"), [("Online?", "Ask the issuer", "system"),
                                                             ("Under the limit?", "Approve offline", "lake")],
                                     ("Decline", "ask for another card", "critical"), medium=medium),
        "era": dg.era_timeline(2000, 2026, eras=[(2000, 2012, "Hand-crafted", P.BLUE), (2012, 2019, "Deep learning", P.TEAL),
                                                 (2019, 2026, "Foundation models", P.ORANGE)],
                               above=[(2005, "Optical flow"), (2014, "CNN classifiers"), (2023, "Pre-training")],
                               below=[(2016, "First standard"), (2023, "Second edition")], ticks=[2000, 2010, 2020, 2026],
                               medium=medium),
        "lanes": dg.lane_timeline([("Standards", "system", [(2016, "Framework"), (2017, "Testing"), (2023, "Second edition")]),
                                   ("Regulator", "agent", [(2024, "Decision"), (2025, "Mandate")]),
                                   ("Industry", "store", [(2019, "Certification"), (2021, "Level 2")])],
                                  2015, 2026, height=3.4 if medium == "report" else 5.0, ticks=[2016, 2020, 2024],
                                  medium=medium),
        "gantt": dg.gantt([("R1", [(0, 2, "", "wait"), (2, 5, "lock", "hold")], "good"),
                           ("R2", [(0, 5, "", "wait"), (5, 7, "lock", "hold")], "good"),
                           ("R3", [(0, 7, "", "wait"), (7, 8, "lock", "hold")], "critical")], 0, 10, ticks=[0, 5, 10],
                          medium=medium),
        "tokens": dg.token_strip([("Input", [("The", "plain"), ("[M]", "mask"), ("[M]", "mask"), ("city", "plain")],
                                   [("brace", 1, 2, "masked span")]),
                                  ("Step 1", [("The", "plain"), ("old", "new"), ("[M]", "mask"), ("city", "plain")],
                                   [("window", 1, 2)])], medium=medium),
        "pairs": dg.pair_matrix(["c1", "c2", "c3"], lambda i, j: ("c1" if 0 in (i, j) else "c3",
                                                                   "win" if (0 if 0 in (i, j) else 2) == i else "lose"),
                                legend={"win": "row wins", "lose": "column wins"}, medium=medium),
        "units": dg.unit_rows([("Correct", 7, P.GOOD), ("Picked", [P.BLUE] * 5 + [None] * 2), ("Wrong", 3, P.CRITICAL)],
                              medium=medium),
        "risk": dg.risk_matrix(["High", "Medium", "Low"], ["Rare", "Possible", "Likely"],
                               {(0, 2): ["Replay", "Lost reversal"], (1, 1): ["Timeout"], (2, 0): ["Log gap"]},
                               col_title="Likelihood", medium=medium),
        "cards": dg.stripe_cards([("1 · FIRM", "Several generators help", "Each answers questions the others miss.",
                                   P.GOOD, "check"),
                                  ("2 · QUALIFIED", "The selector closes part of the gap", "Most of it on one benchmark.",
                                   P.WARNING, "warning"),
                                  ("3 · OPEN", "Cost per question", "Not reported.", P.CRITICAL, "info")], cols=3,
                                 medium=medium),
    }


def native_deck(path):
    """Every diagram as native, grouped PowerPoint shapes, and every native chart, one per slide; returns the
    layout findings."""
    from pptx import Presentation
    from pptx.util import Inches
    import native_charts as nc
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    found = []
    scenes = dict(more_diagrams("slide"))
    scenes["process"] = dg.process([("Profile", "Inspect the input", "search"), ("Plan", "Choose one step", "agent"),
                                    ("Execute", "A tool runs it", "gear"), ("Verify", "Inspect again", "check")],
                                   medium="slide")
    scenes["state"] = dg.state_machine({"Requested": (0, 0), "Active": (1, 0), "Ended": (2, 0)},
                                       [("Requested", "Active", "check passes"), ("Active", "Ended", "user stops"),
                                        ("Active", "Active", "update")], start="Requested", ends=("Ended",),
                                       medium="slide")
    for name, sc in scenes.items():
        s = prs.slides.add_slide(prs.slide_layouts[6])
        found += sc.to_slide(s, 0.3, 0.9, name=name)
    s = prs.slides.add_slide(prs.slide_layouts[6])
    nc.bars(s, 0.3, 0.4, 6.2, 3.3, ["Model A", "Model B"], {"Baseline": [0.28, 0.30], "Method": [0.52, 0.63]},
            ref=0.22, ref_label="No cleaning")
    nc.stacked(s, 6.8, 0.4, 6.2, 3.3, ["Model A", "Model B"], {"Correct": [62, 55], "Wrong": [38, 45]})
    nc.lines(s, 0.3, 3.9, 6.2, 3.3, [1, 3, 5, 10], {"Upper bound": [68, 74, 78, 82], "Selector": [68, 71, 72, 73]})
    nc.doughnut(s, 6.8, 3.9, 6.2, 3.3, {"Correct": 62, "Wrong": 18, "Other": 20}, centre="62%")
    prs.save(path)
    return found


def contact_sheet(out_dir, names, path):
    from PIL import Image
    ims = [(n, Image.open(out_dir / f"{n}.png").convert("RGB")) for n in names]
    w = max(im.width for _, im in ims)
    cols, heights = [[], []], [0, 0]
    for n, im in ims:
        k = 0 if heights[0] <= heights[1] else 1
        cols[k].append(im)
        heights[k] += im.height + 60
    sheet = Image.new("RGB", (2 * w + 90, max(heights) + 30), "#E4E6EA")
    for k in range(2):
        y = 30
        for im in cols[k]:
            sheet.paste(im, (30 + k * (w + 30), y))
            y += im.height + 60
    sheet.thumbnail((3000, 6000))
    sheet.save(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out", nargs="?", default=str(ROOT / "build" / ".cache" / "gallery"))
    ap.add_argument("--lang", default="en")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    found = {"palette": swatches(out / "palette.png")}
    icons.contact_sheet(out / "icons.png")
    found.update(chart_set(out, args.lang))
    found.update(diagram_set(out))
    contact_sheet(out, [n for n in found if n != "palette"] + ["palette"], out / "gallery.png")
    found["native-deck"] = native_deck(out / "gallery-native.pptx")
    bad = {k: v for k, v in found.items() if v}
    print(f"{len(found)} visuals and {len(icons.ICONS)} icons → {out}: "
          f"{sum(len(v) for v in bad.values())} layout findings")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
