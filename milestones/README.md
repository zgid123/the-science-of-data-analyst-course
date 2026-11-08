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
| 5 | `05/milestone-5.pdf` | `05/milestone-5.md` | FAIL on one verifier exception only (below); all 9 pages reviewed |

**Milestone 5 exception.** `text` and `tables` report 17 missing `□` in the checkbox cells of the Traceability
Matrix (page 4, Final Status) and the AQ Revision Log (page 5, Action). The Markdown holds every `□`: the cells print
their options on separate lines, written as `<br>`, and the verifier reads a `□` that starts a line as a list bullet
and drops it. The same copy with those `<br>` written as spaces passes all eleven checks (probe in the log).

**Milestone 5 conventions.** The checklist of section 9 starts each line with `□` (U+25A1), which `pdf2md` treats as
a bullet, so it reads `- item`; the briefs of Milestones 1–4 use `☐` (U+2610) and read `- [ ] item`.

Re-check a copy:

```bash
uv run .claude/skills/pdf2md/scripts/verify.py milestones/05/milestone-5.pdf milestones/05/milestone-5.md
```
