# 3. Data Profiling and Quality

Data understanding must rest on evidence from the data, and the brief lists ten aspects to examine: shape and schema,
missingness, duplicates and key integrity, validity and consistency, distributions, outliers, the balance of the
outcome, temporal coverage, join integrity and representativeness [1]. The profile covers all ten. It ran on all 10.9
million rows of the seven raw tables rather than on a sample, so no rare pattern is missed, and it is written by the
second script of the package, `src/02_profile.py`, to `data/metadata/profile.json`. To guard against an error in that
script, thirteen of its figures were recounted from the same raw files by separate code, our exploration of
the dataset, and all thirteen agree (Appendix I, Table A.5).

Sections 3.1 to 3.4 report the findings by aspect, and each finding that needs a decision receives an issue
identifier, DQ01 to DQ19. Section 3.5 gathers the nineteen issues into the Data Quality Issue Log, with the evidence,
the impact on the questions, a severity and the decision taken.
