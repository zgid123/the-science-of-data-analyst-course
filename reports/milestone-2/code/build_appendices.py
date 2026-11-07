"""Build Appendices I–VI of the Milestone 2 report from the research and package files, so tables stay identical to
their sources.

Usage: venv/bin/python reports/milestone-2/code/build_appendices.py
Reads research/search/search-log-brief.md, research/selection/selection.md, package/metadata/{source.md,
raw_manifest.csv,structure_results.json}, logs/T10_mirrors.log, research/coverage/coverage.md,
research/baseline/m1-baseline.md and research/review/*; writes report/11-01 … 11-06.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
R = ROOT / "research"
OUT = ROOT / "report"
PKG = ROOT / "package"


def table_after(text, marker):
    """The first markdown table after a marker line (header, rule and rows)."""
    lines = text[text.index(marker):].split("\n")
    out, started = [], False
    for l in (lines if lines[0].startswith("|") else lines[1:]):
        if l.startswith("|"):
            if re.fullmatch(r"\|(\s*:?-+:?\s*\|)+", l.strip()):
                l = "|" + " :---- |" * (l.strip().count("|") - 1)
            out.append(l)
            started = True
        elif started:
            break
    return out


def strip_ids(line):
    """Remove research-trail IDs (claims, sources, task codes, file names) that readers cannot follow."""
    line = re.sub(r" ?\((?:C\d-\d{3}[^)]*|S\d{3}[^)]*)\)", "", line)
    line = re.sub(r"\s*\(S\d{3}\)", "", line)
    line = line.replace("(task T06)", "").replace("Replacement for S308", "Replacement for the blocked University of Jordan page")
    line = (line.replace("Seeds S002, S003 (data descriptor and UCI record)", "Data descriptor and UCI record of OULAD")
                .replace("duplicates of S002", "duplicates of the descriptor").replace("replaced by S309", "replaced by the authors' Kaggle listing"))
    return line


def search_log():
    rows = table_after((R / "search" / "search-log-brief.md").read_text(), "| Date |")
    rows = [strip_ids(r) for r in rows]
    t = ["## Appendix I – Dataset Search Log\n",
         "Table A.1 lists every query and hit examined, including the rejected ones, in the format of the brief "
         "(section 7.1). Keywords came from the data requirements of Section 2.\n",
         "**Table A.1. Dataset search log**\n"] + rows
    (OUT / "11-01-search-log.md").write_text("\n".join(t) + "\n")


def scoring():
    rows = table_after((R / "selection" / "selection.md").read_text(), "## 1. Full scoring")
    rows = [re.sub(r" \((?:C\d-\d{3}|S\d{3})[^)]*\)", "", r) for r in rows]
    t = ["## Appendix II – Candidate Scoring Details\n",
         "Table A.2 gives each candidate's score on the brief's ten criteria (0 = not met or not stated, 1 = partly met "
         "or uncertain, 2 = well met) with the fact behind it, and the must-have gates it fails. Every fact comes from "
         "the candidate's official page or descriptor.\n",
         "The ten criteria " + (R / "appendix-text" / "criteria.md").read_text().strip()[len("Every candidate was scored on the ten criteria of the brief [1]. They "):].replace("\n", " ") + "\n",
         "**Table A.2. Scores on the ten criteria and failed gates**\n"] + rows
    (OUT / "11-02-scoring-details.md").write_text("\n".join(t) + "\n")


def acquisition():
    src = table_after((PKG / "metadata" / "source.md").read_text(), "| Item |")
    man = list(csv.reader(open(PKG / "metadata" / "raw_manifest.csv")))
    mirror = [l for l in (ROOT / "logs" / "T10_mirrors.log").read_text().split("\n") if l.startswith("|")]
    mirror = [mirror[0].replace("| Same parsed rows |", "| Same rows |"), mirror[1]] + mirror[2:]
    t = ["## Appendix III – Acquisition Plan and Data Collection Package\n",
         "The Data Collection Package re-creates the team's copy of OULAD exactly. Its layout is shown below; the raw "
         "files are produced by the collection script and are not edited.\n",
         "```text\npackage/\n  README.md\n  data/raw/        published files, unchanged\n  metadata/        source.md, "
         "citation.bib, data_dictionary.md, raw_manifest.csv,\n                   collection_log.txt, structure_report.md, "
         "structure_results.json\n  src/             collect.py (download, verify, extract), verify_structure.py (Section 6)\n```\n",
         "Table A.3 is the source and license sheet of the package.\n",
         "**Table A.3. Source, license and citation**\n"] + src + [
        "", "Table A.4 lists the size, checksums and data rows of every collected file; each table matched its pinned "
        "SHA-256.\n", "**Table A.4. Raw file manifest**\n",
        "| File | Bytes | SHA-256 | MD5 | Data rows | Check |", "| :---- | :---- | :---- | :---- | :---- | :---- |"]
    for r in man[1:]:
        t.append(f"| {r[0]} | {int(r[1]):,} | {r[2]} | {r[3]} | {r[4] and format(int(r[4]), ',')} | {r[5]} |")
    t += ["", (R / "appendix-text" / "copies.md").read_text().strip().replace("\n", " ") + "\n",
          "Table A.5 compares the UCI copy of OULAD with the collected figshare files, table by table.\n",
          "**Table A.5. Comparison of the UCI copy with the collected files**\n"] + mirror
    (OUT / "11-03-acquisition-package.md").write_text("\n".join(t) + "\n")


def structure():
    d = json.loads((PKG / "metadata" / "structure_results.json").read_text())
    c = d["checks"]
    t = ["## Appendix IV – Structural Verification Details\n",
         "Table A.6 gives, for each table, the headers found, the types inferred from the text values and the "
         "missing cells; Table A.7 lists the counts that settle the selection conditions.\n",
         "**Table A.6. Headers, inferred types and missing values**\n",
         "| Table | Headers and inferred types | Missing cells |", "| :---- | :---- | :---- |"]
    for name, r in d["tables"].items():
        types = ", ".join(f"{k} ({v})" for k, v in r["types"].items())
        miss = ", ".join(f"{k} {v:,}" for k, v in r["missing"].items()) or "none"
        t.append(f"| {name} | {types} | {miss} |")
    t += ["", "Table A.7 gives the counts that decide the selection conditions G1, G3 and G5, the timing of the first tasks and "
          "the KPI denominator.\n", "**Table A.7. Counts behind the selection conditions and the denominator**\n",
          "| Check | Result |", "| :---- | :---- |",
          f"| Result values | {', '.join(f'{k} {v:,}' for k, v in c['final_result_values'].items())} |",
          f"| Withdrawn with / without an unregistration day; other results with one | {c['withdrawn_with_date']:,} / {c['withdrawn_without_date']} ; {c['date_but_not_withdrawn']} |",
          f"| Students; students in more than one run | {c['students_total']:,}; {c['students_in_more_than_one_run']:,} |",
          f"| Same-module repeats; repeats with a higher attempt count | {c['same_module_repeats']:,}; {c['repeats_with_higher_attempt_counter']:,} |",
          "| Runs per module | " + "; ".join(f"{m}: {', '.join(r)}" for m, r in c["runs_per_module_all"].items()) + " |",
          f"| Runs with a non-exam task due by day 13 / day 27 (of 22) | {c['runs_with_task_due_by_day_13']} / {c['runs_with_task_due_by_day_27']} |",
          "| First non-exam task due day per run | " + ", ".join(f"{k} {v}" for k, v in c["first_task_due_day"].items()) + " |",
          f"| Exams without a due day | {c['exams_without_cutoff_day']} |",
          f"| Unregistered on or before day 0; registered after day 14; registration day missing | {c['unregistered_on_or_before_day_0']:,}; {c['registered_after_day_14']}; {c['registration_day_missing']} |",
          f"| Still registered on day 14 | {c['still_registered_at_day_14']:,} |",
          f"| Rows without a parent (assessment, submission, click enrolment, click site) | {c['assessment_rows_without_parent']}, {c['submissions_without_enrolment']}, {c['click_rows_without_enrolment']}, {c['click_rows_without_site']} |"]
    (OUT / "11-04-structure-details.md").write_text("\n".join(t) + "\n")


def change_log():
    cov = (R / "coverage" / "coverage.md").read_text()
    rows = table_after(cov, "## 4. Controlled Change Log")
    rows = [re.sub(r",? C\d-\d{3}", "", re.sub(r" ?\((?:C\d-\d{3}|C3-012)\)", "", r)).replace(" (selection.md)", "") for r in rows]
    base = (R / "baseline" / "m1-baseline.md").read_text()
    sums = table_after(base, "## Source files (SHA-256)")
    t = ["## Appendix V – Controlled Change Log and Full Traceability\n",
         "The Milestone 1 baseline was frozen before the search: Table A.8 lists the proposal files it was copied from, "
         "with their SHA-256, so any later edit to them is detectable. Table A.9 records every change to the baseline "
         "with its data evidence, in the format of the brief (section 3.1).\n",
         "**Table A.8. Frozen Milestone 1 files**\n"] + sums + ["", "Table A.9 gives each change with the old and new "
         "content, the data evidence and its effect on the questions, KPIs and decisions.\n", "**Table A.9. Controlled Change Log**\n"] + rows
    full = table_after(cov, "## 3. Full traceability")
    t += ["", "Table A.10 is the full traceability matrix of deliverable B: every row serves the Business Goal of improving "
          "successful course completion by identifying students who stop taking part early enough to support them within "
          "the semester, and links its KPI, question, data requirement, files, actual variables, coverage and decision.\n",
          "**Table A.10. Full traceability from goal to decision with coverage**\n"] + full
    (OUT / "11-05-change-log.md").write_text("\n".join(t) + "\n")


def ai_evidence():
    def prompt(path):
        s = (R / "review" / path).read_text()
        s = re.sub(r"^#.*\n+", "", s).strip()
        return "```text\n" + s + "\n```"

    def decisions(path):
        rows = table_after((R / "review" / path).read_text(), "| # |")
        return [re.sub(r" \(Sections? [^)]*\)|research/requirements/data-requirements\.md", "", r) for r in rows]

    t = ["## Appendix VI – Generative AI Usage Evidence\n",
         "An AI agent searched for candidate datasets for the team with the prompt below; every query it ran is in "
         "Appendix I, and every fact it recorded was checked by team members against the saved official page.\n",
         "Prompt of the search strategist and metadata interpreter:\n", prompt("search-strategist-prompt.md"), "",
         "Two isolated AI agents critiqued the work at fixed points: a requirement critic before any dataset was scored, "
         "and a selection reviewer after the scoring. Each received only the brief and the team's files named in its "
         "prompt. Their prompts are reproduced in English as used; Tables A.11 and A.12 give each critique in short form "
         "with the team's decision and the change made.\n",
         "Prompt of the requirement critic:\n", prompt("requirement-critic-prompt.md"), "",
         "Table A.11 lists the requirement critic's twelve critiques with the team's decisions.\n",
         "**Table A.11. Requirement critic: AI critique, team decision and change**\n"] + \
        decisions("requirement-critic-decisions.md") + [
        "", "Prompt of the selection reviewer:\n", prompt("selection-reviewer-prompt.md"), "",
        "Table A.12 lists the selection reviewer's ten critiques with the team's decisions.\n",
        "**Table A.12. Selection reviewer: AI critique, team decision and change**\n"] + \
        decisions("selection-reviewer-decisions.md")
    # Appendix VI was edited by hand so that its prompts name documents by their place in the report (the submitted
    # report is read without the repository); it is written only when absent. Delete it to regenerate from the trail.
    if not (OUT / "11-06-ai-evidence.md").exists():
        (OUT / "11-06-ai-evidence.md").write_text("\n".join(t) + "\n")


if __name__ == "__main__":
    search_log(); scoring(); acquisition(); structure(); change_log(); ai_evidence()
    print("appendices I–VI written")
