**Flagged records and placed submissions.** In step 5 of the pipeline, the four groups of flagged records are the 45
enrolments without a registration day, the 93 Withdrawn enrolments without a withdrawal day, the 9 Fail enrolments
with one, and the one unregistration on day 444 of a 268-day run. Step 7 places all 168,953 TMA and CMA submissions on
an enrolment-task row, the 1,909 banked results among them with the status "banked", so that they are counted but
never timed; the other 4,959 of the 173,912 submission rows are exam results, which are not tasks.

**Split controls in full.** The paragraphs below explain the controls summarised at the end of Section 6.3.

**Students seen in both years.** The 1,962 test enrolments of students who also enrolled in a 2013 run stay in the
main test set, because a later run of the same modules also contains repeating students, and a flag marks them so that
Milestone 4 can repeat the test on students never seen in training. When Milestone 4 tunes a model, it uses
leave-one-run-out folds inside 2013, holding out one run at a time, and removes from each fold's training data the
students who also appear in the held-out run, since the same student on both sides of a fold would inflate the
estimate [13].

**Fitted transforms.** Transforms that learn parameters from the data, such as filling a missing value with a median
or scaling a variable, are fitted on the training runs alone and then applied to the test runs [11]. As a check, the
parameters were fitted again after every test row had been changed, and they stayed the same, which shows that no
test row informs them. In addition, the 2014 outcomes are not looked at while the data are prepared: the validation
reports test outcome rates only as counts, so that the test set remains an independent check, as the brief requires
[1]. Test results will also be reported without the test enrolments that are Withdrawn without a withdrawal day, 89 at
day 13 and 90 at day 27, because such students may have left before the cut-off without a record of it.

**Package layout in full.**

The package follows the layout that the brief recommends [1]: `data/raw/` holds the immutable
raw tables; `data/interim/` the intermediate results that the pipeline can recreate; `data/processed/` the
analytic-ready views; `data/metadata/` the dictionary, lineage, quality logs and validation results; `notebooks/` the
notebooks for data understanding and preparation; and `src/` the scripts.
