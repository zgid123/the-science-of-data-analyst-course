# Saved states of the Milestone 3 report

Each saved state is a git commit and a path, not a copied folder. Every file below was checked byte for byte
against commit `255c158` before its folder was removed (log: `logs/R_layout_2026-11-08.log`).

Restore a whole state into a scratch folder:

```bash
git archive 255c158 <path> | tar -x -C /tmp/state     # or: git show 255c158:<path>/<file>
```

| Label | Path at commit 255c158 | Files | First committed | What it is |
| :---- | :---- | :---- | :---- | :---- |
| condensed-2026-11-08 | `reports/milestone-3/research/revision/condensed-2026-11-08` | 82 | `5c27f65` (2026-11-08) | The report as it stood before the full-draft revision (the condensed version), kept for page and word comparison in `01-appendix-decisions.md`. |
| after-move2-2026-11-08 | `reports/milestone-3/research/revision/after-move2-2026-11-08` | 66 | `5c27f65` (2026-11-08) | The report after the second pass of moves to the appendices. |
| full-draft-08-03-traceability | `reports/milestone-3/research/revision/full-draft-08-03-traceability.md` | 1 | `5c27f65` (2026-11-08) | Section 8.3 (Updated Traceability) as written in the full draft, before its table moved to an appendix. |
