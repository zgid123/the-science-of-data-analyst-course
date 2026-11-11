"""AQ1 step 1 – extract the analysis tables from the prepared dataset.

Reads   enrolment.parquet, assessment_due.parquet (OULAD-N04-prepared-1.0, hash-checked)
Writes  extracted-datasets/aq1_enrolments_<scope>.csv        one row per enrolment, descriptive columns only
        extracted-datasets/aq1_task_schedule_<scope>.csv     one row per run and task (TMA/CMA): due day and week
        extracted-datasets/aq1_first_missed_recomputed_<scope>.csv   first missed week re-derived from the task table
"""

import polars as pl

from aq1_common import EXTRACT, lib, scope_args

scope, years = scope_args(__doc__)
lib.banner(f"AQ1 extract, scope = {scope}")
print("prepared dataset:", lib.PREPARED_VERSION, "- hashes:", lib.verify_prepared(["enrolment.parquet", "assessment_due.parquet"]))

enr = lib.load_view("enrolment", years, "aq-1/code/01_extract.py", "AQ1 descriptive rates for the 2014 runs")
keep = lib.KEYS + ["run", "year", "start_month", "final_result", "non_completion", "completed", "enrolled_d14",
                   "enrolled_d27", "date_registration", "date_unregistration", "registration_missing",
                   "withdrawal_day_missing", "unregistered_not_withdrawn", "first_missed_week",
                   "tasks_due_while_enrolled", "tasks_missed_while_enrolled", "gender", "disability", "imd_band",
                   "age_band", "run_length"]
enr = enr.select(keep)
lib.save_csv(enr, EXTRACT / f"aq1_enrolments_{scope}.csv", "all enrolments of the scope")

due = lib.load_view("assessment_due", years, "aq-1/code/01_extract.py", "AQ1 first missed task for the 2014 runs")
schedule = (due.group_by("run", "code_module", "code_presentation", "id_assessment", "assessment_type", "due_day", "due_week")
            .agg(pl.len().alias("enrolments_with_row")).sort("run", "due_day", "id_assessment"))
lib.save_csv(schedule, EXTRACT / f"aq1_task_schedule_{scope}.csv", "task calendar per run")

# Independent re-derivation of first_missed_week: earliest due week among tasks not submitted and due while enrolled.
first = (due.filter((pl.col("status") == "not_submitted") & pl.col("due_while_enrolled"))
         .group_by(lib.KEYS).agg(pl.col("due_week").min().alias("first_missed_week_recomputed"),
                                 pl.col("due_day").min().alias("first_missed_due_day")))
lib.save_csv(first.sort(lib.KEYS), EXTRACT / f"aq1_first_missed_recomputed_{scope}.csv", "enrolments with at least one missed task")

print(f"\nenrolments: {enr.height:,}; runs: {enr['run'].n_unique()}; enrolled at day 14: {int(enr['enrolled_d14'].sum()):,}")
print(f"task rows read: {due.height:,}; tasks in the calendar: {schedule.height}")
