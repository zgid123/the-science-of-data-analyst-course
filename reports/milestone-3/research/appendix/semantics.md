| Field | Meaning | Unit and scale | Known at |
| :---- | :---- | :---- | :---- |
| date_registration, date_unregistration | Days the student registered and unregistered; empty unregistration = did not withdraw | days from the start | the day itself |
| assessments.date | Cut-off (due) day of the assessment | days | from the start of the run |
| date_submitted | Day the student submitted; all 1,909 banked results carry −1, a placeholder | days | the day itself |
| is_banked | Result carried over from an earlier run | 0/1 | registration |
| score | Mark, 0–100; below 40 is a fail | points | TMA: tutor marking, usually within ten working days of the cut-off; CMA: automatic, within 7 days |
| weight | Share of the grade; exams 100, other assessments together 100 | % | from the start |
| sum_click | Number of interactions with one resource on one day | count | the day itself |
| studied_credits | Credits of all modules studied at the same time; 60 a year is part-time, 120 full-time | credits | registration |
