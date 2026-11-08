# 6. Data Preparation Pipeline

The pipeline turns the raw files into prepared views with scripts only, with no manual step, so that anyone can rerun
it and obtain the same data, as the brief requires [1]. It carries out the decisions of Table 5.1 in the ten steps
that the brief recommends, from loading the raw files to persisting the prepared data with their documentation [1].
Section 6.1 maps the steps to the code and describes the package; Section 6.2 covers the integration of the tables
and the construction of features; and Section 6.3 sets the split into training and test runs and the controls against
leakage.
