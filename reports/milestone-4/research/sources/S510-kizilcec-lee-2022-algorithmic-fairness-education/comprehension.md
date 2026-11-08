# S510 – Kizilcec, R. F., & Lee, H. (2022). Algorithmic fairness in education. In Ethics in Artific

## Summary in my own words

Kizilcec and Lee introduce algorithmic fairness in education. They define independence, separation and sufficiency with dropout examples, note that any two statistical criteria cannot be met at once except in unrealistic cases, and argue that merit-based criteria (separation, sufficiency) suit dropout prediction used to allocate study support. Fairness through unawareness fails because models reconstruct protected attributes from correlated features. They recommend audit toolkits such as Aequitas for internal and periodic audits.

## Key facts

- Statistical criteria conflict – "Since any two notions of statistical fairness cannot be satisfied simultaneously (except in unrealistic scenarios), one has to prioritize one notion of fairness over others."
- Merit-based criteria fit dropout support – "Merit-based fairness measures are most appropriate in applications like student dropout prediction for allocating additional study resources"
- Independence fits when the action harms – "independence is more appropriate if there is an even playing field to begin with or if the action taken with the algorithmic system has negative consequences"
- Unawareness fails – "a learned model can inadvertently reconstruct protected attributes from a number of seemingly unrelated features."
- Chouldechova A. (Big Data 2017; S507) and Kleinberg J. et al. (ITCS 2017; S508) are cited for the impossibility results – "the impossibility of fairness results (Chouldechova, 2017; Kleinberg et al., 2016)"
- Saleiro P. et al. (arXiv 2018; not registered) Aequitas toolkit for audits – "Open-source toolkits such as Aequitas (Saleiro et al., 2018)"

## Used in

05-02-causal-fairness-use.md (fairness metric choice for support allocation).

## Against reference.md

The outline line for Part 5 reads "fairness and high-stakes use with human oversight" (reference.md, Part 5). Confirms and sharpens: since contact is supportive (not punitive), separation (equal true and false positive rates across groups) is the natural primary audit criterion.

## Reliability

Primary: book chapter in Holmes & Porayska-Pomsta (Eds.), Ethics in Artificial Intelligence in Education, Routledge 2022 (Cornell authors); arXiv preprint 2007.05443. OpenAlex cited_by_count 321 (as of 2026-11-06).

## Open questions

None.
