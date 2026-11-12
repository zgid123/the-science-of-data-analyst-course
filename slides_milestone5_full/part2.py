"""Full Milestone 5 deck, plan slides 22–46: data requirements and selection, dataset description and fit, data
understanding and quality, data preparation and leakage. Slide text follows the ensembled script section
reports/milestone-5/presentation/v2-full/script-parts/part2.md; every number comes from the Milestone 5 report (Sections 2.1,
4 to 7 and Appendices III to VII). Slides 24, 27, 35, 39, 40 and 45 start from the reviewed slides of the 30-slide deck
(build_slides_milestone5_30.py: s_selection, s_oulad, s_quality, s_adddrop, s_rule, s_leakage)."""

from slides_milestone5_full.common import *   # noqa: F401,F403

GOLD_FILL = pal_rgb(pal.tint(pal.GOLD))
GREY_FILL = pal_rgb("#E6E8EC")


# ----------------------------------------------------------------------------- helpers of this range
def widths(fracs, w=CWI):
    """Column widths (EMU) from fractions of width w (inches); the last column takes the rest."""
    col = [int(I(w) * f) for f in fracs[:-1]]
    col.append(int(I(w)) - sum(col))
    return col


def grid_table(s, name, y, rows, fracs, bottom, x=X0, w=CWI, sizes=None, row_h=0.36):
    """A kit table at (x, y) in the largest kit size that fits above `bottom`, its rows stretched to reach it."""
    col = widths(fracs, w)
    sizes = sizes or (PT["body"], BODY)
    size = next((p for p in sizes if table_h(rows, col, p, row_h) <= bottom - y), sizes[-1])
    kit.room("p2 " + name, y + table_h(rows, col, size, row_h), bottom)
    shape = table(s, I(x), I(y), I(w), rows, col, size=size, row_h=I(row_h))
    stretch_table(shape, bottom - y)
    return shape


def paint(shape, i, j, fill=None, color=None, bold=None):
    """Colour one cell of a kit table (fill, text colour, bold)."""
    c = shape.table.cell(i, j)
    if fill is not None:
        c.fill.solid()
        c.fill.fore_color.rgb = fill
    for p in c.text_frame.paragraphs:
        for r in p.runs:
            if color is not None:
                r.font.color.rgb = color
            if bold is not None:
                r.font.bold = bold


def paint_row(shape, i, fill, color=None, bold=None):
    for j in range(len(shape.table.columns)):
        paint(shape, i, j, fill, color, bold)


def heading(s, x, y, w, line):
    """A navy heading line at HEAD size; returns the y below it."""
    h = lh(line, w, HEAD, True)
    text(s, I(x), I(y), I(w), I(h), line, size=HEAD, color=NAVY, bold=True, spacing=1.0)
    return y + h + 0.08


def icon_card(s, x, y, w, h, ic, head, paras, color=NAVY, fill=SOFT, line=LINE, pt=BODY, dashed_line=False):
    """A card with an icon before its head."""
    shape = rect(s, I(x), I(y), I(w), I(h), fill=fill, line=line, radius=True, line_w=1.25)
    if dashed_line:
        dashed(shape)
    icon(s, ic, x + 0.16, y + 0.14, 0.32, color=color, bg=fill)
    hh = lh(head, w - 0.7, HEAD, True)
    text(s, I(x + 0.56), I(y + 0.14), I(w - 0.72), I(hh), head, size=HEAD, color=color, bold=True, spacing=1.0)
    rich(s, x + 0.18, y + 0.14 + max(hh, 0.32) + 0.08, w - 0.36, paras, pt)


def icon_card_h(head, paras, w, pt=BODY):
    return 0.14 + max(lh(head, w - 0.7, HEAD, True), 0.32) + 0.08 + rich_h(paras, w - 0.36, pt) + 0.1


def fill_pt(items, w, room, h_fn):
    """The largest kit size (16 or 14 pt) at which every item's height h_fn(item, w, pt) fits `room`."""
    return PT["body"] if max(h_fn(it, w, PT["body"]) for it in items) <= room else BODY


# ----------------------------------------------------------------------------- 4 Data requirements
def s22(prs):
    s = kit.base(prs, kicker(22), T("Data Requirements, Stated First"), notes(22))
    y = lead(s, T("We wrote what each question needs from the university's records before searching, so the "
                  "questions chose the data and not the reverse."))
    shared = [tb("Unit: ", "one student's enrolment in one course and semester."),
              tb("Population: ", "students still enrolled after the add-drop period."),
              tb("Outcome: ", "the final result, with the date of any withdrawal."),
              tb("Time: ", "each list uses only data up to its cut-off, so every event needs a date.")]
    xs, cw = cols(4, 0.2)
    ch = max(card_h(None, [p], cw) for p in shared)
    for x, p in zip(xs, shared):
        card(s, x, y, cw, None, [p], h=ch)
    y += ch + 0.2
    key22 = T("Key: top row = needs shared by all four questions; AQ = analytical question; D1 = whom to contact; D2 = "
              "where to place support time; orange cell = a record no dataset holds, declared a gap before the search.")
    kb = bottom_key(s, key22)
    rows = [[T("Question"), T("Outcome or measure"), T("Required variables"), T("Time and grain"), T("Decision")],
            [T("AQ1 Descriptive"), T("Pass, fail or withdrawal; first missed week"),
             T("Identifiers; enrolment dates; final result; dated withdrawal; task dates"), T("Four semesters; week"),
             T("D2, semester end")],
            [T("AQ2 Diagnostic"), T("Non-completion with and without each sign"),
             T("AQ1 variables; dated activity; missed and late tasks"), T("Weeks 1–4; day"), T("D2; reasons in D1")],
            [T("AQ3 Predictive"), T("Non-completion by the end of the semester"),
             T("Timestamped activity and submissions; background at enrolment"),
             T("Cut-offs: ends of weeks 2 and 4; runs in time order"), T("D1, weeks 3 and 5")],
            [T("AQ4 Prescriptive"), T("Recall within staff capacity; outcome after contact"),
             T("AQ3 output; capacity (assumed); contact record (to create)"), T("Each review point"), T("D1")]]
    shape = grid_table(s, "requirement matrix", y, rows, (0.15, 0.22, 0.3, 0.19, 0.14), kb - 0.12)
    paint(shape, 4, 2, ACC_FILL, AGENT_INK, True)
    src(s, "Source: Milestone 5 report, Section 4 and Table 4.1, and Appendix IV, Table A.9.")


def s23(prs):
    s = kit.base(prs, kicker(23), T("Six Must-Have Gates"), notes(23))
    y = lead(s, T("Six gates decide first and scores only inform, so a dataset that fails any gate is out whatever "
                  "its total."))
    gates = [(T("G1 · Dated outcome"), T("A final result that separates pass, fail and withdrawal, with the date of "
                                         "each withdrawal."), "flag"),
             (T("G2a · Dated tasks"), T("Due dates and dated submissions, because missed and late tasks are early "
                                        "signs."), "document"),
             (T("G2b · Dated activity"), T("Platform activity per student by day or week, to compare the first "
                                           "weeks."), "chart"),
             (T("G3 · History"), T("At least three runs of the same courses in time order, so a model can be tested "
                                   "on a later run."), "calendar"),
             (T("G4 · Access"), T("An open licence for academic use, documentation and verifiable provenance."),
              "key"),
             (T("G5 · Linkage"), T("Anonymised data with a student identifier that persists across tables and "
                                   "runs."), "user")]
    lower = [(T("Rule"), [T("Gates decide, scores inform: a score of 0–2 on each of the brief's ten criteria never "
                            "rescues a failed gate.")]),
             (T("Optional, not a gate"), [T("Delivery mode, year of study, attendance, leave or transfer: their "
                                            "absence only narrows a question.")]),
             (T("Gap declared before the search"), [T("No dataset would hold a contact record or weekly staff "
                                                      "capacity.")])]
    xs, cw = cols(3, 0.25)
    lh_ = max(card_h(a, b, cw) for a, b in lower)
    ly = END - lh_
    gh = (ly - 0.25 - y - 0.2) / 2
    kit.room("p2 gate grid", max(node_h(a, [b], cw, body_pt=BODY) for a, b, _ in gates) + 0.42, gh)
    for k, (a, b, ic) in enumerate(gates):
        node(s, xs[k % 3], y + (k // 3) * (gh + 0.2), cw, gh, a, [b], "white", body_pt=BODY, icon=ic)
    for k, (x, (a, b)) in enumerate(zip(xs, lower)):
        if k == 2:
            dashed(rect(s, I(x), I(ly), I(cw), I(lh_), fill=GREY_FILL, line=GREY, radius=True, line_w=1.5))
            card(s, x, ly, cw, a, b, color=KEY, h=lh_, fill=GREY_FILL, line=None)
        else:
            card(s, x, ly, cw, a, b, h=lh_)
    src(s, "Source: Milestone 5 report, Sections 4 and 4.1, and Appendix IV.")


def s24(prs):
    s = kit.base(prs, kicker(24), T("Seven Candidates Screened"), notes(24))
    y = lead(s, T("Of seven public candidates, only OULAD passes every gate, so we chose it for fit, not for ease."))
    y = rich(s, X0, y, CWI, [T("Each candidate is scored 0–2 on the brief's ten criteria (20 at most); the must-have "
                               "gates decide first. UCI: the University of California, Irvine, Machine Learning "
                               "Repository. XuetangX and HarvardX: data from massive open online courses.")])
    rows = [[T("Candidate"), T("Score (of 20)"), T("Gates failed"), T("Decision")],
            ["OULAD", "12", T("none"), T("Selected, on condition")],
            ["UCI 697", "10", T("dated outcome, tasks, activity"), T("Rejected")],
            ["UCI 320", "6", T("dated outcome, tasks, activity, runs"), T("Rejected")],
            ["UCI 856", "7", T("dated outcome, tasks, activity, runs"), T("Rejected")],
            ["XuetangX", "8", T("dated outcome, tasks, licence"), T("Rejected")],
            ["HarvardX", "8", T("dated outcome, tasks, activity, runs, licence"), T("Rejected")],
            ["xAPI-Edu-Data", "4", T("dated outcome, tasks, activity, runs"), T("Rejected")]]
    col = widths((0.2, 0.14, 0.44, 0.22))
    shape = table(s, MX, I(y), CW, rows, col, size=BODY, row_h=I(0.31))
    tbl = shape.table
    for j in range(4):                                   # the selected row in the accent colour
        paint(shape, 1, j, ACC_FILL, AGENT_INK, True)
    for i in range(2, len(rows)):                        # failed gates in red
        paint(shape, i, 2, BAD_FILL, MINUS)
    del tbl
    sel_key = T("Key: orange row = selected; red cell = a gate failed.")
    notes24 = [tb("OULAD, the Open University Learning Analytics Dataset: ",
                  "the only candidate that records a dated withdrawal, dated submissions and daily clicks."),
               tb("Why only 12 of 20: ", "the scores count only what each documentation states. Five candidates "
                                         "score higher on quality feasibility, yet none can show when a student "
                                         "stopped taking part (the conditions of the choice: ") +
               [(ref(25) + ").", INK, False)]]
    lower = 0.08 + lh(sel_key, CWI, PT["small"]) + 0.2 + rich_h(notes24, CWI)
    y += stretch_table(shape, END - lower - y)
    y = key(s, y + 0.08, sel_key) + 0.2
    rich(s, X0, y, CWI, notes24)
    src(s, "Source: Milestone 5 report, Section 4.1, Table 4.2 and Appendix IV, Table A.10.")


def s25(prs):
    s = kit.base(prs, kicker(25), T("Why OULAD, and on What Condition"), notes(25))
    y = lead(s, T("OULAD was chosen for its fit with the questions, not for ease of access, and only after its files "
                  "confirmed the facts its documentation left open."))
    lw = 7.3
    rx, rw = X0 + lw + 0.35, CWI - lw - 0.35
    by = END + 0.25
    top = heading(s, X0, y, lw, T("Three facts checked in the files"))
    facts = [("check", PLUS, OUT_FILL, T("Confirmed"),
              T("The results separate pass from fail, and 10,063 of the 10,156 withdrawals carry their date "
                "(dated-outcome gate).")),
             ("check", PLUS, OUT_FILL, T("Confirmed"),
              T("A student keeps one identifier across tables and runs; 3,538 students appear in more than one run "
                "(identifier gate).")),
             ("warning", WARM, ACC_FILL, T("Met in part"),
              T("Enough runs for testing: five of seven modules have three or four runs (history gate). So the "
                "model test uses all 13 runs of 2014, with the 4 runs that have no earlier twin reported apart."))]
    fk = T("Key: green = confirmed; orange = met in part. Twin = an earlier run of the same module and start month.")
    kh = lh(fk, lw, PT["small"])
    room_f = by - 0.25 - kh - 0.08 - top
    fh = (room_f - 2 * 0.15) / 3
    kit.room("p2 three facts", sum(rich_h([b], lw - 1.0, PT["body"]) + lh(a, lw - 1.0, HEAD, True) + 0.2
                                   for _, _, _, a, b in facts) + 0.3, room_f)
    fy = top
    for ic, c, fill, a, b in facts:
        rect(s, I(X0), I(fy), I(lw), I(fh), fill=fill, line=c, radius=True, line_w=1.5)
        icon(s, ic, X0 + 0.18, fy + (fh - 0.44) / 2, 0.44, color=c, bg=fill)
        ph = lh(a, lw - 1.0, HEAD, True) + 0.06 + rich_h([b], lw - 1.0, PT["body"])
        ty = fy + (fh - ph) / 2
        text(s, I(X0 + 0.8), I(ty), I(lw - 1.0), I(0.3), a, size=HEAD, color=c if c != PLUS else OUT_INK, bold=True,
             spacing=1.0)
        rich(s, X0 + 0.8, ty + lh(a, lw - 1.0, HEAD, True) + 0.06, lw - 1.0, [b], pt=PT["body"])
        fy += fh + 0.15
    key(s, fy - 0.15 + 0.08, fk, X0, lw)
    side = [(T("Why OULAD, not ease"), [T("It alone has a final result for every enrolment, including a dated "
                                          "withdrawal, dated submissions and daily clicks per page."),
                                        T("Its 12 of 20 is modest because scores count only what the documentation "
                                          "states; five candidates score higher on quality feasibility.")]),
            (T("Limits of the choice"), [T("UK distance-learning modules of 2013–2014, chosen partly because many "
                                           "students failed them, so rates are likely above a typical program's."),
                                         T("No delivery mode, year of study, attendance, or leave and transfer "
                                           "status.")])]
    sh = (END - y - 0.25) / 2
    pt = fill_pt(side, rw, sh, lambda it, w, p: card_h(it[0], it[1], w, pt=p))
    for k, (a, b) in enumerate(side):
        card(s, rx, y + k * (sh + 0.25), rw, a, b, h=sh, pt=pt)
    src(s, "Source: Milestone 5 report, Section 4.1 and Appendices IV and V.")


def s26(prs):
    s = kit.base(prs, kicker(26), T("Provenance and Licence"), notes(26))
    y = lead(s, T("Our copy of OULAD is a pinned public release under an open licence, so anyone can rebuild every "
                  "number from the same files."))
    rows = [[T("Item"), T("Record")],
            [T("Dataset"), T("Open University Learning Analytics Dataset (OULAD)")],
            [T("Authors"), T("J. Kuzilek, M. Hlosta and Z. Zdrahal, Knowledge Media Institute, The Open University")],
            [T("Copy and version"), T("figshare deposit, doi:10.6084/m9.figshare.5081998.v1, version 1")],
            [T("Accessed"), T("6 November 2026")],
            [T("Raw files"), T("One archive of 46,750,706 bytes holding seven tables in CSV (comma-separated "
                               "values) format")],
            [T("Integrity"), T("Size and SHA-256 checksum of the archive and of each table pinned; all seven tables "
                               "matched, and every checksum was confirmed again before preparation")],
            [T("Licence"), T("Creative Commons Attribution 4.0 (CC BY 4.0): academic use and sharing with "
                             "attribution")],
            [T("Privacy"), T("Anonymised by the publisher with k-anonymity, k = 5; we make no attempt at "
                             "re-identification and enter no record into public AI tools")]]
    key26 = T("Key: SHA-256 = a checksum (a file fingerprint) that changes if a single byte changes; k-anonymity with "
              "k = 5 = every combination of identifying attributes is shared by at least five students.")
    kb = bottom_key(s, key26)
    shape = grid_table(s, "provenance", y, rows, (0.2, 0.8), kb - 0.12, sizes=(PT["lead"], PT["body"], BODY))
    for j in range(2):
        paint(shape, 6, j, ACC_FILL, None, None)
    paint(shape, 6, 0, None, AGENT_INK, True)
    src(s, "Source: Milestone 5 report, Section 4.1 and Appendix IV, Table A.11.")


# ----------------------------------------------------------------------------- 5 Dataset
OUTCOMES = {"Distinction": 3024, "Pass": 12361, "Fail": 7052, "Withdrawn": 10156}     # Section 5


def outcome_bar(fig):
    ax = charts.axes(fig)
    names = [T("Distinction"), T("Pass"), T("Fail"), T("Withdrawn")]
    colours = [pal.shade(pal.OTHER, 0.3), pal.OTHER, pal.ORANGE, pal.shade(pal.ORANGE, 0.3)]
    charts.stacked(ax, [""], {n: [v] for n, v in zip(names, OUTCOMES.values())}, percent=False, colors=colours,
                   min_label=0.05)


def s27(prs):
    s = kit.base(prs, kicker(27), T("OULAD at a Glance"), notes(27))
    y = lead(s, T("OULAD gives every enrolment a final result, with dated tasks and daily clicks, over 22 runs of "
                  "seven UK modules."))
    y = rich(s, X0, y, CWI, [
        T("OULAD, the Open University Learning Analytics Dataset, holds 22 runs of seven distance-learning modules of "
          "the Open University in the UK, coded AAA to GGG, from 2013 and 2014."),
        tb("A run ", "is one offering of a module, named by year and start month (B = February, J = October); days "
                     "count from day 0, the run's start.")], pt=PT["body"])
    tiles = [(T("9 runs"), T("in 2013: six modules, 13,529 enrolments")),
             (T("13 runs"), T("in 2014: all seven modules, 19,064 enrolments")),
             (T("16 of 22"), T("runs have a task other than the exam due by day 27"))]
    xs, cw = cols(3, 0.25)
    th = max(kit.num_h(PT["number"]) + 0.05 + lh(b, cw - 0.3) for _, b in tiles) + 0.3
    ty = END - th
    bar_key = T("Key: greys = completion (Distinction, a pass with honours, and Pass); orange and brown = "
                "non-completion (Fail, Withdrawn).")
    ch = ty - 0.3 - lh(bar_key, CWI, PT["small"]) - 0.05 - (y + 0.35)
    kit.room("p2 outcome bar", 1.2, ch)
    text(s, I(X0), I(y), CW, I(0.3), T("Final results of all 32,593 enrolments of 28,785 students (number of "
                                       "enrolments)"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    chart(s, "m5-full-p2-outcomes", X0, y + 0.35, CWI, ch, outcome_bar)
    key(s, y + 0.35 + ch + 0.05, bar_key)
    for k, (x, (a, b)) in enumerate(zip(xs, tiles)):
        rect(s, I(x), I(ty), I(cw), I(th), fill=ACC_FILL if k == 2 else SOFT, line=WARM if k == 2 else LINE,
             radius=True)
        bignum(s, x, ty + 0.15, cw, a, b, color=WARM if k == 2 else NAVY)
    src(s, "Source: Milestone 5 report, Section 5 and Appendix V, Table A.12.")


def s28(prs):
    s = kit.base(prs, kicker(28), T("Seven Tables and Their Keys"), notes(28))
    y = lead(s, T("Seven tables join on module, run and student, and every link between them holds, so no record is "
                  "lost in a join."))
    rows = [[T("Table (plain meaning)"), T("Rows"), T("One row is")],
            [T("courses (runs)"), "22", T("a module run, with its length in days")],
            [T("assessments (tasks)"), "206", T("a task with its type (TMA, CMA or exam) and due day")],
            [T("vle (platform pages)"), "6,364", T("a page of the learning platform")],
            [T("studentInfo (enrolments)"), "32,593", T("an enrolment, with background attributes and final result")],
            [T("studentRegistration (dates)"), "32,593", T("an enrolment's registration and unregistration day")],
            [T("studentAssessment (submissions)"), "173,912", T("a submitted task, with its day and score")],
            [T("studentVle (clicks)"), "10,655,280", T("one student's clicks on one page in one day; no key")]]
    key28 = T("Key: vle = virtual learning environment, the learning platform; TMA = tutor-marked assignment; CMA = "
              "computer-marked assessment (a quiz). Orange rows = the enrolment tables at the centre of every join; "
              "every submission, task, click record and page has its parent row.")
    kb = bottom_key(s, key28)
    shape = grid_table(s, "tables", y, rows, (0.34, 0.16, 0.5), kb - 0.12)
    for i in (4, 5):
        paint_row(shape, i, ACC_FILL)
        paint(shape, i, 0, None, AGENT_INK, True)
    src(s, "Source: Milestone 5 report, Section 5 and Appendix V, Table A.12.")


RUNS = {  # module: {column: kind}; kinds: run, late (2013 run without a task due by day 27), new (2014 only)
    "AAA": {"2013J": "run", "2014J": "run"},
    "BBB": {"2013B": "run", "2013J": "run", "2014B": "run", "2014J": "run"},
    "CCC": {"2014B": "new", "2014J": "new"},
    "DDD": {"2013B": "run", "2013J": "run", "2014B": "run", "2014J": "run"},
    "EEE": {"2013J": "late", "2014B": "new", "2014J": "run"},
    "FFF": {"2013B": "run", "2013J": "run", "2014B": "run", "2014J": "run"},
    "GGG": {"2013J": "late", "2014B": "new", "2014J": "run"}}
FIRST_TASK = {"EEE": 33, "GGG": 61}       # day of the first task in the October 2013 run (Appendix VI)


def s29(prs):
    s = kit.base(prs, kicker(29), T("Coverage over Years and Runs"), notes(29))
    y = lead(s, T("2013 holds 9 runs of six modules and 2014 holds 13 runs of all seven, so some test runs have no "
                  "earlier twin, and tasks fall due late."))
    gw = 7.6
    rx, rw = X0 + gw + 0.35, CWI - gw - 0.35
    gkey = T("Key: a filled cell is a run, named by year and start month (B = February, J = October); empty = no run. "
             "Orange = a run only in 2014; grey = a 2013 run with no task due by day 27.")
    kh = lh(gkey, gw, PT["small"])
    gb = END - kh - 0.1
    cols_ = ["2013B", "2013J", "2014B", "2014J"]
    heads = [T("2013 February"), T("2013 October"), T("2014 February"), T("2014 October")]
    lw_ = 0.95
    cx0 = X0 + lw_
    cwid = (gw - lw_) / 4
    hy = y
    for k, hd in enumerate(heads):
        text(s, I(cx0 + k * cwid), I(hy), I(cwid), I(0.3), hd, size=PT["small"] + 2, color=NAVY, bold=True,
             align=PP_ALIGN.CENTER, spacing=1.0)
    ry0 = hy + 0.4
    rh = (gb - ry0) / 7
    kit.room("p2 run grid", 7 * 0.5, gb - ry0)
    for r, (mod, runs) in enumerate(RUNS.items()):
        yy = ry0 + r * rh
        text(s, I(X0), I(yy), I(lw_ - 0.1), I(rh - 0.08), mod, size=PT["body"], color=NAVY, bold=True,
             anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        for k, c in enumerate(cols_):
            x = cx0 + k * cwid + 0.06
            kind = runs.get(c)
            if kind is None:
                dashed(rect(s, I(x), I(yy + 0.04), I(cwid - 0.12), I(rh - 0.12), fill=None, line=LINE, radius=True))
                continue
            lab = mod + " " + c
            if kind == "late":
                lab = T("{run} · first task day {d}").format(run=lab, d=FIRST_TASK[mod])
            fill, lc, tc = {"run": (SOFT, LINE, INK), "late": (GREY_FILL, GREY, KEY),
                            "new": (ACC_FILL, WARM, AGENT_INK)}[kind]
            chip(s, x, yy + 0.04, cwid - 0.12, rh - 0.12, lab, fill=fill, line_color=lc, color=tc,
                 size=PT["small"] + 1 if kind == "late" else PT["small"] + 2, bold=kind == "new")
    key(s, END - kh, gkey, X0, gw)
    side = [(T("2013: development"), [T("9 runs of six modules, 13,529 enrolments."),
                                      T("7 of the 9 runs have a task due by day 27; none has one by day 13.")]),
            (T("2014: single test"), [T("13 runs of all seven modules, 19,064 enrolments."),
                                      T("Module CCC and the February runs of EEE and GGG appear only here, so they "
                                        "test transfer to runs a model has not seen.")]),
            (T("Tasks fall due late"), [T("Over all 22 runs, a task other than the exam falls due by day 27 in 16 "
                                          "runs and by day 13 in only 1.")])]
    pt = fill_pt(side, rw, (END - y - 0.5) / 3, lambda it, w, p: card_h(it[0], it[1], w, pt=p))
    hs = [card_h(a, b, rw, pt=pt) for a, b in side]
    extra = (END - y - 0.5 - sum(hs)) / 3
    yy = y
    for k, ((a, b), h) in enumerate(zip(side, hs)):
        card(s, rx, yy, rw, a, b, h=h + extra, pt=pt, color=AGENT_INK if k == 1 else NAVY)
        yy += h + extra + 0.25
    src(s, "Source: Milestone 5 report, Sections 5 and 6.2, and Appendices V and VI.")


def s30(prs):
    s = kit.base(prs, kicker(30), T("Key Variables"), notes(30))
    y = lead(s, T("A short data dictionary names the variables every question rests on; two of them serve only the "
                  "fairness checks."))
    rows = [[T("Variable (name in OULAD)"), T("Meaning"), T("Used by")],
            [T("Final result (final_result)"), T("Pass, Distinction, Fail or Withdrawn"), T("Target of all four")],
            [T("Module and run (code_module, code_presentation)"), T("Module AAA–GGG; run by year and start month"),
             T("All four")],
            [T("Registration days (date_registration, date_unregistration)"),
             T("Registration and unregistration day, counted from day 0"), T("Populations; withdrawal timing")],
            [T("Tasks (assessment_type, date, date_submitted)"),
             T("Kind of task (TMA, CMA, exam), due day and submission day"), T("AQ1–AQ3")],
            [T("Clicks (sum_click, date)"), T("Clicks of one student on one page in one day"), T("AQ2, AQ3")],
            [T("Background (num_of_prev_attempts, studied_credits)"),
             T("Earlier attempts at the module; credits studied in the run"), T("AQ2, AQ3")],
            [T("Group attributes (imd_band, disability)"),
             T("Deprivation band of the home area; declared disability"), T("Group checks only, never a predictor")]]
    key30 = T("Key: TMA = tutor-marked assignment; CMA = computer-marked assessment (a quiz). AQ1 descriptive, AQ2 "
              "diagnostic, AQ3 predictive, AQ4 prescriptive ranking question. Grey row = audit only. The full data "
              "dictionary travels with the Final Project Package.")
    kb = bottom_key(s, key30)
    shape = grid_table(s, "key variables", y, rows, (0.4, 0.38, 0.22), kb - 0.12)
    paint_row(shape, 7, GREY_FILL)
    src(s, "Source: Milestone 5 report, Section 5, Table 5.1, and Appendix V.")


def s31(prs):
    s = kit.base(prs, kicker(31), T("Requirement–Data Fit"), notes(31))
    y = lead(s, T("No question fits OULAD in full: three are narrowed and AQ4 lacks its key concept, yet every "
                  "question keeps a core the data can answer."))
    rows = [[T("Question"), T("Fit"), T("Missing or weak in OULAD"), T("Handling"), T("Action"), T("Status")],
            [T("AQ1 Descriptive"), T("YELLOW"), T("Year of study, delivery mode; exam results in only 2 of 7 modules"),
             T("TMA and CMA only; day-14 population rule; both years"), T("Modify"), T("Answered")],
            [T("AQ2 Diagnostic"), T("YELLOW"), T("Attendance; the several-modules sign in 2013"),
             T("Signs up to day 27; several-modules sign on 2014 only"), T("Modify"), T("Answered")],
            [T("AQ3 Predictive"), T("YELLOW"), T("A task-only rule fires in 1 of 22 runs at day 13"),
             T("Early-sign rule with an inactivity part; test on 2014"), T("Modify"), T("Deferred")],
            [T("AQ4 Prescriptive"), T("RED"), T("Contacts, staff capacity, outcomes after contact"),
             T("Ranking part only; contact to the pilot"), T("Modify + Defer"), T("Deferred")]]
    msg = T("Missing values keep a category and are never imputed; missing variables are never simulated; no "
            "question is dropped.")
    mh = lh(msg, CWI - 0.6, PT["lead"], True) + 0.3
    my = END - mh
    closing_box(s, my, msg, h=mh)
    key31 = T("Key: GREEN = the data are enough (none); YELLOW = the question is narrowed or its claim changed; RED = a "
              "key concept, variable or intervention is missing. TMA = tutor-marked assignment; CMA = computer-marked "
              "assessment. Deferred = designed, not yet run.")
    kh = lh(key31, CWI, PT["small"])
    kt = my - 0.15 - kh
    key(s, kt, key31)
    shape = grid_table(s, "fit matrix", y, rows, (0.15, 0.1, 0.27, 0.27, 0.11, 0.1), kt - 0.1)
    for i in range(1, 4):
        paint(shape, i, 1, GOLD_FILL, AGENT_INK, True)
    paint(shape, 4, 1, BAD_FILL, MINUS, True)
    src(s, "Source: Milestone 5 report, Section 5.1, Table 5.2, and Appendix V, Table A.13.")


def s32(prs):
    s = kit.base(prs, kicker(32), T("Gaps Only the University Can Fill"), notes(32))
    y = lead(s, T("We never impute a missing value or simulate a missing variable, so three parts of the proposal wait "
                  "for the university's own records."))
    rows = [[T("Class of gap"), T("Cases in OULAD"), T("Handling")],
            [T("Missing value"), T("Deprivation band (1,111 enrolments); registration day (45); TMA score (173)"),
             T("A \"Missing\" category or an indicator; no imputation")],
            [T("Recorded absence"), T("No click row; no submission row"), T("Zero counts after the joins")],
            [T("Missing variable"), T("Year of study, delivery mode, attendance, leave or transfer, contacts, staff "
                                      "capacity"), T("Never imputed or simulated; questions narrowed or the contact "
                                                     "part deferred")],
            [T("Missing target"), T("None: every enrolment has a final result"), T("Supervised target available")]]
    cards_ = [(T("Contact part of AQ4"), [T("AQ4, the ranking question: which contact works for which student, "
                                            "and whether contact raises completion: a randomised pilot with logged "
                                            "contacts.")]),
              (T("Group comparisons"), [T("By year of study, delivery mode or attendance; on OULAD they "
                                                      "become comparisons by module, run and start month.")]),
              (T("Contact parts of the KPIs"), [T("The two secondary key performance indicators (KPIs) need a "
                                                  "record of each contact.")])]
    xs, cw = cols(3, 0.25)
    pt = BODY
    chh = max(icon_card_h(a, b, cw, pt) for a, b in cards_)
    cy = END - chh
    hy = cy - 0.08 - lh(T("Needs the university's records"), CWI, HEAD, True)
    heading(s, X0, hy, CWI, T("Needs the university's records"))
    for x, (a, b) in zip(xs, cards_):
        icon_card(s, x, cy, cw, chh, "lock", a, b, pt=pt)
    tk = T("Key: TMA = tutor-marked assignment. Orange row = the class only new records can close.")
    kt = hy - 0.25 - lh(tk, CWI, PT["small"])
    key(s, kt, tk)
    shape = grid_table(s, "gap classes", y, rows, (0.2, 0.42, 0.38), kt - 0.08)
    paint_row(shape, 3, ACC_FILL)
    paint(shape, 3, 0, None, AGENT_INK, True)
    src(s, "Source: Milestone 5 report, Section 5.1 and Appendix V, Table A.14.")


# ----------------------------------------------------------------------------- 6 Data understanding
def balance_chart(fig):
    ax = charts.axes(fig)
    charts.style(ax)
    cats = [T("Day 13 list population"), T("Day 14 KPI population"), T("Day 27 list population"),
            T("Range over the 22 runs")]
    vals = [45.3, 45.3, 44.2]
    for i, (v, c) in enumerate(zip(vals, [C_GREY, C_ACC, C_GREY])):
        ax.barh(i, v, height=0.62, color=c, zorder=3)
        ax.text(v - 1.2, i, fmt(v) + "%", va="center", ha="right", fontsize=PT["small"] + 2, color="white",
                fontweight="bold", zorder=4)
    ax.plot([24.9, 58.3], [3, 3], color=C_INK, lw=2.5, zorder=3, solid_capstyle="butt")
    ax.plot([24.9, 58.3], [3, 3], "|", color=C_INK, ms=16, mew=2.5, zorder=4)
    ax.text(23.4, 3, fmt(24.9) + "%", ha="right", va="center", fontsize=PT["small"] + 2, color=C_INK)
    ax.text(59.8, 3, fmt(58.3) + "%", ha="left", va="center", fontsize=PT["small"] + 2, color=C_INK)
    ax.axvline(50, color=C_MUTED, lw=1.2, ls="--", zorder=2)
    ax.text(51, -0.55, T("even split, 50%"), ha="left", va="bottom", fontsize=PT["small"], color=C_MUTED)
    ax.set_yticks(range(4), cats)
    ax.set_ylim(3.55, -0.85)
    ax.set_xlim(0, 72)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="y", labelsize=PT["small"] + 2, labelcolor=C_INK)


def s33(prs):
    s = kit.base(prs, kicker(33), T("Outcome Balance and Skewed Activity"), notes(33))
    y = lead(s, T("Completers and non-completers are close in number, so no resampling is needed, while activity is "
                  "so skewed that counts enter models as logarithms."))
    dec = [tb("Profile: ", "all 10.9 million rows of the seven raw tables, not a sample; 13 figures recounted by "
                           "separate code, all 13 in agreement."),
           tb("Decision: ", "no resampling or reweighting; counts enter models as logarithms; no value is removed; AQ1, "
                            "the descriptive question, reports Fail and Withdrawn apart.")]
    dh = card_h(None, dec, CWI, pt=PT["body"])
    dy = END - dh
    card(s, X0, dy, CWI, None, dec, pt=PT["body"], h=dh)
    lw = 6.6
    rx, rw = X0 + lw + 0.35, CWI - lw - 0.35
    bottom = dy - 0.25
    hy = heading(s, X0, y, lw, T("Non-completion (Fail or Withdrawn), share of enrolments"))
    mix = [T("Mix by module: withdrawal is highest in the CCC runs (43–46%); GGG has the fewest withdrawals but the "
             "most failures.")]
    bkey = T("Key: orange = the KPI population, the 28,061 enrolments still registered at day 14 (54.7% completed); "
             "grey = enrolments registered at the list cut-offs, day 13 and day 27; line = lowest and highest run.")
    mh = rich_h(mix, lw)
    kh = lh(bkey, lw, PT["small"])
    ch = bottom - mh - 0.1 - kh - 0.05 - hy
    kit.room("p2 balance chart", 1.7, ch)
    chart(s, "m5-full-p2-balance", X0, hy, lw, ch, balance_chart)
    key(s, hy + ch + 0.05, bkey, X0, lw)
    rich(s, X0, bottom - mh, lw, mix)
    ty = y + 0.05
    tiles = [(T("602"), T("median clicks")), (T("3,365"), T("with no click")),
             (T("2,503"), T("outliers")), (T("6,977"), T("in one record"))]
    tkey = T("Key: clicks per enrolment over a run. 602 and 6,977 count clicks, the others enrolments; outliers lie "
             "beyond the upper fence of the interquartile range; one record = one student, one page, one day.")
    tkh = lh(tkey, rw, PT["small"])
    key(s, bottom - tkh, tkey, rx, rw)
    tw = (rw - 0.2) / 2
    th = (bottom - tkh - 0.1 - ty - 0.15) / 2
    kit.room("p2 activity tiles", 2 * (kit.num_h(PT["number"]) + 0.05 + max(lh(b, tw - 0.3) for _, b in tiles) + 0.06)
             + 0.15,
             bottom - tkh - 0.1 - ty)
    for k, (a, b) in enumerate(tiles):
        x, yy = rx + (k % 2) * (tw + 0.2), ty + (k // 2) * (th + 0.15)
        rect(s, I(x), I(yy), I(tw), I(th), fill=SOFT, line=LINE, radius=True)
        nh = kit.num_h(PT["number"]) + 0.05 + lh(b, tw - 0.3)
        bignum(s, x, yy + (th - nh) / 2, tw, a, b)
    src(s, "Source: Milestone 5 report, Section 6 and Appendix VI.")


def s34(prs):
    s = kit.base(prs, kicker(34), T("The Populations Behind Every Number"), notes(34))
    y = lead(s, T("Every later number refers to one of seven populations, set by year and by the day a student is "
                  "counted as enrolled."))
    rows = [[T("Population"), T("Enrolments"), T("Non-completers"), T("Used by")],
            [T("All 2013 enrolments (9 runs)"), "13,529", T("6,959 (51.4%)"), T("AQ1, second denominator")],
            [T("2013, registered at day 14"), "12,076", T("5,515 (45.7%)"), T("AQ1, primary denominator")],
            [T("2013, registered at day 13"), "12,080", "5,519", T("AQ3 development, day 13")],
            [T("2013, registered at day 27"), "11,811", T("5,245 (44.4%)"), T("AQ2; AQ3 development, day 27")],
            [T("2013, day 27, 7 runs with a task due"), "9,960", "–", T("AQ2 task-based signs")],
            [T("2014, registered at day 14"), "15,985", T("7,185 (44.9%)"), T("AQ1, primary denominator")],
            [T("2014 test (13 runs), day 13 and day 27"), T("15,989 and 15,724"), T("day 27: 6,911 (44.0%)"),
             T("AQ2 replication; AQ3 and AQ4 test")]]
    key34 = T("Key: registered at day d = registered by day d and not unregistered by it; day 14 = end of the "
              "add-drop window on OULAD; day 13 and day 27 = cut-offs of the week-3 and week-5 lists. AQ1 descriptive, "
              "AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking question. Orange rows = the AQ1 primary "
              "denominators and the single test population.")
    rule = [tb("Split rule: ", "models are developed on the 9 runs of 2013 and tested once on the 13 runs of 2014; "
                               "AQ1 and AQ2 describe both years.")]
    kb = bottom_key(s, key34)
    rb = kb - 0.15 - rich_h(rule, CWI, PT["body"])
    rich(s, X0, rb, CWI, rule, pt=PT["body"])
    shape = grid_table(s, "populations", y, rows, (0.34, 0.17, 0.2, 0.29), rb - 0.15)
    for i in (2, 6, 7):
        paint_row(shape, i, ACC_FILL)
        paint(shape, i, 0, None, AGENT_INK, True)
    src(s, "Source: Milestone 5 report, Section 6, Table 6.1.")


def s35(prs):
    s = kit.base(prs, kicker(35), T("Three Quality Issues That Change the Method"), notes(35))
    y = lead(s, T("Of nineteen logged quality issues, three are serious enough to change the method."))
    y = rich(s, X0, y, CWI, [
        tb("Issue log: ", "19 issues, each rated against the questions: High = ignoring it would change a rate, the "
                          "target or a feature; Medium = it changes a measure by a known amount; Low = otherwise.")],
        pt=PT["body"]) + 0.1
    lw = 5.4
    rx = X0 + 0.25 + lw + 0.7
    rw = XR - rx
    text(s, I(X0 + 0.25), I(y), I(lw), I(0.3), T("High issue"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    text(s, I(rx), I(y), I(rw), I(0.3), T("Change in method"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    y += 0.38
    rows = [(T("18 of 24 exams have no result rows, so counting exams would make every student of those modules "
               "miss one."),
             T("A task means a TMA or a CMA only (TMA: tutor-marked assignment; CMA: computer-marked assessment, a "
               "quiz).")),
            (T("Few tasks fall due by the cut-offs: no 2013 run has a task due by day 13, and 7 of 9 have one by day "
               "27."), T("The early-sign rule needs an activity part: a week with no click.")),
            (T("The data are seven UK modules of 2013–2014."),
             T("The scope is stated with every result, and students are compared within module."))]
    other = [tb("Medium and Low issues: ", "duplicate click rows, activity after unregistration, missing values and "
                                           "outliers are handled by flags, truncation or a \"Missing\" group; "
                                           "nothing is deleted or imputed (") + [(ref(36) + ").", INK, False)]]
    oh = card_h(None, other, CWI, pt=PT["body"])
    q_key = T("Key: the orange row marks the issue that reshapes the early-sign rule (") + ref(40) + ")."
    room_rows = END - oh - 0.3 - lh(q_key, CWI, PT["small"]) - 0.08 - y
    gap = 0.18
    rpt = PT["body"]
    if sum(max(lh(a, lw - 0.3, rpt), lh(b, rw - 0.3, rpt)) + 0.22 for a, b in rows) + 2 * gap > room_rows:
        rpt = BODY
    hs = [max(lh(a, lw - 0.3, rpt), lh(b, rw - 0.3, rpt)) + 0.22 for a, b in rows]
    kit.room("p2 quality rows", sum(hs) + 2 * gap, room_rows)
    grow = max(0.0, (room_rows - sum(hs) - gap * (len(rows) - 1)) / len(rows))
    for k, ((a, b), h) in enumerate(zip(rows, hs)):
        h += grow
        acc = k == 1
        if acc:
            rect(s, I(X0), I(y), I(0.12), I(h), fill=WARM)
        node(s, X0 + 0.25, y, lw, h, None, [a], "agent" if acc else "white", body_pt=rpt, align=PP_ALIGN.LEFT)
        arrow(s, X0 + 0.25 + lw + 0.08, y + h / 2, rx - 0.08, y + h / 2)
        node(s, rx, y, rw, h, None, [b], "white", body_pt=rpt, align=PP_ALIGN.LEFT)
        y += h + gap
    key(s, y - gap + 0.08, q_key)
    card(s, X0, END - oh, CWI, None, other, pt=PT["body"], h=oh)
    src(s, "Source: Milestone 5 report, Sections 6 and 6.1, Table 6.2, and Appendix VI, Table A.15.")


def s36(prs):
    s = kit.base(prs, kicker(36), T("Duplicates, Missing Values and Invalid Records"), notes(36))
    y = lead(s, T("Every other issue gets a stated rule, and the two whose size is known become sensitivity runs "
                  "instead of silent choices."))
    rows = [[T("Issue"), T("Evidence"), T("Severity"), T("Decision")],
            [T("Duplicate click rows"), T("787,170 rows (7.39%) repeat another exactly, carrying 3.19% of clicks"),
             T("Medium"), T("Keep every row, sum by day; a de-duplicated twin of each click feature")],
            [T("Late CMAs"), T("32,991 of 69,956 CMAs late; counting them would raise the share the rule flags at "
                               "day 27 from 28.8% to 41.2%"), T("Medium"), T("The rule uses TMA lateness; late CMAs in a "
                                                                 "sensitivity run")],
            [T("Missing deprivation band"), T("1,111 enrolments (3.41%), who pass in 65.7% of cases against 46.6%"),
             T("Medium"), T("Kept as its own \"Missing\" group; never imputed")],
            [T("Activity after unregistration"), T("98,745 clicks and 588 submissions after the student left"),
             T("Medium"), T("Truncated at the unregistration day")],
            [T("Banked results"), T("1,909 results carried over from an earlier attempt, dated −1"), T("Medium"),
             T("Known at registration, never timed")],
            [T("Outliers"), T("2,503 enrolments beyond the upper fence; one record of 6,977 clicks"), T("Low"),
             T("Every value kept; logarithms in model inputs")]]
    key36 = T("Key: TMA = tutor-marked assignment; CMA = computer-marked assessment (a quiz); orange rows = issues "
              "kept visible as a sensitivity run; upper fence = the outlier bound from the interquartile range.")
    kb = bottom_key(s, key36)
    shape = grid_table(s, "other issues", y, rows, (0.2, 0.37, 0.11, 0.32), kb - 0.12)
    for i in (1, 2):
        paint_row(shape, i, ACC_FILL)
        paint(shape, i, 0, None, AGENT_INK, True)
    src(s, "Source: Milestone 5 report, Section 6.1, Table 6.2, and Appendix VI, Table A.15.")


def s37(prs):
    s = kit.base(prs, kicker(37), T("Time Coverage and Representativeness"), notes(37))
    y = lead(s, T("The run structure leaves one honest test, train on 2013 and test on 2014, and the narrow sample "
                  "means every result needs a re-check at the university."))
    msg = T("Results describe OULAD: groups are compared within module, and each result is re-checked on the "
            "university's records before decisions D1–D3.")
    mh = lh(msg, CWI - 0.6, PT["lead"], True) + 0.3
    my = END - mh
    closing_box(s, my, msg, h=mh)
    k37 = T("Key: D1 = whom to contact; D2 = where to place support time; D3 = whether to extend the approach. Twin = "
            "an earlier run of the same module and start month.")
    kh = lh(k37, CWI, PT["small"])
    key(s, my - 0.1 - kh, k37)
    bottom = my - 0.1 - kh - 0.15
    lw = (CWI - 0.3) / 2
    rx = X0 + lw + 0.3
    time_ = [tb("Busiest weeks: ", "weekly clicks peak in week 3, so the cut-offs at day 13 and day 27 fall in the "
                                   "weeks of highest activity."),
             tb("One earlier run: ", "each module has at most one earlier run of the same start month, so the only "
                                     "test on a later run is to train on 2013 and test on 2014.")]
    tpt = PT["body"] if bottom - y - card_h(T("Time coverage"), time_, lw, pt=PT["body"]) - 0.2 >= 1.1 else BODY
    th = card_h(T("Time coverage"), time_, lw, pt=tpt)
    card(s, X0, y, lw, T("Time coverage"), time_, h=th, pt=tpt)
    fy = y + th + 0.2
    fh = bottom - fy
    kit.room("p2 split flow", 1.0, fh)
    nw = (lw - 0.45) / 2
    node(s, X0, fy, nw, fh, T("Train: 2013"), [T("9 runs of six modules")], "white", body_pt=BODY)
    arrow(s, X0 + nw + 0.06, fy + fh / 2, X0 + nw + 0.39, fy + fh / 2)
    node(s, X0 + nw + 0.45, fy, nw, fh, T("Test once: 2014"),
         [T("13 runs: 9 with a twin in 2013, 4 unseen")], "agent", body_pt=BODY)
    rep = [tb("Chosen modules: ", "the publisher chose modules partly because many students failed them, so rates "
                                  "are likely above a typical program's."),
           tb("Distance learners: ", "70.4% are under 35, and 63.1% study 60 credits or fewer."),
           tb("Uneven mix: ", "women are 11.5% of the enrolments of EEE and 88.4% of those of BBB."),
           tb("Unseen module: ", "module CCC appears only in the test year.")]
    pt = PT["body"] if card_h(T("Representativeness"), rep, lw, pt=PT["body"]) <= bottom - y else BODY
    card(s, rx, y, lw, T("Representativeness"), rep, pt=pt, h=bottom - y)
    src(s, "Source: Milestone 5 report, Section 6.2 and Appendix VI.")


def s38(prs):
    s = kit.base(prs, kicker(38), T("Sensitive Fields and Privacy"), notes(38))
    y = lead(s, T("We keep six sensitive attributes for the fairness audit and out of the predictors, because bias "
                  "cannot be audited without knowing group membership."))
    lw = 6.9
    rx, rw = X0 + lw + 0.3, CWI - lw - 0.3
    rows = [[T("Attribute"), T("Role"), T("Known group size")],
            [T("Gender"), T("Audit only"), T("Women 11.5% of EEE, 88.4% of BBB")],
            [T("Age band"), T("Audit only"), T("Aged 55 or over: 216 enrolments")],
            [T("Declared disability"), T("Audit only; fairness group"), T("3,164 enrolments")],
            [T("Deprivation band"), T("Audit only; fairness group"), T("1,111 with a missing band, its own group")],
            [T("Region"), T("Audit only"), "–"],
            [T("Highest education"), T("Predictor, also audited"), T("Postgraduates: 313 enrolments")]]
    key38 = T("Key: orange row = the one attribute used as a predictor. Deprivation band = the deprivation level of the "
              "home area, not of the student.")
    kh = lh(key38, lw, PT["small"])
    key(s, END - kh, key38, X0, lw)
    shape = grid_table(s, "sensitive attributes", y, rows, (0.3, 0.32, 0.38), END - kh - 0.1, w=lw)
    paint_row(shape, 6, ACC_FILL)
    paint(shape, 6, 0, None, AGENT_INK, True)
    cards_ = [(T("Why we keep them"), [T("Bias can enter through proxies, other fields that carry the same "
                                         "information, so removing the attributes hides bias instead of preventing "
                                         "it."),
                                       T("A published fairness study on OULAD reproduced a gap of five to six "
                                         "percentage points in favour of male students.")], "shield"),
              (T("Privacy"), [T("Under Vietnam's Personal Data Protection Law, re-identifying de-identified data is "
                                "prohibited, so OULAD is never linked to another source."),
                              T("In a pilot, a declared disability is health information and needs the student's "
                                "consent.")], "lock")]
    ch = (END - y - 0.25) / 2
    pt = fill_pt(cards_, rw, ch, lambda it, w, p: icon_card_h(it[0], it[1], w, p))
    for k, (a, b, ic) in enumerate(cards_):
        icon_card(s, rx, y + k * (ch + 0.25), rw, ch, ic, a, b, pt=pt)
    src(s, "Source: Milestone 5 report, Section 6.2 and Appendix VI, Table A.16; the fairness study and the law are in "
           "its reference list.")


# ----------------------------------------------------------------------------- 7 Preparation
def s39(prs):
    s = kit.base(prs, kicker(39), T("Who Counts: the Add-drop Rule"), notes(39))
    y = lead(s, T("We count only students still registered at day 14, because that is when registration closes on "
                  "OULAD."))
    y = rich(s, X0, y, CWI, [tb("University rule: ", "the completion rate counts students enrolled after the add-drop "
                                                     "period."),
                             tb("OULAD proxy: ", "an enrolment counts when it is still registered at day 14, because "
                                                 "registration closes two weeks after a run starts.")])
    rule = [tb("One population rule: ", "an enrolment counts on day d when the student registered by day d and had not "
                                        "unregistered by it. It removes the 58 late registrants (days 16–167) from the "
                                        "KPI population and gives each list the students it can name on its day."),
            [(T("The denominator alone can move a run's rate by up to 13.6 points (") + ref(66) + ").", INK, False)]]
    pt = PT["body"]
    key_ = T("Key: the orange marker is the KPI (key performance indicator) population; grey markers are the "
             "populations of the two lists.")
    below = card_h(None, rule, CWI, pt=pt)
    ry = END - below
    block = 2.5 + lh(key_, CWI, PT["small"])
    kit.room("p2 add-drop timeline", y + block, ry - 0.25)
    ya = y + 1.25 + (ry - 0.25 - y - block) / 2
    ky = ya + 1.25
    xa, xb = 1.0, 12.4
    dx = lambda d: xa + d / 30 * (xb - xa)         # noqa: E731
    rect(s, I(xa), I(ya - 0.02), I(xb - xa), I(0.04), fill=GREY)
    for d in (0, 7, 21):
        rect(s, I(dx(d) - 0.01), I(ya - 0.06), I(0.02), I(0.12), fill=GREY)
        text(s, I(dx(d) - 0.5), I(ya + 0.1), I(1.0), I(0.25), T("Day {d}").format(d=d), size=PT["small"],
             color=KEY, align=PP_ALIGN.CENTER, spacing=1.0)
    text(s, I(xb + 0.08), I(ya - 0.15), I(0.6), I(0.3), T("days"), size=PT["small"], color=KEY, spacing=1.0)
    marks = [(13, False, T("Day 13 (end of week 2): week-3 list"), T("28,069 enrolments"), "above"),
             (14, True, T("Day 14: the completion KPI"), T("28,061 enrolments"), "below"),
             (27, False, T("Day 27 (end of week 4): week-5 list"), T("27,535 enrolments"), "above")]
    for d, acc, head, body, where in marks:
        c = WARM if acc else GREY
        dot = s.shapes.add_shape(9, I(dx(d) - 0.14), I(ya - 0.14), I(0.28), I(0.28))
        dot.fill.solid()
        dot.fill.fore_color.rgb = c
        dot.line.fill.background()
        lw_ = 3.6
        lx = min(dx(d) - lw_ / 2, XR - lw_)
        if where == "above":
            rect(s, I(dx(d) - 0.01), I(ya - 0.6), I(0.02), I(0.46), fill=LINE)
            rich(s, lx, ya - 1.2, lw_, [[(head, INK, True)], body], pt=PT["small"] + 2, align=PP_ALIGN.CENTER)
        else:
            rect(s, I(dx(d) - 0.01), I(ya + 0.14), I(0.02), I(0.36), fill=LINE)
            rich(s, lx, ya + 0.5, lw_, [[(head, AGENT_INK, True)], body], pt=PT["small"] + 2,
                 align=PP_ALIGN.CENTER)
    key(s, ky, key_)
    card(s, X0, ry, CWI, None, rule, pt=pt, h=below)
    src(s, "Source: Milestone 5 report, Sections 2.1, 6 and 11.2, Tables 2.1 and 6.1, and Appendices III, V and VII.")


def s40(prs):
    s = kit.base(prs, kicker(40), T("The Early-sign Rule"), notes(40))
    y = lead(s, T("Few tasks fall due in the first weeks, so the early-sign rule also counts a week without "
                  "activity."))
    lw = 4.3
    y1 = card(s, X0, y, lw, T("Milestone 1 rule"), [T("Two or more assessed tasks missed or late by week 4.")])
    due = [T("One or more tasks fall due by day 27 in 16 of 22 runs, and by day 13 in only 1; no 2013 run has a task "
             "due by day 13.")]
    dy = END - rich_h(due, lw)
    bh = dy - 0.2 - (y1 + 0.2)
    num_label = T("runs has two or more tasks due by day 27.")
    nh = kit.num_h(PT["number"]) + 0.05 + lh(num_label, lw - 0.3)
    kit.room("p2 rule number", y1 + 0.2 + nh + 0.24, dy - 0.2)
    rect(s, I(X0), I(y1 + 0.2), I(lw), I(bh), fill=SOFT, line=LINE, radius=True)
    bignum(s, X0, y1 + 0.2 + (bh - nh) / 2, lw, T("1 of 22"), num_label, color=WARM)
    rich(s, X0, dy, lw, due)
    rx, rw = X0 + lw + 0.4, CWI - lw - 0.4
    text(s, I(rx), I(y), I(rw), I(0.6), T("Early-sign rule (final): by the data cut-off, any one of three parts"),
         size=HEAD, color=NAVY, bold=True, spacing=1.0)
    parts = [(T("Missed task"), T("a TMA or CMA due by the cut-off, not submitted"), "white", "document"),
             (T("Late TMA"), T("a TMA submitted late"), "white", "clock"),
             (T("No click in the last 7 days"), T("no platform activity in the seven days before the cut-off"), "agent",
              "calendar")]
    xs, cw = cols(3, 0.2, rx, rw)
    key_ = T("Key: the orange part is the activity part added for the data. TMA: tutor-marked assignment; CMA: "
             "computer-marked quiz. Cut-off: day 13 for the week-3 list, day 27 for the week-5 list.")
    more = [T("One rule serves OULAD and the pilot. AQ2, the diagnostic question, tests these three parts and two more "
              "activity signs: activity below the run median and no click before the start."),
            tb("Late quizzes stay out: ", "the meaning of a late CMA in 2013–2014 is not documented, and counting them "
                                          "would raise the share flagged at day 27 from 28.8% to 41.2%."),
            tb("Reach: ", "the rule flags 20.2% of 28,069 enrolments at day 13 and 28.8% of 27,535 at day 27.")]
    my = END - rich_h(more, rw)
    ph = my - 0.15 - lh(key_, rw, PT["small"]) - 0.08 - (y + 0.45)
    kit.room("p2 rule parts", 2.1, ph)
    for x, (a, b, st, ic) in zip(xs, parts):
        node(s, x, y + 0.45, cw, ph, a, [b], st, body_pt=BODY, icon=ic)
    key(s, y + 0.45 + ph + 0.08, key_, rx, rw)
    rich(s, rx, my, rw, more)
    src(s, "Source: Milestone 5 report, Sections 2.1 and 6.1, and Appendices II, III and VI.")


def s41(prs):
    s = kit.base(prs, kicker(41), T("Three Rules That Govern Preparation"), notes(41))
    y = lead(s, T("Preparation deletes or imputes nothing, dates every feature by its cut-off, and learns every "
                  "parameter from the training runs alone."))
    msg = T("Before any record changed, each issue got a decision, its reason and a check that fails if the decision "
            "is not carried out: 22 checks, all passing.")
    mh = lh(msg, CWI - 0.6, PT["lead"], True) + 0.3
    my = END - mh
    closing_box(s, my, msg, h=mh)
    rules = [(T("1 · Delete or impute nothing"), T("Nothing recorded is deleted or imputed in the prepared views."),
              T("Every count traces back to the raw files; only model fitting fills or scales values."),
              T("Missing counts and value ranges are the same after preparation as before.")),
             (T("2 · Date every feature"), T("Every feature uses only events dated on or before its cut-off, day 13 "
                                             "or day 27."),
              T("No information from after the moment of the list can reach a model."),
              T("A recount without the date filter differs only where later clicks exist.")),
             (T("3 · Learn from training runs only"), T("Every learned parameter, such as a median or a scale, comes "
                                                        "from the 2013 training runs alone."),
              T("The 2014 runs stay an independent test."),
              T("Parameters stay unchanged when test rows are altered."))]
    xs, cw = cols(3, 0.25)
    ch = my - 0.25 - y

    def paras(r):
        return [[(r[1], INK, True)], tb("Why: ", r[2]), tb("Check: ", r[3], OUT_INK)]
    pt = fill_pt(rules, cw, ch, lambda r, w, p: card_h(r[0], paras(r), w, pt=p, hp=PT["head"]))
    if all(card_h(r[0], paras(r), cw, pt=PT["lead"], hp=PT["head"]) <= ch for r in rules):
        pt = PT["lead"]
    kit.room("p2 rule cards", max(card_h(r[0], paras(r), cw, pt=pt, hp=PT["head"]) for r in rules), ch)
    for x, r in zip(xs, rules):
        card(s, x, y, cw, r[0], paras(r), h=ch, pt=pt, hp=PT["head"])
    src(s, "Source: Milestone 5 report, Sections 7 and 7.2, and Appendix VII, Tables A.17 and A.20.")


def s42(prs):
    s = kit.base(prs, kicker(42), T("Preparation Decision Matrix"), notes(42))
    y = lead(s, T("Every preparation need has one decision, and one check that fails if the decision is not carried "
                  "out."))
    rows = [[T("Need"), T("Decision"), T("Check that would fail")],
            [T("Population"), T("Flags for days 13, 14 and 27; views keep those enrolled"),
             T("Populations equal the profile")],
            [T("Missing values"), T("\"Missing\" category or indicator; no imputation"),
             T("Counts unchanged; filling from training rows")],
            [T("Duplicates, keys, joins"), T("All rows kept; clicks summed by day; left joins"),
             T("Unique keys; totals reconcile; no row lost")],
            [T("Invalid values, outliers"), T("Labels corrected; carried-over results untimed; values kept"),
             T("Every category in its set; ranges unchanged")],
            [T("Activity after withdrawal"), T("Truncated at the unregistration day"),
             T("No click or submission counted after it")],
            [T("Derived features"), T("Assignment and quiz tasks; early-sign rule; run-median activity"),
             T("Features recomputed by separate code")],
            [T("Time, encoding"), T("Cut-offs at days 13 and 27; transforms learned on training rows"),
             T("Date-filter recount; parameters stable")],
            [T("Sensitive attributes, split"), T("Audit columns outside predictors; train 2013, test 2014"),
             T("No audit predictor; no run in both parts")]]
    grid_table(s, "decision matrix", y, rows, (0.24, 0.44, 0.32), END)
    src(s, "Source: Milestone 5 report, Section 7, Table 7.1, and Appendix VII, Table A.17.")


def s43(prs):
    s = kit.base(prs, kicker(43), T("Ten Scripted Steps"), notes(43))
    y = lead(s, T("Preparation runs in ten scripted steps with no manual step, and no join loses or multiplies a "
                  "row."))
    y = heading(s, X0, y, CWI, T("The ten steps, in order"))
    row1 = [(T("1 Load and check"), T("raw tables against SHA-256 checksums"), "white", "shield"),
            (T("2 Select"), T("the populations at days 13, 14 and 27"), "white", "filter"),
            (T("3 Standardise"), T("3,516 deprivation band labels fixed"), "white", "gear"),
            (T("4 Keys and duplicates"), T("10,655,280 click rows into 1,808,119 enrolment-days"), "agent", "layers"),
            (T("5 Missing values"), T("1,111 missing bands; doubtful records flagged"), "white", "flag")]
    row2 = [(T("6 Invalid values"), T("98,745 clicks recorded after withdrawal left out"), "white", "cross"),
            (T("7 Integrate"), T("286,898 enrolment-task rows"), "agent", "table"),
            (T("8 Build features"), T("at day 13 and at day 27"), "white", "chart"),
            (T("9 Analysis views"), T("the prepared views for each question"), "white", "document"),
            (T("10 Save"), T("with a dictionary, lineage and version record"), "out", "document")]
    joins = [tb("Joins that keep every row: ", "integration starts from the enrolment table, one row for each of the "
                                               "32,593 enrolments, and adds each other table by a left join after "
                                               "summing it to the enrolment; all 25 joins kept their input rows, and "
                                               "the 3,365 enrolments with no click stay in.")]
    jkey = T("Key: orange = steps that change the grain of the data (one row per enrolment and day, or per enrolment "
             "and task).")
    jh = card_h(None, joins, CWI, pt=BODY)
    jy = END - jh
    card(s, X0, jy, CWI, None, joins, pt=BODY, h=jh)
    kh = lh(jkey, CWI, PT["small"])
    ky = jy - 0.2 - kh
    key(s, ky, jkey)
    gap = 0.28
    nh = (ky - 0.1 - y - gap) / 2
    xs, w = cols(5, 0.3)
    kit.room("p2 pipeline nodes", 2 * max(node_h(a, [b], w, body_pt=BODY) for a, b, *_ in row1 + row2) + gap,
             ky - 0.1 - y)
    for k, (a, b, st, ic) in enumerate(row1):
        node(s, xs[k], y, w, nh, a, [b], st, body_pt=BODY)
        if k < 4:
            arrow(s, xs[k] + w + 0.03, y + nh / 2, xs[k + 1] - 0.03, y + nh / 2)
    y2 = y + nh + gap
    path(s, [(xs[4] + w / 2, y + nh + 0.02), (xs[4] + w / 2, y + nh + gap / 2), (xs[0] + w / 2, y + nh + gap / 2),
             (xs[0] + w / 2, y2 - 0.02)])
    for k, (a, b, st, ic) in enumerate(row2):
        node(s, xs[k], y2, w, nh, a, [b], st, body_pt=BODY)
        if k < 4:
            arrow(s, xs[k] + w + 0.03, y2 + nh / 2, xs[k + 1] - 0.03, y2 + nh / 2)
    src(s, "Source: Milestone 5 report, Section 7 and Appendix VII; Milestone 3 report, pipeline steps table.")


def s44(prs):
    s = kit.base(prs, kicker(44), T("Derived Variables and Encoding"), notes(44))
    y = lead(s, T("We derive activity, task and rule variables dated to each cut-off, giving 19 usable predictors "
                  "encoded so that a model can handle an unseen module."))
    lw = 7.5
    rx, rw = X0 + lw + 0.3, CWI - lw - 0.3
    rows = [[T("Derived variable"), T("Meaning, at cut-off c")],
            [T("Clicks before the start"), T("Clicks before day 0")],
            [T("Clicks and active days"), T("Clicks, and days with a click, from day 0 to c")],
            [T("Activity against the run"), T("(clicks + 1) ÷ (median clicks of the same run + 1)")],
            [T("No click in the last 7 days"), T("No click on days c − 6 to c")],
            [T("Missed tasks"), T("A TMA or CMA due by c, due on or after the registration day, not submitted")],
            [T("Late tasks"), T("Submitted after the due day but by c, counted by type")],
            [T("Early-sign rule"), T("A missed task, a late TMA, or no click in the last 7 days")]]
    key44 = T("Key: c = cut-off day (13 or 27); TMA = tutor-marked assignment; CMA = computer-marked assessment (a "
              "quiz); fold = the 2013 runs with one run held out.")
    kh = lh(key44, lw, PT["small"])
    key(s, END - kh, key44, X0, lw)
    shape = grid_table(s, "derived variables", y, rows, (0.36, 0.64), END - kh - 0.1, w=lw)
    paint_row(shape, 7, ACC_FILL)
    paint(shape, 7, 0, None, AGENT_INK, True)
    side = [(T("Never used"), [T("Activity after the cut-off, the withdrawal day, the final result, and TMA marks, "
                                 "which have no release day.")], MINUS, BAD_FILL, MINUS),
            (T("Predictor set"), [T("19 usable predictors, 23 parameters once module and start month are coded."),
                                  T("The mean CMA mark is set aside: known for only 1.4% (day 13) and 5.2% (day 27) "
                                    "of training rows, below the 10% required.")], NAVY, SOFT, LINE),
            (T("Encoding"), [T("Counts as log(1 + count); transforms refitted in each development fold; module "
                               "terms coded so an unseen module gets the average effect.")], NAVY,
             SOFT, LINE)]
    avail = END - y - 2 * 0.2
    pt = PT["body"] if sum(card_h(a, b, rw, pt=PT["body"]) for a, b, *_ in side) <= avail else BODY
    hs = [card_h(a, b, rw, pt=pt) for a, b, *_ in side]
    kit.room("p2 derived side", sum(hs), avail)
    extra = max(0.0, (avail - sum(hs)) / 3)
    yy = y
    for (a, b, c, fill, line), h in zip(side, hs):
        card(s, rx, yy, rw, a, b, color=c, fill=fill, line=line, h=h + extra, pt=pt)
        yy += h + extra + 0.2
    src(s, "Source: Milestone 5 report, Section 7.1 and Appendix VII, Table A.18.")


def s45(prs):
    s = kit.base(prs, kicker(45), T("Leakage Control"), notes(45))
    y = lead(s, T("Leakage, using information that would not exist at the moment of prediction, is blocked in four "
                  "ways, and the date-filter check is built so that it can fail."))
    xa, xb, xc = 0.8, 12.6, 7.1
    ya = y + 0.82
    rect(s, I(xa), I(ya - 0.02), I(xb - xa), I(0.04), fill=GREY)
    text(s, I(xa - 0.4), I(ya + 0.08), I(1.2), I(0.25), T("Day 0"), size=PT["small"], color=KEY,
         align=PP_ALIGN.CENTER, spacing=1.0)
    cut = rect(s, I(xc - 0.015), I(ya - 0.8), I(0.03), I(1.05), fill=NAVY)
    cut.line.fill.background()
    text(s, I(xc - 2.5), I(ya + 0.28), I(5.0), I(0.28), T("Data cut-off: day 27 (the same rule holds at day 13)"),
         size=PT["small"] + 2, color=NAVY, bold=True, align=PP_ALIGN.CENTER, spacing=1.0)
    left = [T("Registration"), T("Clicks up to day 27"), T("Tasks due by day 27")]
    right = [T("Later clicks"), T("Withdrawal day"), T("Final result")]
    lxs, lw = cols(3, 0.15, xa + 0.1, xc - xa - 0.35)
    for x, lab in zip(lxs, left):
        chip(s, x, ya - 0.66, lw, 0.46, lab, fill=SOFT, line_color=GREY, size=PT["small"] + 2)
    rxs, rw = cols(3, 0.15, xc + 0.25, xb - xc - 0.3)
    for x, lab in zip(rxs, right):
        chip(s, x, ya - 0.66, rw, 0.46, "", fill=BAD_FILL, line_color=MINUS)
        icon(s, "cross", x + 0.08, ya - 0.58, 0.3, color=MINUS, bg=BAD_FILL)
        text(s, I(x + 0.4), I(ya - 0.66), I(rw - 0.45), I(0.46), lab, size=PT["small"] + 2, color=MINUS,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    y = key(s, ya + 0.6, T("Key: grey = events left of the cut-off that may feed a feature; red cross = events right "
                           "of it that never enter. TMA = tutor-marked assignment.")) + 0.15
    check = [tb("The check can fail: ", "recounting the click features without the date filter changes them only for "
                                        "the enrolments that clicked after the cut-off, 26,755 at day 13 and 25,663 "
                                        "at day 27, and for no other.")]
    chh = card_h(None, check, CWI)
    cy = END - chh
    card(s, X0, cy, CWI, None, check, h=chh, fill=OUT_FILL, line=PLUS)
    rows = [[T("Form of leakage"), T("Case in OULAD"), T("Control")],
            [T("Target leakage"), T("Final result, withdrawal day, later activity, TMA marks"),
             T("Features only from events dated up to the cut-off")],
            [T("Train–test contamination"), T("Medians, scales and levels computed on all runs"),
             T("Learned on 2013 only, refitted inside each fold")],
            [T("Student leakage"), T("1,586 test enrolments at day 27 of students seen in 2013"),
             T("Kept in the test; removed in a strict check")],
            [T("Temporal leakage"), T("A random split that mixes the two years"),
             T("Train on 9 runs of 2013, test on 13 of 2014")]]
    grid_table(s, "leakage table", y, rows, (0.22, 0.4, 0.38), cy - 0.15, sizes=(BODY,), row_h=0.3)
    src(s, "Source: Milestone 5 report, Section 7.1 and Appendix VII, Tables A.19 and A.20.")


def s46(prs):
    s = kit.base(prs, kicker(46), T("The Final Versioned Dataset"), notes(46))
    y = lead(s, T("The prepared dataset is named and versioned, passes all 22 checks, and rebuilds byte for byte from "
                  "the public download."))
    lw = 5.2
    rx, rw = X0 + lw + 0.3, CWI - lw - 0.3
    pid = T("OULAD-N04-prepared-1.0")
    paras = [tb("Documented: ", "a data dictionary gives each of the 88 prepared variables its source, "
                                "transformation, role and sensitivity."),
             tb("Stored: ", "as Parquet files, a column-based file format."),
             tb("Rebuilt: ", "one command, from the pinned figshare download; two runs give byte-identical files."),
             tb("Shared: ", "the CC BY 4.0 licence (Creative Commons Attribution) allows sharing with attribution."),
             tb("No invented data: ", "synthetic records appear only in unit tests, never in a view or a finding.")]
    hh = 0.6
    rect(s, I(X0), I(y), I(lw), I(END - y), fill=SOFT, line=LINE, radius=True)
    rect(s, I(X0), I(y), I(lw), I(hh), fill=NAVY, radius=True)
    text(s, I(X0 + 0.15), I(y), I(lw - 0.3), I(hh), pid, size=PT["head"], color=WHITE, bold=True,
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, spacing=1.0)
    room = END - y - hh - 0.2
    pt = PT["body"] if rich_h(paras, lw - 0.36, PT["body"]) <= room else BODY
    kit.room("p2 dataset card", rich_h(paras, lw - 0.36, pt), room)
    rich(s, X0 + 0.18, y + hh + 0.1 + max(0.0, (room - rich_h(paras, lw - 0.36, pt)) / 2), lw - 0.36, paras, pt=pt)
    rows = [[T("Check"), T("Raw data → prepared data"), T("Result")],
            [T("Enrolments"), T("32,593 enrolments of 28,785 students and their outcome mix: identical"), T("Pass")],
            [T("Populations"), T("28,069 at day 13; 28,061 at day 14; 27,535 at day 27, equal to the profile"),
             T("Pass")],
            [T("Clicks"), T("39,506,354 kept; 98,745 after withdrawal left out"), T("Pass")],
            [T("Missing values"), T("Deprivation band 1,111; registration day 45; TMA score 173: identical"),
             T("Pass")],
            [T("Joins"), T("25 joins, rows in equal rows out"), T("Pass")],
            [T("Features"), T("Six features recomputed by separate code: 0 differences in 55,604 rows"), T("Pass")]]
    key46 = T("Key: TMA = tutor-marked assignment; days 13 and 27 = list cut-offs; day 14 = the KPI population.")
    kh = lh(key46, rw, PT["small"])
    key(s, END - kh, key46, rx, rw)
    shape = grid_table(s, "before-after checks", y, rows, (0.2, 0.66, 0.14), END - kh - 0.1, x=rx, w=rw)
    for i in range(1, len(rows)):
        paint(shape, i, 2, OUT_FILL, OUT_INK, True)
    src(s, "Source: Milestone 5 report, Section 7.2 and Appendix VII, Tables A.20 and A.21.")


SLIDES = {22: s22, 23: s23, 24: s24, 25: s25, 26: s26, 27: s27, 28: s28, 29: s29, 30: s30, 31: s31, 32: s32, 33: s33,
          34: s34, 35: s35, 36: s36, 37: s37, 38: s38, 39: s39, 40: s40, 41: s41, 42: s42, 43: s43, 44: s44, 45: s45,
          46: s46}
