# Saved states of the Milestone 5 report

Each saved state is a git commit and a path, not a copied folder.

Restore a whole state into a scratch folder:

```bash
git archive <commit> reports/milestone-5/report | tar -x -C /tmp/state     # or: git show <commit>:<path>
```

| Label | Path at the commit | Commit | What it is |
| :---- | :---- | :---- | :---- |
| full-draft-2026-11-09 | `reports/milestone-5/report` | `a6a8d5a` | The complete English draft of Sections 1–14 (about 47,000 words, 115 pages on the pessimistic layout) after the two AI reviews, before detail moved to the appendices |
