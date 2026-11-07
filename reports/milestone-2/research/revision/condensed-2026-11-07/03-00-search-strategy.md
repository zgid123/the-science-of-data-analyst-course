# 3. Open Dataset Search Strategy

The search started from the requirements of Section 2, not from datasets already known to the team. Its keywords came
from the requirement matrix: student completion, dropout and withdrawal; learning-management or virtual learning
environment interaction; assessment submission; clickstream; higher education; learning analytics; and massive open online course (MOOC) dropout.
The search covered the sources the brief suggests [1], the University of California, Irvine (UCI) Machine Learning Repository, data repositories with
DOIs (figshare, Harvard Dataverse, Zenodo), the provider pages of research groups and general web search. Three rules
applied to every hit: read the documentation and license before judging the data; trace a dataset found on Kaggle, a
blog or a mirror back to its provider; and reject re-uploads without provenance [1].

The search log in Appendix I records 16 queries and hits, including the rejected ones: copies of a descriptor already
held, superseded addresses, third-party re-uploads of the KDD Cup 2015 data and secondary metadata. Seven candidates
remained, each documented from its official page or descriptor; Table 3.1 summarises them.

**Table 3.1. Candidate open datasets**

| Candidate | Provider and source | Population | Unit | Outcome | Timing within the course |
| :---- | :---- | :---- | :---- | :---- | :---- |
| A. OULAD | The Open University (UK); provider page, data descriptor [2], [3] | Seven distance-learning modules, 2013–2014 [3] | Student–module–run [3] | Final result with Withdrawal and a dated unregistration [3] | Assessment cut-off and submission days; daily clicks [3] |
| B. UCI 697 Dropout and Academic Success | Polytechnic Institute of Portalegre; UCI and descriptor [4], [5] | Undergraduates of one institution, 2008–2019 [5] | Student [4] | Degree dropout, enrolled or graduate [4] | Semester aggregates only [5] |
| C. UCI 320 Student Performance | Two Portuguese secondary schools; UCI [6] | Secondary pupils [6] | Student–subject [6] | Grade 0–20 [6] | Three period grades [6] |
| D. UCI 856 Higher Education Students Performance Evaluation | One 2019 collection; UCI [7] | Two faculties' students [7] | Questionnaire [7] | Letter grade [7] | None [7] |
| E. XuetangX MOOC dropout data | Tsinghua University, MOOCData [8], [9] | Chinese MOOC users, 2015–2017 [8] | User–course [8] | Binary dropout [8] | Timestamped actions [8] |
| F. HarvardX Person-Course 2013 | HarvardX, Harvard Dataverse [10] | HarvardX learners, 2012–2013 [10] | Person–course aggregate [10] | Certification | First and last event only [10] |
| G. xAPI-Edu-Data | Kalboard 360 data, authors' Kaggle listing [11] | Students of several countries [11] | Student [11] | Grade band [11] | None documented |
