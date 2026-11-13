# Self-assessment (team N04, Milestones 1–5)

The preliminary self-assessment the team submits with Milestones 1–5 ("Bảng đánh giá sơ bộ kết quả của nhóm trên nhiệm
vụ được giao (mẫu mỗi nhóm tự biên soạn)"): the team's comments by milestone on the problems met and how they were solved (Section 1, the main content), with the
results and contribution of each milestone (Appendix I), the rating scale (Appendix II) and every grading criterion of the
five briefs (`milestones/0N/`) rated against the submitted reports (Appendix III). Its text-heavy tables take landscape pages.

| Path | Content |
| :---- | :---- |
| `report/` | Sections in English (`*.md`) and their Vietnamese twins (`*.vi.md`); compact layout, no contents page |
| `build/` | `N04_SelfAssessment_EN.docx`, `N04_SelfAssessment_VI.docx` |
| `logs/` | Build, page-budget, pair-check and consistency logs |
| `research/reviews/` | Vietnamese review rounds: native reviews, reader tests and re-tests, decisions on every flag (01–04 first layout, 05–14 after the restructure) |
| `code/check_pairs.py` | Pair-by-pair check of each English source and Vietnamese twin |
| `PROGRESS.md` | Ledger: decisions and the source of every number in the document |

```bash
make all TASK=self-assessment        # prechecks, Word build (EN, VI), postchecks, skill tests
make pages TASK=self-assessment      # pessimistic page count
venv/bin/python reports/self-assessment/code/check_pairs.py   # pair-by-pair check (structure, rows, numbers)
```
