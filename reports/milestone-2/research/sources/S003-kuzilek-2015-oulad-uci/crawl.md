---
id: S003
url: https://archive.ics.uci.edu/dataset/349/open+university+learning+analytics+dataset
requested: https://archive.ics.uci.edu/dataset/349/open+university+learning+analytics+dataset
fetched: 2026-11-02T00:46+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T03
part: 1
raw: raw.html (76 KB)
conversion: html-text of https://archive.ics.uci.edu/dataset/349/open+university+learning+analytics+dataset (readable, 348 words)
---
title: UCI Machine Learning RepositoryOpen University Learning Analytics dataset - UCI Machine Learning Repository

-
-

-
-

-

-
-
-

Login

# Open University Learning Analytics dataset

## Donated on 12/20/2015

Open University Learning Analytics Dataset contains data about courses, students and their interactions with Virtual Learning Environment for seven selected courses and more than 30000 students.

# Dataset Characteristics

Multivariate, Sequential, Time-Series

# Subject Area

Computer Science

# Associated Tasks

Classification, Regression, Clustering

# Feature Type

Integer

# # Instances

-

# # Features

-

# Dataset Information

Additional Information

Open University Learning Analytics Dataset (OULAD) contains data about courses, students and their interactions with Virtual Learning Environment (VLE) for seven selected courses (called modules). Presentations of courses start in February and October - they are marked by 'B' and 'J' respectively. The dataset consists of tables connected using unique identifiers. Dataset is stored in several csv files. More information, examples and news can be found at: https://analyse.kmi.open.ac.uk/open_dataset

Has Missing Values?

Yes

# Variable Information

see description file

# Dataset Files

| File | Size

| studentVle.csv | 432.8 MB

| studentAssessment.csv | 5.4 MB

| studentInfo.csv | 3.3 MB

| studentRegistration.csv | 1.1 MB

| vle.csv | 264.3 KB

Rows per page
0 to 5 of 8

Download (44.6 MB)

Install the ucimlrepo package

pip install ucimlrepo

Import the dataset into your code

from ucimlrepo import fetch_ucirepo

# fetch dataset
open_university_learning_analytics_dataset = fetch_ucirepo(id=349)

# data (as pandas dataframes)
X = open_university_learning_analytics_dataset.data.features
y = open_university_learning_analytics_dataset.data.targets

# metadata
print(open_university_learning_analytics_dataset.metadata)

# variable information
print(open_university_learning_analytics_dataset.variables)

View the full documentation

0 citations

30112 views

Citation

Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2015). Open University Learning Analytics dataset [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5KK69.

Style:

# Creators

Jakub Kuzilek

Martin Hlosta

Zdenek Zdrahal

# DOI

10.24432/C5KK69

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

<!-- fetch 2: https://web.archive.org/web/2id_/https://analyse.kmi.open.ac.uk/open_dataset | fetch.py html-text | 2026-11-02T00:52+07:00 | unreadable -->
No readable copy was found. Attempts:
- L1 https://research.stem.open.ac.uk/ouanalyse/: unreadable (exploded layout (40% of lines have ≤2 characters))
- L3 https://web.archive.org/web/2id_/https://analyse.kmi.open.ac.uk/open_dataset: unreadable (exploded layout (40% of lines have ≤2 characters))
