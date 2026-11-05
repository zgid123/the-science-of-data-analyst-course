# Milestone 1 proposal (team N04)

Requirement analysis and analytics project proposal for MTH045 on low course completion and mid-semester
disengagement in online and blended courses, following `final-project/milestones/01/milestone-1.md`.

- `reference.md`, `EXECUTION_PLAN.md`, `plan.toml`, `PROGRESS.md`: outline, plan and ledger (research-report skill).
- `research/`: sources and claims (`sources.md`, `part*-claims.md`, `sources/Sxxx-*`), interview records
  (`interviews/`: persona notes and cards, question lists, transcripts, key statements, synthesis, validation),
  AI review (`review/`), Vietnamese review logs (`vi-review/`).
- `report/`: English sections and Vietnamese twins (`*.vi.md`); `build/`: Word documents.
- `code/`: task scripts; `logs/`: check and build logs.

## Commands (from the repository root)

```bash
venv/bin/python reports/milestone-1/code/build_appendices.py        # Appendices I–IV from research/interviews and research/review
venv/bin/python reports/milestone-1/code/check_quotes.py \
  reports/milestone-1/research/interviews/key-statements.md \
  reports/milestone-1/research/interviews/validation-results.md       # every quote verbatim in its transcript
make all TASK=milestone-1                                              # checks, EN and VI Word build, post-checks
venv/bin/python reports/milestone-1/code/estimate_parts.py reports/milestone-1/build/N04_Milestone1_EN.docx  # pages per part
venv/bin/python .claude/skills/research-report/scripts/progress.py --base reports/milestone-1 status
```

`research/interviews/ask.sh <role> <label> "<question>"` records an interviewer turn in a transcript before it is sent.
