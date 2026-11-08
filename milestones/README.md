# Milestone briefs

The instructor briefs of MTH045, one folder per milestone. Each `milestone-<n>.pdf` is kept as received;
`milestone-<n>.md` is its Markdown copy made with the `pdf2md` skill and checked against the PDF by `verify.py` and
a page-by-page visual review. The team's own deliverables are in `final-project/milestones/<nn>/`.

| Milestone | Brief | Markdown copy | Verification (`logs/verify_2026-11-08.log`) |
| :---- | :---- | :---- | :---- |
| 1 | `01/milestone-1.pdf` | `01/milestone-1.md` | PASS |
| 2 | `02/milestone-2.pdf` | `02/milestone-2.md`, `02/milestone-2_assets/` | PASS |
| 3 | `03/milestone-3.pdf` | `03/milestone-3.md`, `03/milestone-3_assets/` | PASS |
| 4 | `04/milestone-4.pdf` | `04/milestone-4.md`, `04/milestone-4_assets/` | PASS |
| 5 | `05/milestone-5.pdf` | `05/milestone-5.md` | PASS; all 9 pages reviewed |

**Checkboxes.** Milestone 5 marks its checklist and table options with `□` (U+25A1), Milestones 1–4 with `☐`
(U+2610). In every copy a checklist line is a native Markdown task item (`- [ ] …`); a box inside a table cell stays
as the PDF's own glyph, because Markdown has no task items in table cells.

Re-check a copy:

```bash
uv run .claude/skills/pdf2md/scripts/verify.py milestones/05/milestone-5.pdf milestones/05/milestone-5.md
```
