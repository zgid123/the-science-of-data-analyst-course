# 6. Data Preparation Pipeline

The pipeline turns the raw files into prepared views with scripts only, so anyone can rerun it and obtain the same
data, as the brief requires [1]. The brief's ten preparation steps are functions of one script, which runs as one of eight scripted stages, and the
stages form five phases from the raw files to the validated package (Appendix II, Figure A.3). Section 6.1 maps the
steps to the code, Section 6.2 covers integration and features, and Section 6.3 sets the split and the leakage controls.
