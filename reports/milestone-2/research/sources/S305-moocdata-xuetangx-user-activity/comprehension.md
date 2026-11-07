# S305 – MOOCData: User Activity datasets (XuetangX; Tsinghua University)

## Summary in my own words

The MOOCData site of Tsinghua University distributes the XuetangX data used in the AAAI 2019 paper "Understanding Dropouts in MOOCs" (S306): two raw tracking logs (August 2015 to August 2017, about 1.6 GB of JSON), a dropout prediction dataset (299 MB: timestamped action logs per enrolment plus a binary dropout label), user profiles (gender, birth year, education level), course information (start and end dates, instructor-paced or self-paced) and the full KDD Cup 2015 data (158 MB). The unit of the prediction set is a user–course enrolment; the label is dropout against non-dropout, so pass and fail are not separated. The page states no licence or terms of use and no anonymisation statement; it only asks users to cite the AAAI paper.

## Key facts

- Provenance – "These files are the datasets used in the paper" (the AAAI 2019 paper, S306)
- Period and platform – "Tracking log files (201508-201608, 201608-201708) include all users' learning activities in XuetangX platform from 201508 to 201708."
- Unit – "1st column: enroll_id, the id of (user, course) pair."
- Timestamped actions – "7th column: time, the occurence time of the action."
- Binary label – "2nd column: truth, the label of user's dropout (1: dropout, 0: non-dropout)."
- Profile attributes – "User profile is the information of XuetangX users, including gender, birth year and education level."
- Course dates – "Course information includes course start date, course end date, course category and course type."
- Course mode – "5th column: course_type, course mode (0: instructor-paced course, 1: self-paced course)."
- Sizes – "| Dropout Prediction Dataset" with "| 299 MB"
- KDD Cup 2015 copy – "The full dataset of KDDCUP 15, details can be found in KDDCUP 2015."
- Ownership line – "© 2020 Tsinghua University"

## Used in

03-00-search-strategy.md, 04-02-selection-matrix.md, 11-01-search-log.md

## Against reference.md

Not in brief section 13; extends the search with a MOOC dropout source. No licence is shown, which conflicts with the brief's rule that a dataset needs clear terms of use (section 7).

## Reliability

Primary; the data provider's own page (Tsinghua University, KEG group / XuetangX); accessed 2026-11-06. Licence and anonymisation not stated.

## Open questions

The definition of dropout (window of inactivity) is not on the page and the paper's full text could not be read (S306 abstract only). No licence or terms; reuse rights must be confirmed with the provider before use.
