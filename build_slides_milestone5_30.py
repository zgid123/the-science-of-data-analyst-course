"""Presentation deck of team N04's Milestone 5 final project (25-minute talk, 30 slides), built with the build-report
slide kit.

Usage: venv/bin/python build_slides_milestone5_30.py [--lang en|vi|all]
Output: reports/milestone-5/build/N04_Milestone5_Slides-30_EN.pptx and N04_Milestone5_Slides-30_VI.pptx (SLIDES_OUT_DIR
overrides the folder for draft builds); chart images are cached in build/.cache/slides/milestone-5.

Content source: reports/milestone-5/presentation/v1-30-slides/speech-script.md (slide text = its "Lead" and "On the slide" fields,
speaker notes = its "Speaker notes" field without the timing marks and cut markers). Chart numbers come from the
Milestone 5 report and its result tables (reports/milestone-5/results/2013, 2014 and compare). The Vietnamese strings
live in slides_milestone5_30_vi.py (a dict VI keyed by the English text).
"""

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / ".claude" / "skills" / "build-report" / "scripts"))
sys.path.insert(0, str(ROOT))
import charts                                                   # noqa: E402
import palette as pal                                           # noqa: E402
import slidekit as kit                                          # noqa: E402
from matplotlib.lines import Line2D                             # noqa: E402
from matplotlib.patches import Patch                            # noqa: E402
from pptx.enum.dml import MSO_LINE_DASH_STYLE                   # noqa: E402
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN                 # noqa: E402
from slidekit import (AGENT_FILL, AGENT_INK, BAD_FILL, CW, EMU, END, GREY, H, I, INK, LINE, MINUS, MX, NAVY,  # noqa: E402
                      OUT_FILL, OUT_INK, PLUS, PT, SOFT, TOP, W, WARM, WHITE, T, arrow, bignum, chart, chip,
                      icon, lead, lh, node, node_h, note, path, picture, rect, table, text)

DECK_TITLE = "Milestone 5 final presentation of team N04: early identification of disengaging students on OULAD"
FOOTER_EN = ""                                  # no footer: the slide number sits top right, sources go to the notes
OUT_DIR = Path(os.environ.get("SLIDES_OUT_DIR") or ROOT / "reports" / "milestone-5" / "build")
OUT = {"en": OUT_DIR / "N04_Milestone5_Slides-30_EN.pptx", "vi": OUT_DIR / "N04_Milestone5_Slides-30_VI.pptx"}
CACHE = ROOT / "build" / ".cache" / "slides" / "milestone-5"
LOGO = ROOT / "reports" / "milestone-5" / "report" / "assets" / "university-logo.png"
K = {}
END = kit.END = 7.2                             # no footer, so content runs to 0.3 in above the slide edge
kit.use_strings("slides_milestone5_30_vi")

X0 = MX / EMU                                   # left edge of the content area (in)
CWI = CW / EMU                                  # content width (in)
XR = X0 + CWI                                   # right edge of the content area (in)
BODY = PT["small"] + 2                          # dense slide text and diagram bodies (14 pt, the kit's node body size)
HEAD = PT["body"]                               # card heads on dense slides (16 pt)
GOLD = kit.GOLD
C_GREY, C_ACC, C_INK, C_MUTED = f"#{kit.C_GREYBAR}", f"#{kit.C_WARM}", f"#{kit.C_INK}", f"#{kit.C_MUTED}"
ACC_FILL = AGENT_FILL                           # light tint of the accent colour
KEY = pal.rgb("#4A505C")                       # key lines, darker than GREY so they read on a projector


def kickers():
    K.update(intro=T("Introduction"), p1=T("Part 1 · The Problem (Milestone 1)"), p2=T("Part 2 · The Data (Milestone 2)"),
             p3=T("Part 3 · Preparation (Milestone 3)"), p4=T("Part 4 · Method (Milestone 4)"),
             p5=T("Part 5 · Evidence (Milestone 5)"), p6=T("Part 6 · Integration and Use (Milestone 5)"),
             end=T("Conclusions"))


# ----------------------------------------------------------------------------- speaker notes (from the speech script)
NOTES = {
    1: (
        '(~29 seconds) Good morning, teachers and friends. We are team N04, and this is our final '
        'presentation: Early Identification of Disengaging Students in Online Courses. Over five milestones '
        'we followed one chain, from a problem staff describe, to the data, their preparation, the method, '
        "the evidence, and the decisions it can support. Let's start with the moment a drifting student is "
        'finally noticed. [click]'
    ),
    2: (
        '(~45 seconds) Picture a student in an online course. She misses one assignment, logs in less, then '
        'goes quiet. Nothing is recorded yet: no fail, no withdrawal. When does anyone notice? In our '
        'setting, the lecturer becomes sure around week five or six. The program manager sees the numbers '
        'after the semester. The support office meets these students on the warning list, at the very end. '
        'But published work puts the window for effective support between week two and week four. Everyone '
        'who could help arrives after it closes. So here is our answer in brief. [click]'
    ),
    3: (
        "(~59 seconds) [pause] Here's the whole talk on one slide. Non-completion means a fail or a "
        'withdrawal. An early sign is something in the records by the end of week four, like a missed task or'
        ' a week with no activity. Of the twenty-eight thousand sixty-one enrolments still registered at day '
        'fourteen, forty-five point three percent did not complete. Fewer than one in five of them had missed'
        ' a task by week four, so a list built on missed tasks alone comes too late. Yet all five early signs'
        ' go with later non-completion in both years. That gives staff a factual reason beside each name '
        'today. Not yet measured: whether a model beats a simple rule, and whether contact helps. Now, how we'
        ' got here. [click]'
    ),
    4: (
        '(~47 seconds) Three groups take three decisions. D1 is whom to contact at each review point, in week'
        " three or five; lecturers, lecturer-advisors and the support office take it, and it's reversible. D2"
        ' is where the program manager puts support time. D3 is whether leadership extends the approach, '
        'which is close to irreversible. Their needs come from simulated interviews where AI played both '
        'sides, so they shaped the design but are never evidence. All asked for the same thing: a short list '
        'at weeks three and five, with a factual reason beside each name. Next, the goal behind these '
        'decisions. [click]'
    ),
    5: (
        '(~43 seconds) Those decisions serve one business goal: more students completing their courses, '
        'because we spot those who stop taking part in time. The SMART goal makes it measurable: five more '
        'points of completion in about four pilot courses by the end of the 2027–2028 year, from an assumed '
        'baseline of seventy percent that the real recount replaces. The primary KPI is the completion rate '
        'after add-drop. The two secondary KPIs ask whether contact happens, so they can be measured only in '
        'a pilot. Next, the questions that feed the decisions. [click]'
    ),
    6: (
        "(~48 seconds) To serve the decisions, we asked four analytical questions on one unit: a student's "
        'enrolment in one course run. AQ1 is descriptive: how many complete, and when do non-completers first'
        ' miss a task? AQ2 is diagnostic: which signs by week four go with later non-completion? "Go with" '
        'means an association, never a cause. AQ3 is predictive: can a model beat a simple early-sign rule? '
        'AQ4 is prescriptive: who should top a list staff can handle? Each list sees only data up to its cut-'
        'off: day thirteen for week three, day twenty-seven for week five. Where would the data come from? '
        '[click]'
    ),
    7: (
        '(~46 seconds) In Milestone two, before searching, we wrote down what the data must contain, so the '
        'questions choose the data. Every question needs the enrolment, the final result and a dated '
        'withdrawal. Above all, every event needs a date, because a week-three list may only see what '
        'happened before its cut-off. That gave six must-have gates: a dated outcome, dated tasks, dated '
        'activity, at least three runs in time order, an open licence, and a stable anonymised identifier. We'
        ' also declared one gap in advance: no dataset would record staff contacts. With these gates, we went'
        ' searching. [click]'
    ),
    8: (
        '(~47 seconds) No open dataset of Vietnamese courses exists, so we needed a stand-in. We screened '
        'seven candidates from open repositories, among them the UCI repository, and scored each from zero to'
        " two on the brief's ten criteria, with the gates deciding first. OULAD, the Open University Learning"
        ' Analytics Dataset, scores only twelve of twenty, but every other candidate lacks a dated outcome '
        'and dated tasks. OULAD alone records a dated withdrawal, dated submissions and daily clicks. So we '
        "chose it for fit, not for ease. It's openly licensed and anonymised, and we never re-identify "
        "anyone. So what's inside? [click]"
    ),
    9: (
        '(~48 seconds) OULAD covers twenty-two runs of seven distance-learning modules at the Open University'
        ' in the UK, in 2013 and 2014. A run is one offering of a module, our counterpart of a semester. It '
        'holds thirty-two thousand five hundred ninety-three enrolments, each with a final result; completion'
        ' means pass or distinction. Nine runs fall in 2013 and thirteen in 2014. In Milestone three we rated'
        ' each question against these data. AQ1 to AQ3 are yellow: we narrowed them, because OULAD has no '
        'delivery mode, year of study or attendance. AQ4 is red: no contact record, so only its ranking part '
        'stays. [click]'
    ),
    10: (
        '(~61 seconds) [checkpoint 1: on time if this slide starts by 7:00] Next, quality: nineteen issues, '
        'and three serious enough to change the method.\n[if behind by more than 30 seconds: skip to the last'
        ' sentence] We profiled all ten point nine million rows, and recounted thirteen key figures with '
        'separate code; all thirteen agreed. We rated each issue by whether ignoring it would change a rate, '
        'the target or a feature. First, eighteen of twenty-four exams have no result rows, so a task means '
        'an assignment or a quiz, never the exam. Second, few tasks fall due in the first weeks; keep that '
        'one in mind for later. Third, these are seven UK modules from two years, so we compare students only'
        ' within the same module. Clicks are very skewed, with a median of six hundred two, so we use '
        'logarithms and remove nothing.\nTwo of these facts forced changes. [click]'
    ),
    11: (
        '(~43 seconds) The first change is about who counts. At the university, the completion rate counts '
        'only students enrolled after the add-drop period, because those who leave during add-drop never '
        'really started. OULAD has no add-drop field, but registration closes two weeks after a run starts. '
        "So an enrolment counts if it's still registered at day fourteen. That leaves twenty-eight thousand "
        'sixty-one enrolments for the KPI. Fifty-eight enrolments registered even later, so the same rule '
        'defines the lists at day thirteen and day twenty-seven. The second change is about the early sign. '
        '[click]'
    ),
    12: (
        '(~48 seconds) In Milestone one, interviews said the first sign is usually a missed quiz or '
        'assignment, so our rule was two or more tasks missed or late by week four. The data said no. Two '
        'tasks fall due by day twenty-seven in only one of twenty-two runs; even one task, in only sixteen. A'
        " task-only rule can't fire in many runs. So the final early-sign rule has three parts: a task due "
        'and not submitted, an assignment submitted late, or no platform activity in the last seven days. One'
        ' rule serves OULAD and the pilot. Next, keeping the future out. [click]'
    ),
    13: (
        "(~58 seconds) Preparation guards against leakage: using information that wouldn't exist when the "
        'list is made.\n[if behind by more than 30 seconds: skip to the last sentence] So every feature uses '
        'only what was recorded by its cut-off. Two more rules govern the pipeline: nothing recorded is '
        'deleted or imputed, and every learned value comes from the 2013 runs alone, so the 2014 runs stay '
        'unseen. On the timeline, everything right of the line is crossed out: later clicks, the withdrawal '
        'day, the final result. We also split by year, and flag one thousand five hundred eighty-six test '
        'enrolments of students already seen in 2013. All twenty-two validation checks pass, and features '
        'rebuilt from raw by separate code match in all fifty-five thousand six hundred four rows.\nNow, '
        'which method for which question? [click]'
    ),
    14: (
        '(~48 seconds) In Milestone four we chose a method for each question without training any model. The '
        'rule: the simplest method that fits, and always a baseline to beat. AQ1 needs no model, only rates '
        'with Wilson intervals. AQ2 uses a logistic regression with a term for each run, so students are '
        'compared only within their own run, and it reports risk differences in percentage points. AQ3 '
        'proposes a penalised logistic regression, because staff need a reason beside each name, and it must '
        'beat the early-sign rule. AQ4 cuts those scores into a short list per run. How do we judge it? '
        '[click]'
    ),
    15: (
        '(~49 seconds) Capacity fixes the list length: three or five per twenty. A toy example: twenty '
        "students, nine won't complete, a list of five. If four of our five are right, recall is four of "
        'nine. But five is the most a list of five can reach, so normalised recall is four of five, because '
        'that ceiling ranges from forty-six to one hundred percent between runs. Lift compares the list with '
        "the run's base rate; one means chance. And we must rank: the rule names twenty-eight point eight "
        'percent at day twenty-seven, more than any list holds. So when is a model good enough? [click]'
    ),
    16: (
        '(~63 seconds) The key word is "once". Under gate S1, the model\'s list must clearly beat the rule\'s '
        'list on the 2014 runs, or the simple rule stays.\n[if behind by more than 30 seconds: skip to the '
        'last sentence] Clearly means an interval above zero and a test below zero point zero five, scored '
        'once on all thirteen runs. Every choice before that is made on the nine runs of 2013, holding out '
        'one run at a time. A more complex challenger replaces the primary model only with a gain of at least'
        ' zero point zero three in normalised recall, in at least seven of nine folds. The test year even '
        'includes a module, CCC, that the model has never seen. And probabilities are shown only if '
        'calibration holds, that is, if predicted risks match observed rates.\nA good list also has to be '
        'fair. [click]'
    ),
    17: (
        '(~48 seconds) A list could still miss a whole group. Group attributes stay out of the predictors, '
        "but we keep them for the audit, because bias can't be audited without knowing group membership. Rule"
        ' FR1 flags a group for human review when its recall is more than ten points below the other '
        "students', and the interval of that gap, corrected for several tests, lies below zero. We check "
        'three groups in the test year. No flag means no evidence of a gap, not proof of fairness. And each '
        "name's reasons come from the model that ranked it. So what have we run? [click]"
    ),
    18: (
        '(~48 seconds) [checkpoint 2: on time if this slide starts by 14:00] A word on status. Level one, the'
        ' compulsory level, is complete: the modeling strategy and the evaluation design. AQ1 and AQ2 need no'
        ' predictive model, so we ran them as Milestone four fixed them, on the nine runs of 2013 and again '
        'on the thirteen runs of 2014. AQ3 and AQ4 are designed in full, but no model has been trained, so '
        "there's no model metric in this talk. That's our choice of scope: the 2014 runs are our only "
        'independent test, and we keep them for one complete run of the frozen protocol. First, the size of '
        'the problem. [click]'
    ),
    19: (
        '(~47 seconds) Of the twenty-eight thousand sixty-one enrolments still registered at day fourteen, '
        'forty-five point three percent did not complete, with a narrow interval, forty-four point seven to '
        'forty-five point eight. The two years agree: forty-five point seven in 2013, forty-four point nine '
        'in 2014. Roughly a quarter failed and a fifth withdrew. Bars are modules by year; the dashed line is'
        ' the pooled rate. Modules range from twenty-six point three percent in AAA to fifty-four point three'
        ' in CCC. Two independent computations agree in all one hundred seventy-six outcome cells. But one '
        'choice moves these rates a lot. [click]'
    ),
    20: (
        '(~48 seconds) Runs differ, from twenty-four point nine percent in AAA 2013J to fifty-eight point '
        "three in CCC 2014B, and the denominator alone moves one run's rate by up to thirteen point six "
        'points. Now the years. Count every enrolment, and 2014 looks worse by two point three points. Count '
        'only those registered at day fourteen, and 2014 is slightly better, with an interval including zero.'
        " In the six modules run in both years, it's three point five points better. Same data, opposite "
        'stories, because more 2014 enrolments left before day fourteen: sixteen point two percent against '
        'ten point seven. Now, timing. [click]'
    ),
    21: (
        '(~61 seconds) [pause] Now the moment this talk was built around. Staff told us the first sign is '
        'usually a missed quiz or assignment. And missing a task does separate the groups: seventy-eight '
        'point one percent of non-completers in 2013, and seventy-two point seven in 2014, missed a task at '
        'some point, against about one in five completers. [point at the accent bars] Now look at the short '
        'bars. By the end of week four, when the week-five list is made, only nineteen point six percent of '
        'non-completers in 2013, and fourteen point seven in 2014, had missed one. A list built on missed '
        "tasks alone arrives too late for most of the students it should reach. That's why our rule also "
        'counts a silent week. So, does silence matter? [click]'
    ),
    22: (
        '(~49 seconds) AQ2 answers that. Each dot is a risk difference: how many more percentage points of '
        'non-completion among students with the sign than without it, within the same run. A missed task: '
        'forty point eight in 2013, thirty-nine point three in 2014. A late assignment: twenty point two and '
        'twenty point three. No click in the last seven days: fourteen point five and fifteen point eight. '
        'Activity below the run median: thirteen point four and fourteen point six. No click before the '
        'start: ten point six and eight point seven. All five clear the five-point line in both years. How '
        'firm is this? [click]'
    ),
    23: (
        '(~49 seconds) We tried to break this result. Between the years, no sign moves by more than two '
        'points, and each keeps its direction in every module and under six sensitivity runs. One small '
        'exception: a late assignment in AAA in 2014, on three hundred forty-eight students, with an interval'
        ' including zero. One real weakness: our click signs are yes or no. With clicks added as a continuous'
        ' measure, below-median activity shrinks to five point eight points in 2013, and in 2014 it no longer'
        ' meets our criterion. The other four signs still do. So confidence is moderate, and these are '
        'associations, not causes. [click]'
    ),
    24: (
        '(~43 seconds) The Traceability Matrix puts all four side by side. Each row follows one question from'
        ' goal to decision. In the first two rows every link holds evidence. AQ1 rests on twenty-eight '
        'thousand sixty-one enrolments and feeds D2 and D3. AQ2 rests on both years and five of five signs, '
        'and feeds D2 and the reasons for D1. GAP marks only what OULAD lacks: delivery mode, year of study, '
        'attendance, contacts. The last two rows stop at the evaluation design, marked N.A. So what would AQ3'
        ' and AQ4 give? [click]'
    ),
    25: (
        '(~48 seconds) For AQ3 and AQ4 we can show only the shape of the answer; this card is a mock-up with '
        'no data. AQ3 would give each enrolment a risk rank, with a probability only if calibration holds. '
        "Gate S1 decides it once, on the 2014 runs. If the model doesn't beat the rule, the rule's order "
        'stays. AQ4 would cut the ranking to three or five names per twenty students, each with its signs, '
        'and must also pass the fairness rule or have its flags reviewed. Neither says who should call, or '
        'whether calling helps. So what can decisions use today? [click]'
    ),
    26: (
        '(~48 seconds) D1, whom to contact, is reversible, so it can start with the early-sign rule: '
        'computable from records the university already holds, and each part went with later non-completion '
        'in both years. A staff member checks every name; nothing is automated. Since the rule names more '
        'students than staff can reach, ranking within capacity is the next test. D2 gets a hypothesis: put '
        'early support time first where non-completion and early signs are highest, to check on the '
        "university's records. D3 gets a measurement method, a gate and a fairness audit, and waits for a "
        'pilot. How did AI help? [click]'
    ),
    27: (
        '(~46 seconds) We used generative AI in four roles: simulated stakeholder, research and code '
        'assistant, critic, and writing partner. One rule held in all four: AI was never a source of data, '
        'statistics or results. Everything it offered, we checked against a saved source, the data, or code '
        'we ran. It helped most as a critic: in Milestone three it caught tasks due before a student '
        'registered being counted as missed, and a leakage check that could never fail. The key decisions '
        'stayed ours, such as keeping 2014 out of every AQ3 choice. So, what can we conclude? [click]'
    ),
    28: (
        "(~59 seconds) [checkpoint 3: the last two slides must start by 22:00] Let's bring it together, "
        'firmest first. [pause] One, with high confidence for OULAD: forty-five point three percent of '
        'students still registered at day fourteen did not complete, in both years. Runs varied from twenty-'
        'four point nine to fifty-eight point three percent, the year comparison depends on the add-drop '
        'rule, and most non-completers first missed a task after week four. Two, with moderate confidence: '
        'all five early signs, silence included, go with later non-completion in both years, a missed task by'
        " forty point eight and thirty-nine point three points. That's an association. Three, for AQ3 and AQ4"
        " we have the right design, not a result. What we can't conclude: that the signs cause non-"
        'completion, that a model beats the rule, or that a call helps. [click]'
    ),
    29: (
        '(~61 seconds) Three kinds of limits stay apart. "No evidence found": we compared and saw no clear '
        'difference, like the year difference in shared modules. "No data to test": no screened dataset holds'
        ' it, like any record of contact. "Not yet tested": AQ3 and AQ4. And our results describe UK distance'
        ' learning in 2013 and 2014. Three next steps. First, the single AQ3 test, then the AQ4 list and its '
        "fairness audit. Second, a recount on the university's own records, and the risk classification the "
        'law requires. Third, a randomised pilot, because only random assignment separates the effect of a '
        'call from the reasons a student was flagged. [pause] If you remember one thing: a missed task comes '
        'too late; count silence too, and test contact before you trust it. [click]'
    ),
    30: (
        '(~31 seconds) We began with students noticed too late, and staff who asked for a short list with a '
        'reason beside each name. Records dated by week four can give those reasons now, as long as silence '
        'counts beside missed tasks. Whether a model ranks better, and whether a call helps, are the next '
        "test and the pilot. Thank you. We're happy to take your questions."
    ),
}


# ----------------------------------------------------------------------------- helpers (inches)
def tb(term, rest, color=NAVY):
    """A paragraph that opens with a bold term in colour, then plain text."""
    return [(T(term), color, True), (T(rest), INK, False)]


def rich_h(paras, w, pt=BODY):
    """Height of paragraphs (plain strings or run lists) wrapped to width w, as rich() lays them out."""
    h = 0.0
    for p in paras:
        t = p if isinstance(p, str) else "".join(r[0] for r in p)
        bold = not isinstance(p, str) and any(r[2] for r in p)
        h += lh(t, w, pt, bold) + pt * 0.45 / 72
    return h


def rich(s, x, y, w, paras, pt=BODY, color=INK, align=PP_ALIGN.LEFT):
    """Paragraphs at (x, y); returns the y below them."""
    runs = [[(p, color, False)] if isinstance(p, str) else p for p in paras]
    h = rich_h(paras, w, pt)
    text(s, I(x), I(y), I(w), I(h), runs, size=pt, color=color, align=align, spacing=1.0)
    return y + h


def card_h(head, paras, w, pt=BODY, hp=HEAD):
    return 0.16 + (lh(head, w - 0.36, hp, True) + 0.06 if head else 0) + rich_h(paras, w - 0.36, pt) + 0.08


def card(s, x, y, w, head, paras, color=NAVY, h=None, fill=SOFT, line=LINE, pt=BODY, hp=HEAD, line_w=1.0):
    """A rounded card with a bold head in `color` and paragraphs under it; returns its bottom."""
    h = h or card_h(head, paras, w, pt, hp)
    rect(s, I(x), I(y), I(w), I(h), fill=fill, line=line, radius=True, line_w=line_w)
    ty = y + 0.16
    if head:
        hh = lh(head, w - 0.36, hp, True)
        text(s, I(x + 0.18), I(ty), I(w - 0.36), I(hh), head, size=hp, color=color, bold=True, spacing=1.0)
        ty += hh + 0.06
    rich(s, x + 0.18, ty, w - 0.36, paras, pt)
    return y + h


def cols(n, gap=0.25, x=None, w=None):
    """x positions and width of n equal columns across the content area (or across [x, x + w])."""
    x = X0 if x is None else x
    w = CWI if w is None else w
    cw = (w - (n - 1) * gap) / n
    return [x + k * (cw + gap) for k in range(n)], cw


def text_w(line, pt):
    """Width in inches of one line of bold Arial at pt."""
    return kit.ImageFont.truetype(kit.TITLE_FONT, pt * 10).getlength(line) / 720


def dashed(shape):
    shape.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    return shape


def key(s, y, line, x=None, w=None):
    """A key line (what a mark or colour means) at PT["small"] in a dark grey; returns the y below it."""
    return note(s, line, y, x, w, color=KEY)


def fit_pt(paras, w, room):
    """The largest kit size (lead 18, body 16, dense 14 pt) at which the paragraphs fit `room` inches."""
    return next((pt for pt in (PT["lead"], PT["body"]) if rich_h(paras, w, pt) <= room), BODY)


def table_h(rows, col_w, size, row_h=0.42):
    """Height (inches) the kit's table() gives these rows, measured before drawing so a size can be chosen."""
    total = 0
    for i, row in enumerate(rows):
        need = max(kit.line_h(v, cw / EMU - 0.24, size, i == 0 or j == 0) for j, (v, cw) in enumerate(zip(row, col_w)))
        total += max(need + 0.16, row_h if i else 0.55)
    return total


def stretch_table(shape, height):
    """Grow a kit table to `height` inches by sharing the extra over its body rows (never shrinks it)."""
    rows = list(shape.table.rows)[1:]
    extra = height - shape.height / EMU
    if extra <= 0 or not rows:
        return shape.height / EMU
    for r in rows:
        r.height = r.height + I(extra / len(rows))
    shape.height = sum(r.height for r in shape.table.rows)
    return shape.height / EMU


def bottom_key(s, line, x=None, w=None):
    """A key line set on the bottom edge of the content area; returns its top (inches)."""
    w = w if w is not None else CWI
    top = END - lh(line, w, PT["small"])
    key(s, top, line, x, w)
    return top


def src(s, line):
    """The slide's source, appended to its speaker notes (the slide face carries no source line)."""
    tf = s.notes_slide.notes_text_frame
    tf.text = tf.text + "\n\n" + T(line)


def closing_box(s, y, line, h=None):
    """A navy box with one white message line across the content width; returns its bottom."""
    mh = h or lh(line, CWI - 0.6, PT["lead"], True) + 0.3
    rect(s, MX, I(y), CW, I(mh), fill=NAVY, radius=True)
    text(s, MX + I(0.3), I(y), CW - I(0.6), I(mh), line, size=PT["lead"], color=WHITE, bold=True,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    return y + mh


def fmt(v, digits=1, sign=False):
    """A number in the language's style with a true minus sign."""
    return charts.num(v, digits, sign=sign).replace("-", "−")


# ----------------------------------------------------------------------------- Introduction
def s_title(prs):
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
                             T("University of Science · November 2026")], pt=PT["small"] + 2, color=GREY)
    s.notes_slide.notes_text_frame.text = T(NOTES[1])


def timeline_noticed(s, y0, band_slots=(1, 3), band_label="Window for effective support (weeks 2–4)"):
    """Weeks 1-8, the semester end and after it: the window for support against the moments each group notices.
    band_slots = (first slot, number of slots) of the orange band; band_label is its English label."""
    xa, xb = 0.9, 12.75
    slots = [T("Week 1"), T("Week 2"), T("Week 3"), T("Week 4"), T("Week 5"), T("Week 6"), T("Week 7"), T("Week 8"),
             "…", T("Semester end"), T("After the semester")]
    sw = (xb - xa) / len(slots)
    ya = y0 + 1.65                                   # the axis
    cx = lambda k: xa + (k + 0.5) * sw             # noqa: E731  centre of slot k (0-based)
    b0, bn = band_slots
    band = rect(s, I(xa + b0 * sw), I(y0), I(bn * sw), I(ya - y0), fill=ACC_FILL, line=WARM)
    band.line.width = kit.Pt(1.0)
    rich(s, xa + b0 * sw + 0.08, y0 + 0.06, bn * sw - 0.16, [T(band_label)], pt=PT["small"] + 2, color=AGENT_INK)
    rect(s, I(xa), I(ya - 0.02), I(xb - xa), I(0.04), fill=GREY)
    for k, name in enumerate(slots):
        rect(s, I(cx(k) - 0.01), I(ya - 0.06), I(0.02), I(0.12), fill=GREY)
        lab = lh(name, sw - 0.02, PT["small"])
        text(s, I(cx(k) - sw / 2), I(ya + 0.1), I(sw), I(lab), name, size=PT["small"], color=INK,
             align=PP_ALIGN.CENTER, spacing=1.0)
    # the moments each group notices (grey markers)
    lect = rect(s, I(xa + 4 * sw + 0.05), I(ya - 0.13), I(2 * sw - 0.1), I(0.26), fill=GREY, radius=True)
    lect.adjustments[0] = 0.5
    rich(s, xa + 4 * sw - 0.15, ya - 0.95, 2 * sw + 0.6,
         [[(T("Lecturers become sure"), INK, True)], T("around week 5 or 6")], pt=PT["small"] + 2,
         align=PP_ALIGN.CENTER)
    lw_ = 3.3
    for k, y_lab, lx, line_top, head, body in [
            (9, ya - 0.95, cx(9) - 0.12 - lw_, ya - 0.72, T("Support office meets the student"),
             T("on the academic warning list")),
            (10, y0, XR - lw_, y0 + 0.62, T("Program manager sees counts"), T("after the semester"))]:
        dot = s.shapes.add_shape(9, I(cx(k) - 0.13), I(ya - 0.13), I(0.26), I(0.26))   # 9 = oval
        dot.fill.solid()
        dot.fill.fore_color.rgb = GREY
        dot.line.fill.background()
        rect(s, I(cx(k) - 0.01), I(line_top), I(0.02), I(ya - 0.13 - line_top), fill=LINE)
        rich(s, lx, y_lab, lw_, [[(head, INK, True)], body], pt=PT["small"] + 2, align=PP_ALIGN.RIGHT)
    return ya + 0.6


def s_noticed(prs):
    s = kit.base(prs, K["intro"], T("Noticed Too Late"), T(NOTES[2]))
    y = lead(s, T("Staff notice a student who has stopped taking part only after the window in which help works best."))
    y = timeline_noticed(s, y + 0.2)
    y = key(s, y - 0.05, T("Key: the orange band marks the window for effective support; grey markers mark the moment "
                           "each group of staff notices."))
    y = key(s, y + 0.02, T("Basis: the window of weeks 2–4 comes from a published study of predictive learning "
                           "analytics at the Open University (Herodotou et al., 2019); the moments staff notice come "
                           "from simulated stakeholder interviews.")) + 0.25
    xs, cw = cols(3)
    items = [(T("Setting"), [T("A Vietnamese university expands online and blended learning on its learning management "
                               "system (LMS); one program has about 1,200 students (a scenario assumption).")]),
             (T("Disengagement"), [T("A student misses a task, opens the course less often and falls silent before a "
                                     "fail or a withdrawal is recorded.")]),
             (T("Stakes"), [T("Circular 01/2024 caps withdrawal at 10% a year and 15% in the first year; Circular "
                              "83/2026 keeps these caps from 15 November 2026. Withdrawal, one part of non-completion, "
                              "is therefore a regulated quality measure.")])]
    h = max(card_h(a, b, cw) for a, b in items)
    kit.room("noticed cards", y + h, END)
    h = END - y                                  # the cards fill the rest of the slide
    for x, (a, b) in zip(xs, items):
        card(s, x, y, cw, a, b, h=h)
    src(s, "Source: Milestone 5 report, Section 1; Herodotou et al. (2019).")


def s_answer(prs):
    s = kit.base(prs, K["intro"], T("Our Answer in Brief"), T(NOTES[3]))
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
             (T("Signs"), T("5 of 5"), T("early signs, from tasks and from activity, go with later non-completion in both years; a missed "
                                         "task adds 40.8 (2013) and 39.3 (2014) percentage points."))]
    vh = kit.num_h(PT["title"] + 6)
    h = max(0.14 + lh(a, cw - 0.36, HEAD, True) + 0.04 + vh + 0.04 + rich_h([c], cw - 0.36) + 0.06
            for a, b, c in items)
    oh_ = rich_h([[(T("Still open: "), GREY, True), (T("the prediction model and the ranked list are designed, not run; "
                                                        "the effect of contact is untested."), INK, False)]],
                 CWI - 0.36) + 0.1
    h = max(h, END - oh_ - 0.25 - y)             # the cards fill down to the open strip
    for x, (a, b, c) in zip(xs, items):
        rect(s, I(x), I(y), I(cw), I(h), fill=SOFT, line=LINE, radius=True)
        ah = lh(a, cw - 0.36, HEAD, True)
        text(s, I(x + 0.18), I(y + 0.14), I(cw - 0.36), I(ah), a, size=HEAD, color=NAVY, bold=True, spacing=1.0)
        text(s, I(x + 0.18), I(y + 0.18 + ah), I(cw - 0.36), I(vh), b, size=PT["title"] + 6, color=WARM, bold=True,
             spacing=1.0)
        rich(s, x + 0.18, y + 0.22 + ah + vh, cw - 0.36, [c])
    open_line = [[(T("Still open: "), GREY, True),
                  (T("the prediction model and the ranked list are designed, not run; the effect of contact is "
                     "untested."), INK, False)]]
    oh = rich_h(open_line, CWI - 0.36) + 0.1
    kit.room("answer strip", y + h + 0.25 + oh, END)
    y = END - oh                                 # the open strip sits on the bottom edge
    rect(s, MX, I(y), CW, I(oh), fill=pal_rgb("#E6E8EC"), radius=True)
    rich(s, X0 + 0.18, y + 0.07, CWI - 0.36, open_line)
    src(s, "Source: Milestone 5 report, Sections 2.1, 3, 10, 11.2, 11.3 and 11.4.")


def pal_rgb(hexc):
    return pal.rgb(hexc)


# ----------------------------------------------------------------------------- Part 1: the problem
def decision_cards(s, y, items, gap=0.25, bottom=None):
    """Three decision cards (head, body paragraphs, tag, accent?) in a row, down to `bottom` when given; returns their
    bottom."""
    xs, cw = cols(3, gap)
    th = 0.36
    h = max(card_h(a, b, cw) + (th + 0.12 if t else 0) for a, b, t, _ in items)
    if bottom:
        kit.room("decision cards", y + h, bottom)
        h = bottom - y
    for x, (a, b, t, acc) in zip(xs, items):
        card(s, x, y, cw, a, b, color=AGENT_INK if acc else NAVY, h=h, fill=ACC_FILL if acc else SOFT,
             line=WARM if acc else LINE, line_w=2.0 if acc else 1.0)
        if t:
            tw = min(cw - 0.36, 0.35 + text_w(t, PT["small"]))
            chip(s, x + 0.18, y + h - th - 0.14, tw, th, t, fill=WHITE, line_color=WARM if acc else GREY,
                 color=AGENT_INK if acc else INK, bold=True)
    return y + h


def s_stakeholders(prs):
    s = kit.base(prs, K["p1"], T("Stakeholders, Needs and Decisions"), T(NOTES[4]))
    y = lead(s, T("Three groups of staff each take one decision, and all of them asked for a short list with a factual "
                  "reason beside each name."))
    review = [tb("Review point: ", "a moment in week 3 or week 5 when staff decide whom to contact.")]
    needs = [T("A list at weeks 3 and 5, with a factual reason beside each name."),
             T("About 30–40 contacts a week for the support office, and three to five for each lecturer-advisor."),
             T("Support only, with no automated step.")]
    needs = [[("•  ", NAVY, True), (n, INK, False)] for n in needs]
    source = T("Source of the needs: simulated interviews with AI on both sides (five stakeholders, 51 key "
               "statements, six themes); they motivate the design and are never evidence.")
    lower = rich_h(review, CWI) + 0.12 + card_h(T("What all three groups need"), needs, CWI) + 0.12 + \
        lh(source, CWI, PT["small"])                 # the review line, the needs card and the key, on the bottom edge
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
    src(s, "Source: Milestone 5 report, Sections 1.1 and 2.1, and Appendix I.")


def s_goal(prs):
    s = kit.base(prs, K["p1"], T("Business Goal and KPIs"), T(NOTES[5]))
    y = lead(s, T("Success is more students passing, measured by one completion KPI and two contact KPIs."))
    tw = 8.85                                                     # the goal tree on the left
    bg = [tb("Business Goal: ", "improve successful course completion by identifying students who stop taking part "
                                "early enough to support them within the semester.")]
    sm = [tb("SMART Goal ", "(specific, measurable, achievable, relevant, time-bound): completion after add-drop in "
                            "the pilot courses rises five points from the recounted baseline by the end of 2027–2028, "
                            "in about four pilot courses with about 600 enrolments (assumptions).")]
    y1 = card(s, X0, y, tw, None, bg, fill=WHITE, line=NAVY)
    arrow(s, X0 + tw / 2, y1 + 0.02, X0 + tw / 2, y1 + 0.38)
    y2 = card(s, X0, y1 + 0.4, tw, None, sm, fill=WHITE, line=NAVY)
    xs, cw = cols(3, 0.2, X0, tw)
    kpis = [(T("Primary KPI"), T("Completion rate after add-drop."), T("Proxy on OULAD"), OUT_FILL, PLUS, OUT_INK),
            (T("Secondary KPI 1"), T("Students flagged by the early-sign rule (a missed or late task, or a silent "
                                     "week) at week 4 and contacted by the end of week 5."), T("Sign part on OULAD"), WHITE, PLUS, OUT_INK),
            (T("Secondary KPI 2"), T("Listed students contacted within seven days."), T("Pilot only"), WHITE, GREY,
             GREY)]
    ky = y2 + 0.5
    on = [T("OULAD (Open University Learning Analytics Dataset) is our public data. Primary KPI: a proxy at day 14 "
            "(28,061 enrolments). KPI 1: sign part only (28.8% flagged at day 27). Contact parts: pilot only.")]
    lab = T("Completion in the pilot courses, from the assumed baseline to the target.")
    rw_ = CWI - tw - 0.3
    side_top = y + 0.15 + kit.num_h(PT["cover"]) + 0.06 + rich_h([lab], rw_ - 0.36) + 0.45 + 0.15
    tags_h = lh(T("Tags: green = measured on OULAD; grey = pilot only. KPI: key performance indicator."), rw_,
                PT["small"])
    kp = PT["body"]                                  # 16 pt where both columns fit, else the dense 14 pt
    if (ky + max(card_h(a, [b], cw, pt=kp) for a, b, *_ in kpis) + 0.42 > END
            or side_top + card_h(T("On OULAD"), on, rw_, pt=kp) + 0.1 + tags_h > END):
        kp = BODY
    kh = max(card_h(a, [b], cw, pt=kp) for a, b, *_ in kpis) + 0.42
    kit.room("goal tree", ky + kh, END)
    kh = END - ky                                # the KPI cards fill to the bottom edge
    rect(s, I(X0 + tw / 2 - 0.01), I(y2), I(0.02), I(0.25), fill=GREY)
    rect(s, I(xs[0] + cw / 2), I(y2 + 0.25), I(xs[2] - xs[0]), I(0.02), fill=GREY)
    for x, (a, b, t, fill, lc, tc) in zip(xs, kpis):
        arrow(s, x + cw / 2, y2 + 0.25, x + cw / 2, ky - 0.02)
        card(s, x, ky, cw, a, [b], h=kh, pt=kp)
        chip(s, x + 0.18, ky + kh - 0.42, cw - 0.36, 0.3, t, fill=fill, line_color=lc, color=tc, bold=True)
    kit.room("goal tree", ky + kh, END)
    rx, rw = X0 + tw + 0.3, CWI - tw - 0.3
    lab = T("Completion in the pilot courses, from the assumed baseline to the target.")
    th_ = 0.15 + kit.num_h(PT["cover"]) + 0.06 + rich_h([lab], rw - 0.36) + 0.45
    rect(s, I(rx), I(y), I(rw), I(th_), fill=SOFT, line=LINE, radius=True)
    text(s, I(rx), I(y + 0.15), I(rw), I(kit.num_h(PT["cover"])), T("70% → 75%"), size=PT["cover"], color=WARM,
         bold=True, align=PP_ALIGN.CENTER, spacing=1.0)
    ly = rich(s, rx + 0.18, y + 0.21 + kit.num_h(PT["cover"]), rw - 0.36, [lab], align=PP_ALIGN.CENTER)
    chip(s, rx + rw / 2 - 0.6, ly + 0.0, 1.2, 0.32, T("Assumed"), fill=WHITE, line_color=GREY, color=GREY, bold=True)
    tags = T("Tags: green = measured on OULAD; grey = pilot only. KPI: key performance indicator.")
    tk = lh(tags, rw, PT["small"])
    oy = y + th_ + 0.15
    kit.room("goal side", oy + card_h(T("On OULAD"), on, rw, pt=kp) + 0.1 + tk, END)
    card(s, rx, oy, rw, T("On OULAD"), on, h=END - tk - 0.1 - oy, pt=kp)
    key(s, END - tk, tags, rx, rw)
    src(s, "Source: Milestone 5 report, Sections 2 and 2.1, Table 2.1; 70% and 75% are assumptions that the "
           "university's recount replaces.")


def s_questions(prs):
    s = kit.base(prs, K["p1"], T("Four Analytical Questions"), T(NOTES[6]))
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
    bottom = END - lh(ladder_key, CWI, PT["small"]) - 0.12      # the rungs stand on the key at the bottom edge
    kit.room("question ladder", need + 3 * step, bottom - (y + 0.25))
    top0 = y + 0.25                                 # top of the highest rung (AQ4)
    for k, (x, (a, b, c, d)) in enumerate(zip(xs, rungs)):
        top = top0 + (3 - k) * step
        run = k < 2
        card(s, x, top, cw, a, [b, c, [(d, AGENT_INK, True)]], h=bottom - top,
             fill=ACC_FILL if run else WHITE,
             line=WARM if run else GREY, line_w=2.0 if run else 1.0)
        chip(s, x + 0.18, bottom - tag_h + 0.02, cw - 0.36, 0.3, T("Run on the data") if run else T("Design only"),
             fill=WARM if run else WHITE, line_color=WARM if run else GREY, color=WHITE if run else GREY, bold=True)
    key(s, bottom + 0.12, ladder_key)
    src(s, "Source: Milestone 5 report, Section 3 and Table 3.1.")


# ----------------------------------------------------------------------------- Part 2: the data
def s_requirements(prs):
    s = kit.base(prs, K["p2"], T("Data Requirements"), T(NOTES[7]))
    y = lead(s, T("We wrote what the data must contain before searching, so the questions chose the data and not the "
                  "reverse."))
    lw = 5.3
    rx, rw = X0 + lw + 0.45, CWI - lw - 0.45
    gates = [T("A dated outcome"), T("Dated tasks"), T("Dated activity"), T("At least three time-ordered runs"),
             T("An open licence with provenance"), T("A persistent anonymised identifier")]
    gap_line = [tb("Known gap, declared before the search: ", "no dataset records staff contacts.", GREY)]
    gh = rich_h(gap_line, rw - 0.36, PT["body"]) + 0.2
    gate_key = T("Key: a ticked box is a must-have gate; the grey box is a known gap.")
    kh = lh(gate_key, rw, PT["small"])
    gb = END - kh - 0.15                            # bottom of the known-gap box
    head_h = 0.45
    step = (gb - gh - 0.3 - (y + head_h)) / len(gates)          # the gates share the column evenly
    kit.room("gate list", 0.45 * len(gates), gb - gh - 0.3 - (y + head_h))
    text(s, I(rx), I(y), I(rw), I(0.35), T("Six must-have gates"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    gy = y + head_h
    for g in gates:
        cy = gy + (step - 0.36) / 2
        rect(s, I(rx), I(cy), I(0.36), I(0.36), fill=WHITE, line=NAVY, line_w=1.5)
        icon(s, "check", rx + 0.04, cy + 0.04, 0.28, color=NAVY, bg=WHITE)
        text(s, I(rx + 0.55), I(cy + 0.01), I(rw - 0.6), I(0.34), g, size=PT["body"], color=INK, spacing=1.0)
        gy += step
    dashed(rect(s, I(rx), I(gb - gh), I(rw), I(gh), fill=pal_rgb("#E6E8EC"), line=GREY, radius=True, line_w=1.5))
    rich(s, rx + 0.18, gb - gh + 0.1, rw - 0.36, gap_line, pt=PT["body"])
    key(s, END - kh, gate_key, rx, rw)
    ch = (gb - y - 0.3) / 2                         # the two needs cards, level with the gate column
    left = [(T("Every question needs"), [T("One enrolment as the unit, the population enrolled after add-drop, and "
                                           "the final result with a dated withdrawal.")]),
            (T("Every event needs a date"), [T("Each list may use only data recorded up to its cut-off, so every event "
                                               "must carry its date.")])]
    kit.room("needs cards", max(card_h(a, b, lw, pt=PT["lead"], hp=PT["head"]) for a, b in left), ch)
    for k, (a, b) in enumerate(left):
        card(s, X0, y + k * (ch + 0.3), lw, a, b, h=ch, pt=PT["lead"], hp=PT["head"])
    src(s, "Source: Milestone 5 report, Section 4 and Table 4.1.")


def s_selection(prs):
    s = kit.base(prs, K["p2"], T("Dataset Search and Selection"), T(NOTES[8]))
    y = lead(s, T("Of seven public candidates, only OULAD passes every gate, so we chose it for fit, not for ease."))
    y = rich(s, X0, y, CWI, [T("Each candidate is scored 0–2 on the brief's ten criteria (20 at most); the must-have "
                               "gates decide first. UCI: the University of California, Irvine, Machine Learning "
                               "Repository.")])
    rows = [[T("Candidate"), T("Score (of 20)"), T("Gates failed"), T("Decision")],
            ["OULAD", "12", T("none"), T("Selected")],
            ["UCI 697", "10", T("dated outcome, tasks, activity"), T("Rejected")],
            ["UCI 320", "6", T("dated outcome, tasks, activity, runs"), T("Rejected")],
            ["UCI 856", "7", T("dated outcome, tasks, activity, runs"), T("Rejected")],
            ["XuetangX", "8", T("dated outcome, tasks, licence"), T("Rejected")],
            ["HarvardX", "8", T("dated outcome, tasks, activity, runs, licence"), T("Rejected")],
            ["xAPI-Edu-Data", "4", T("dated outcome, tasks, activity, runs"), T("Rejected")]]
    widths = [int(CW * f) for f in (0.2, 0.14, 0.48)]
    widths.append(CW - sum(widths))
    shape = table(s, MX, I(y), CW, rows, widths, size=BODY, row_h=I(0.31))
    tbl = shape.table
    for j in range(4):                                   # the selected row in the accent colour
        c = tbl.cell(1, j)
        c.fill.solid()
        c.fill.fore_color.rgb = ACC_FILL
        for r in c.text_frame.paragraphs[0].runs:
            r.font.bold, r.font.color.rgb = True, AGENT_INK
    for i in range(2, len(rows)):                        # failed gates in red
        c = tbl.cell(i, 2)
        c.fill.solid()
        c.fill.fore_color.rgb = BAD_FILL
        for r in c.text_frame.paragraphs[0].runs:
            r.font.color.rgb = MINUS
    sel_key = T("Key: orange row = selected; red cell = a gate failed.")
    notes8 = [tb("OULAD, the Open University Learning Analytics Dataset: ",
                 "the only candidate with a dated withdrawal, dated submissions and daily clicks; version 1, "
                 "accessed 6 November 2026, CC BY 4.0 licence, anonymised, and we never re-identify anyone."),
              tb("Why only 12 of 20: ", "OULAD scores 1 of 2 on most criteria, but no other candidate shows "
                                        "when a student stopped.")]
    lower = 0.08 + lh(sel_key, CWI, PT["small"]) + 0.2 + rich_h(notes8, CWI)
    y += stretch_table(shape, END - lower - y)       # the table rows take the free height
    y = key(s, y + 0.08, sel_key) + 0.2
    rich(s, X0, y, CWI, notes8)
    src(s, "Source: Milestone 5 report, Section 4.1, Table 4.2 and Appendix IV, Table A.10.")


OUTCOMES = {"Distinction": 3024, "Pass": 12361, "Fail": 7052, "Withdrawn": 10156}     # Section 5


def outcome_bar(fig):
    ax = charts.axes(fig)
    names = [T("Distinction"), T("Pass"), T("Fail"), T("Withdrawn")]
    colours = [pal.shade(pal.OTHER, 0.3), pal.OTHER, pal.ORANGE, pal.shade(pal.ORANGE, 0.3)]
    charts.stacked(ax, [""], {n: [v] for n, v in zip(names, OUTCOMES.values())}, percent=False, colors=colours,
                   min_label=0.05)


def s_oulad(prs):
    s = kit.base(prs, K["p2"], T("OULAD and Its Fit"), T(NOTES[9]))
    y = lead(s, T("OULAD dates every outcome, task and click, but lacks delivery mode, year of study, attendance and "
                  "any contact record."))
    y = rich(s, X0, y, CWI, [
        T("OULAD holds 22 runs of seven UK distance-learning modules (AAA–GGG): in 2013, 9 runs of six modules with "
          "13,529 enrolments; in 2014, 13 runs of all seven modules with 19,064 enrolments."),
        tb("Module runs ", "are named by year and start month (B = February, J = October); days count from day 0, the "
                           "run's start.")])
    bar_key = T("Key: greys = completion (Distinction, Pass); orange and brown = non-completion (Fail, Withdrawn).")
    rates = [tb("Two rates: ", "over all 32,593 enrolments, 17,208 (52.8%) did not complete; among the 28,061 still "
                               "registered at day 14 (the add-drop rule, Slide 11), 45.3% did not complete.")]
    fit_key = T("Fit rating: GREEN = the data are enough; YELLOW = the question is narrowed; RED = a key concept, "
                "variable or intervention is missing. Nothing is imputed or simulated, and no question is dropped.")
    for chip_h, chip_step, gap9 in ((0.46, 0.56, 0.2), (0.38, 0.44, 0.08)):   # roomy where it fits, else compact
        fit_top = END - lh(fit_key, CWI, PT["small"]) - 0.12 - (chip_step + chip_h) - 0.4
        ch9 = fit_top - gap9 - rich_h(rates, CWI) - 0.04 - lh(bar_key, CWI, PT["small"]) - 0.05 - (y + 0.3)
        if ch9 >= 1.0:
            break
    kit.room("outcome bar", y + 0.3 + 1.0, y + 0.3 + ch9)
    ch9 = max(ch9, 0.8)
    text(s, I(X0), I(y + 0.0), CW, I(0.3), T("Final results of all 32,593 enrolments of 28,785 students (number of "
                                             "enrolments)"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    chart(s, "m5-30-outcomes", X0, y + 0.3, CWI, ch9, outcome_bar)
    y = key(s, y + 0.3 + ch9 + 0.05, bar_key)
    rich(s, X0, y + 0.04, CWI, rates)
    y = fit_top
    text(s, I(X0), I(y), I(4), I(0.3), T("Fit of the data with each question"), size=HEAD, color=NAVY, bold=True,
         spacing=1.0)
    y += 0.4
    fits = [(T("AQ1: YELLOW"), T("No year of study or delivery mode."), GOLD),
            (T("AQ2: YELLOW"), T("No attendance record."), GOLD),
            (T("AQ3: YELLOW"), T("A task-only rule rarely fires early."), GOLD),
            (T("AQ4: RED"), T("No contact data: ranking part only."), MINUS)]
    xs, cw = cols(2, 0.2)
    for k, (a, b, c) in enumerate(fits):
        x, yy = xs[k % 2], y + (k // 2) * chip_step
        chip(s, x, yy, cw, chip_h, "", fill=BAD_FILL if c == MINUS else pal_rgb(pal.tint(pal.GOLD)), line_color=c)
        text(s, I(x + 0.15), I(yy), I(cw - 0.3), I(chip_h), [[(a + "  ", c if c == MINUS else AGENT_INK, True),
                                                            (b, INK, False)]], size=BODY, anchor=MSO_ANCHOR.MIDDLE,
             spacing=1.0)
    key(s, END - lh(fit_key, CWI, PT["small"]), fit_key)
    src(s, "Source: Milestone 5 report, Sections 5 and 5.1, Table 5.2.")


# ----------------------------------------------------------------------------- Part 3: preparation
def s_quality(prs):
    s = kit.base(prs, K["p3"], T("Data Quality"), T(NOTES[10]))
    y = lead(s, T("Of nineteen quality issues, three are serious enough to change the method."))
    y = rich(s, X0, y, CWI, [
        T("We profiled all 10.9 million rows of the seven raw tables and recounted 13 figures independently; all 13 "
          "agree."),
        tb("Issue log: ", "19 issues, rated High (would change a rate, the target or a feature), Medium (changes a "
                          "measure by a known amount) or Low.")]) + 0.1
    lw = 5.4
    rx = X0 + 0.25 + lw + 0.7
    rw = XR - rx
    text(s, I(X0 + 0.25), I(y), I(lw), I(0.3), T("High issue"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    text(s, I(rx), I(y), I(rw), I(0.3), T("Change in method"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    y += 0.38
    rows = [(T("18 of 24 exams have no result rows."),
             T("A task means a TMA or a CMA only (TMA: tutor-marked assignment; CMA: computer-marked assessment, a "
               "quiz).")),
            (T("Few tasks fall due by the cut-offs."), T("The early-sign rule needs an activity part.")),
            (T("The data are seven UK modules of 2013–2014."),
             T("The scope is stated, and students are compared within module run."))]
    items = [(T("Duplicate click rows (Medium)"), [T("They are 7.39% of click rows and carry 3.19% of clicks, so each "
                                                     "click feature has a de-duplicated twin that tests their "
                                                     "effect.")]),
             (T("Skewed activity"), [T("The median is 602 clicks and 3,365 enrolments have no click, so counts enter "
                                       "as logarithms and no value is removed.")])]
    xs, cw = cols(2)
    ch10 = max(card_h(a, b, cw) for a, b in items)
    q_key = T("Key: the orange bar marks the issue that reshapes the early-sign rule (Slide 12).")
    hs = [max(lh(a, lw - 0.3, BODY), lh(b, rw - 0.3, BODY)) + 0.22 for a, b in rows]
    room_rows = END - ch10 - 0.3 - lh(q_key, CWI, PT["small"]) - 0.08 - y
    kit.room("quality rows", sum(hs) + 0.3, room_rows)
    gap10 = 0.18
    grow = max(0.0, (room_rows - sum(hs) - gap10 * (len(rows) - 1)) / len(rows))
    for k, ((a, b), h) in enumerate(zip(rows, hs)):
        h += grow
        acc = k == 1
        if acc:
            rect(s, I(X0), I(y), I(0.12), I(h), fill=WARM)
        node(s, X0 + 0.25, y, lw, h, None, [a], "agent" if acc else "white", body_pt=BODY, align=PP_ALIGN.LEFT)
        arrow(s, X0 + 0.25 + lw + 0.08, y + h / 2, rx - 0.08, y + h / 2)
        node(s, rx, y, rw, h, None, [b], "white", body_pt=BODY, align=PP_ALIGN.LEFT)
        y += h + gap10
    key(s, y - gap10 + 0.08, q_key)
    for x, (a, b) in zip(xs, items):
        card(s, x, END - ch10, cw, a, b, h=ch10)
    src(s, "Source: Milestone 5 report, Sections 6 and 6.1, Table 6.2.")


def s_adddrop(prs):
    s = kit.base(prs, K["p3"], T("Who Counts: the Add-drop Rule"), T(NOTES[11]))
    y = lead(s, T("We count only students still registered at day 14, because that is when registration closes on "
                  "OULAD."))
    y = rich(s, X0, y, CWI, [tb("University rule: ", "the completion rate counts students enrolled after the add-drop "
                                                     "period."),
                             tb("OULAD proxy: ", "an enrolment counts when it is still registered at day 14, because "
                                                 "registration closes two weeks after a run starts.")])
    rule11 = [tb("One population rule: ", "an enrolment counts on day d when the student registered by day d and had not "
                                          "unregistered by it. It removes the 58 late registrants (days 16–167) from the "
                                          "KPI population and gives each list the students it can name on its day."),
              T("The denominator alone can move a run's rate by up to 13.6 points (Slide 20).")]
    pt11 = PT["body"]
    key11 = T("Key: the orange marker is the KPI population; grey markers are the populations of the two lists.")
    below = card_h(None, rule11, CWI, pt=pt11)
    ry = END - below                                 # the closing panel sits on the bottom edge
    block = 2.5 + lh(key11, CWI, PT["small"])        # timeline (1.25 above the axis, 1.25 below) and its key
    kit.room("add-drop timeline", y + block, ry - 0.25)
    ya = y + 1.25 + (ry - 0.25 - y - block) / 2      # centred above the closing paragraphs
    ky11 = ya + 1.25
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
    key(s, ky11, key11)
    card(s, X0, ry, CWI, None, rule11, pt=pt11, h=below)
    src(s, "Source: Milestone 5 report, Sections 1.2, 2.1, 6, 6.1 and 11.2, Tables 2.1, 6.1 and 6.2, and Appendices III "
           "and VII.")


def s_rule(prs):
    s = kit.base(prs, K["p3"], T("The Early-sign Rule"), T(NOTES[12]))
    y = lead(s, T("Few tasks fall due in the first weeks, so the early-sign rule also counts a week without "
                  "activity."))
    lw = 4.3
    y1 = card(s, X0, y, lw, T("Milestone 1 rule"), [T("Two or more assessed tasks missed or late by week 4.")])
    due = [T("One or more tasks fall due by day 27 in 16 of 22 runs, and by day 13 in only 1; no 2013 run has a task "
             "due by day 13.")]
    dy = END - rich_h(due, lw)                       # the note on the bottom edge, the number box above it
    bh = dy - 0.2 - (y1 + 0.2)
    num_label = T("runs has two or more tasks due by day 27.")
    nh = kit.num_h(PT["number"]) + 0.05 + lh(num_label, lw - 0.3)
    kit.room("rule number", y1 + 0.2 + nh + 0.24, dy - 0.2)
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
    key12 = T("Key: the orange part is the activity part added for the data. TMA: tutor-marked assignment; CMA: "
              "computer-marked quiz.")
    more = [T("One rule serves OULAD and the pilot. AQ2 tests these three parts and two more activity signs: activity "
              "below the run median and no click before the start."),
            tb("Late quizzes stay out: ", "the meaning of a late CMA in 2013–2014 is not documented, and counting them "
                                          "would raise the share flagged at day 27 from 28.8% to 41.2%; they become a "
                                          "sensitivity run."),
            tb("At day 27 ", "the rule flags 28.8% of 27,535 enrolments.")]
    my = END - rich_h(more, rw)                      # the notes on the bottom edge
    ph = my - 0.15 - lh(key12, rw, PT["small"]) - 0.08 - (y + 0.45)
    kit.room("rule parts", 2.1, ph)
    for x, (a, b, st, ic) in zip(xs, parts):
        node(s, x, y + 0.45, cw, ph, a, [b], st, body_pt=BODY, icon=ic)
    key(s, y + 0.45 + ph + 0.08, key12, rx, rw)
    rich(s, rx, my, rw, more)
    src(s, "Source: Milestone 5 report, Sections 2.1 and 6.1, and Appendices III and VI.")


def s_leakage(prs):
    s = kit.base(prs, K["p3"], T("Preparation and Leakage Control"), T(NOTES[13]))
    y = lead(s, T("Every feature uses only events dated on or before its cut-off, and every learned value comes from "
                  "2013 alone."))
    y = rich(s, X0, y, CWI, [tb("Leakage: ", "using information that would not exist at the moment of prediction.")])
    xa, xb, xc = 0.8, 12.6, 7.1
    ya = y + 1.4
    rect(s, I(xa), I(ya - 0.02), I(xb - xa), I(0.04), fill=GREY)
    text(s, I(xa - 0.4), I(ya + 0.08), I(1.2), I(0.25), T("Day 0"), size=PT["small"], color=KEY,
         align=PP_ALIGN.CENTER, spacing=1.0)
    cut = rect(s, I(xc - 0.015), I(ya - 0.85), I(0.03), I(1.15), fill=NAVY)
    cut.line.fill.background()
    text(s, I(xc - 2.5), I(ya + 0.32), I(5.0), I(0.28), T("Data cut-off: day 27 (the same rule holds at day 13)"),
         size=PT["small"] + 2, color=NAVY, bold=True, align=PP_ALIGN.CENTER, spacing=1.0)
    left = [T("Registration"), T("Clicks up to day 27"), T("Tasks due by day 27")]
    right = [T("Later clicks"), T("Withdrawal day"), T("Final result")]
    lxs, lw = cols(3, 0.15, xa + 0.1, xc - xa - 0.35)
    for x, lab in zip(lxs, left):
        chip(s, x, ya - 0.72, lw, 0.5, lab, fill=SOFT, line_color=GREY, size=PT["small"] + 2)
    rxs, rw = cols(3, 0.15, xc + 0.25, xb - xc - 0.3)
    for x, lab in zip(rxs, right):
        chip(s, x, ya - 0.72, rw, 0.5, "", fill=BAD_FILL, line_color=MINUS)
        icon(s, "cross", x + 0.08, ya - 0.62, 0.3, color=MINUS, bg=BAD_FILL)
        text(s, I(x + 0.4), I(ya - 0.72), I(rw - 0.45), I(0.5), lab, size=PT["small"] + 2, color=MINUS,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    y = key(s, ya + 0.66, T("Key: grey = events left of the cut-off that may feed a feature; red cross = events right "
                           "of it that never enter.")) + 0.3
    ws3 = [3.35, 3.35, CWI - 7.1]
    xs3 = [X0, X0 + 3.35 + 0.2, X0 + 6.9 + 0.2]
    items = [(T("Governing decisions"), [T("Nothing recorded is deleted or imputed."),
                                          T("Every feature uses only events up to its cut-off."),
                                          T("Every learned parameter comes from the training runs.")]),
             (T("Leakage blocked by"), [T("The timing rule, learning on 2013 only and the split by year."),
                                        T("1,586 test enrolments at day 27 of students already seen in 2013 are "
                                          "marked as repeat students.")]),
             (T("Result: one versioned prepared dataset"),
              [T("19 usable predictors, 23 parameters once module and start month are coded."),
               T("All 22 validation checks pass; 32,593 enrolments and their outcome mix are unchanged."),
               T("Six features recomputed from raw by separate code differ in none of 55,604 feature rows; 88 "
                 "variables are documented, and one command rebuilds it.")])]
    pt13 = PT["body"] if max(card_h(a, b, w, pt=PT["body"]) for (a, b), w in zip(items, ws3)) <= END - y else BODY
    h = max(card_h(a, b, w, pt=pt13) for (a, b), w in zip(items, ws3))
    kit.room("leakage cards", y + h, END)
    for x, w, (a, b) in zip(xs3, ws3, items):
        card(s, x, y, w, a, b, h=END - y, pt=pt13)
    src(s, "Source: Milestone 5 report, Sections 7, 7.1 and 7.2.")


# ----------------------------------------------------------------------------- Part 4: method
def s_methods(prs):
    s = kit.base(prs, K["p4"], T("Methods by Question"), T(NOTES[14]))
    y = lead(s, T("Each question gets the simplest method that fits its level, judged against a baseline it must "
                  "beat."))
    rows = [[T("Question"), T("Method"), T("Baseline it must beat")],
            [T("AQ1 – Descriptive"), T("Grouped rates with Wilson intervals (the 95% interval of a share), on two "
                                       "denominators: registered at day 14, and all enrolments."),
             T("Pooled rate: the rate over all enrolments.")],
            [T("AQ2 – Diagnostic"), T("Logistic regression with run fixed effects (a term per module run, so students "
                                      "are compared only within their module run) and sign × module terms; effects as "
                                      "average risk differences (the difference in later non-completion, in "
                                      "percentage points, with and without a sign)."),
             T("Unadjusted rate difference.")],
            [T("AQ3 – Predictive"), T("Penalised logistic regression on the 19 predictors (background, clicks before "
                                      "and after day 0, activity against the run median, recent inactivity, missed and "
                                      "late tasks); challenger: gradient-boosted trees."),
             T("The early-sign rule ranked by its number of signs; a background-only model (module, start month, "
               "previous attempts, credits, education, registration lead; no activity); a random list.")],
            [T("AQ4 – Prescriptive"), T("Top-k list per run (the k highest-ranked students) from the AQ3 scores, with "
                                        "the signs behind each name."), T("A random list; a rule-ranked list.")]]
    widths = [int(CW * f) for f in (0.17, 0.5)]
    widths.append(CW - sum(widths))
    key14 = T("Key: the orange column is the baseline each method must beat. Eight course criteria guide each "
              "choice; ties go to the simpler, more interpretable method.")
    room14 = END - 0.1 - lh(key14, CWI, PT["small"]) - y
    size14 = PT["body"] if table_h(rows, widths, PT["body"]) <= room14 else BODY    # 16 pt where it fits
    shape = table(s, MX, I(y), CW, rows, widths, size=size14)
    tbl = shape.table
    c = tbl.cell(0, 2)
    c.fill.fore_color.rgb = WARM
    for i in range(1, len(rows)):
        c = tbl.cell(i, 2)
        c.fill.solid()
        c.fill.fore_color.rgb = ACC_FILL
    y += stretch_table(shape, room14) + 0.1
    y = key(s, y, key14)
    src(s, "Source: Milestone 5 report, Sections 7.1, 8 and 8.1, Table 8.1, and Appendix VIII.")


def s_judging(prs):
    s = kit.base(prs, K["p4"], T("Judging a Contact List"), T(NOTES[15]))
    y = lead(s, T("A list is judged by how many later non-completers it reaches against the most a list of its length "
                  "could reach."))
    lw = 5.6
    nc = {0, 1, 2, 4, 6, 9, 12, 15, 18}             # 9 later non-completers, 4 of them in the list (the first row)
    sz, gx, gy = 0.5, 0.95, 0.6
    lines = [tb("Recall ", "= 4 of 9 non-completers."),
             tb("Normalised recall ", "= 4 of 5, the most a list of 5 can reach."),
             tb("Lift ", "= (4 of 5) ÷ (9 of 20) = 1.8."),
             [(T("Key: orange figure = later non-completer; navy box = on the list. Illustration, not data."), KEY,
               False)]]
    gy0 = y + 0.58
    gy = max(gy, (END - y - 0.06 - rich_h(lines, lw - 0.4) - 0.02 - 0.58 - 0.12) / 4)   # rows spread to the bottom
    yk = gy0 + 4 * gy + 0.02 - (gy - sz) + 0.12
    ph = yk - y + rich_h(lines, lw - 0.4) + 0.06
    rect(s, I(X0), I(y), I(lw), I(ph), fill=SOFT, line=LINE, radius=True)
    text(s, I(X0 + 0.2), I(y + 0.12), I(lw - 0.4), I(0.3), T("Worked example: 20 students, a list of 5"), size=HEAD,
         color=NAVY, bold=True, spacing=1.0)
    x0 = X0 + (lw - 4 * gx - sz) / 2
    for k in range(20):
        r, c = divmod(k, 5)
        icon(s, "user", x0 + c * gx, gy0 + r * gy, sz, color=WARM if k in nc else GREY, bg=SOFT)
    box = rect(s, I(x0 - 0.12), I(gy0 - 0.06), I(4 * gx + sz + 0.24), I(sz + 0.12), line=NAVY, line_w=2.25)
    box.fill.background()
    rich(s, X0 + 0.2, yk, lw - 0.4, lines)
    kit.room("worked example", y + ph, END)
    rx, rw = X0 + lw + 0.35, CWI - lw - 0.35
    defs = [
        tb("Capacity k: ", "3 or 5 contacts per 20 students, that is 15% or 25% of a run; the main operating point is "
                           "5 per 20 at day 27."),
        tb("Recall at capacity: ", "the share of a run's non-completers who are on its list."),
        tb("Normalised recall: ", "recall divided by the most a list of length k can reach. A list of k can hold at "
                                  "most k non-completers; in the training runs that ceiling is 46% to 100% of a run's "
                                  "non-completers."),
        tb("Lift: ", "the share of non-completers on the list divided by the run's base rate (the share of the run "
                     "who do not complete); 1 = chance."),
        tb("Why rank: ", "the rule names 28.8% at day 27, more than a list of 15% or 25% can hold."),
        tb("Why not \"precision of at least 50%\" (Milestone 1): ", "with non-completion near 45%, a random list "
                                                                     "already reaches about 45% precision.")]
    pt15 = next((pt for pt in (PT["lead"], PT["body"]) if rich_h(defs, rw, pt) <= END - y), BODY)
    rich(s, rx, y, rw, defs, pt=pt15)
    src(s, "Source: Milestone 5 report, Sections 8 and 9, and Appendix III, Table A.8.")


def s_gate(prs):
    s = kit.base(prs, K["p4"], T("Validation and Gate S1"), T(NOTES[16]))
    y = lead(s, T("The model is built on 2013 and scored once on all 13 runs of 2014, under a protocol frozen in "
                  "advance."))
    bw = 5.4
    a = [T("Leave-one-run-out folds on the 9 runs of 2013: each run is held out in turn."),
         T("A challenger replaces the primary model only with a gain of at least 0.03 in pooled normalised recall, "
           "and in 7 of 9 folds.")]
    b = [T("The frozen model is scored once on the 13 runs of 2014."),
         T("Paired runs: the 9 test runs whose module and start month also ran in 2013; the other 4 are unpaired. "
           "Both groups are also reported apart.")]
    h = max(card_h(T("2013: build and choose"), a, bw), card_h(T("2014: score once"), b, bw))
    ws = [5.9, 3.0, CWI - 9.3]
    xs = [X0, X0 + 5.9 + 0.2, X0 + 9.1 + 0.2]
    items = [(T("Gate S1: the success test the model must pass to replace the rule"),
              [tb("Recall: ", "its pooled normalised recall must exceed the early-sign rule list's."),
               tb("Paired bootstrap interval: ", "model and rule compared on the same runs, resampled; it must lie "
                                                 "above 0."),
               tb("Sign-flip test: ", "how often per-run gains this favourable would appear by chance; p must be "
                                      "below 0.05.")]),
             (T("Calibration"), [T("Probabilities are shown only if predicted risks match observed rates: intercept "
                                   "between −0.2 and 0.2, slope between 0.8 and 1.2.")]),
             (T("AQ2 criterion"), [T("A risk difference of at least 5 points, an interval excluding 0, and the same "
                                     "direction in at least two-thirds of modules; p-values take no part.")])]
    key16 = T("Key: lock = protocol frozen before any 2014 outcome is used. Frozen protocol: evaluation choices "
              "fixed in advance, so the test runs are scored once.")
    pt16 = PT["body"] if max(card_h(a_, b_, w, pt=PT["body"]) for (a_, b_), w in zip(items, ws)) + h + 0.5 + \
        lh(key16, CWI, PT["small"]) <= END - y else BODY
    hh = max(card_h(a_, b_, w, pt=pt16) for (a_, b_), w in zip(items, ws))
    free16 = END - y - h - 0.1 - lh(key16, CWI, PT["small"]) - 0.15 - hh
    kit.room("gate cards", 0, free16)
    h += free16 / 2                                  # the free height is shared by the two rows
    card(s, X0, y, bw, T("2013: build and choose"), a, h=h)
    card(s, XR - bw, y, bw, T("2014: score once"), b, color=AGENT_INK, h=h, fill=ACC_FILL, line=WARM, line_w=2.0)
    mx = (X0 + bw + XR - bw) / 2
    arrow(s, X0 + bw + 0.08, y + h / 2, XR - bw - 0.08, y + h / 2)
    circ = s.shapes.add_shape(9, I(mx - 0.42), I(y + h / 2 - 0.42), I(0.84), I(0.84))
    circ.fill.solid()
    circ.fill.fore_color.rgb = NAVY
    circ.line.fill.background()
    icon(s, "lock", mx - 0.25, y + h / 2 - 0.25, 0.5, color=WHITE, bg=NAVY)
    y += h + 0.1
    y = key(s, y, key16) + 0.15
    for x, w, (a_, b_) in zip(xs, ws, items):
        card(s, x, y, w, a_, b_, h=END - y, pt=pt16)
    src(s, "Source: Milestone 5 report, Sections 9 and 9.1, Table 9.1, and Appendix IX.")


def s_fairness(prs):
    s = kit.base(prs, K["p4"], T("Fairness and Interpretability"), T(NOTES[17]))
    y = lead(s, T("The list is audited for equal recall across groups, and every name carries the reasons of the "
                  "ranking that listed it."))
    lw = 6.3
    fair = [
        T("Group attributes stay out of the predictors and are kept only for the audit, because bias cannot be "
          "audited without group membership."),
        tb("Criterion: ", "equal recall at capacity."),
        tb("Rule FR1 (fairness review rule): ", "flag a group for human review when its recall is more than 10 points "
                                                "below the other students' and the Holm-adjusted (corrected for "
                                                "several tests) one-sided interval of the gap lies below 0."),
        tb("No flag ", "means no evidence of a gap at that precision, not proof that the list is fair."),
        tb("Reasons ", "come from what ranks the student: the rule's signs today, the model only if it passes gate S1; "
                       "no coefficient is read as a cause.")]
    pt17 = next((pt for pt in (PT["lead"], PT["body"]) if rich_h(fair, lw, pt) <= END - y), BODY)
    rich(s, X0, y, lw, fair, pt=pt17)
    rx, rw = X0 + lw + 0.4, CWI - lw - 0.4
    text(s, I(rx), I(y), I(rw), I(0.6), T("Confirmatory groups in the 2014 test at day 27 (enrolments)"), size=HEAD,
         color=NAVY, bold=True, spacing=1.0)
    xs, cw = cols(3, 0.2, rx, rw)
    for x, (v, lab) in zip(xs, [("1,488", T("declared disability")), ("1,486", T("most deprived band (0–10%)")),
                                ("610", T("missing deprivation band"))]):
        rect(s, I(x), I(y + 0.68), I(cw), I(1.4), fill=SOFT, line=LINE, radius=True)
        v = v.replace(",", ".") if kit.LANG == "vi" else v     # Vietnamese thousands separator
        text(s, I(x), I(y + 0.76), I(cw), I(0.5), v, size=PT["cover"] - 4, color=NAVY, bold=True,
             align=PP_ALIGN.CENTER, spacing=1.0)
        rich(s, x + 0.1, y + 1.3, cw - 0.2, [lab], align=PP_ALIGN.CENTER)
    yk = key(s, y + 2.16, T("Confirmatory groups: fixed in advance for the audit, each with at least 400 test "
                           "enrolments. Deprivation band: band of the Index of Multiple Deprivation of the student's "
                           "home area."), rx, rw)
    key17 = T("Key: the bar is the largest recall gap, in percentage points, allowed before human review. No recall "
              "values exist yet.")
    by_low = END - lh(key17, rw, PT["small"]) - 1.2
    by = max(yk + 0.15, yk + 0.15 + (by_low - yk - 0.15) / 2)      # the threshold block in the middle of the free space
    text(s, I(rx), I(by), I(rw), I(0.3), T("FR1 threshold"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    scale = (rw - 0.4) / 30                         # inches per recall point
    bx = rx + 0.2
    rect(s, I(bx), I(by + 0.42), I(10 * scale), I(0.3), fill=WARM)
    rect(s, I(bx), I(by + 0.85), I(30 * scale), I(0.02), fill=GREY)
    for p in (0, 10, 20, 30):
        rect(s, I(bx + p * scale - 0.01), I(by + 0.8), I(0.02), I(0.1), fill=GREY)
        text(s, I(bx + p * scale - 0.5), I(by + 0.92), I(1.0), I(0.25), str(p), size=PT["small"], color=KEY,
             align=PP_ALIGN.CENTER, spacing=1.0)
    text(s, I(bx + 10 * scale + 0.15), I(by + 0.42), I(rw - 10 * scale - 0.4), I(0.3),
         T("10 points"), size=PT["small"] + 2, color=AGENT_INK, bold=True, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    yk2 = key(s, by + 1.2, key17, rx, rw)
    kit.room("fairness column", yk2, END)
    src(s, "Source: Milestone 5 report, Sections 6.2 and 9.2, and Appendices VI and IX.")


# ----------------------------------------------------------------------------- Part 5: evidence
def s_status(prs):
    s = kit.base(prs, K["p5"], T("What We Ran"), T(NOTES[18]))
    y = lead(s, T("We answered AQ1 and AQ2 on both years; AQ3 and AQ4 remain complete designs with no model "
                  "trained."))
    xs, cw = cols(4)
    for x, (q, st, done) in zip(xs, [("AQ1", T("Answered"), True), ("AQ2", T("Answered"), True),
                                     ("AQ3", T("Deferred"), False), ("AQ4", T("Deferred"), False)]):
        rect(s, I(x), I(y), I(cw), I(1.4), fill=WARM if done else WHITE, line=WARM if done else GREY, radius=True,
             line_w=2.0)
        text(s, I(x), I(y + 0.2), I(cw), I(0.5), q, size=PT["title"] + 6, color=WHITE if done else GREY, bold=True,
             align=PP_ALIGN.CENTER, spacing=1.0)
        text(s, I(x), I(y + 0.82), I(cw), I(0.35), st, size=PT["head"], color=WHITE if done else GREY, bold=True,
             align=PP_ALIGN.CENTER, spacing=1.0)
    y += 1.5
    y = key(s, y, T("Key: filled orange = Answered, the results answer all of the question; grey outline = Deferred, "
                    "the design is complete and no result exists yet. No question is dropped.")) + 0.2
    why = [[(T("Why AQ3 and AQ4 are deferred: "), AGENT_INK, True),
            (T("Level 1, the compulsory level of the course brief (method and evaluation design), is complete. Level 2, "
               "the optional experiment, was not run, because the 2014 runs are the only independent test and are kept "
               "for one complete run of the frozen protocol."), INK, False)]]
    y = card(s, X0, y, CWI, None, why, fill=ACC_FILL, line=WARM, pt=PT["body"], line_w=1.5) + 0.3
    xs, cw = cols(2)
    items = [(T("AQ1 and AQ2"), [T("Run as fixed in Milestone 4, on the 9 runs of 2013 and again on the 13 runs of "
                                   "2014. No predictive model is trained, and nothing in the AQ3 design changed.")]),
             (T("AQ3 and AQ4"), [T("Designed in full. No model is trained, so no model metric exists; the 13 runs of "
                                   "2014 are kept as the one independent test.")])]
    h = max(card_h(a, b, cw, pt=PT["body"]) for a, b in items)
    kit.room("status cards", y + h, END)
    for x, (a, b) in zip(xs, items):
        card(s, x, y, cw, a, b, h=END - y, pt=PT["body"])
    src(s, "Source: Milestone 5 report, Sections 3, 10 and 11, Table 3.1.")


# AQ1 non-completion per module, students registered at day 14 (Section 11.2; Appendix XII, Figure A.2, Table A.30): rate and
# 95% Wilson interval in %.
AQ1_2013 = {"AAA": (24.9, 20.7, 29.5), "BBB": (45.8, 44.2, 47.5), "DDD": (53.5, 51.7, 55.3), "EEE": (34.8, 31.8, 37.9),
            "FFF": (46.7, 45.0, 48.3), "GGG": (36.1, 33.0, 39.2)}
AQ1_2014 = {"AAA": (27.7, 23.3, 32.6), "BBB": (39.4, 37.6, 41.1), "CCC": (54.3, 52.7, 55.9), "DDD": (49.8, 47.8, 51.7),
            "EEE": (36.5, 34.2, 38.9), "FFF": (44.6, 42.9, 46.3), "GGG": (39.4, 37.0, 41.9)}
POOLED = 45.3


def aq1_modules(fig):
    ax = charts.axes(fig)
    mods = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
    w = 0.38
    ax.set_xlim(-0.6, len(mods) - 0.4)
    ax.set_ylim(0, 66)
    for j, (data, col) in enumerate([(AQ1_2013, C_GREY), (AQ1_2014, C_ACC)]):
        for i, m in enumerate(mods):
            if m not in data:
                continue
            v, lo, hi = data[m]
            x = i + (j - 0.5) * (w + 0.03)
            ax.bar(x, v, w, color=col, zorder=3)
            ax.errorbar(x, v, yerr=[[v - lo], [hi - v]], fmt="none", ecolor=C_INK, elinewidth=1.0, capsize=2.5,
                        zorder=4)
            ax.annotate(charts.num(v, 1), (x, hi), xytext=(0, 2), textcoords="offset points", ha="center",
                        va="bottom", fontsize=charts.size("value"), color=C_INK)
    ax.axhline(POOLED, color=C_MUTED, lw=1.2, ls=(0, (4, 3)), zorder=2)
    ax.set_xticks(range(len(mods)), mods)
    ax.set_yticks([0, 20, 40, 60])
    charts.ticks(ax.yaxis, pct=True)
    ax.grid(axis="y", color=f"#{kit.C_GRID}", lw=0.6)
    ax.set_axisbelow(True)
    handles = [Patch(fc=C_GREY, label="2013"), Patch(fc=C_ACC, label="2014"),
               Line2D([], [], color=C_INK, lw=1.0, label=T("95% Wilson interval")),
               Line2D([], [], color=C_MUTED, lw=1.2, ls=(0, (3, 2)), label=T("Pooled rate, 45.3%"))]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0, 1.02), ncol=4, frameon=False, handlelength=1.4,
              columnspacing=1.0, borderaxespad=0, fontsize=charts.size("small"))
    ax.set_ylabel(T("Non-completion (%)"), fontsize=charts.size("small"), color=C_MUTED)


def s_aq1_size(prs):
    s = kit.base(prs, K["p5"], T("AQ1: How Many Do Not Complete"), T(NOTES[19]))
    y = lead(s, T("Close to half of the students still registered at day 14 do not complete, and the two years "
                  "agree."))
    lw, rw, rx = kit.split(0.6)
    text(s, I(X0), I(y), I(lw), I(0.3), T("Non-completion per module, students registered at day 14"), size=HEAD,
         color=NAVY, bold=True, spacing=1.0)
    ky = bottom_key(s, T("CCC ran only in 2014. Bar = rate in %; whisker = 95% Wilson interval (the 95% interval of a "
                         "rate)."), X0, lw)
    chart(s, "m5-30-aq1-modules", X0, y + 0.35, lw, ky - y - 0.45, aq1_modules)
    rect(s, I(rx), I(y), I(rw), I(1.72), fill=SOFT, line=LINE, radius=True)
    bignum(s, rx, y + 0.08, rw, T("45.3%"), T("(44.7–45.8) of 28,061 enrolments did not complete: 12,700."), color=WARM)
    facts = [
        tb("2013: ", "45.7% (44.8–46.6) of 12,076."),
        tb("2014: ", "44.9% (44.2–45.7) of 15,985."),
        T("About a quarter failed and a fifth withdrew."),
        tb("Modules, both years pooled: ", "26.3% (AAA) to 54.3% (CCC, 2014 only)."),
        tb("February above October: ", "51.6% against 42.4% in 2013, 49.6% against 41.6% in 2014."),
        tb("Check: ", "prepared views and raw tables agree in all 176 outcome cells.")]
    rich(s, rx, y + 1.9, rw, facts, pt=fit_pt(facts, rw, END - y - 1.9))
    src(s, "Source: Milestone 5 report, Section 11.2 and Appendix XII, Figure A.2 and Tables A.30 and A.32.")


YEAR_DIFF = [("All enrolments, all runs", 2.3, 1.2, 3.4, False),
             ("All enrolments, six modules\nrun in both years", -0.2, -1.4, 0.9, False),
             ("Registered at day 14, all\nruns (the KPI rule)", -0.7, -1.9, 0.5, True),
             ("Registered at day 14, six\nmodules run in both years", -3.5, -4.8, -2.3, True)]


def year_diff(fig):
    ax = charts.axes(fig)
    n = len(YEAR_DIFF)
    ax.set_ylim(n - 0.5, -0.6)
    ax.set_xlim(-6.5, 5.5)
    ax.axvline(0, color=C_MUTED, lw=1.2, zorder=1)
    for i, (lab, v, lo, hi, acc) in enumerate(YEAR_DIFF):
        col = C_ACC if acc else C_GREY
        ax.plot([lo, hi], [i, i], color=col, lw=2.2, solid_capstyle="butt", zorder=2)
        for e in (lo, hi):
            ax.plot([e, e], [i - 0.09, i + 0.09], color=col, lw=2.2, zorder=2)
        ax.plot(v, i, "o", ms=11, color=col, mec="white", mew=1.4, zorder=3)
        ax.annotate(f"{fmt(v, 1, sign=True)} ({fmt(lo)} {T('to')} {fmt(hi)})", (v, i), xytext=(0, 10),
                    textcoords="offset points", ha="center", va="bottom", fontsize=charts.size("value"),
                    color=C_INK, fontweight="bold" if acc else "normal",
                    bbox=dict(fc="white", ec="none", pad=1.5))
    ax.set_yticks(range(n), [T(r[0]) for r in YEAR_DIFF])
    ax.set_xticks([-6, -4, -2, 0, 2, 4])
    ax.xaxis.set_major_formatter(charts.matplotlib.ticker.FuncFormatter(lambda v, _: fmt(v, 0, sign=v != 0)))
    ax.set_xlabel(T("2014 minus 2013, percentage points (left of 0: 2014 lower)"), fontsize=charts.size("small"),
                  color=C_MUTED)


def s_aq1_denominator(prs):
    s = kit.base(prs, K["p5"], T("AQ1: The Denominator Matters"), T(NOTES[20]))
    y = lead(s, T("Who counts as enrolled can move a run's rate by 13.6 points and reverse the year comparison, so the "
                  "KPI must fix the add-drop rule."))
    lw, rw, rx = kit.split(0.6)
    text(s, I(X0), I(y), I(lw), I(0.3), T("Change in non-completion from 2013 to 2014"), size=HEAD,
         color=NAVY, bold=True, spacing=1.0)
    ky = bottom_key(s, T("Key: dot = 2014 minus 2013 in points; whisker = 95% interval, and one that crosses 0 shows no "
                         "clear difference. Grey = over all enrolments; orange = registered at day 14 (the KPI rule). "
                         "Each is shown for all runs and for the six modules run in both years."), X0, lw)
    chart(s, "m5-30-year-diff", X0, y + 0.35, lw, ky - y - 0.45, year_diff)
    side = [(T("Runs differ"), T("Run rates span 24.9% (AAA 2013J) to 58.3% (CCC 2014B)."), NAVY),
            (T("The denominator moves rates"), T("BBB 2014J: 49.7% over all enrolments, 36.2% among those registered "
                                                  "at day 14."), NAVY),
            (T("Why the years flip"), T("16.2% of 2014 enrolments against 10.7% of 2013 were not registered at "
                                        "day 14."), WARM)]
    kit.side_cards(s, rx, y, rw, side, bottom=END, gap=0.2)
    src(s, "Source: Milestone 5 report, Section 11.2 and Appendix XII, Table A.32.")


MISSED = {"any": [78.1, 72.7], "week4": [19.6, 14.7]}


def missed_bars(fig):
    ax = charts.axes(fig)
    charts.bars(ax, ["2013", "2014"], {T("Missed a task during the run"): MISSED["any"],
                                       T("Missed a task by week 4 (day 27)"): MISSED["week4"]},
                horizontal=True, pct=True, digits=1, limit=100, colors=[C_GREY, C_ACC])


def s_aq1_missed(prs):
    s = kit.base(prs, K["p5"], T("AQ1: When Non-completers First Miss a Task"), T(NOTES[21]))
    y = lead(s, T("Most non-completers miss a task at some point, but under one in five has missed one by week 4."))
    lw, rw, rx = kit.split(0.5)
    text(s, I(X0), I(y), I(lw), I(0.6), T("Share of non-completers who missed a task (TMA or CMA), %"), size=HEAD,
         color=NAVY, bold=True, spacing=1.0)
    ky = bottom_key(s, T("Population: non-completers registered at day 14, 5,515 in 2013 and 7,185 in 2014. Bar length "
                      "= share of them, on a scale from 0 to 100%. Completers: about one in five missed a task during "
                      "the run."), X0, lw)
    chart(s, "m5-30-missed", X0, y + 0.65, lw, ky - y - 0.75, missed_bars)
    side = [(T("What staff expected"), T("The first sign is usually a missed quiz or assignment (simulated "
                                         "interviews)."), NAVY),
            (T("So"), T("A rule on tasks alone comes too late for most non-completers, which is why the early-sign "
                        "rule counts inactivity."), WARM),
            (T("Confidence"), T("High for OULAD 2013–2014: the first missed week agrees for all 32,593 enrolments in "
                                "two independent computations. Validity for the university's courses remains "
                                "open."), NAVY)]
    kit.side_cards(s, rx, y, rw, side, bottom=END, gap=0.2)
    src(s, "Source: Milestone 5 report, Section 11.2, Appendix I and Appendix XII, Table A.31.")


# AQ2 mutually adjusted risk differences at day 27, percentage points, 95% intervals (Section 11.3; Appendix XIII, Figure A.3;
# Table A.33): (label, 2013 estimate, low, high, 2014 estimate, low, high), sorted by the 2013 estimate.
AQ2 = [("Missed task", 40.8308, 37.7305, 43.9311, 39.2638, 36.4493, 42.0783),
       ("Late TMA", 20.1978, 15.8725, 24.5231, 20.2543, 15.6397, 24.8689),
       ("No click in the last 7 days", 14.4602, 11.3025, 17.6178, 15.8245, 13.2999, 18.3491),
       ("Activity below the run median", 13.3567, 11.4819, 15.2316, 14.5996, 12.9798, 16.2194),
       ("No click before the start", 10.5623, 7.8395, 13.2852, 8.6542, 6.4378, 10.8706)]


def aq2_dots(fig):
    ax = charts.axes(fig)
    n = len(AQ2)
    ax.set_ylim(n - 0.5, -0.6)
    ax.set_xlim(0, 52)
    ax.axvline(5, color=C_MUTED, lw=1.2, ls=(0, (4, 3)), zorder=1)
    for i, row in enumerate(AQ2):
        for j, (v, lo, hi), col in [(0, row[1:4], C_GREY), (1, row[4:7], C_ACC)]:
            yy = i + (j - 0.5) * 0.38
            ax.plot([lo, hi], [yy, yy], color=col, lw=2.0, zorder=2)
            ax.plot(v, yy, "o", ms=8.5, color=col, mec="white", mew=1.2, zorder=3)
            ax.annotate(charts.num(v, 1), (hi, yy), xytext=(5, 0), textcoords="offset points", ha="left",
                        va="center", fontsize=charts.size("value"), color=C_INK)
    ax.set_yticks(range(n), [T(r[0]) for r in AQ2])
    ax.set_xticks([0, 10, 20, 30, 40, 50])
    charts.ticks(ax.xaxis)
    ax.grid(axis="x", color=f"#{kit.C_GRID}", lw=0.6)
    ax.set_axisbelow(True)
    ax.set_xlabel(T("Risk difference, percentage points"), fontsize=charts.size("small"), color=C_MUTED)
    handles = [Line2D([], [], color=C_GREY, marker="o", lw=2.0, label="2013"),
               Line2D([], [], color=C_ACC, marker="o", lw=2.0, label="2014"),
               Line2D([], [], color=C_MUTED, lw=1.2, ls=(0, (3, 2)), label=T("5-point criterion"))]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0, 1.02), ncol=3, frameon=False, handlelength=1.6,
              columnspacing=1.2, borderaxespad=0, fontsize=charts.size("small"))


def s_aq2_signs(prs):
    s = kit.base(prs, K["p5"], T("AQ2: Five Early Signs"), T(NOTES[22]))
    y = lead(s, T("All five early signs, inactivity included, go with later non-completion within module run, by "
                  "similar amounts in 2013 and 2014."))
    lw, rw, rx = kit.split(0.5 if kit.LANG == "en" else 0.57)   # the Vietnamese row labels need the wider chart
    head22 = T("Extra later non-completion with each sign at day 27")
    hh22 = lh(head22, lw, HEAD, True)
    text(s, I(X0), I(y), I(lw), I(hh22), head22, size=HEAD,
         color=NAVY, bold=True, spacing=1.0)
    ky = bottom_key(s, T("Key: dot = risk difference; whisker = 95% interval; dashed line = the 5-point criterion. Task "
                         "signs on runs with a task due by day 27; click signs on all runs."), X0, lw)
    chart(s, "m5-30-aq2-signs", X0, y + hh22 + 0.05, lw, ky - y - hh22 - 0.15, aq2_dots)
    paras = [
        tb("The five signs: ", "the rule's three parts (Missed task, Late TMA, No click in the last 7 days, that is "
                               "days 21–27) and two activity signs tested only here: Activity below the run median "
                               "(clicks on days 0–27) and No click before the start (day 0)."),
        tb("Risk difference: ", "the extra percentage points of later non-completion among enrolments with the sign "
                                "against those without, within module run, adjusted for the other signs."),
        tb("Population: ", "registered at day 27; 11,811 enrolments in 2013 (44.4% non-completion) and 15,724 in "
                           "2014 (44.0%); task signs on 9,960 and 12,585."),
        tb("Criterion: ", "at least 5 points, an interval excluding 0, and the same direction in two-thirds of "
                          "modules."),
        [(T("These are associations, not causes."), AGENT_INK, True)]]
    kit.room("aq2 text", y + rich_h(paras, rw), END)
    rich(s, rx, y, rw, paras, pt=fit_pt(paras, rw, END - y))
    src(s, "Source: Milestone 5 report, Sections 9 and 11.3, Table 9.1 and Appendices VIII and XIII, "
           "Figure A.3 and Table A.33.")


def s_aq2_robust(prs):
    s = kit.base(prs, K["p5"], T("AQ2: How Far the Signs Hold"), T(NOTES[23]))
    y = lead(s, T("The signs keep their direction across modules and checks, but the click signs are coarse, and every "
                  "result is an association, not a cause."))
    lw = 5.0
    msg = [[(T("Confidence: moderate. "), WHITE, True),
            (T("Two years agree, but the yes-or-no click signs miss part of a graded activity gradient (a known "
               "misfit), and unrecorded reasons could explain the associations."), WHITE, False)]]
    mh = rich_h(msg, CWI - 0.6) + 0.18
    yb = END - mh                                    # the confidence bar on the bottom edge
    note23 = [tb("2014: ", "14.6 → 5.9 points under the same check; the sign then keeps its direction in only 4 of 7 "
                           "modules and no longer meets the criterion. The other four signs still meet it.")]
    pt_n = fit_pt(note23, lw, 1.3)
    ny = yb - 0.3 - rich_h(note23, lw, pt_n)
    num_lab = T("points for Activity below the run median (2013) once clicks enter as a continuous adjustment, the "
                "check that shrinks the click signs.")
    bh23 = ny - 0.15 - y
    nh23 = kit.num_h(PT["number"]) + 0.05 + lh(num_lab, lw - 0.3)
    kit.room("robust number", nh23 + 0.2, bh23)
    rect(s, I(X0), I(y), I(lw), I(bh23), fill=SOFT, line=LINE, radius=True)
    bignum(s, X0, y + (bh23 - nh23) / 2, lw, T("13.4 → 5.8"), num_lab, color=WARM)
    rich(s, X0, ny, lw, note23, pt=pt_n)
    rx, rw = X0 + lw + 0.4, CWI - lw - 0.4
    checks = [("check", PLUS, OUT_FILL, T("Years agree: "), T("no sign moves by more than two points between the "
                                                              "years.")),
              ("check", PLUS, OUT_FILL, T("Sensitivity runs agree: "),
               T("each sign keeps its direction under six sensitivity runs (repeats of an estimate under a changed "
                 "choice), in both years.")),
              ("warning", GOLD, pal_rgb(pal.tint(pal.GOLD)), T("Modules agree, with one exception: "),
               T("each sign keeps its direction in every module except a late TMA in AAA 2014 (−1.2 points on 348 "
                 "enrolments, interval −14.4 to 12.1, which includes 0); no CCC student had a late TMA by day 27."))]
    key23 = T("Key: tick = check passed; amber mark = passed with one exception.")
    col = yb - 0.3 - lh(key23, rw, PT["small"]) - 0.1 - y          # height of the check list
    paras23 = [[[(head, c if c != GOLD else AGENT_INK, True), (body, INK, False)]] for _, c, _, head, body in checks]
    pt23 = next((pt for pt in (PT["body"], BODY) if sum(max(rich_h(q, rw - 0.65, pt), 0.4) for q in paras23)
                 + 0.15 * 2 <= col), BODY)
    hs23 = [max(rich_h(q, rw - 0.65, pt23), 0.4) for q in paras23]
    gap23 = max(0.15, (col - sum(hs23)) / (len(checks) - 1))
    cy = y
    for (ic, c, fill, head, body), para, h in zip(checks, paras23, hs23):
        rect(s, I(rx), I(cy), I(0.4), I(0.4), fill=fill, line=c, radius=True)
        icon(s, ic, rx + 0.06, cy + 0.06, 0.28, color=c, bg=fill)
        rich(s, rx + 0.6, cy + 0.03, rw - 0.65, para, pt=pt23)
        cy += h + gap23
    cy -= gap23
    key(s, cy + 0.1, key23, rx, rw)
    kit.room("robust checks", cy + 0.25, yb)
    rect(s, MX, I(yb), CW, I(mh), fill=NAVY, radius=True)
    rich(s, X0 + 0.3, yb + 0.1, CWI - 0.6, msg, color=WHITE)
    src(s, "Source: Milestone 5 report, Sections 9 and 11.3, Table 9.1, and Appendix XIII, Tables A.34 to A.36.")


# ----------------------------------------------------------------------------- Part 6: integration and use
def s_matrix(prs):
    s = kit.base(prs, K["p6"], T("Traceability Matrix"), T(NOTES[24]))
    y = lead(s, T("For AQ1 and AQ2 every link from goal to decision holds evidence; for AQ3 and AQ4 the chain stops at "
                  "the evaluation design."))
    rows = [[T("Question"), T("Goal and KPI"), T("Data"), T("Preparation"), T("Method"), T("Evaluation"),
             T("Decision"), T("Status")],
            ["AQ1", T("Primary KPI"), T("22 runs; day 14: 28,061"), T("Day-14 rule"), T("Grouped rates"),
             T("Two computations agree; 45.3%"), "D2, D3", T("Answered")],
            ["AQ2", T("Primary KPI; KPI 1 (sign part)"), T("Day 27: 11,811 and 15,724"), T("Dated by day 27"),
             T("Logistic, run effects"), T("5 of 5 signs, both years"), "D2, D1", T("Answered")],
            ["AQ3", T("Early-sign rule (the baseline)"), T("19 predictors; 2014 test"), T("Refit per fold"),
             T("Penalised logistic"), T("S1 planned; N.A."), "D1", T("Deferred")],
            ["AQ4", T("KPIs 1–2, contact parts: GAP"), T("Contacts: GAP"), T("3 or 5 per 20"), T("Top-k with signs"),
             T("S1, FR1; N.A."), "D1", T("Deferred")]]
    fr = [0.08, 0.16, 0.15, 0.12, 0.13, 0.15, 0.09]
    widths = [int(CW * f) for f in fr]
    widths.append(CW - sum(widths))
    shape = table(s, MX, I(y), CW, rows, widths, size=BODY)
    tbl = shape.table
    designed = pal_rgb(pal.tint(pal.BLUE))
    for i in range(1, len(rows)):
        for j in range(1, 7):
            c = tbl.cell(i, j)
            c.fill.solid()
            empty = "GAP" in rows[i][j] or "N.A." in rows[i][j]
            if empty:
                c.fill.fore_color.rgb = WHITE
                for r in c.text_frame.paragraphs[0].runs:
                    r.font.bold, r.font.color.rgb = True, MINUS
            else:
                c.fill.fore_color.rgb = designed if (i >= 3 and j >= 3) else pal_rgb("#E6E8EC")
        c = tbl.cell(i, 7)
        c.fill.solid()
        c.fill.fore_color.rgb = WARM if i < 3 else ACC_FILL
        for r in c.text_frame.paragraphs[0].runs:
            r.font.bold, r.font.color.rgb = True, WHITE if i < 3 else AGENT_INK
    k24a = T("Key: grey = the link holds evidence (data, rule or result); blue = designed, not run; red on white "
             "= GAP (a link without evidence) or N.A. (no result exists); orange column = status.")
    k24b = T("GAP marks only what OULAD lacks: delivery mode, year of study, attendance and contacts. "
             "KPI 1's sign part (the rule's flags) is computed on OULAD; its contact part needs the "
             "pilot. Decisions: D1 whom to contact, D2 where to place support time, D3 whether to "
             "extend. S1: the gate a model must pass to replace the rule; FR1: the fairness review "
             "rule.")
    y += stretch_table(shape, END - 0.1 - lh(k24a, CWI, PT["small"]) - 0.06 - lh(k24b, CWI, PT["small"]) - y) + 0.1
    y = key(s, y, k24a) + 0.06
    key(s, y, k24b)
    src(s, "Source: Milestone 5 report, Sections 2.1 and 11.1, Tables 2.1, 11.1 and 11.2.")


def s_expected(prs):
    s = kit.base(prs, K["p6"], T("AQ3 and AQ4: Expected Outputs"), T(NOTES[25]))
    y = lead(s, T("AQ3 and AQ4 would give a ranked, capacity-limited list with reasons, and the simple rule stays if "
                  "the model does not beat it."))
    lw = 5.3
    key25 = T("Key: tag = the sign behind the name. The card shows the form of the output only: no names and no numbers.")
    ch = END - 0.08 - lh(key25, lw, PT["small"]) - y          # the output card fills the left column
    kit.room("expected card", 3.85, ch)
    step25 = (ch - 0.65 - 0.45 - 0.2) / 4
    dashed(rect(s, I(X0), I(y), I(lw), I(ch), fill=WHITE, line=GREY, radius=True, line_w=1.5))
    text(s, I(X0 + 0.2), I(y + 0.15), I(lw - 0.4), I(0.3), T("Expected output – not a result"), size=HEAD,
         color=GREY, bold=True, spacing=1.0)
    tags = [[T("Missed task")], [T("No click in the last 7 days")], [T("Late TMA"), T("Missed task")],
            [T("Missed task"), T("Late TMA")], [T("No click in the last 7 days")]]
    ry = y + 0.65
    for row in tags:
        chip(s, X0 + 0.2, ry, 0.45, 0.45, "", fill=SOFT, line_color=LINE)
        rect(s, I(X0 + 0.8), I(ry + 0.14), I(0.9), I(0.17), fill=LINE, radius=True)
        tx = X0 + 1.85
        for t in row:
            tw = 0.3 + text_w(t, PT["small"])
            chip(s, tx, ry + 0.04, tw, 0.37, t, fill=ACC_FILL, line_color=WARM, color=AGENT_INK)
            tx += tw + 0.1
        ry += step25
    key(s, y + ch + 0.08, key25, X0, lw)
    rx, rw = X0 + lw + 0.4, CWI - lw - 0.4
    out25 = [
        tb("AQ3 would give: ", "a risk rank per enrolment at days 13 and 27, and a probability only if calibration "
                               "holds; gate S1 answers it on the 13 runs of 2014."),
        tb("If the model does not beat the rule: ", "the rule's order stays, and its list is measured as a "
                                                     "baseline."),
        tb("AQ4 would give: ", "a list of 3 or 5 per 20 students per run, with the signs behind each name. It is "
                               "answered when it meets S1 (the gate to replace the rule), rule FR1 "
                              "(the fairness review) passes or its flags are reviewed, and the "
                               "assumption that the order of risk matches the order of need is stated as untested."),
        tb("Neither says ", "who should make contact or whether contact helps."),
        tb("Status: ", "Deferred; expected outputs, no model metric.")]
    rich(s, rx, y, rw, out25, pt=fit_pt(out25, rw, END - y))
    src(s, "Source: Milestone 5 report, Sections 11.1 and 11.4, and Appendix XIV.")


def s_decisions(prs):
    s = kit.base(prs, K["p6"], T("Decision Support"), T(NOTES[26]))
    y = lead(s, T("The early-sign rule is the candidate list for whom to contact; the patterns are a hypothesis for "
                  "where support goes; the design is a method for whether to extend."))
    items = [(T("D1 – Whom to contact (reversible)"),
              T("The early-sign rule as the candidate list: interpretable, computable from records the university "
                "already holds, and each part goes with later non-completion in 2013 and in 2014. A member of staff "
                "checks every name."),
              T("Ranking within capacity, because the rule names 28.8% at day 27."), True),
             (T("D2 – Where support time goes"),
              T("A hypothesis: support time first where non-completion and early signs are highest."),
              T("A check on the university's records."), False),
             (T("D3 – Whether to extend (close to irreversible)"),
              T("A measurement method, a gate and a fairness audit."),
              T("A pilot result: extension waits for it."), False)]
    xs, cw = cols(3)
    paras = lambda g, n, acc: [[(T("What it gets"), AGENT_INK if acc else NAVY, True)], g,   # noqa: E731
                               [(T("What it still needs"), KEY, True)], n]
    key26 = T("Key: orange = usable now (D1); grey = not usable yet: D2 waits for a check on the university's records, "
              "D3 for a pilot result.")
    opt26 = [tb("Decision option: ", "a statement from observational data offered as a hypothesis for the pilot, not a "
                                     "proven remedy.")]
    oy = END - rich_h(opt26, CWI, PT["body"])        # the decision option on the bottom edge, the key above it
    ky26 = oy - 0.2 - lh(key26, CWI, PT["small"])
    h = ky26 - 0.12 - y
    pt26 = PT["body"] if max(card_h(a, paras(g, n, acc), cw, pt=PT["body"]) for a, g, n, acc in items) <= h else BODY
    kit.room("decision cards", max(card_h(a, paras(g, n, acc), cw, pt=pt26) for a, g, n, acc in items), h)
    for x, (a, g, n, acc) in zip(xs, items):
        card(s, x, y, cw, a, paras(g, n, acc), color=AGENT_INK if acc else NAVY, h=h, pt=pt26,
             fill=ACC_FILL if acc else SOFT, line=WARM if acc else GREY, line_w=2.0 if acc else 1.0)
    key(s, ky26, key26)
    rich(s, X0, oy, CWI, opt26, pt=PT["body"])
    src(s, "Source: Milestone 5 report, Sections 2.1, 8, 11.4 and 11.5, Table 11.3.")


def s_genai(prs):
    s = kit.base(prs, K["p6"], T("Generative AI Use"), T(NOTES[27]))
    y = lead(s, T("AI proposed and challenged, and we verified; it was never a source of data, statistics or "
                  "results."))
    lw, gap = 3.6, 0.9
    items = [(T("Where it helped most"), [T("A critic found tasks due before registration counted as missed, and a "
                                            "leakage check that could not fail, that is, one that would pass even "
                                            "with leakage.")]),
             (T("Decisions that stayed ours"), [T("Keep 2014 out of every AQ3 choice; one early-sign rule; AQ3 and AQ4 "
                                                  "as designs; every association stated as an association.")])]
    xs, cw = cols(2)
    rule27 = [T("AI is never a source of data, statistics, licence information or results; every fact it offered was "
                "checked against a saved source, the data files or code we ran."),
              T("No AI produced a metric value, threshold or result.")]
    rule_h = card_h(T("One rule"), rule27, XR - (X0 + lw + gap + 5.0 + 0.3))
    pt27 = PT["body"] if y + rule_h + 0.3 + max(card_h(a, b, cw, pt=PT["body"]) for a, b in items) <= END else BODY
    h = max(card_h(a, b, cw, pt=pt27) for a, b in items)
    cy27 = END - h                                   # the two lower cards on the bottom edge
    chip_h = 0.55
    step = min(0.85, (cy27 - 0.3 - (y + 0.42) - chip_h) / 3)   # the chips spread over the space above
    kit.room("ai chips", 0.62, step)
    text(s, I(X0), I(y), I(lw), I(0.3), T("AI proposed"), size=HEAD, color=AGENT_INK, bold=True, spacing=1.0)
    roles = [T("Simulated stakeholder"), T("Research and code assistant"), T("Critic"), T("Writing partner")]
    ry = y + 0.42
    for r in roles:
        chip(s, X0, ry, lw, chip_h, r, fill=ACC_FILL, line_color=WARM, color=AGENT_INK, size=BODY, bold=True)
        ry += step
    rx = X0 + lw + gap
    rw = 5.0
    ay = y + 0.42 + 1.5 * step + chip_h / 2
    arrow(s, X0 + lw + 0.1, ay, rx - 0.1, ay)
    text(s, I(rx), I(y), I(rw), I(0.3), T("We verified with"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    checks = [T("Quotes against transcripts"), T("Literature against saved copies"),
              T("Code against fixtures (small inputs with known answers) and independent recounts"),
              T("Critics confined to the brief and the data")]
    ry = y + 0.42
    for c in checks:
        chip(s, rx, ry, rw, chip_h, c, fill=WHITE, line_color=NAVY, size=PT["small"] if len(c) > 50 else BODY)
        ry += step
    fx = rx + rw + 0.3
    rh27 = max(rule_h, ry - step + chip_h - y)
    kit.room("one rule card", y + rh27 + 0.2, cy27)
    card(s, fx, y, XR - fx, T("One rule"), rule27, h=rh27)
    for x, (a, b) in zip(xs, items):
        card(s, x, cy27, cw, a, b, h=h, pt=pt27)
    src(s, "Source: Milestone 5 report, Sections 13, 13.1 and 13.2.")


# ----------------------------------------------------------------------------- Conclusions
def s_conclusions(prs):
    s = kit.base(prs, K["end"], T("Conclusions"), T(NOTES[28]))
    y = lead(s, T("On OULAD, an early list cannot rest on missed tasks alone, and the early signs can serve as reasons "
                  "that staff check beside each name."))
    tiers = [(T("1. High confidence, OULAD 2013–2014"), PLUS, OUT_FILL,
              T("45.3% of the enrolments registered at day 14 did not complete; runs varied from 24.9% to 58.3%; the "
                "year comparison depends on the add-drop rule; most non-completers first missed a task after "
                "week 4.")),
             (T("2. Moderate confidence"), WARM, ACC_FILL,
              T("All five early signs go with later non-completion in both years, a missed task by 40.8 and 39.3 "
                "points, in the same direction across modules, with one wide exception. These are associations.")),
             (T("3. Design only"), GREY, SOFT,
              T("A penalised logistic model judged once against the rule, and a capacity-limited list audited for "
                "fairness; outputs are expected, not measured."))]
    lab_w = 3.3
    nc = [[(T("Not concluded: "), KEY, True),
           (T("that the signs cause non-completion, that a model ranks better than the rule, or that contact raises "
              "completion."), KEY, False)]]
    key28 = T("Key: tiers run from the firmest finding at the top; the label of each tier is its confidence level or "
              "status.")
    low = 0.12 + rich_h(nc, CWI, PT["body"]) + 0.02 + lh(key28, CWI, PT["small"])
    sep = END - low                                  # the separator, "not concluded" and the key on the bottom edge

    def tier_h(pt):
        return [max(rich_h([b], CWI - 2 * k * 0.45 - lab_w - 0.5, pt), lh(h_, lab_w - 0.3, HEAD, True)) + 0.3
                for k, (h_, _, _, b) in enumerate(tiers)]
    pt28 = PT["body"] if sum(tier_h(PT["body"])) + 0.3 + 0.25 <= sep - y else BODY
    bhs = tier_h(pt28)
    kit.room("conclusion tiers", sum(bhs) + 0.3 + 0.25, sep - y)
    gap28 = min(0.35, (sep - 0.25 - y - sum(bhs)) / 2)
    for k, ((head, c, fill, body), bh) in enumerate(zip(tiers, bhs)):
        inset = k * 0.45
        x, w = X0 + inset, CWI - 2 * inset
        rect(s, I(x), I(y), I(w), I(bh), fill=fill, line=c, radius=True, line_w=2.0)
        text(s, I(x + 0.18), I(y + 0.15), I(lab_w - 0.3), I(bh - 0.3), head, size=HEAD, color=c if c != GREY else INK,
             bold=True, spacing=1.0)
        rich(s, x + lab_w, y + 0.15, w - lab_w - 0.2, [body], pt=pt28)
        y += bh + gap28
    rect(s, MX, I(sep), CW, I(0.02), fill=GREY)
    y = rich(s, X0, sep + 0.12, CWI, nc, pt=PT["body"])
    key(s, y + 0.02, key28)
    src(s, "Source: Milestone 5 report, Sections 11.2, 11.3, 11.4 and 14.")


def s_limits(prs):
    s = kit.base(prs, K["end"], T("Limitations, Open Problems and Take-home"), T(NOTES[29]))
    y = lead(s, T("We keep apart what showed no evidence, what has no data to test and what is not yet tested, and "
                  "each open problem has the step that answers it."))
    kinds = [(T("No evidence found"), T("Year difference over all enrolments in the six shared modules: −0.2 points "
                                        "(−1.4 to 0.9); click signs in small modules: intervals include 0."),
              T("No claim; uncertain."), MINUS),
             (T("No data to test"), T("Contact and its outcome; delivery mode, year of study, attendance; capacity."),
              T("Randomised pilot."), kit.BLUE),
             (T("Not yet tested"), T("AQ3 and AQ4 results."), T("Single AQ3 test, design unchanged."), WARM),
             (T("Measurement"), T("Yes-or-no click signs; the KPI proxy and its denominator."), T("Continuous measures; one add-drop rule."), kit.VIOLET),
             (T("Scope and causal"), T("UK distance learning of 2013–2014; an observational design."),
              T("University recount; options as hypotheses."), kit.TEAL)]
    rows = [[T("Kind"), T("Limitation"), T("Response")]] + [[a, b, c] for a, b, c, _ in kinds]
    fr = (0.22, 0.5) if kit.LANG == "vi" else (0.14, 0.54)      # the Vietnamese kind labels need a wider column
    widths = [int(CW * f) for f in fr]
    widths.append(CW - sum(widths))
    flag = [[(T("A flag must not become a label, "), MINUS, True),
             (T("because predictive analysis can carry bias and stereotyping."), INK, False)]]
    steps = [(T("Next step 1: on OULAD"), T("The single AQ3 test under the frozen protocol, then the AQ4 list and "
                                            "its fairness audit."), "white"),
             (T("Next step 2: at the university"), T("Recount the baseline under the add-drop rule, replace assumed "
                                                     "values, and do the risk classification the law requires."),
              "white"),
             (T("Next step 3: randomised pilot"), T("Among flagged students, contacts logged with their outcomes before "
                                                    "any model is retrained."), "agent")]
    xs, sw = cols(3, 0.42)
    sh = max(node_h(a, [b], sw, body_pt=PT["small"]) for a, b, _ in steps) - 0.3
    take29 = T("Take-home: a missed task comes too late; count silence too, and test contact before trusting it.")
    mh = lh(take29, CWI - 0.6, PT["lead"], True) + 0.26     # the take-home bar, sized to its wrapped line
    lower29 = 0.12 + rich_h(flag, CWI) + 0.1 + sh + 0.2 + mh
    size29 = BODY if y + table_h(rows, widths, BODY, 0.3) <= END - lower29 else PT["small"]   # 14 pt where it fits
    shape = table(s, MX, I(y), CW, rows, widths, size=size29, row_h=I(0.3))
    tbl = shape.table
    for i, (_, _, _, c) in enumerate(kinds, 1):
        cell = tbl.cell(i, 0)
        cell.fill.solid()
        cell.fill.fore_color.rgb = c
        for r in cell.text_frame.paragraphs[0].runs:
            r.font.color.rgb = WHITE
    y += stretch_table(shape, END - lower29 - y) + 0.12      # the table rows take the free height
    y = rich(s, X0, y, CWI, flag)
    sy = y + 0.1
    for k, (x, (a, b, st)) in enumerate(zip(xs, steps)):
        node(s, x, sy, sw, sh, a, [b], st, body_pt=PT["small"], head_pt=BODY)
        if k < 2:
            arrow(s, x + sw + 0.04, sy + sh / 2, x + sw + 0.38, sy + sh / 2)
    bottom = END - mh
    kit.room("limitations take-home", sy + sh + 0.05, bottom)
    closing_box(s, bottom, h=mh, line=take29)
    src(s, "Source: Milestone 5 report, Sections 12, 12.1 and 14, Table 12.1, and Appendix XII, Table A.32.")


def s_thanks(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, fill=NAVY)
    text(s, 0, I(1.7), W, I(0.9), T("Thank you. Questions?"), size=PT["cover"], color=WHITE, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    text(s, I(1.0), I(2.75), W - I(2.0), I(0.45), T("Early Identification of Disengaging Students in Online Courses – "
                                                    "team N04"), size=PT["lead"], color=WHITE,
         align=PP_ALIGN.CENTER, spacing=1.0)
    msg = T("Take-home: a missed task comes too late; count silence too, and test contact before trusting it.")
    mh = lh(msg, 10.5, PT["lead"] + 4, True) + 0.4
    rect(s, I(1.3), I(3.65), W - I(2.6), I(mh), fill=pal_rgb(pal.shade(pal.NAVY, 0.25)), radius=True)
    text(s, I(1.6), I(3.65), W - I(3.2), I(mh), msg, size=PT["lead"] + 4, color=WHITE, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    text(s, I(1.0), I(6.3), W - I(2.0), I(0.35), T("Data: Open University Learning Analytics Dataset (Kuzilek, Hlosta "
                                                   "and Zdrahal), CC BY 4.0."), size=PT["small"],
         color=pal_rgb("#C9D3E3"), align=PP_ALIGN.CENTER, spacing=1.0)
    s.notes_slide.notes_text_frame.text = T(NOTES[30])


SLIDES = [s_title, s_noticed, s_answer, s_stakeholders, s_goal, s_questions, s_requirements, s_selection, s_oulad,
          s_quality, s_adddrop, s_rule, s_leakage, s_methods, s_judging, s_gate, s_fairness, s_status, s_aq1_size,
          s_aq1_denominator, s_aq1_missed, s_aq2_signs, s_aq2_robust, s_matrix, s_expected, s_decisions, s_genai,
          s_conclusions, s_limits, s_thanks]


def build(lang):
    kit.build_deck(lang, SLIDES, OUT[lang], FOOTER_EN, cache=CACHE, before=kickers)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", choices=["en", "vi", "all"], default="all")
    args = ap.parse_args()
    for lang in (["en", "vi"] if args.lang == "all" else [args.lang]):
        build(lang)
