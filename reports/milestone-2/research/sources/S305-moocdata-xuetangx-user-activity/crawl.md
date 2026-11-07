---
id: S305
url: http://moocdata.cn/data/user-activity
requested: http://moocdata.cn/data/user-activity
fetched: 2026-11-06T01:07+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T06
part: 3
raw: raw.html (12 KB)
conversion: html-text of http://moocdata.cn/data/user-activity (readable, 457 words)
---
title: MoocData

-

-
-

-

| Name
| Size
| Keywords
| Download link
| Reference

| tracking log (201508-201608)
| 1048 MB
| Activity Log
| data
| AAAI'19

| Tracking Log (201608-201708)
| 583 MB
| Activity Log
| data
| AAAI'19

| Dropout Prediction Dataset
| 299 MB
| Dropout Prediction Dataset
| data
| AAAI'19

| User Profile
| 112 MB
| User Profile
| data
| AAAI'19

| Course Information
| 527 KB
| Course Information
| data
| AAAI'19

| KDDCUP Data
| 158 MB
| KDDCUP Data
| data
| AAAI'19

#### User Activity

These files are the datasets used in the paper "Understanding Dropouts in MOOCs" in AAAI 2019.

Tracking log files (201508-201608, 201608-201708) include all users' learning activities in XuetangX platform from 201508 to 201708. These logs are the supporting data of the analyses in the paper.

Dropout prediction dataset includes the training set and test set used in the paper for the dropout prediction task.

User profile is the information of XuetangX users, including gender, birth year and education level.

Course information includes course start date, course end date, course category and course type.

Tracking log:

Each json file includes user tracking log in a specific period. For example, 20150801-20151101-raw_user_activity.json is the tracking log from 20150801 to 20151101.

The format of these json files is as follow:

Each json file includes user tracking log in a specific period. For example, 20150801-20151101-raw_user_activity.json is the tracking log from 20150801 to 20151101. The format of these json files is as follow:

[

    [course_id,

        {user_id:

            { session_id:

                [

                    [activity_event_1, time_1],

                    [activity_event_2, time_2],

                ... ],

            ... },

        ...}

    ],

...]

Dropout Prediction Dataset:

train_log.csv, test_log.csv:

1st column: enroll_id, the id of (user, course) pair.

2nd column: username, the id of user.

3rd column: course_id, the id of course.

4th column: session_id, the id of session.

5th column: action, the type of user activity.

6th column: object, the corresonding object of the action.

7th column: time, the occurence time of the action.

train_truth.csv, test_truth.csv:

1st column: enroll_id, the id of (user, course) pair

2nd column: truth, the label of user's dropout (1: dropout, 0: non-dropout).

User Profile:

1st column: user_id, the id of user.

2nd column: gender, the gender of user.

3st column: education, user's education level.

4th column: birth, user's birth year.

Course Information:

1st column: id, the id (number) of course, which is used in dropout prediction dataset.

2nd column: course_id, the id (string) of course, which is used in tracking log.

3st column: start, course start time.

4th column: end, course end time.

5th column: course_type, course mode (0: instructor-paced course, 1: self-paced course).

6th column: category, the category of course.

KDDCUP Data:

The full dataset of KDDCUP 15, details can be found in KDDCUP 2015.

#### Reference

@inproceedings{feng2019dropout,

    title={Understanding Dropouts in MOOCs},

    author={Wenzheng Feng and Jie Tang and Tracy Xiao Liu and Shuhuai Zhang and Jian Guan},

    booktitle={Proceedings of the 33rd AAAI Conference on Artificial Intelligence},

    year={2019}

}

© 2020 Tsinghua University 京ICP备19000880号-1
