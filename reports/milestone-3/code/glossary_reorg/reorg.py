"""Split the course-completion topic glossary into focused topic files and move general rows to common/.
Usage: reorg.py SRC_GLOSSARIES DST_GLOSSARIES  (SRC: the pre-reorganisation copy; row placement in assign.txt by source line)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
SRC = Path(sys.argv[1])
DST = Path(sys.argv[2])
lines = (SRC / "topics/course-completion-early-contact.md").read_text(encoding="utf-8").splitlines()
assign = {}
for l in (HERE / "assign.txt").read_text().splitlines():
    code, nums = l.split(":")
    for n in nums.split():
        assign[int(n)] = code.strip()

def key(n):
    en = lines[n - 1].strip().strip("|").split("|")[0]
    return re.sub(r"[^a-z0-9 ]", "", en.lower().replace("…", "")).strip()

HEAD = "| English | Vietnamese | Usage | Replaces |\n| --- | --- | --- | --- |"

FILES = {
 "course-completion-early-contact": ("Topic glossary: course completion and early contact in online and blended courses",
  "The proposal vocabulary of team N04's MTH045 project on low course completion and mid-semester disengagement in a "
  "university's online and blended courses: the courses and their outcomes, the university's systems and staff, the early "
  "signs and contact process, the goals, KPIs and analytical questions, and the stakeholder interviews behind them. Terms "
  "that the course brief writes in English stay in English. Vietnamese forms follow what a Vietnamese lecturer or "
  "academic-affairs officer would say (guide section 4, rule 8): plain, everyday words of the field, not mirrors of the "
  "English. The project's other topic files hold the OULAD data vocabulary (oulad-data-preparation), the prediction and "
  "evaluation vocabulary (early-warning-evaluation) and the course brief's labels, AI roles and running-text wording "
  "(course-completion-report-conventions); a term is defined in one of these files only.",
  [("A1", "Courses, completion and withdrawal"), ("A2", "The university: programs, systems, records and rules"),
   ("A3", "Stakeholders, staff and offices"), ("A4", "Early signs, contact and follow-up"),
   ("A5", "Goals, KPIs and analytical questions"), ("A6", "Decisions and levels of analytics"),
   ("A7", "Stakeholder interviews and their synthesis"), ("A8", "Law, privacy and how students perceive monitoring")]),
 "oulad-data-preparation": ("Topic glossary: OULAD data collection, understanding and preparation",
  "The data vocabulary of team N04's course-completion project: the search for and selection of an open dataset, the "
  "reproducible collection of the Open University Learning Analytics Dataset (OULAD), its modules, runs, enrolments and "
  "fields, the data-quality findings, and the prepared views, features and checks built from it. OULAD names its units "
  "in Open University terms (module, presentation, tutor-marked assessment); the Vietnamese forms below keep those units "
  "distinct from the university's own courses and terms in course-completion-early-contact.",
  [("B1", "Datasets, search and selection"), ("B2", "Data requirements, collection and provenance"),
   ("B3", "OULAD modules, runs and enrolments"), ("B4", "OULAD fields: background, assessments and activity"),
   ("B5", "Table structure and keys"), ("B6", "Data quality"),
   ("B7", "Preparation, measures and features"), ("B8", "Preparation deliverables and ratings")]),
 "early-warning-evaluation": ("Topic glossary: early-warning prediction, evaluation and fairness",
  "The modelling vocabulary of team N04's course-completion project: the prediction set-up, time-based splits and "
  "leakage controls, the candidate models, the evaluation measures and statistical tests, the capacity-limited contact "
  "list, fairness and governance checks, and the limits on causal claims. General statistical and machine-learning "
  "terms live in the common layer (research-and-evaluation, ai-and-ml); the rows here fix the project's own sense of "
  "a term or its wording around the contact list.",
  [("C1", "Prediction set-up"), ("C2", "Splits, folds and leakage"), ("C3", "Models and approaches"),
   ("C4", "Evaluation measures and statistical tests"), ("C5", "Contact lists, flags and capacity"),
   ("C6", "Fairness, risk and governance"), ("C7", "Causal questions and the limits of observational data"),
   ("C8", "Modelling deliverables and success criteria")]),
 "course-completion-report-conventions": ("Topic glossary: report conventions of the course-completion project",
  "Wording that team N04's MTH045 reports share across milestones: the course brief's own labels and deliverable names "
  "(kept in English where the brief writes them in English), the AI roles in the team's workflow, and fixed phrases of "
  "the running text. Concepts of the analysis itself are in course-completion-early-contact, oulad-data-preparation and "
  "early-warning-evaluation.",
  [("D1", "Course brief labels and deliverable names"), ("D2", "AI roles in the team's workflow"),
   ("D3", "Fixed wording in the running text")]),
}
COMMON = {
 "XRES": ("research-and-evaluation", "Statistics and predictive-model evaluation"),
 "XDATA": ("data-and-databases", "Tables, keys and data preparation"),
 "XAI": ("ai-and-ml", "Predictive models and tuning"),
 "XSW": ("software-and-systems", "File systems"),
 "XSEC": ("security-and-privacy", "Data anonymisation"),
}
by = {}
for n, c in assign.items():
    by.setdefault(c, []).append(n)
for c in by:
    by[c].sort(key=key)

for name, (title, intro, secs) in FILES.items():
    out = [f"# {title}", "", intro, ""]
    for code, h in secs:
        out += [f"## {h}", "", HEAD] + [lines[n - 1] for n in by[code]] + [""]
    (DST / "topics" / f"{name}.md").write_text("\n".join(out), encoding="utf-8")
    print(f"topics/{name}.md: {sum(len(by[c]) for c, _ in secs)} rows; " + "; ".join(f"{h} ({len(by[c])})" for c, h in secs))

for code, (fname, h) in COMMON.items():
    base = (SRC / "common" / f"{fname}.md").read_text(encoding="utf-8").rstrip("\n")
    rows = [lines[n - 1] for n in by[code]]
    (DST / "common" / f"{fname}.md").write_text(base + f"\n\n## {h}\n\n{HEAD}\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"common/{fname}.md + {len(rows)} rows under '## {h}': " + "; ".join(r.strip('|').split('|')[0].strip() for r in rows))
