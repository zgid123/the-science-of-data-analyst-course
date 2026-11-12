"""Plan slides 1–21 of the full Milestone 5 deck: title, hook, introduction, business understanding and the analytical
questions (ensemble plan, reports/milestone-5/presentation/v2-full/ensemble-plan.md)."""

from slides_milestone5_full.common import *   # noqa: F401,F403

YELLOW_FILL = pal_rgb("#FFF1C2")
GREY_FILL = pal_rgb("#E6E8EC")


# ----------------------------------------------------------------------------- local helpers (inches)
def heading(s, x, y, w, line, color=NAVY, pt=HEAD):
    """A bold heading line; returns the y below it."""
    h = lh(line, w, pt, True)
    text(s, I(x), I(y), I(w), I(h), line, size=pt, color=color, bold=True, spacing=1.0)
    return y + h


def bullets(items, color=NAVY):
    """Paragraphs that open with a coloured bullet."""
    return [[("•  ", color, True), (t, INK, False)] if isinstance(t, str) else [("•  ", color, True)] + t
            for t in items]


def strip(s, y, paras, fill=GREY_FILL, h=None, pt=BODY, line=None, dash=False):
    """A full-width rounded strip holding paragraphs; returns its bottom."""
    sh = h or rich_h(paras, CWI - 0.36, pt) + 0.16
    shape = rect(s, MX, I(y), CW, I(sh), fill=fill, line=line, radius=True, line_w=1.5 if line else 1.0)
    if dash:
        dashed(shape)
    rich(s, X0 + 0.18, y + 0.08, CWI - 0.36, paras, pt=pt)
    return y + sh


def strip_h(paras, pt=BODY):
    return rich_h(paras, CWI - 0.36, pt) + 0.16


def card_pt(items, w, h):
    """The largest kit size (18, 16, else 14 pt) at which every (head, paragraphs) card fits height h, with a margin
    that grows with the number of paragraphs (the renderer spaces paragraphs a little wider than the measure)."""
    return next((p_ for p_ in (PT["lead"], PT["body"])
                 if max(card_h(a, b, w, pt=p_) + 0.05 * len(b) for a, b in items) <= h - 0.15), BODY)


def colour_cell(tbl, i, j, fill, color=None, bold=None):
    c = tbl.cell(i, j)
    c.fill.solid()
    c.fill.fore_color.rgb = fill
    for p in c.text_frame.paragraphs:
        for r in p.runs:
            if color is not None:
                r.font.color.rgb = color
            if bold is not None:
                r.font.bold = bold


# ----------------------------------------------------------------------------- 1 title
def s01(prs):
    """Title slide: project title, subtitle, purpose line, lecturers and team members, course line, logo."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    title = T("Early Identification of Disengaging Students in Online Courses")
    sub = T("Final project report: from the problem to the integrated answer")
    purpose = T("A final report on finding students who drift away from online courses early enough to help them.")
    tw = 10.0
    if LOGO.exists():
        picture(s, LOGO, 11.2, 0.55, 1.5, 1.5)
    th = lh(title, tw, PT["cover"], True)
    rect(s, I(0.7), I(0.9), I(0.9), I(0.06), fill=NAVY)
    text(s, I(0.7), I(1.1), I(tw), I(th), title, size=PT["cover"], color=NAVY, bold=True, spacing=1.0)
    y = 1.1 + th + 0.2
    sh = lh(sub, tw, PT["lead"], True)
    text(s, I(0.7), I(y), I(tw), I(sh), sub, size=PT["lead"], color=INK, bold=True, spacing=1.0)
    y += sh + 0.12
    y = rich(s, 0.7, y, tw, [purpose], pt=PT["body"], color=GREY)
    members = ["25C12002 – Lê Ngọc Trúc Huỳnh", "25C12003 – Phan Trần Khanh",      # as on the report's title page
               "25C12031 – Dương Tấn Huỳnh Phong"]
    py = max(y + 0.45, 3.55)                         # lecturers on the left, the team with student IDs on the right
    lec = rich(s, 0.7, py, 5.4, [[(T("Lecturers: "), NAVY, True)], [(T("Dr. Nguyễn Trần Minh Thư"), INK, False)],
                                 [(T("MSc. Phạm Minh Tú"), INK, False)]], pt=PT["lead"])
    team = rich(s, 6.4, py, 5.6, [[(T("Team N04: "), NAVY, True)]] + [[(m, INK, False)] for m in members],
                pt=PT["lead"])
    kit.room("title people", max(lec, team) + 0.2, 5.95)
    rich(s, 0.7, 5.95, 11.8, [T("MTH045 – The Science of Data Analytics"),
                             T("University of Science, VNU-HCM · November 2026")], pt=PT["small"] + 2, color=GREY)
    s.notes_slide.notes_text_frame.text = notes(1)
    src(s, "Source: Milestone 5 report, title page.")


# ----------------------------------------------------------------------------- 2 hook
HOOK_MISSED = {"any": [78.1, 72.7], "week4": [19.6, 14.7]}      # Appendix XII, Table A.31 (day-14 population)


def hook_bars(fig):
    ax = charts.axes(fig)
    charts.bars(ax, ["2013", "2014"], {T("Missed a task at any point in the run"): HOOK_MISSED["any"],
                                       T("Missed a task by the end of week 4 (day 27)"): HOOK_MISSED["week4"]},
                horizontal=True, pct=True, digits=1, limit=100, colors=[C_GREY, C_ACC])


def s02(prs):
    s = kit.base(prs, kicker(2), T("The Surprising Number"), notes(2))
    y = lead(s, T("Nearly half of the enrolments still registered after the add-drop period did not complete, yet "
                  "fewer than one in five of these non-completers had missed a task by week 4."))
    keyl = T("Key: data = OULAD (Open University Learning Analytics Dataset), our open stand-in: 22 module runs (one "
             "offering of a module) of seven UK distance-learning modules, 2013–2014. Day 14 = end of the add-drop "
             "period. Non-completion = a fail or a withdrawal. Task = an assessed assignment or quiz, never the exam.")
    ky = bottom_key(s, keyl)
    xs, cw = cols(2, 0.3)
    items = [(T("How many do not complete"), "45.3%",
              [T("of the 28,061 enrolments still registered at day 14 did not complete (95% interval 44.7–45.8%), "
                 "over all 22 module runs.")], False),
             (T("How many show it by week 4"), T("19.6% and 14.7%"),
              [T("of the non-completers of 2013 (5,515) and of 2014 (7,185) had missed a task by the end of week 4."),
               [(T("So a list built on missed tasks alone comes too late for most of them."), AGENT_INK, True)]],
              True)]
    vh = kit.num_h(PT["number"])
    ch = max(0.16 + lh(a, cw - 0.36, HEAD, True) + 0.06 + vh + 0.08 + rich_h(c, cw - 0.36, PT["body"]) + 0.1
             for a, b, c, _ in items)
    for x, (a, b, c, acc) in zip(xs, items):
        rect(s, I(x), I(y), I(cw), I(ch), fill=ACC_FILL if acc else SOFT, line=WARM if acc else LINE, radius=True,
             line_w=2.0 if acc else 1.0)
        hy = heading(s, x + 0.18, y + 0.16, cw - 0.36, a, color=AGENT_INK if acc else NAVY)
        text(s, I(x + 0.18), I(hy + 0.06), I(cw - 0.36), I(vh), b, size=PT["number"], color=WARM if acc else NAVY,
             bold=True, spacing=1.0)
        rich(s, x + 0.18, hy + 0.14 + vh, cw - 0.36, c, pt=PT["body"])
    y += ch + 0.25
    hy = heading(s, X0, y, CWI, T("Share of the non-completers who had missed a task (%), day-14 population"))
    kit.room("hook chart", hy + 0.05 + 1.2, ky - 0.15)
    chart(s, "m5-full-p1-hook-missed", X0, hy + 0.05, CWI, ky - 0.15 - hy - 0.05, hook_bars)
    src(s, "Source: Milestone 5 report, Abstract, Section 11.2 and Appendix XII, Tables A.29 and A.31.")


# ----------------------------------------------------------------------------- 3 noticed too late (deck slide 2)
def s03(prs):
    s = kit.base(prs, kicker(3), T("Noticed Too Late"), notes(3))
    y = lead(s, T("Staff notice a student who has stopped taking part only after the early weeks, when help is "
                  "easiest."))
    y = timeline_noticed(s, y + 0.2, band_slots=(0, 4), band_label="Early weeks, when help is easiest")
    y = key(s, y - 0.05, T("Key: the orange band marks the early weeks; grey markers mark the moment each group of staff "
                           "notices."))
    y = key(s, y + 0.02, T("Basis: a published study of predictive learning analytics at the Open University finds the "
                           "window for effective support of a student at risk short, two to four weeks (Herodotou et "
                           "al., 2019); the moments staff notice come from simulated stakeholder interviews.")) + 0.25
    xs, cw = cols(3)
    items = [(T("Setting"), [T("A Vietnamese university expands online and blended learning on its learning management "
                               "system (LMS); one program has about 1,200 students (a scenario assumption).")]),
             (T("Disengagement"), [T("A student misses a task, opens the course less often and falls silent before a "
                                     "fail or a withdrawal is recorded."),
                                   T("The records show these traces weeks before any final result.")]),
             (T("The gap"), [T("Every moment of notice falls after the early weeks, so by the time anyone acts the "
                               "student has been drifting for weeks."),
                             T("Help comes when it is hardest to give.")])]
    pt = card_pt(items, cw, END - y)
    h = max(card_h(a, b, cw, pt=pt) for a, b in items)
    kit.room("noticed cards", y + h, END)
    for x, (a, b) in zip(xs, items):
        card(s, x, y, cw, a, b, h=END - y, pt=pt)
    src(s, "Source: Milestone 5 report, Section 1 and Appendix I; Herodotou et al. (2019).")


# ----------------------------------------------------------------------------- 4 our answer in brief (deck slide 3)
def s04(prs):
    s = kit.base(prs, kicker(4), T("Our Answer in Brief"), notes(4))
    y = lead(s, T("Early records give staff a factual reason beside each name now; whether a model ranks better, and "
                  "whether contact helps, still needs one held-out test on the 2014 runs and a randomised pilot."))
    terms = [tb("Non-completion: ", "a fail or a withdrawal."),
             tb("Early sign: ", "a record dated by the data cut-off, such as a task missed or a week without any "
                                "platform activity."),
             tb("Data cut-offs: ", "day 13 (end of week 2) gives the data for the week-3 list; day 27 (end of week 4) "
                                   "gives the data for the week-5 list."),
             tb("Add-drop period: ", "the first weeks in which students may still register or drop; on our data it "
                                     "ends at day 14.")]
    half = (CWI - 0.36 - 0.3) / 2
    kh_ = 0.14 + lh(T("Key terms"), 3, HEAD, True) + 0.04 + max(rich_h(terms[:2], half), rich_h(terms[2:], half)) + 0.04
    rect(s, MX, I(y), CW, I(kh_), fill=SOFT, line=LINE, radius=True)
    text(s, I(X0 + 0.18), I(y + 0.12), I(4), I(0.3), T("Key terms"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    ty_ = y + 0.16 + lh(T("Key terms"), 3, HEAD, True)
    rich(s, X0 + 0.18, ty_, half, terms[:2])
    rich(s, X0 + 0.18 + half + 0.3, ty_, half, terms[2:])
    y += kh_ + 0.25
    xs, cw = cols(3)
    items = [(T("Size"), T("45.3%"), T("of the 28,061 enrolments still registered at day 14 did not complete.")),
             (T("Timing"), T("Under 1 in 5"), T("non-completers had missed a task by week 4 (day 27).")),
             (T("Signs"), T("5 of 5"), T("early signs, from tasks and from activity, go with later non-completion in "
                                         "both years; a missed task adds 40.8 (2013) and 39.3 (2014) percentage "
                                         "points."))]
    vh = kit.num_h(PT["title"] + 6)
    open_line = [[(T("Still open: "), GREY, True),
                  (T("the prediction model and the ranked list are designed, not run; the effect of contact is "
                     "untested."), INK, False)]]
    oh = rich_h(open_line, CWI - 0.36) + 0.1
    h = max(0.14 + lh(a, cw - 0.36, HEAD, True) + 0.04 + vh + 0.04 + rich_h([c], cw - 0.36) + 0.06
            for a, b, c in items)
    kit.room("answer strip", y + h + 0.25 + oh, END)
    h = END - oh - 0.25 - y                       # the cards fill down to the open strip
    bpt = min(fit_pt([c], cw - 0.36, h - 0.3 - lh(a, cw - 0.36, HEAD, True) - vh) for a, b, c in items)
    for x, (a, b, c) in zip(xs, items):
        rect(s, I(x), I(y), I(cw), I(h), fill=SOFT, line=LINE, radius=True)
        ah = lh(a, cw - 0.36, HEAD, True)
        text(s, I(x + 0.18), I(y + 0.14), I(cw - 0.36), I(ah), a, size=HEAD, color=NAVY, bold=True, spacing=1.0)
        text(s, I(x + 0.18), I(y + 0.18 + ah), I(cw - 0.36), I(vh), b, size=PT["title"] + 6, color=WARM, bold=True,
             spacing=1.0)
        rich(s, x + 0.18, y + 0.22 + ah + vh, cw - 0.36, [c], pt=bpt)
    y = END - oh                                 # the open strip sits on the bottom edge
    rect(s, MX, I(y), CW, I(oh), fill=GREY_FILL, radius=True)
    rich(s, X0 + 0.18, y + 0.07, CWI - 0.36, open_line)
    src(s, "Source: Milestone 5 report, Abstract and Sections 2.1, 3, 10, 11.2 and 11.3.")


# ----------------------------------------------------------------------------- 5 how the talk is built
def s05(prs):
    s = kit.base(prs, kicker(5), T("How the Talk Is Built"), notes(5))
    y = lead(s, T("The talk follows the project's chain of eleven links, from the stakeholder problem to the decisions, "
                  "in six parts and the conclusions."))
    parts = [(T("Part 1 · The Problem"), T("Milestone 1"),
              [T("1 Stakeholder problem"), T("2 Measurable goal"), T("3 Analytical questions")],
              T("Context, goal, KPIs, decisions D1–D3 and questions AQ1–AQ4.")),
             (T("Part 2 · The Data"), T("Milestones 2–3"),
              [T("4 Required data"), T("5 Selected open dataset"), T("6 Actual data fit and gaps")],
              T("Requirements first, then the dataset, its fit and its quality.")),
             (T("Part 3 · Preparation"), T("Milestone 3"), [T("7 Prepared data")],
              T("Who counts, the early-sign rule, and no future information in an early sign.")),
             (T("Part 4 · Method"), T("Milestone 4"), [T("8 Candidate methods"), T("9 Evaluation design")],
              T("How each question is answered and judged, fixed before any result.")),
             (T("Part 5 · Evidence"), T("Milestone 5"), [T("10 Findings and limitations")],
              T("AQ1 and AQ2 answered on 2013 and 2014; what AQ3 and AQ4 would give.")),
             (T("Part 6 · Integration and Use"), T("Milestone 5"), [T("11 Educational decision support")],
              T("What each decision can use now, limits, next steps and the use of AI."))]
    keyl = T("Key: numbered boxes = the eleven links of the project chain, in the order the talk follows them. "
             "D1–D3 = the three decisions: whom to contact, where to place support time, whether to extend the "
             "approach. AQ1–AQ4 = the four analytical questions. KPI = key performance indicator.")
    ky = bottom_key(s, keyl)
    cy = ky + 0.05
    gap = 0.14
    rh = (cy - 0.25 - y - 5 * gap) / 6               # one lane per part, as the lanes of the report's Figure 1.1
    lw, chw, cg = 3.0, 1.4, 0.1
    cx0 = X0 + lw + 0.2
    tx = cx0 + 3 * chw + 2 * cg + 0.25
    tw_ = XR - tx - 0.1
    pt = min(fit_pt([body], tw_, rh - 0.04) for *_, body in parts)
    kit.room("talk lanes", max(rich_h([body], tw_, BODY) for *_, body in parts), rh)
    for k, (a, m, cs, body) in enumerate(parts):
        ly = y + k * (rh + gap)
        rect(s, I(X0), I(ly), I(CWI), I(rh), fill=SOFT, line=LINE, radius=True)
        rect(s, I(X0), I(ly), I(lw), I(rh), fill=NAVY, radius=True)
        text(s, I(X0 + 0.15), I(ly), I(lw - 0.3), I(rh), [[(a, WHITE, True)], [(m, pal_rgb("#C9D3E6"), False)]],
             size=BODY, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        if k < len(parts) - 1:
            arrow(s, X0 + 0.5, ly + rh + 0.01, X0 + 0.5, ly + rh + gap - 0.01, color=NAVY)
        cw_ = (3 * chw + 2 * cg - (len(cs) - 1) * cg) / len(cs)
        for j, c in enumerate(cs):
            chip(s, cx0 + j * (cw_ + cg), ly + 0.07, cw_, rh - 0.14, c, fill=WHITE, line_color=NAVY, color=NAVY,
                 bold=True)
        bh = rich_h([body], tw_, pt)
        rich(s, tx, ly + (rh - bh) / 2 + 0.03, tw_, [body], pt=pt)
    src(s, "Source: Milestone 5 report, Section 1.2 and Figure 1.1.")


# ----------------------------------------------------------------------------- 6 educational context
def s06(prs):
    s = kit.base(prs, kicker(6), T("Educational Context"), notes(6))
    y = lead(s, T("The university already holds the records that could show students drifting away, but has not "
                  "decided which questions they should answer."))
    keyl = T("Key: every figure about the university (program and faculty size) is a scenario assumption of the course "
             "brief. LMS = learning management system.")
    ky = bottom_key(s, keyl)
    stakes = [[(T("Stakes: "), AGENT_INK, True),
               (T("withdrawal is a regulated quality measure in Vietnam, capped at 10% a year and 15% in the first "
                  "year (") + ref(7) + T("), while a program may teach up to 30% of its volume in online classes."),
                INK, False)]]
    sh = strip_h(stakes, PT["body"])
    sy = ky - 0.2 - sh
    strip(s, sy, stakes, fill=ACC_FILL, line=WARM, pt=PT["body"])
    xs, cw = cols(3)
    items = [(T("Setting"), "globe",
              [T("A Vietnamese university expands online and blended learning on its LMS, the web platform where "
                 "lecturers publish materials, quizzes and assignments."),
               T("We work with one undergraduate program of about 1,200 students in a faculty of about 4,000.")]),
             (T("What it observes"), "trend",
              [T("In several of the program's online and blended courses, students take part less as the semester "
                 "goes on."),
               T("Some do not complete the course.")]),
             (T("Records it holds"), "database",
              [T("LMS activity, enrolment and result records, assignment and quiz results, grades and student "
                 "surveys."),
               T("Which questions these should answer, and which decisions they should support, is still open.")])]
    h = sy - 0.25 - y
    pt = min(fit_pt(b, cw - 0.36, h - 0.7) for _, _, b in items)
    for x, (a, ic, b) in zip(xs, items):
        rect(s, I(x), I(y), I(cw), I(h), fill=SOFT, line=LINE, radius=True)
        icon(s, ic, x + 0.18, y + 0.16, 0.34, color=NAVY, bg=SOFT)
        text(s, I(x + 0.62), I(y + 0.17), I(cw - 0.8), I(0.35), a, size=PT["head"], color=NAVY, bold=True,
             spacing=1.0)
        rich(s, x + 0.18, y + 0.66, cw - 0.36, b, pt=pt)
    src(s, "Source: Milestone 5 report, Section 1 and Appendix I.")


# ----------------------------------------------------------------------------- 7 withdrawal is regulated
def s07(prs):
    s = kit.base(prs, kicker(7), T("Withdrawal Is a Regulated Measure"), notes(7))
    y = lead(s, T("Vietnamese regulation caps withdrawal, so a university needs an exact record of each student's "
                  "status and an early view of who is drifting away."))
    keyl = T("Basis: the two Circulars and the 2021 training regulation are cited through Vietnamese news reports "
             "(2021, 2024 and 2026), which are secondary sources.")
    ky = bottom_key(s, keyl)
    xs, cw = cols(3)
    tiles = [("10%", T("Cap on the annual withdrawal rate (Circular 01/2024).")),
             ("15%", T("Cap on the first-year withdrawal rate; a university above it may not raise its enrolment "
                       "quota.")),
             ("30%", T("Share of a full-time or work-study program that may be taught in online classes (2021 "
                       "training regulation)."))]
    vh = kit.num_h(PT["number"])
    th = 0.15 + vh + 0.05 + max(rich_h([b], cw - 0.36, PT["body"]) for _, b in tiles) + 0.15
    for k, (x, (v, b)) in enumerate(zip(xs, tiles)):
        acc = k < 2
        rect(s, I(x), I(y), I(cw), I(th), fill=ACC_FILL if acc else SOFT, line=WARM if acc else LINE, radius=True)
        text(s, I(x), I(y + 0.15), I(cw), I(vh), v, size=PT["number"], color=WARM if acc else NAVY, bold=True,
             align=PP_ALIGN.CENTER, spacing=1.0)
        rich(s, x + 0.18, y + 0.2 + vh, cw - 0.36, [b], pt=PT["body"], align=PP_ALIGN.CENTER)
    y += th + 0.3
    lw = (CWI - 0.3) / 2
    cards = [(T("Circular 83/2026, in force from 15 November 2026"),
              [T("Replaces Circular 01/2024 and keeps both caps."),
               T("Students on approved leave, and those who transfer to another program or institution, no longer "
                 "count as withdrawn.")]),
             (T("What follows for our project"),
              [T("Completion means passing the course, and withdrawal follows Circular 83/2026, so the university's "
                 "baseline is recounted under its rule."),
               T("Our open stand-in data record neither leave nor transfer, so there they count as withdrawal.")])]
    h = ky - 0.2 - y
    pt = card_pt([(a, bullets(b)) for a, b in cards], lw, h)
    for k, (a, b) in enumerate(cards):
        card(s, X0 + k * (lw + 0.3), y, lw, a, bullets(b), h=h, pt=pt)
    src(s, "Source: Milestone 5 report, Section 1 and Appendix I (news reports of the Circulars, 2024 and 2026, and of "
           "the 2021 training regulation).")


# ----------------------------------------------------------------------------- 8 why early matters
def s08(prs):
    s = kit.base(prs, kicker(8), T("Why Early Matters: What Studies Report"), notes(8))
    y = lead(s, T("Published studies agree that non-completion online is common and that the useful moment for support "
                  "lies in the first weeks of a course."))
    bot = END
    lw = 5.5
    rx, rw = X0 + lw + 0.35, CWI - lw - 0.35
    # left: how common
    hy = heading(s, X0, y, lw, T("How common non-completion is"))
    studies = [(T("A review of 110 articles, 2013–2023"),
                T("Dropout in online higher education is a significant concern, with several contributors acting at "
                  "once (Rahmani et al., 2024).")),
               (T("A review of 40 studies, 2010–2018"),
                T("Completion in online courses is about 8 to 14 points below face-to-face courses (Muljana and "
                  "Luo, 2019).")),
               (T("A Vietnamese review, 2024"),
                T("Dropout among university students is about 20–30% (Lê et al., 2024)."))]
    gap = 0.18
    ch = (bot - hy - 0.12 - 2 * gap) / 3
    kit.room("studies", max(card_h(a, [b], lw) for a, b in studies), ch)
    pt = next((p_ for p_ in (PT["lead"], PT["body"]) if max(card_h(a, [b], lw, pt=p_) for a, b in studies) <= ch),
              BODY)
    cy = hy + 0.12
    for a, b in studies:
        card(s, X0, cy, lw, a, [b], h=ch, pt=pt)
        cy += ch + gap
    # right: when, as week bands
    hy = heading(s, rx, y, rw, T("When support is most useful, by week of the course"))
    weeks = 8
    ax0, ax1 = rx + 0.1, rx + rw - 0.1
    ww = (ax1 - ax0) / weeks
    ay = hy + 0.15
    for k in range(weeks):
        rect(s, I(ax0 + k * ww + 0.02), I(ay), I(ww - 0.04), I(0.32), fill=SOFT, line=LINE)
        text(s, I(ax0 + k * ww), I(ay), I(ww), I(0.32), f"{T('Week')} {k + 1}", size=PT["small"], color=INK, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             spacing=1.0)
    rows = [(1, 2, False, T("Massive open online courses: about half of enrolled students never show up, and the "
                            "first two weeks are critical (Jordan, 2015).")),
            (None, None, True, T("The window for effective support of a student at risk is short: it lasts two to "
                                 "four weeks (Herodotou et al., 2019, at the Open University).")),
            (5, 6, False, T("Best point for an early warning in a blended first-year statistics course (Howard et al., "
                            "2018)."))]
    msg = T("So a useful signal must arrive early, and the time to act on it is short.")
    mh = lh(msg, rw - 0.4, PT["body"], True) + 0.24
    my = bot - mh
    rect(s, I(rx), I(my), I(rw), I(mh), fill=NAVY, radius=True)
    text(s, I(rx + 0.2), I(my), I(rw - 0.4), I(mh), msg, size=PT["body"], color=WHITE, bold=True,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    wkey = T("Key: each grey bar spans the weeks a study names; the orange text gives a length of time, not weeks of "
             "the course.")
    wk = my - 0.15 - lh(wkey, rw, PT["small"])
    key(s, wk, wkey, rx, rw)
    top = ay + 0.32 + 0.2
    rh = (wk - 0.1 - top) / len(rows)
    rpt = min(fit_pt([line], rw - 0.2, rh - 0.48) for *_, line in rows)
    for k, (a, b, acc, line) in enumerate(rows):
        ry = top + k * rh
        for w_ in range(weeks if a is not None else 0):   # faint week guides
            rect(s, I(ax0 + w_ * ww + ww / 2 - 0.005), I(ry), I(0.01), I(0.28), fill=LINE)
        if a is not None:
            bar = rect(s, I(ax0 + (a - 1) * ww + 0.04), I(ry), I((b - a + 1) * ww - 0.08), I(0.28),
                       fill=WARM if acc else GREY, radius=True)
            bar.adjustments[0] = 0.5
        tx = rx + 0.1
        kit.room("week rows", 0.28 + 0.08 + lh(line, rw - 0.2, BODY), rh - 0.1)
        rich(s, tx, ry + 0.36, rw - 0.2, [line], pt=rpt,
             color=AGENT_INK if acc else INK)
    src(s, "Source: Milestone 5 report, Appendix I; Rahmani et al. (2024); Muljana and Luo (2019); Lê et al. (2024); "
           "Jordan (2015); Herodotou et al. (2019); Howard et al. (2018).")


# ----------------------------------------------------------------------------- 9 stakeholders (deck slide 4)
def s09(prs):
    s = kit.base(prs, kicker(9), T("Stakeholders and Their Decisions"), notes(9))
    y = lead(s, T("Three groups of staff each take one decision, and all of them asked for a short list with a factual "
                  "reason beside each name."))
    review = [tb("Review point: ", "a moment in week 3 or week 5 when staff decide whom to contact."),
              tb("Students: ", "the subject of every data use; they decide whether to accept help.")]
    needs = [T("A list at weeks 3 and 5, with a factual reason beside each name."),
             T("About 30–40 contacts a week for the support office, and three to five for each lecturer-advisor."),
             T("Support only, with no automated step.")]
    needs = bullets(needs)
    source = T("Source of the needs: simulated interviews with AI on both sides (five stakeholders, 51 key "
               "statements, six themes); they motivate the design and are never evidence.")
    lower = rich_h(review, CWI) + 0.12 + card_h(T("What all three groups need"), needs, CWI) + 0.12 + \
        lh(source, CWI, PT["small"])
    y = decision_cards(s, y, [
        (T("D1 – Whom to contact"), [T("At each review point. Course lecturers, lecturer-advisors (lecturers who "
                                       "advise a student class) and the support office decide.")],
         T("Operational and reversible"), True),
        (T("D2 – Where to place support time"), [T("Each semester. The program manager decides.")],
         T("Set each semester"), False),
        (T("D3 – Whether to extend the approach"), [T("Leadership decides with legal staff and the data office.")],
         T("Close to irreversible"), False)], bottom=END - lower - 0.3)
    y = rich(s, X0, y + 0.3, CWI, review) + 0.12
    y = card(s, X0, y, CWI, T("What all three groups need"), needs)
    key(s, y + 0.12, source)
    src(s, "Source: Milestone 5 report, Sections 1.1 and 2.1, and Appendix I, Table A.1.")


# ----------------------------------------------------------------------------- 10 what staff asked for
def s10(prs):
    s = kit.base(prs, kicker(10), T("What Staff Asked For"), notes(10))
    y = lead(s, T("Simulated interviews set the shape of the list, short, timed and with a reason for each name, but "
                  "they are never evidence."))
    how = [tb("How the needs were established: ",
              "in Milestone 1, generative AI played both the stakeholder and the interviewer, followed by a "
              "validation round; we verified every transcript and kept 51 key statements, each labelled as an "
              "opinion, an assumption or scenario information.")]
    y = strip(s, y, how, fill=GREY_FILL, line=GREY, dash=True) + 0.25
    keyl = T("Status: simulated stakeholder views; they set the timing and the length of the lists, and every finding "
             "rests on the data or on published work. Lecturer-advisor: a lecturer who advises a student class.")
    ky = bottom_key(s, keyl)
    lw = (CWI - 0.3) / 2
    themes = [T("Students are noticed late."),
              T("Disengagement starts early, often with a missed quiz or assignment."),
              T("Capacity is small: about 30–40 contacts a week for the support office, three to five per "
                "lecturer-advisor."),
              T("Contact helps when it comes from someone the student knows."),
              T("The data must be trusted: linked records, correct status, a lawful purpose."),
              T("Support only: no labels, no effect on grades, no evaluation of lecturers.")]
    settled = [T("Lists at two review points, week 3 and week 5."),
               T("A factual reason beside each name, checked by a member of staff."),
               T("Contact from the lecturer or the student's lecturer-advisor; the support office takes the harder "
                 "cases."),
               T("No step is automated."),
               T("The validation round added: completion means passing; review points avoid registration and "
                 "examination weeks; the target runs over a full academic year.")]
    h = ky - 0.2 - y
    cards = [(T("Six themes that recur across five stakeholders"), bullets(themes)),
             (T("How we settled where they differed"), bullets(settled, WARM))]
    pt = card_pt(cards, lw, h)
    for k, (a, b) in enumerate(cards):
        card(s, X0 + k * (lw + 0.3), y, lw, a, b, h=h, pt=pt, color=AGENT_INK if k else NAVY,
             fill=ACC_FILL if k else SOFT, line=WARM if k else LINE)
    src(s, "Source: Milestone 5 report, Section 1.1 and Appendix I.")


# ----------------------------------------------------------------------------- 11 scope and objective
def s11(prs):
    s = kit.base(prs, kicker(11), T("Scope and Objective"), notes(11))
    y = lead(s, T("We aim to turn records the university already holds into a short, timely contact list with an "
                  "observed reason for each name, for decisions staff can take within a semester."))
    obj = [tb("Objective: ", "a short, timely list of students to contact at each review point, with an observed "
                             "reason for each name, and patterns that show the program where and when students are "
                             "lost.")]
    y = card(s, X0, y, CWI, None, obj, fill=WHITE, line=NAVY, pt=PT["body"], line_w=1.5) + 0.25
    cond = [tb("Condition: ", "no open dataset of Vietnamese courses exists, so OULAD (Open University Learning "
                              "Analytics Dataset, UK, 2013–2014) stands in, and every result must be re-checked on the "
                              "university's records before it supports a decision.", GREY)]
    ch_ = strip_h(cond)
    cy = END - ch_
    strip(s, cy, cond)
    lw = (CWI - 0.3) / 2
    ins = [T("Students enrolled in the program's online and blended courses after the add-drop period, the first "
             "weeks in which students may still register or drop."),
           T("One semester at a time."),
           T("Decisions staff can take within a semester: whom to contact, when, by whom and with which offer."),
           T("Completion means passing the course; withdrawal follows Circular 83/2026, which excludes approved leave "
             "and transfers.")]
    outs = [tb("Assessment rules: ", "a lecturer cannot change them during a semester.", INK),
            tb("Admissions and financial aid: ", "university policy.", INK),
            tb("Students' circumstances outside the course: ", "beyond the university's control.", INK),
            tb("The evaluation of lecturers: ", "it would stop lecturers from using the results.", INK),
            tb("Any automated decision: ", "every contact stays a decision of a member of staff.", INK)]
    h = cy - 0.25 - y
    cards = [(T("In scope"), bullets(ins, PLUS), PLUS), (T("Out of scope, and why"), bullets(outs, MINUS), MINUS)]
    pt = card_pt([(a, b) for a, b, _ in cards], lw, h)
    for k, (a, b, c) in enumerate(cards):
        card(s, X0 + k * (lw + 0.3), y, lw, a, b, h=h, pt=pt, color=c)
    src(s, "Source: Milestone 5 report, Section 1.2 and Appendix I.")


# ----------------------------------------------------------------------------- 12 business goal and SMART goal
def s12(prs):
    s = kit.base(prs, kicker(12), T("Business Goal and SMART Goal"), notes(12))
    y = lead(s, T("The goal is more students passing their courses, not a model or a dashboard, and the SMART Goal makes "
                  "it measurable with assumed values."))
    tw = 8.55
    rx, rw = X0 + tw + 0.3, CWI - tw - 0.3
    bg = [tb("Business Goal: ", "improve successful course completion in the program's online and blended courses by "
                                "identifying students who stop taking part early enough to support them within the "
                                "semester."),
          [(T("An outcome for the organisation; a model, a list or a dashboard is only a means."), GREY, False)]]
    sm = [tb("SMART Goal ", "(specific, measurable, achievable, relevant, time-bound): raise the course completion "
                            "rate of students enrolled after the add-drop period in the pilot courses from their "
                            "recounted baseline (assumed 70%) by five percentage points (assumed target 75%) by the "
                            "end of the 2027–2028 academic year.")]
    y1 = card(s, X0, y, tw, None, bg, fill=WHITE, line=NAVY, line_w=1.5)
    arrow(s, X0 + tw / 2, y1 + 0.02, X0 + tw / 2, y1 + 0.26, color=NAVY)
    y2 = card(s, X0, y1 + 0.28, tw, None, sm, fill=WHITE, line=NAVY, line_w=1.5)
    pilot = bullets([tb("Pilot courses: ", "about four courses with about 600 enrolments (assumptions), fixed in "
                                           "advance and compared with similar courses outside the pilot.", INK),
                     tb("Baseline: ", "completion of the same courses in 2024–2025 and 2025–2026, recounted under "
                                      "Circular 83/2026 so that approved leave and transfers do not count.", INK)])
    ly = y2 + 0.25
    h = END - ly
    kit.room("goal lower", ly + card_h(T("Pilot design"), pilot, tw), END)
    card(s, X0, ly, tw, T("Pilot design"), pilot, h=h, pt=card_pt([(T("Pilot design"), pilot)], tw, h))
    # right: the target tile and the limit
    lab = T("Completion in the pilot courses, from the assumed baseline to the assumed target.")
    vh = kit.num_h(PT["cover"])
    th = 0.2 + vh + 0.08 + rich_h([lab], rw - 0.36) + 0.12 + 0.34 + 0.2
    rect(s, I(rx), I(y), I(rw), I(th), fill=ACC_FILL, line=WARM, radius=True, line_w=1.5)
    text(s, I(rx), I(y + 0.2), I(rw), I(vh), T("70% → 75%"), size=PT["cover"], color=WARM, bold=True,
         align=PP_ALIGN.CENTER, spacing=1.0)
    ly_ = rich(s, rx + 0.18, y + 0.28 + vh, rw - 0.36, [lab], align=PP_ALIGN.CENTER)
    chip(s, rx + rw / 2 - 0.6, ly_ + 0.1, 1.2, 0.32, T("Assumed"), fill=WHITE, line_color=GREY, color=GREY, bold=True)
    lim = [T("Students who are contacted may have passed anyway, so a rise in completion shows progress, not why."),
           T("Whether contact itself helps is tested only in the randomised pilot.")]
    oy = y + th + 0.25
    card(s, rx, oy, rw, T("What the goal cannot show"), lim, h=END - oy, pt=card_pt([(T("What the goal cannot show"), lim)], rw, END - oy),
         fill=GREY_FILL)
    src(s, "Source: Milestone 5 report, Section 2 and Appendix II; 70% and 75% are assumptions that the university's "
           "recount replaces.")


# ----------------------------------------------------------------------------- 13 is the target achievable?
def s13(prs):
    s = kit.base(prs, kicker(13), T("Is the Target Achievable?"), notes(13))
    y = lead(s, T("At the assumed baseline, five more points means about one in six non-completers passing after "
                  "support, which fits staff capacity but stays an assumption."))
    keyl = T("Key: the one-in-six share is an assumption, not an estimate; no data in the project measure the effect of "
             "contact, so the pilot tests it. KPI = key performance indicator.")
    ky = bottom_key(s, keyl)
    lw = 4.4
    rx, rw = X0 + lw + 0.35, CWI - lw - 0.35
    hy = heading(s, X0, y, lw, T("Worked example"))
    steps = [("600", T("enrolments in about four pilot courses (assumed)"), False),
             (T("about 180"), T("end without a pass at the assumed 70% completion"), False),
             (T("about 30"), T("more passes give five more points: one in six of the 180"), True)]
    gap = 0.26
    top = hy + 0.12
    nh = (ky - 0.2 - top - 2 * gap) / 3
    vh = kit.num_h(PT["title"] + 6)
    for k, (v, b, acc) in enumerate(steps):
        ny = top + k * (nh + gap)
        rect(s, I(X0), I(ny), I(lw), I(nh), fill=ACC_FILL if acc else SOFT, line=WARM if acc else LINE, radius=True,
             line_w=2.0 if acc else 1.0)
        bh = lh(b, lw - 0.36, PT["body"])
        kit.room("worked step", vh + bh + 0.12, nh)
        oy = ny + (nh - vh - 0.04 - bh) / 2
        text(s, I(X0), I(oy), I(lw), I(vh), v, size=PT["title"] + 6, color=WARM if acc else NAVY, bold=True,
             align=PP_ALIGN.CENTER, spacing=1.0)
        rich(s, X0 + 0.18, oy + vh + 0.04, lw - 0.36, [b], pt=PT["body"], align=PP_ALIGN.CENTER)
        if k < 2:
            arrow(s, X0 + lw / 2, ny + nh + 0.02, X0 + lw / 2, ny + nh + gap - 0.02, color=NAVY)
    hy = heading(s, rx, y, rw, T("The goal against the five SMART criteria"))
    rows = [[T("Criterion"), T("How the goal meets it")],
            [T("Specific"), T("One measure (completion), one population (enrolled after add-drop) and one set of pilot "
                              "courses, fixed in advance.")],
            [T("Measurable"), T("Completion and its denominator are read from the academic management system at the "
                                "end of each semester (the primary KPI).")],
            [T("Achievable"), T("About 30 more passes in 600 enrolments; reaching them fits the weekly capacity staff "
                                "reported (worked example on the left).")],
            [T("Relevant"), T("Measures the Business Goal directly and answers the program manager's and the support "
                              "office's needs.")],
            [T("Time-bound"), T("Contact runs from Semester 2 of 2026–2027; the target is read on the pilot courses "
                                "over the 2027–2028 year.")]]
    widths = [I(1.6), I(rw - 1.6)]
    room_ = ky - 0.2 - (hy + 0.15)
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room_ else BODY
    shape = table(s, I(rx), I(hy + 0.15), I(rw), rows, widths, size=size)
    colour_cell(shape.table, 3, 0, ACC_FILL, AGENT_INK)
    colour_cell(shape.table, 3, 1, ACC_FILL)
    kit.room("smart table", shape.height / EMU, room_)
    stretch_table(shape, room_)
    src(s, "Source: Milestone 5 report, Section 2 and Appendix II, Table A.2.")


# ----------------------------------------------------------------------------- 14 KPIs
def s14(prs):
    s = kit.base(prs, kicker(14), T("Key Performance Indicators"), notes(14))
    y = lead(s, T("One primary KPI measures the goal and two secondary KPIs show during the semester whether contact "
                  "happens; on OULAD only their non-contact parts can be computed."))
    keyl = T("Key: KPI = key performance indicator. OULAD = Open University Learning Analytics Dataset, our open "
             "stand-in. Day 14: registration closes two weeks after a run starts; day 27 = end of week 4. LMS = "
             "learning management system. Last column: green = computed as a proxy; orange = part computed; grey = "
             "pilot only.")
    ky = bottom_key(s, keyl)
    rule = [tb("Early-sign rule: ", "by the data cut-off, a tutor-marked assignment (TMA) or computer-marked assessment "
                                    "(CMA) due but not submitted, a TMA submitted late, or no platform activity in the "
                                    "previous seven days; the one rule of the project, on OULAD and in the pilot ("
               ) + [(ref(40) + T(")."), INK, False)]]
    rh_ = strip_h(rule)
    ry = ky - 0.2 - rh_
    strip(s, ry, rule, fill=ACC_FILL, line=WARM)
    rows = [[T("KPI"), T("Definition"), T("When and from where"), T("On OULAD")],
            [T("Primary: completion rate"), T("Passes over enrolments after the add-drop period; leave and transfer "
                                              "leave the denominator."),
             T("End of each semester; academic records."), T("Proxy: enrolments still registered at day 14, 28,061 "
                                                             "over 22 runs.")],
            [T("Secondary 1: early-sign contact rate"), T("Students meeting the early-sign rule at the end of week 4 "
                                                          "who are contacted by the end of week 5, over students "
                                                          "meeting it."),
             T("Week 6; LMS, academic and contact records."), T("Sign part only: the rule flags 28.8% of 27,535 "
                                                                "enrolments at day 27.")],
            [T("Secondary 2: follow-up rate"), T("Listed students contacted within seven days, over students listed."),
             T("A week after each review point; contact record."), T("Pilot only: no contact record exists.")]]
    fr = (0.22, 0.34, 0.2)
    widths = [int(CW * f) for f in fr]
    widths.append(CW - sum(widths))
    room_ = ry - 0.2 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room_ else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    tbl = shape.table
    colour_cell(tbl, 1, 3, OUT_FILL, OUT_INK, True)
    colour_cell(tbl, 2, 3, ACC_FILL, AGENT_INK, True)
    colour_cell(tbl, 3, 3, GREY_FILL, GREY, True)
    kit.room("kpi table", shape.height / EMU, room_)
    stretch_table(shape, room_)
    src(s, "Source: Milestone 5 report, Section 2.1, Table 2.1, and Appendix II.")


# ----------------------------------------------------------------------------- 15 three decisions
def s15(prs):
    s = kit.base(prs, kicker(15), T("Three Decisions, Three Kinds of Evidence"), notes(15))
    y = lead(s, T("The more reversible a decision, the simpler the evidence it can start with: D1 can start with a "
                  "staff-checked rule, D3 needs a pilot and legal approval."))
    keyl = T("Key: a two-way door is a decision that can be reversed quickly; a one-way door is nearly irreversible. "
             "Early-sign rule: a missed or late task, or a week with no platform activity, by the data cut-off. Review "
             "point: week 3 or week 5.")
    ky = bottom_key(s, keyl)
    # the reversibility scale above the cards
    left, right = T("Easy to reverse (two-way door)"), T("Hard to reverse (one-way door)")
    text(s, I(X0), I(y), I(5), I(0.3), left, size=PT["small"] + 2, color=NAVY, bold=True, spacing=1.0)
    text(s, I(XR - 5), I(y), I(5), I(0.3), right, size=PT["small"] + 2, color=AGENT_INK, bold=True,
         align=PP_ALIGN.RIGHT, spacing=1.0)
    arrow(s, X0, y + 0.42, XR, y + 0.42, color=NAVY)
    y += 0.65
    items = [(T("D1 – Whom to contact at each review point"),
              [tb("Who: ", "course lecturers, lecturer-advisors and the support office."),
               tb("Kind: ", "operational, repeated at every review point; a contact that does not help can be "
                            "followed by another."),
               tb("Evidence needed: ", "a list that reaches more later non-completers than the early-sign rule at the "
                                       "same length; each name checked by staff.")],
              T("Two-way door"), False),
             (T("D2 – Where to place support time each semester"),
              [tb("Who: ", "the program manager."),
               tb("Kind: ", "management control, with judgement about courses and staff; staff can be moved again next "
                            "semester."),
               tb("Evidence needed: ", "a pattern repeated over several semesters, correct records and agreement with "
                                       "staff.")],
              T("Two-way door"), False),
             (T("D3 – Whether to extend the approach and link data routinely"),
              [tb("Who: ", "university leadership, legal staff and the data office."),
               tb("Kind: ", "strategic, with no earlier case; it changes the university's data practice and students' "
                            "trust."),
               tb("Evidence needed: ", "pilot results, legal approval, and completion and the KPIs (key performance "
                                       "indicators) measured before and after the pilot.")],
              T("Close to a one-way door"), True)]
    decision_cards(s, y, items, bottom=ky - 0.2)
    src(s, "Source: Milestone 5 report, Section 2.1 and Appendix II, Table A.3.")


# ----------------------------------------------------------------------------- 16 four questions (deck slide 6)
def s16(prs):
    s = kit.base(prs, kicker(16), T("Four Questions, Four Analytics Levels"), notes(16))
    y = lead(s, T("Four questions climb the analytics levels, and each answer may claim only what its level allows."))
    y = rich(s, X0, y, CWI, [tb("Unit of analysis: ", "one student's enrolment in one module run (one offering of a "
                                                       "module). AQ: analytical question.")])
    rungs = [(T("AQ1 – Descriptive"), T("What share pass, fail or withdraw, and in which week do non-completers first "
                                        "miss a task?"), T("Serves D2 and D3."), T("Reads as: what happened.")),
             (T("AQ2 – Diagnostic"), T("Which signs by week 4 go with later non-completion, within module run?"),
              T("Serves D2, and gives the reasons for D1."), T("Reads as: an association.")),
             (T("AQ3 – Predictive"), T("How well do data up to days 13 and 27 estimate non-completion, against the "
                                       "early-sign rule (built on 2013, applied to 2014)?"), T("Serves D1."),
              T("Reads as: a forecast, valid only on data the model never saw.")),
             (T("AQ4 – Prescriptive"), T("Who ranks first on a list of fixed capacity, overall and by group?"),
              T("Serves D1."), T("Reads as: an option to test, because it comes from observational data."))]
    xs, cw = cols(4, 0.2)
    step = 0.25
    tag_h = 0.4
    need = max(card_h(a, [b, c, [(d, AGENT_INK, True)]], cw) for a, b, c, d in rungs) + tag_h
    ladder_key = T("Key: orange rungs were run on the data, white "
                   "rungs are designs. Data cut-offs: day 13 (end of week 2) for the week-3 list; day 27 (end "
                   "of week 4) for the week-5 list. Decisions: D1 whom to contact, D2 where to place "
                   "support time, D3 whether to extend. Early-sign rule: a missed or late task, or a week "
                   "with no activity.")
    bottom = END - lh(ladder_key, CWI, PT["small"]) - 0.12
    kit.room("question ladder", need + 3 * step, bottom - (y + 0.25))
    top0 = y + 0.25
    for k, (x, (a, b, c, d)) in enumerate(zip(xs, rungs)):
        top = top0 + (3 - k) * step
        run = k < 2
        card(s, x, top, cw, a, [b, c, [(d, AGENT_INK, True)]], h=bottom - top,
             fill=ACC_FILL if run else WHITE, line=WARM if run else GREY, line_w=2.0 if run else 1.0)
        chip(s, x + 0.18, bottom - tag_h + 0.02, cw - 0.36, 0.3, T("Run on the data") if run else T("Design only"),
             fill=WARM if run else WHITE, line_color=WARM if run else GREY, color=WHITE if run else GREY, bold=True)
    key(s, bottom + 0.12, ladder_key)
    src(s, "Source: Milestone 5 report, Section 3 and Table 3.1.")


# ----------------------------------------------------------------------------- 17 how each level may be read
def s17(prs):
    s = kit.base(prs, kicker(17), T("How Each Level May Be Read"), notes(17))
    y = lead(s, T("The analytics level of a question fixes what its answer may claim: a diagnostic answer is an "
                  "association, and a prescriptive answer on observational data is an option to test."))
    keyl = T("Key: AQ = analytical question. Observational data = records of what students did, with no assigned "
             "treatment. Orange = real results; grey = designs only.")
    ky = bottom_key(s, keyl)
    msg = T("Every finding in this talk is held to this table: an association is never read as a cause.")
    mh = lh(msg, CWI - 0.6, PT["lead"], True) + 0.3
    my = ky - 0.2 - mh
    closing_box(s, my, msg, h=mh)
    rows = [[T("Question and level"), T("Evidence reached"), T("What the answer states"),
             T("What the answer does not state")],
            [T("AQ1 – Descriptive: completion and timing"), T("Real results, 2013 and 2014"),
             T("Outcome shares and the week of the first missed task, with denominator and 95% interval."),
             T("Why a module or run has a higher rate; any rate for the university's own courses.")],
            [T("AQ2 – Diagnostic: early signs by week 4"), T("Real results, 2013, replicated on 2014"),
             T("Which signs go with later non-completion within module runs, by how many points."),
             T("That a sign causes non-completion, or that removing a sign would raise completion.")],
            [T("AQ3 – Predictive: estimate at weeks 2 and 4"), T("Design only; no model trained"),
             T("The expected output and the gate that would decide it."),
             T("Any recall, precision, calibration or other model metric.")],
            [T("AQ4 – Prescriptive: ranking under capacity"), T("Design only; depends on AQ3"),
             T("The expected list and the conditions under which it would be used."),
             T("Whom contact helps, or which contact works: options for a randomised pilot.")]]
    widths = [int(CW * f) for f in (0.22, 0.17, 0.3)]
    widths.append(CW - sum(widths))
    room_ = my - 0.25 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room_ else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    tbl = shape.table
    for i in (1, 2):
        colour_cell(tbl, i, 1, ACC_FILL, AGENT_INK, True)
    for i in (3, 4):
        colour_cell(tbl, i, 1, GREY_FILL, GREY, True)
    kit.room("reading table", shape.height / EMU, room_)
    stretch_table(shape, room_)
    src(s, "Source: Milestone 5 report, Section 3 and Appendix XI, Table A.26.")


# ----------------------------------------------------------------------------- 18 quality check
def s18(prs):
    s = kit.base(prs, kicker(18), T("Quality Check of the Questions"), notes(18))
    y = lead(s, T("All four questions are clear, specific, scoped and data-oriented; they differ only in how far the "
                  "data can answer them."))
    keyl = T("Key: AQ = analytical question; AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive "
             "(ranking under staff capacity). Cell colours: green = met or answered; orange = answerable in part; "
             "grey = answerable only by a design not yet run.")
    ky = bottom_key(s, keyl)
    status = [tb("Final status: ", "Answered when results answer all of a question; Partial when they answer its core "
                                   "while a named part waits; Deferred when the design is complete but no result "
                                   "exists; Dropped when abandoned. AQ1 and AQ2 are Answered, AQ3 and AQ4 Deferred, and "
                                   "no question is dropped.")]
    sh = strip_h(status)
    sy = ky - 0.2 - sh
    strip(s, sy, status)
    met = T("Met")
    rows = [[T("Criterion"), T("Test"), "AQ1", "AQ2", "AQ3", "AQ4"],
            [T("Clear"), T("Asks one thing a reader can restate"), met, met, met, met],
            [T("Specific"), T("Names its measure and groups"), met, met, met, met],
            [T("Scoped"), T("Fixes its population and period"), met, met, met, met],
            [T("Data-oriented"), T("Names its data"), met, met, met, met],
            [T("Answerable"), T("Those data can settle it"), T("Answered for 2013 and 2014"),
             T("Answered, as an association"), T("By a design not yet run"),
             T("Ranking part only; contact has no data")]]
    widths = [int(CW * f) for f in (0.14, 0.26, 0.15, 0.15, 0.15)]
    widths.append(CW - sum(widths))
    room_ = sy - 0.2 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room_ else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    tbl = shape.table
    for i in range(1, 5):
        for j in range(2, 6):
            colour_cell(tbl, i, j, OUT_FILL, OUT_INK, True)
    colour_cell(tbl, 5, 2, OUT_FILL, OUT_INK, True)
    colour_cell(tbl, 5, 3, OUT_FILL, OUT_INK, True)
    colour_cell(tbl, 5, 4, GREY_FILL, GREY, True)
    colour_cell(tbl, 5, 5, ACC_FILL, AGENT_INK, True)
    for i in range(1, 6):
        for j in range(2, 6):
            tbl.cell(i, j).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    kit.room("check table", shape.height / EMU, room_)
    stretch_table(shape, room_)
    src(s, "Source: Milestone 5 report, Sections 3 and 3.1, Table 3.1, and Appendix III, Table A.4.")


# ----------------------------------------------------------------------------- 19 how the questions changed
def s19(prs):
    s = kit.base(prs, kicker(19), T("How the Questions Changed"), notes(19))
    y = lead(s, T("Every question was narrowed by what the data lack, each change traces to a finding in the data, and "
                  "no question was dropped."))
    keyl = T("Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive. OULAD = Open University Learning "
             "Analytics Dataset. Ratings of the data fit: YELLOW = narrow the question; RED = a key concept or "
             "intervention is missing. Modify = narrow how it is measured; Defer = keep a part for the pilot. "
             "Early-sign rule: a missed or late task, or a week with no activity. Base rate: share that do not "
             "complete.")
    ky = bottom_key(s, keyl)
    same = [tb("Unchanged: ", "the Business Goal, the SMART Goal and the three decisions; the data narrowed how each "
                              "question is measured, not what the project aims for.")]
    sh = strip_h(same)
    sy = ky - 0.2 - sh
    strip(s, sy, same)
    rows = [[T("AQ"), T("At Milestone 1"), T("What the data showed"), T("Final question"), T("Action")],
            ["AQ1", T("Outcome shares by course, delivery mode and year of study"),
             T("OULAD has no delivery mode or year of study (YELLOW)"),
             T("By module, run, start month and year"), T("Modify")],
            ["AQ2", T("Signs in weeks 1–4 with attendance, across modes and years"),
             T("No in-class sessions, so no attendance (YELLOW)"),
             T("Signs by week 4, compared within each module"), T("Modify")],
            ["AQ3", T("Estimate at weeks 2 and 4 against a two-task rule"),
             T("Few tasks fall due by the data cut-offs (YELLOW)"),
             T("Against the early-sign rule, built on 2013, applied to 2014"), T("Modify")],
            ["AQ4", T("List, order and contact; precision of at least 50%"),
             T("No contact data; base rate about 45% (RED)"),
             T("Ranking under capacity, overall and by group"), T("Modify + Defer")]]
    widths = [int(CW * f) for f in (0.07, 0.28, 0.25, 0.27)]
    widths.append(CW - sum(widths))
    room_ = sy - 0.2 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room_ else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    tbl = shape.table
    for i in (1, 2, 3):
        colour_cell(tbl, i, 2, YELLOW_FILL)
    colour_cell(tbl, 4, 2, BAD_FILL, MINUS)
    for i in range(1, 5):
        colour_cell(tbl, i, 3, ACC_FILL, AGENT_INK, True)
    kit.room("revision table", shape.height / EMU, room_)
    stretch_table(shape, room_)
    src(s, "Source: Milestone 5 report, Section 3.2, Table 3.2, and Appendix III, Tables A.5 and A.6.")


# ----------------------------------------------------------------------------- 20 what the data forced us to change
def s20(prs):
    s = kit.base(prs, kicker(20), T("What the Data Forced Us to Change"), notes(20))
    y = lead(s, T("Six changes came straight from the data; none of them touched the goal or the decisions."))
    keyl = T("Key: OULAD = Open University Learning Analytics Dataset. Lift = share of non-completers on the list ÷ "
             "share in the whole run (1 = chance). Normalised recall = share of later non-completers the list reaches "
             "÷ the most a list of that length can reach.")
    ky = bottom_key(s, keyl)
    items = [(T("Setting"), T("a Vietnamese university."),
              T("OULAD module runs as an open stand-in; the pilot uses the university's records."),
              T("no open Vietnamese course data exist.")),
             (T("Time"), T("a semester, weeks 1–5."),
              T("a module run counted in days; cut-offs on day 13 (week-3 list) and day 27 (week-5 list)."),
              T("OULAD dates events in days from the run start.")),
             (T("Who counts"), T("students enrolled after the add-drop period."),
              T("enrolments still registered at day 14; 58 late registrants removed."),
              T("registration closes two weeks after a run starts (") + ref(39) + ")."),
             (T("Comparisons"), T("by delivery mode and year of study."),
              T("by module and run; fairness by deprivation band and disability."),
              T("OULAD records neither field.")),
             (T("Early-sign rule"), T("two or more missed or late tasks."),
              T("a missed or late task, or no platform activity in the last seven days."),
              T("two tasks fall due by day 27 in only 1 of 22 runs (") + ref(40) + ")."),
             (T("List quality"), T("a precision of at least 50%."),
              T("lift over the run's base rate and normalised recall."),
              T("about 45% do not complete, so a random list already reaches about 45% precision."))]
    xs, cw = cols(3, 0.25)
    gap = 0.25
    ch = (ky - 0.2 - y - gap) / 2
    paras = [[tb("Before: ", b, GREY), tb("After: ", a), tb("Why: ", w, AGENT_INK)] for _, b, a, w in items]
    plain = [[("".join(r[0] for r in q), INK, False) for q in p] for p in paras]   # measured without bold
    pt = next((p_ for p_ in (PT["body"], BODY) if max(card_h(h, [[r] for r in q], cw, pt=p_)
                                                      for (h, *_), q in zip(items, plain)) <= ch), BODY)
    kit.room("change cards", max(card_h(h, [[r] for r in q], cw, pt=pt) for (h, *_), q in zip(items, plain)), ch)
    for k, ((h, *_), p) in enumerate(zip(items, paras)):
        x, cy = xs[k % 3], y + (k // 3) * (ch + gap)
        card(s, x, cy, cw, h, p, h=ch, pt=pt)
    src(s, "Source: Milestone 5 report, Sections 2.1 and 3.2, and Appendix III, Table A.8.")


# ----------------------------------------------------------------------------- 21 questions mapped to decisions
def s21(prs):
    s = kit.base(prs, kicker(21), T("Questions Mapped to Decisions"), notes(21))
    y = lead(s, T("Each decision draws on different questions: D1 on the list and its reasons, D2 on patterns, D3 on "
                  "a measure."))
    keyl = T("Key: orange boxes and lines = questions answered on the 2013 and 2014 runs; white boxes and grey lines = "
             "designed, not yet run. KPI = key performance indicator. Early-sign rule: a missed or late task, or a week "
             "with no platform activity.")
    ky = bottom_key(s, keyl)
    bot = ky - 0.25
    lw = 4.3
    rw = 5.9
    rx = XR - rw
    left = [("AQ1", T("Descriptive: outcome shares and timing"), True),
            ("AQ2", T("Diagnostic: early signs by week 4"), True),
            ("AQ3", T("Predictive: a model against the early-sign rule"), False),
            ("AQ4", T("Prescriptive: a ranked list within capacity"), False),
            (T("KPIs"), T("Completion rate and the two contact rates"), False)]
    right = [(T("D1 – Whom to contact at each review point"),
              [tb("Uses: ", "the list and its order (AQ3, AQ4); the reason beside each name (AQ2)."),
               tb("Now: ", "the reasons; the ranked list waits.", AGENT_INK)]),
             (T("D2 – Where to place support time"),
              [tb("Uses: ", "the patterns of AQ1 and AQ2 and the primary KPI."),
               tb("Now: ", "a hypothesis on where support time goes first.", AGENT_INK)]),
             (T("D3 – Whether to extend the approach"),
              [tb("Uses: ", "AQ1's count of completion and the KPIs in pilot and comparison courses."),
               tb("Now: ", "a way to measure; the decision waits for the pilot.", AGENT_INK)])]
    lgap = 0.18
    lh_ = (bot - y - 4 * lgap) / 5
    lys = [y + k * (lh_ + lgap) for k in range(5)]
    for (a, b, run), ly in zip(left, lys):
        rect(s, I(X0), I(ly), I(lw), I(lh_), fill=ACC_FILL if run else WHITE, line=WARM if run else GREY,
             radius=True, line_w=2.0 if run else 1.0)
        text(s, I(X0 + 0.15), I(ly), I(0.8), I(lh_), a, size=PT["head"], color=AGENT_INK if run else NAVY, bold=True,
             anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        bh = lh(b, lw - 1.1, BODY)
        rich(s, X0 + 0.95, ly + (lh_ - bh) / 2 - 0.03, lw - 1.1, [b])
    rgap = 0.2
    rh_ = (bot - y - 2 * rgap) / 3
    rys = [y + k * (rh_ + rgap) for k in range(3)]
    for (a, b), ry in zip(right, rys):
        kit.room("decision box", card_h(a, [[(t, INK, False) for t in ["".join(r[0] for r in q)]] for q in b], rw),
                 rh_)
        card(s, rx, ry, rw, a, b, h=rh_, pt=card_pt([(a, b_) for a, b_ in right], rw, rh_))
    # edges: (left index, right index, answered?)
    edges = [(0, 1, True), (0, 2, True), (1, 0, True), (1, 1, True), (2, 0, False), (3, 0, False), (4, 1, False),
             (4, 2, False)]
    ins = {}
    for _, r, _ in edges:
        ins[r] = ins.get(r, 0) + 1
    seen = {}
    x1, x2 = X0 + lw + 0.04, rx - 0.04
    for li, ri, run in sorted(edges, key=lambda e: (e[1], e[0])):
        k = seen.get(ri, 0)
        seen[ri] = k + 1
        y1 = lys[li] + lh_ / 2
        y2 = rys[ri] + rh_ * (k + 1) / (ins[ri] + 1)
        arrow(s, x1, y1, x2, y2, color=WARM if run else GREY)
    src(s, "Source: Milestone 5 report, Abstract, Section 3, Table 3.1, and Appendix II, Table A.3.")


SLIDES = {1: s01, 2: s02, 3: s03, 4: s04, 5: s05, 6: s06, 7: s07, 8: s08, 9: s09, 10: s10, 11: s11, 12: s12,
          13: s13, 14: s14, 15: s15, 16: s16, 17: s17, 18: s18, 19: s19, 20: s20, 21: s21}
