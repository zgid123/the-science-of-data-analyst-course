## 2.2. Outcome, Time and Measurement Semantics

**Outcome.** The outcome is final_result, recorded at the end of each run as Pass (12,361 enrolments), Withdrawn
(10,156), Fail (7,052) or Distinction (3,024); the data descriptor calls the withdrawn value "Withdrawal" [2]. It is
a real outcome, not a proxy, but it is observed only when the run ends, so every feature must be dated before the
moment of prediction. Non-completion, the target of AQ1 to AQ3, is a final result of Fail or Withdrawn, and
completion is Pass or Distinction, which matches the proposal's definition of completion as passing the course.

**Time.** Time is a count of days from day 0, the official start of the run. Students may register from a few months
before the start until two weeks after it [2], so negative days are valid and mean "before the start". Week n covers
days 7(n−1) to 7n−1, so week 1 is days 0 to 6. On this scale the two data cut-offs fall on day 13, the end of week 2,
and day 27, the end of week 4. Each date field has its own meaning: the registration and unregistration days record
when a student joined and left, an empty unregistration day means the student did not withdraw, the assessment date
is the task's due day, which the OU calls its cut-off date [2], and the submission day records when the student
submitted. A field may only feed a prediction once it is known, and Appendix I (Table A.2) gives the meaning, unit
and moment of knowledge of every key field.

**Measures.** Three issues need care before the fields become measures (Appendix I): the 1,909 banked results, carried
over from an earlier run, carry the placeholder submission day −1 and cannot time a submission; OULAD holds no day on
which a mark was released, while a TMA mark usually returns within ten working days and a CMA score within 7 days
under the OU's policy of 2025 [3]; and coursework weighs zero in the GGG runs, while studied credits count every
module taken at once [2], 60 a year being part-time and 120 full-time study [4].
