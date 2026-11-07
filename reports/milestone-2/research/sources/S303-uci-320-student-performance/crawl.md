---
id: S303
url: https://archive.ics.uci.edu/dataset/320/student+performance
requested: https://archive.ics.uci.edu/dataset/320/student+performance
fetched: 2026-11-06T01:06+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T06
part: 3
raw: raw.html (258 KB)
conversion: html-text of https://archive.ics.uci.edu/dataset/320/student+performance (readable, 1051 words)
---
title: UCI Machine Learning RepositoryStudent Performance - UCI Machine Learning Repository

-
-

-
-

-

-
-
-

Login

# Student Performance

## Donated on 11/26/2014

Predict student performance in secondary education (high school).

# Dataset Characteristics

Multivariate

# Subject Area

Social Science

# Associated Tasks

Classification, Regression

# Feature Type

Integer

# # Instances

649

# # Features

30

# Dataset Information

Additional Information

This data approach student achievement in secondary education of two Portuguese schools. The data attributes include student grades, demographic, social and school related features) and it was collected by using school reports and questionnaires. Two datasets are provided regarding the performance in two distinct subjects: Mathematics (mat) and Portuguese language (por). In [Cortez and Silva, 2008], the two datasets were modeled under binary/five-level classification and regression tasks. Important note: the target attribute G3 has a strong correlation with attributes G2 and G1. This occurs because G3 is the final year grade (issued at the 3rd period), while G1 and G2 correspond to the 1st and 2nd period grades. It is more difficult to predict G3 without G2 and G1, but such prediction is much more useful (see paper source for more details).

Has Missing Values?

No

# Introductory Paper

Using data mining to predict secondary school student performance
By P. Cortez, A. M. G. Silva. 2008

Published in Proceedings of 5th Annual Future Business Technology Conference

# Variables Table

| Variable Name | Role | Type | Demographic | Description | Units | Missing Values

| school | Feature | Categorical | | student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira) | | no

| sex | Feature | Binary | Sex | student's sex (binary: 'F' - female or 'M' - male) | | no

| age | Feature | Integer | Age | student's age (numeric: from 15 to 22) | | no

| address | Feature | Categorical | | student's home address type (binary: 'U' - urban or 'R' - rural) | | no

| famsize | Feature | Categorical | Other | family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3) | | no

| Pstatus | Feature | Categorical | Other | parent's cohabitation status (binary: 'T' - living together or 'A' - apart) | | no

| Medu | Feature | Integer | Education Level | mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) | | no

| Fedu | Feature | Integer | Education Level | father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education) | | no

| Mjob | Feature | Categorical | Occupation | mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') | | no

| Fjob | Feature | Categorical | Occupation | father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') | | no

Rows per page
0 to 10 of 33

# Additional Variable Information

# Attributes for both student-mat.csv (Math course) and student-por.csv (Portuguese language course) datasets:
1 school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
2 sex - student's sex (binary: 'F' - female or 'M' - male)
3 age - student's age (numeric: from 15 to 22)
4 address - student's home address type (binary: 'U' - urban or 'R' - rural)
5 famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6 Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7 Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
8 Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
9 Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
10 Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
11 reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
12 guardian - student's guardian (nominal: 'mother', 'father' or 'other')
13 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
14 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16 schoolsup - extra educational support (binary: yes or no)
17 famsup - family educational support (binary: yes or no)
18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
19 activities - extra-curricular activities (binary: yes or no)
20 nursery - attended nursery school (binary: yes or no)
21 higher - wants to take higher education (binary: yes or no)
22 internet - Internet access at home (binary: yes or no)
23 romantic - with a romantic relationship (binary: yes or no)
24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 health - current health status (numeric: from 1 - very bad to 5 - very good)
30 absences - number of school absences (numeric: from 0 to 93)

# these grades are related with the course subject, Math or Portuguese:
31 G1 - first period grade (numeric: from 0 to 20)
31 G2 - second period grade (numeric: from 0 to 20)
32 G3 - final grade (numeric: from 0 to 20, output target)

# Dataset Files

| File | Size

| student.zip | 20 KB

| .student.zip_old | 19.6 KB

# Papers Citing this Dataset

Sort by Year, desc

-
-
-
-

The Latent of Student Learning Analytic with K-mean Clustering for Student Behaviour Classification
By Andi Mansur, Norazah Yusof. 2018

Published in Journal of Information Systems Engineering and Business Intelligence.

Adding bias to reduce variance in psychological results: A tutorial on penalized regression
By Nathaniel Helwig. 2017

Published in The Quantitative Methods for Psychology.

Feature Selection based on the Local Lift Dependence Scale
By Diego Marcondes, Adilson Simonis, Junior Barrera. 2017

Published in ArXiv.

Data Mining of Students' Performance : Turkish Students as a Case Study
By Oyebade Oyedotun, Sam Tackie, Ebenezer Olaniyi, Adnan Khashman. 2015

Published in International Journal of Intelligent Systems and Applications.

A Wrapper for Reweighting Training Instances for Handling Imbalanced Data Sets
By M. Karagiannopoulos, D. Anyfantis, Sotiris Kotsiantis, Panayiotis Pintelas. 2007

Published in AIAI.

Rows per page
0 to 5 of 6

Download (39.8 KB)

Install the ucimlrepo package

pip install ucimlrepo

Import the dataset into your code

from ucimlrepo import fetch_ucirepo

# fetch dataset
student_performance = fetch_ucirepo(id=320)

# data (as pandas dataframes)
X = student_performance.data.features
y = student_performance.data.targets

# metadata
print(student_performance.metadata)

# variable information
print(student_performance.variables)

View the full documentation

6 citations

755068 views

Citation

Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T.

Style:

# Creators

Paulo Cortez

# DOI

10.24432/C5TG7T

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
