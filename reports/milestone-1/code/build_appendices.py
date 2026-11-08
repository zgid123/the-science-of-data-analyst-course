"""Build Appendices I-III of the Milestone 1 proposal from the interview records, so every quotation stays verbatim.

Usage: venv/bin/python reports/milestone-1/code/build_appendices.py
Reads research/interviews/{questions/*.md, key-statements.md, validation-results.md, validation-brief.md} and writes
report/11-01-interview-questions.md, 11-02-interview-excerpts.md, 11-03-validation-round.md.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IV = ROOT / "research" / "interviews"
OUT = ROOT / "report"
ROLES = [("PM", "program-manager", "Program Manager"), ("CL", "lecturer", "Course Lecturer"),
         ("AD", "advisor", "Academic Advisor / Student Support Officer"), ("ST", "student", "Student"),
         ("DO", "data-officer", "Learning Technology and Data Officer")]
GROUPS = {"BG": "Business goals", "SV": "Success vision", "CH": "Challenges", "DM": "Decision making",
          "RA": "Risk anticipation"}
LABELS = {"O": "Opinion", "A": "Assumption", "S": "Scenario", "S/O": "Scenario and opinion"}


def inner(cell):
    """A quotation inside a quoted excerpt takes single quotes, so the outer quotes stay unambiguous."""
    if len(cell) > 2 and cell[0] == cell[-1] == '"':
        return '"' + cell[1:-1].replace('"', "'") + '"'
    return cell


def rows(path, pattern):
    return [[c.strip().replace("\\\"", "\"") for c in l.strip().strip("|").split(" | ")] for l in path.read_text().splitlines()
            if re.match(pattern, l)]


def questions():
    t, n = [], 1
    t.append("## Appendix I – Interview Questions\n")
    t.append("The questions below were written before the interviews and cover the five information groups of the brief "
             "(business goals, success vision, challenges, decision making and risk anticipation). They are listed by "
             "stakeholder: Table A.1 for the Program Manager, Table A.2 for the Course Lecturer, Table A.3 for the "
             "Academic Advisor, Table A.4 for the Student and Table A.5 for the Learning Technology and Data Officer. Each question was asked in order, and a question was dropped when an earlier "
             "answer had already covered it in full. Table A.6 shows two drafts that were rewritten because they led the "
             "stakeholder towards an answer.\n")
    for code, slug, name in ROLES:
        t.append(f"**Table A.{n}. {name}: interview questions**\n")
        t.append("| Code | Group | Question |\n| :---- | :---- | :---- |")
        for r in rows(IV / "questions" / f"{slug}.md", rf"\| {code}-Q\d"):
            t.append(f"| {r[0]} | {GROUPS[r[1]]} | {r[2]} |")
        t.append("")
        n += 1
    t.append(f"**Table A.{n}. Leading drafts and their final form**\n")
    t.append("| Draft | Problem | Final question |\n| :---- | :---- | :---- |")
    for r in rows(IV / "questions" / "README.md", r"\| (CL|ST): "):
        t.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    (OUT / "11-01-interview-questions.md").write_text("\n".join(t) + "\n")
    return n + 1


def excerpts(n):
    t = ["## Appendix II – Interview Excerpts\n",
         "The key statements of each interview are quoted word for word from the transcripts: Table A.7 for the "
         "Program Manager, Table A.8 for the Course Lecturer, Table A.9 for the Academic Advisor, Table A.10 for the "
         "Student and Table A.11 for the Learning Technology and Data Officer. "
         "The code in the first column is the one used in the main text (for example PM1). The label marks each "
         "statement as the stakeholder's opinion, an assumption (an estimate or impression the stakeholder gives as a "
         "figure or fact) or information from the scenario; Q1 to Q8 refer to the questions of Appendix I, and "
         "\"follow-up\" marks a question added during the interview.\n"]
    data = rows(IV / "key-statements.md", r"\| [A-Z]{2}\d+ \|")
    for code, slug, name in ROLES:
        t.append(f"**Table A.{n}. {name}: key statements**\n")
        t.append("| Code | Question | Excerpt | Label | Meaning for the project |\n| :---- | :---- | :---- | :---- | :---- |")
        for r in data:
            if r[1] == code:
                turn = r[2].replace("f-up", "follow-up")
                t.append(f"| {r[0]} | {turn} | {inner(r[4])} | {LABELS[r[5]]} | {r[6]} |")
        t.append("")
        n += 1
    (OUT / "11-02-interview-excerpts.md").write_text("\n".join(t))
    return n


def validation(n):
    brief = (IV / "validation-brief.md").read_text().split("---\n")[1].strip()
    quoted = "\n".join("> " + l if l else ">" for l in brief.splitlines())
    t = ["## Appendix III – Validation Round\n",
         "After the synthesis, each stakeholder was shown the summary below in the same conversation as the interview, "
         "followed by one question for that role, and asked what was right, what should be corrected and what was "
         "missing. The program manager's answer led to a revised SMART Goal, which was presented again and confirmed.\n",
         quoted + "\n",
         f"Table A.{n} gives the key statements of the validation round, quoted word for word, with their effect on the "
         "proposal; Section 2.4 summarises the result, and Table A.17 in Appendix VI gives it in full.\n",
         f"**Table A.{n}. Validation statements and their effect on the proposal**\n",
         "| Code | Excerpt | Effect on the proposal |\n| :---- | :---- | :---- |"]
    for r in rows(IV / "validation-results.md", r"\| V[A-Z]{2}\d+ \|"):
        t.append(f"| {r[0]} | {inner(r[3])} | {r[4]} |")
    (OUT / "11-03-validation-round.md").write_text("\n".join(t) + "\n")
    return n + 1


def review(n):
    prompt = (ROOT / "research" / "reviews" / "01-ai-reviewer-prompt.md").read_text().split("---\n")[1].strip()
    # the submitted report is read without the repository: file paths in the prompt become the documents' names
    prompt = prompt.replace("the instructor brief (final-project/milestones/01/milestone-1.md) and the proposal sections\n"
                            "reports/milestone-1/report/01-*.md to 07-*.md (English). Do not read any other file.",
                            "the instructor brief and Sections 1–7 of the proposal (English). Do not read any other\n"
                            "document.")
    quoted = "```text\n" + prompt + "\n```"
    t = ["## Appendix IV – AI Critique, Team Decisions and Reviewer Prompt\n",
         f"An isolated AI reviewer read the brief and Sections 1–7 with the prompt below and returned twelve critiques. "
         f"Table A.{n} gives each critique in short form, the team's decision and the reason or change; Section 8 "
         "discusses three of them.\n",
         f"**Table A.{n}. AI critique, team decision and reason**\n",
         "| No. | AI critique | Team decision | Reason or change |\n| :---- | :---- | :---- | :---- |"]
    for r in rows(ROOT / "research" / "reviews" / "01-ai-reviewer-decisions.md", r"\| R\d+ \|"):
        t.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")
    t += ["", "The reviewer prompt, with documents named by their place in this report:\n", quoted]
    (OUT / "11-04-ai-critique-review.md").write_text("\n".join(t) + "\n")
    return n + 1


if __name__ == "__main__":
    nxt = review(validation(excerpts(questions())))
    print(f"appendices I-III written; next table number A.{nxt}")
