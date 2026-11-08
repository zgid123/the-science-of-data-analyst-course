"""Build Appendices I–VI of the Milestone 3 report from the package and research files, so every appendix table is
identical to the file it comes from.

Usage: venv/bin/python reports/milestone-3/code/build_appendices.py
Reads package/data/metadata/{quality_issue_log.md, profile.json, profile_crosscheck.csv, transformation_log.md,
version_manifest.json, lineage.md, traceability.md, change_log.md, ai_decision_log.md, validation_summary.json},
research/reviews/NN-ai-*-decisions.md and -prompt.md; writes report/12-00 … 12-06.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "package" / "data" / "metadata"
REV = ROOT / "research" / "reviews"
EXTRA = ROOT / "research" / "appendix"     # tables moved from the main text
OUT = ROOT / "report"


def table_after(text, marker=None):
    """The first markdown table (after a marker, if given), separators normalised to ':----'."""
    if marker:
        text = text[text.index(marker):]
    out, started = [], False
    for line in text.split("\n"):
        if line.startswith("|"):
            if re.fullmatch(r"\|(\s*:?-+:?\s*\|)+", line.strip()):
                line = "|" + " :---- |" * (line.strip().count("|") - 1)
            out.append(line)
            started = True
        elif started:
            break
    return "\n".join(out)


def drop_cols(table, names):
    rows = [r.split("|")[1:-1] for r in table.split("\n")]
    head = [c.strip() for c in rows[0]]
    keep = [i for i, c in enumerate(head) if c not in names]
    return "\n".join("|" + "|".join(r[i] for i in keep) + "|" for r in rows)


def rename_cols(table, names):
    """Rename header cells: names maps old header text to new."""
    lines = table.split("\n")
    cells = lines[0].split("|")
    lines[0] = "|".join(f" {names.get(c.strip(), c.strip())} " if c.strip() else c for c in cells)
    return "\n".join(lines)


def map_cells(table, fn, cols=None):
    """Apply fn(text) to body cells (of the named columns, or all)."""
    lines = table.split("\n")
    head = [c.strip() for c in lines[0].split("|")[1:-1]]
    idx = {i for i, h in enumerate(head) if cols is None or h in cols}
    out = lines[:2]
    for line in lines[2:]:
        cells = line.split("|")[1:-1]
        out.append("|" + "|".join(f" {fn(c.strip())} " if i in idx else c for i, c in enumerate(cells)) + "|")
    return "\n".join(out)


def short_keys(text):
    """P.section.key and U.section.key evidence pointers shortened to their section (P.validity)."""
    return re.sub(r"\b([PU])\.([A-Za-z]\w*)(?:\.[\w.]+)", r"\1.\2", text)


SIGNS = [(" -> ", " → "), ("->", "→"), (" x ", " × "), ("<=", "≤"), (">=", "≥")]


def signs(text):
    for a, b in SIGNS:
        text = text.replace(a, b)
    return text


def fmt_value(v):
    """A validation value written for a reader: numbers with thousands separators, lists and dicts as text."""
    import ast
    def num(x):
        return f"{x:,}" if isinstance(x, int) else (f"{x:g}" if isinstance(x, float) else str(x))
    def one(x):
        if isinstance(x, dict):
            vals = list(x.values())
            if vals and all(v in ([], "") for v in vals):
                return "none"
            if vals and all(v == 0 for v in vals):
                return f"0 in all {len(vals)}" if len(vals) > 2 else "0"
            return "; ".join(f"{k}: {one(v)}" for k, v in x.items())
        if isinstance(x, (list, tuple)):
            if not x:
                return "none"
            if all(isinstance(i, tuple) and len(i) == 2 for i in x):
                return ", ".join(f"{a} {num(b)}" for a, b in x)
            if len(x) == 2 and all(isinstance(i, (int, float)) for i in x):
                return f"{num(x[0])}–{num(x[1])}"
            return ", ".join(one(i) for i in x)
        return num(x)
    parts = []
    for part in str(v).split("; "):
        try:
            if not part.strip().startswith(("[", "{", "(")):
                raise ValueError
            parts.append(one(ast.literal_eval(part.strip())))
        except (ValueError, SyntaxError):
            part = re.sub(r"\[(-?[\d.]+), (-?[\d.]+)\]", r"\1–\2", part)
            part = re.sub(r"(\w+) \[\]", r"no \1 column", part)
            parts.append(re.sub(r"(?<![\d,.])(\d{4,})(?![\d,.])", lambda m: f"{int(m.group(1)):,}", part))
    return "; ".join(parts)


def md(rows, cols):
    out = ["| " + " | ".join(cols) + " |", "|" + " :---- |" * len(cols)]
    out += ["| " + " | ".join(str(r[c]).replace("|", "\\|") for c in cols) + " |" for r in rows]
    return "\n".join(out)


# The prompts name files as the agents saw them in the team's workspace; the appendix names them as the reader finds
# them: relative to the Prepared Data Package, or as the report section that holds the document.
PROMPT_PATHS = [
    ("reports/milestone-3/research/preparation/decision-matrix.md`, `feature-spec.md`, `split-spec.md`",
     "data/metadata/decision_matrix.md`, `feature_spec.md`, `split_spec.md`"),
    ("`reports/milestone-3/research/fit/aq-data-fit.md`", "the AQ–Data Fit Decision Log (Section 4)"),
    ("reports/milestone-3/package/", ""),
    ("with `venv/bin/python` (polars)", "with Python (polars)"),
]
# Sources named by author and year in the package's AI Decision Log, as numbered in the report's reference list.
LOG_CITATIONS = [("(OU TMA and iCMA policy, The Open University, 2025)", "[3]"),
                 ("(DCLG, 2015; Abel et al., 2016)", "[5], [6]")]


def quote_block(path):
    text = "\n".join(l for l in path.read_text().split("\n") if l.startswith(">"))
    for a, b in PROMPT_PATHS:
        text = text.replace(a, b)
    return text


def cite(text):
    for a, b in LOG_CITATIONS:
        text = text.replace(a, b)
    return text


def main():
    prof = json.loads((META / "profile.json").read_text())
    val = json.loads((META / "validation_summary.json").read_text())
    man = json.loads((META / "version_manifest.json").read_text())

    (OUT / "12-00-appendices.md").write_text(
        "# Appendices\n\nThe appendices hold the evidence behind the main text: the full profiling and quality "
        "results (Appendix I), the pipeline and the Prepared Data Package (Appendix II), the data dictionary and "
        "lineage (Appendix III), the updated traceability and Controlled Change Log (Appendix IV), the AI Decision "
        "Log with its prompts (Appendix V) and the validation ledger (Appendix VI). Each table is generated from the "
        "file named with it, so it matches the package exactly.\n")

    # I. Profiling and quality details
    cc = list(csv.DictReader((META / "profile_crosscheck.csv").open()))
    cc_rows = [{"Measure": r["measure"], "Independent recount": f"{int(r['exploration']):,}",
                "Milestone 3 profile": f"{int(r['milestone3']):,}", "Equal": "yes" if r["equal"] == "True" else "no"}
               for r in cc]
    ct = prof["duplicates"]["chance_test_two_row_groups"]
    ct_rows = [{"Activity type": a, "Two-row groups": f"{n:,}", "Equal counts observed": f"{o:.1%}"}
               for a, o, n in ct["observed_by_activity_type_top6"]]
    (OUT / "12-01-profiling-details.md").write_text(
        "## Appendix I – Data Understanding, Profiling and Quality Details\n\n"
        "Figure A.1 shows the seven OULAD tables with their row counts and the keys that link them; each link was "
        "checked on the data (`understanding.json`).\n\n"
        "![Figure A.1. Tables, row counts and keys of OULAD](assets/figures/fig-2-1-tables.png)\n\n"
        "Figure A.2 shows weekly clicks per enrolled student by start month, with the two cut-offs at the end of weeks "
        "2 and 4 (`fig_weekly_activity.csv`).\n\n"
        "![Figure A.2. Weekly clicks per enrolled student by start month, with the two cut-offs](assets/figures/fig-3-2-weekly.png)\n\n"
        "The inputs required by the brief, checked before preparation began, are listed in Table A.1 with their status."
        "\n\n**Table A.1. Inputs from Milestone 2 and their status**\n\n"
        + (EXTRA / "inputs.md").read_text().strip() +
        "\n\nTable A.2 sets out what each day field and measure of OULAD means and when it becomes known; the "
        "meanings come from the data descriptor and the OU's assessment policy, the counts from `understanding.json`."
        "\n\n**Table A.2. Meaning and timing of the key fields**\n\n" + (EXTRA / "semantics.md").read_text().strip() +
        "\n\nTable A.3 lists the six sensitive attributes with their codes, smallest group and the number of module-run "
        "groups with fewer than 20 students.\n\n**Table A.3. Sensitive attributes**\n\n"
        + (EXTRA / "sensitive.md").read_text().strip() + "\n\n"
        "The Data Quality Issue Log in Table A.4 gives the full evidence of every issue of Table 3.1; P. refers to sections of "
        "`data/metadata/profile.json` and U. to `understanding.json`.\n\n"
        "**Table A.4. Data Quality Issue Log with evidence**\n\n" + map_cells(rename_cols(table_after((META / "quality_issue_log.md").read_text()), {"Issue ID": "ID"}),
                   lambda c: short_keys(re.sub(r"; quizzes, wikis and questionnaires fall below chance, forums and "
                                               r"content pages above it \(P\.duplicates\.chance_test_two_row_groups\)",
                                               " (Table A.6)",
                                               {"High for exams, none for coursework": "High (exams)",
                                                "High for claims": "High (claims)"}.get(c, c)))) +
        "\n\nThirteen figures of the profile were recounted by an independent exploration of the same files with separate "
        "code (`profile_crosscheck.csv`); "
        f"Table A.5 shows the {len(cc_rows)} measures compared, all equal.\n\n"
        "**Table A.5. Cross-check with an independent recount**\n\n" + md(cc_rows, list(cc_rows[0])) +
        f"\n\nThe chance test of duplicate click rows compares, in the {ct['groups']:,} student-resource-day groups "
        f"with exactly two rows, the share with equal click counts ({ct['observed_equal_share']:.1%}) with the share "
        f"expected by chance from each resource's own counts ({ct['expected_by_site']:.1%}) or from each activity "
        f"type's counts ({ct['expected_by_activity_type']:.1%}). Table A.6 gives the observed share for the six "
        "activity types with the most such groups.\n\n**Table A.6. Equal counts in two-row groups by activity type**\n\n"
        + md(ct_rows, list(ct_rows[0])) + "\n")

    # II. Pipeline and package
    steps = [("00", "link_raw.py", "raw files hard-linked, SHA-256 checked against the Milestone 2 pins"),
             ("01", "01_understand.py", "Dataset Understanding Map (Section 2.1)"),
             ("02", "02_profile.py", "profile and quality evidence (Section 3)"),
             ("03", "unittest on tests/", "formula tests on synthetic fixtures"),
             ("04", "prepare_data.py", "ten preparation steps, views and transformation log (Section 6)"),
             ("05", "fit_transforms.py", "transforms fitted on 2013 runs, model-ready matrices (Section 6.3)"),
             ("06", "validate_prepared.py", "22 checks, dictionary, lineage, version manifest (Section 7)"),
             ("07", "build_notebooks.py", "notebooks 02 and 03, executed")]
    out_rows = [{"File": k, "Rows": f"{v['rows']:,}", "SHA-256 (first 16)": v["sha256"][:16]}
                for k, v in man["outputs"].items()]
    tl = map_cells(table_after((META / "transformation_log.md").read_text()),
                   lambda c: signs(c.replace(" (SHA-256 pinned, columns as documented)", "")))
    (OUT / "12-02-pipeline-package.md").write_text(
        "## Appendix II – Preparation Pipeline and Prepared Data Package\n\n"
        "Figure A.3 shows the five phases of the pipeline, from the read-only raw files to the validated package.\n\n"
        "![Figure A.3. From the raw files to the prepared views](assets/figures/fig-6-1-pipeline.png)\n\n"
        "Table A.7 maps the ten preparation steps of the brief to the function of `src/prepare_data.py` or the script "
        "that carries each out, with the row counts it produced.\n\n**Table A.7. Pipeline steps, code and results**\n\n"
        + (EXTRA / "steps.md").read_text().strip() + "\n\n"
        "The Prepared Data Package, submitted with this report, is laid out as the brief recommends: "
        "`data/raw/` (immutable inputs), `data/interim/`, `data/processed/`, `data/metadata/`, `notebooks/`, `src/`, "
        "`tests/` and `logs/`. One command, run from the package folder, rebuilds it from the raw files; when "
        "`data/raw/` is empty it first downloads the published archive and checks every table against its pinned "
        "SHA-256:\n\n"
        "```\nbash src/run_all.sh\n```\n\n"
        "Table A.8 lists the eight stages the command runs, each recording its command, time, output and exit "
        "status in `logs/`.\n\n**Table A.8. Stages of run_all.sh**\n\n"
        + md([{"Stage": a, "Script": f"`{b}`", "Output": c} for a, b, c in steps], ["Stage", "Script", "Output"]) +
        "\n\nThe transformation log records every operation with its row counts, in the order the pipeline runs them; "
        "each raw table is loaded only after its SHA-256 matches the pin and its columns match the documentation. "
        "Table A.9 reproduces it.\n\n"
        "**Table A.9. Transformation log**\n\n" + tl +
        f"\n\nThe prepared files are identified by version {man['prepared_dataset_version']}; Table A.10 gives their "
        "row counts and hashes from `version_manifest.json`, identical across two runs from the raw files.\n\n"
        "**Table A.10. Prepared files**\n\n" + md(out_rows, list(out_rows[0])) + "\n")

    # III. Dictionary and lineage
    lin = table_after((META / "lineage.md").read_text())
    rows_l = [r.split("|")[1:-1] for r in lin.split("\n")]
    head_l = [c.strip() for c in rows_l[0]]
    js, jp = head_l.index("Sensitivity"), head_l.index("Purpose / AQ")
    for r in rows_l[2:]:
        if r[js].strip() == "sensitive":
            r[jp] = f" {r[jp].strip()} (sensitive) "
    lin = drop_cols("\n".join("|" + "|".join(r) + "|" for r in rows_l), {"Sensitivity"})
    (OUT / "12-03-dictionary-lineage.md").write_text(
        "## Appendix III – Prepared Data Dictionary and Lineage\n\n"
        "Table A.11 links each analytics level to its prepared view, population and grain, with the check the brief "
        "sets before Milestone 4 and its result.\n\n**Table A.11. Prepared views by analytics level**\n\n"
        + (EXTRA / "views.md").read_text().strip() + "\n\n"
        "The data dictionary (`data/metadata/data_dictionary.md`) lists every column of every view with its type, "
        "role, source, transformation and sensitivity. Table A.12 is the lineage table of brief section 13.1, one row "
        "per prepared variable other than the keys; the six sensitive variables are marked in the purpose column.\n\n**Table A.12. Data lineage**\n\n" + lin + "\n")

    # IV. Traceability and change log
    (OUT / "12-04-traceability-change-log.md").write_text(
        "## Appendix IV – Updated Traceability and Controlled Change Log\n\n"
        "Table A.13 is the updated traceability of deliverable B: each row runs from the goal and KPI through the "
        "question and its analytics type to the raw variables, the preparation, the prepared variables and the "
        "decision supported.\n\n**Table A.13. Updated traceability**\n\n" + map_cells(table_after((META / "traceability.md").read_text()),
                   lambda c: {"AQ4 (rewritten, C11)": "AQ4", "Prescriptive (ranking requirement)":
                              "Prescriptive (ranking; AQ4 rewritten, C11)"}.get(c, c)) +
        "\n\nTable A.14 is the Controlled Change Log of deliverable E: C01–C08 from Milestone 2 and C09–C13 from the "
        "data understanding of Milestone 3 (column M), each with its evidence and effect.\n\n**Table A.14. Controlled Change Log**\n\n"
        + rename_cols(table_after((META / "change_log.md").read_text()), {"Milestone": "M"}) + "\n")

    # V. AI decision log and prompts
    crit = map_cells(table_after((REV / "01-ai-preparation-critic-decisions.md").read_text()), short_keys)
    aud = drop_cols(table_after((REV / "02-ai-leakage-auditor-decisions.md").read_text()), {"Decision"})
    (OUT / "12-05-ai-decision-log.md").write_text(
        "## Appendix V – AI Decision Log and Prompts\n\n"
        "Table A.15 is the AI Decision Log of deliverable F, one row per significant AI suggestion with the team's "
        "decision and the evidence used to verify it.\n\n**Table A.15. AI Decision Log**\n\n"
        + cite(map_cells(table_after((META / "ai_decision_log.md").read_text()), short_keys)) +
        "\n\nThe preparation critic received the following instruction and read only the issue log, the matrix, "
        "the specifications, the fit log and the profile. In both instructions, files are named by their place in "
        "the Prepared Data Package.\n\n" + quote_block(REV / "01-ai-preparation-critic-prompt.md") +
        "\n\nTable A.16 records the decision on each of its 12 critiques.\n\n"
        "**Table A.16. Decisions on the preparation critic's critiques**\n\n" + crit +
        "\n\nThe leakage auditor received the following instruction and could query the prepared and raw files "
        "without changing them.\n\n" + quote_block(REV / "02-ai-leakage-auditor-prompt.md") +
        "\n\nTable A.17 records the evidence and the effect of each of its 8 findings, all of which were accepted.\n\n"
        "**Table A.17. Decisions on the leakage auditor's findings**\n\n" + aud + "\n")

    # VI. Validation ledger
    rng = lambda t: re.sub(r"\[(-?[\d.,]+), (-?[\d.,]+)\]", r"\1–\2", t).translate(str.maketrans("", "", "{}'"))
    def vkey(c):
        m = re.match(r"V(\d+)(.*)", c["ID"])
        return (int(m.group(1)), m.group(2))
    rows = []
    for c in sorted(val["checks"], key=vkey):
        e, o = fmt_value(c["Expected"]), fmt_value(c["Observed"])
        rows.append({"ID": c["ID"], "Check": c["Check"], "Expected": e, "Observed": "as expected" if o == e else o,
                     "Status": c["Status"]})
    ex = val["extra"]
    (OUT / "12-06-validation-ledger.md").write_text(
        "## Appendix VI – Validation Ledger\n\n"
        f"Table A.18 lists the {len(rows)} checks of `src/validate_prepared.py` with their expected and observed "
        "values, from `data/metadata/validation_summary.json`.\n\n**Table A.18. Validation ledger**\n\n"
        + md(rows, list(rows[0])) +
        "\n\nThe validation also reports, without using any test outcome, the figures that the Milestone 4 plan "
        f"relies on: the early-sign rule flags {ex['rule_rate_overall']['d13']:.1%} of enrolled students at day 13 "
        f"and {ex['rule_rate_overall']['d27']:.1%} at day 27 ({ex['rule_rate_cma_variant']['d27']:.1%} with CMA "
        f"lateness); CMA marks known by the cut-off cover {ex['cma_score_coverage_training_rows']['d13']:.1%} and "
        f"{ex['cma_score_coverage_training_rows']['d27']:.1%} of training rows; and completion in the day-14 "
        f"population is {ex['kpi_sensitivity']['completion_day14']:.1%}, or "
        f"{ex['kpi_sensitivity']['completion_without_138_flagged']:.1%} without the 138 enrolments flagged for an unknown withdrawal day (93) or registration day (45). "
        "Rule rates per run and cut-off are in `rule_rates.csv`.\n")
    # Blocks moved from the main text: research/appendix/detail-NN.md is appended to Appendix NN (12-NN-*.md).
    for extra in sorted(EXTRA.glob("detail-*.md")):
        nn = extra.stem.split("-")[1]
        target = next(f for f in OUT.glob(f"12-{nn}-*.md") if not f.name.endswith(".vi.md"))
        target.write_text(target.read_text().rstrip() + "\n\n" + extra.read_text().strip() + "\n")
    print("wrote", ", ".join(sorted(p.name for p in OUT.glob("12-0*.md"))))


if __name__ == "__main__":
    main()
