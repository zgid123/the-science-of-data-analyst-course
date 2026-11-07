---
id: S304
url: https://archive.ics.uci.edu/dataset/856/higher+education+students+performance+evaluation
requested: https://archive.ics.uci.edu/dataset/856/higher+education+students+performance+evaluation
fetched: 2026-11-06T01:06+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T06
part: 3
raw: raw.html (217 KB)
conversion: html-text of https://archive.ics.uci.edu/dataset/856/higher+education+students+performance+evaluation (readable, 706 words)
---
title: UCI Machine Learning RepositoryHigher Education Students Performance Evaluation - UCI Machine Learning Repository

-
-

-
-

-

-
-
-

Login

# Higher Education Students Performance Evaluation

## Donated on 8/14/2023

The data was collected from the Faculty of Engineering and Faculty of Educational Sciences students in 2019. The purpose is to predict students' end-of-term performances using ML techniques.

# Dataset Characteristics

Multivariate

# Subject Area

Social Science

# Associated Tasks

Classification

# Feature Type

Integer

# # Instances

145

# # Features

31

# Dataset Information

For what purpose was the dataset created?

The purpose is to predict students' end-of-term performances using ML techniques.

Additional Information

1-10 of the data are the personal questions, 11-16. questions include family questions, and the remaining questions include education habits.

Has Missing Values?

No

# Introductory Paper

Student Performance Classification Using Artificial Intelligence Techniques
By N. Yilmaz, B. Şekeroğlu. 2019

Published in Advances in Intelligent Systems and Computing, vol 1095

# Variables Table

| Variable Name | Role | Type | Demographic | Description | Units | Missing Values

| Student Age | Feature | Categorical | Age | 1: 18-21, 2: 22-25, 3: above 26 | | no

| Sex | Feature | Binary | Sex | 1: female, 2: male | | no

| Graduated high-school type | Feature | Categorical | Education Level | 1: private, 2: state, 3: other | | no

| Scholarship type | Feature | Categorical | | 1: None, 2: 25%, 3: 50%, 4: 75%, 5: Full | | no

| Additional work | Feature | Binary | | 1: Yes, 2: No | | no

| Regular artistic or sports activity | Feature | Binary | | 1: Yes, 2: No | | no

| Do you have a partner | Feature | Binary | Marital Status | 1: Yes, 2: No | | no

| Total salary if available | Feature | Categorical | Income | 1: USD 135-200, 2: USD 201-270, 3: USD 271-340, 4: USD 341-410, 5: above 410 | | no

| Transportation to the university | Feature | Categorical | | 1: Bus, 2: Private car/taxi, 3: bicycle, 4: Other | | no

| Accomodation type in Cyprus | Feature | Categorical | | 1: rental, 2: dormitory, 3: with family, 4: Other | | no

Rows per page
0 to 10 of 33

# Additional Variable Information

Class Labels

Student ID
1- Student Age (1: 18-21, 2: 22-25, 3: above 26)
2- Sex (1: female, 2: male)
3- Graduated high-school type: (1: private, 2: state, 3: other)
4- Scholarship type: (1: None, 2: 25%, 3: 50%, 4: 75%, 5: Full)
5- Additional work: (1: Yes, 2: No)
6- Regular artistic or sports activity: (1: Yes, 2: No)
7- Do you have a partner: (1: Yes, 2: No)
8- Total salary if available (1: USD 135-200, 2: USD 201-270, 3: USD 271-340, 4: USD 341-410, 5: above 410)
9- Transportation to the university: (1: Bus, 2: Private car/taxi, 3: bicycle, 4: Other)
10- Accommodation type in Cyprus: (1: rental, 2: dormitory, 3: with family, 4: Other)
11- Mothersâ€™ education: (1: primary school, 2: secondary school, 3: high school, 4: university, 5: MSc., 6: Ph.D.)
12- Fathersâ€™ education: (1: primary school, 2: secondary school, 3: high school, 4: university, 5: MSc., 6: Ph.D.)
13- Number of sisters/brothers (if available): (1: 1, 2:, 2, 3: 3, 4: 4, 5: 5 or above)
14- Parental status: (1: married, 2: divorced, 3: died - one of them or both)
15- Mothersâ€™ occupation: (1: retired, 2: housewife, 3: government officer, 4: private sector employee, 5: self-employment, 6: other)
16- Fathersâ€™ occupation: (1: retired, 2: government officer, 3: private sector employee, 4: self-employment, 5: other)
17- Weekly study hours: (1: None, 2: <5 hours, 3: 6-10 hours, 4: 11-20 hours, 5: more than 20 hours)
18- Reading frequency (non-scientific books/journals): (1: None, 2: Sometimes, 3: Often)
19- Reading frequency (scientific books/journals): (1: None, 2: Sometimes, 3: Often)
20- Attendance to the seminars/conferences related to the department: (1: Yes, 2: No)
21- Impact of your projects/activities on your success: (1: positive, 2: negative, 3: neutral)
22- Attendance to classes (1: always, 2: sometimes, 3: never)
23- Preparation to midterm exams 1: (1: alone, 2: with friends, 3: not applicable)
24- Preparation to midterm exams 2: (1: closest date to the exam, 2: regularly during the semester, 3: never)
25- Taking notes in classes: (1: never, 2: sometimes, 3: always)
26- Listening in classes: (1: never, 2: sometimes, 3: always)
27- Discussion improves my interest and success in the course: (1: never, 2: sometimes, 3: always)
28- Flip-classroom: (1: not useful, 2: useful, 3: not applicable)
29- Cumulative grade point average in the last semester (/4.00): (1: <2.00, 2: 2.00-2.49, 3: 2.50-2.99, 4: 3.00-3.49, 5: above 3.49)
30- Expected Cumulative grade point average in the graduation (/4.00): (1: <2.00, 2: 2.00-2.49, 3: 2.50-2.99, 4: 3.00-3.49, 5: above 3.49)
31- Course ID
32- OUTPUT Grade (0: Fail, 1: DD, 2: DC, 3: CC, 4: CB, 5: BB, 6: BA, 7: AA)

# Dataset Files

| File | Size

| DATA (1).csv | 10.8 KB

Download (2.2 KB)

Install the ucimlrepo package

pip install ucimlrepo

Import the dataset into your code

from ucimlrepo import fetch_ucirepo

# fetch dataset
higher_education_students_performance_evaluation = fetch_ucirepo(id=856)

# data (as pandas dataframes)
X = higher_education_students_performance_evaluation.data.features
y = higher_education_students_performance_evaluation.data.targets

# metadata
print(higher_education_students_performance_evaluation.metadata)

# variable information
print(higher_education_students_performance_evaluation.variables)

View the full documentation

1 citations

89336 views

Citation

Yilmaz, N. & Şekeroğlu, B. (2019). Higher Education Students Performance Evaluation [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C51G82.

Style:

# Keywords

education

# Creators

Nevriye Yilmaz

nevriye.yilmaz@neu.edu.tr

Boran Şekeroğlu

boran.sekeroglu@neu.edu.tr

# DOI

10.24432/C51G82

# License

This dataset is licensed under a
Creative Commons Attribution 4.0 International
(CC BY 4.0) license.

This allows for the sharing and adaptation of the datasets for any purpose,
provided that the appropriate credit is given.

By using the UCI Machine Learning Repository,
you acknowledge and accept the cookies and privacy practices used by the UCI Machine Learning Repository.

Read Policy

- Browse Datasets
- Donate a Dataset
- Link an external Dataset
-
- Who We Are
- Citation Metadata
- Contact Information
-
- Login
