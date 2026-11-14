"""'What Changed Along the Way': the turning points of the project, milestone by milestone (15-slide deck, slide 14).

Content from the team comments of the self-assessment (Section 1, Table 1.1) and the Milestone 5 report (Change Log,
Sections 3.2, 7, 10 and 13). Plan number 95: the full deck has no such slide.
"""
from slides_milestone5_full.common import *  # noqa: F401,F403

PATH_ID = 95
TITLE = "What Changed Along the Way"


def s_path(prs, notes_text=""):
    s = kit.base(prs, kicker(91), T(TITLE), notes_text)
    y = lead(s, T("The plan of Milestone 1 did not survive the data; each turning point was recorded, tested and turned "
                  "into a rule the next milestone could rely on."))
    rows = [[T("Milestone"), T("What happened"), T("What we did"), T("Where it stands")],
            ["1", T("No real staff: AI played the five stakeholders"),
             T("51 quotes checked against transcripts; a validation round"),
             T("Confirm with real staff before a pilot")],
            ["2–3", T("Duplicate clicks, missing exam results, documentation unlike the files"),
             T("Nineteen issues logged, each with a decision"),
             T("Duplicates barely matter: the early-click comparison stays the same")],
            ["2–3", T("The Milestone 1 rule could fire in 1 of 22 runs"),
             T("New early-sign rule: missed task, late TMA or 7 silent days"),
             T("Resolved; one rule for analysis and pilot")],
            ["3", T("AI leakage audit found eight errors our checks missed"),
             T("Reproduced, fixed; every check shown to catch an error"),
             T("Resolved; all 22 data checks pass")],
            ["3–5", T("A 50% precision target: a random list reaches about 45%"),
             T("Questions revised; lists judged within capacity"),
             T("AQ1–AQ3 answered; AQ4 in part")],
            ["5", T("No tuning measure in the plan; the 2014 test set grew from the 9 runs with a 2013 twin to all 13, "
               "unrecorded until Milestone 5"),
             T("Log loss chosen and disclosed; both changes in the Change Log"),
             T("Gate S1 met under log loss and under recall")]]
    fr = (0.1, 0.33, 0.31)
    widths = [int(CW * f) for f in fr]
    widths.append(CW - sum(widths))
    kp = T("Key: AQ = analytical question; gate S1 = the threshold a model must pass to replace the early-sign rule; "
           "Change Log = the record of every change with its reason; log loss = how far the predicted risks fall "
           "from the actual outcomes.")
    kh = lh(kp, CWI, PT["small"])
    room = END - kh - 0.1 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    th = stretch_table(shape, room)
    key(s, y + th + 0.1, kp)
    src(s, "Source: self-assessment, Section 1, Table 1.1; Milestone 5 report, Sections 3.2, 7, 10 and 13.")
