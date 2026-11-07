# 3. Open Dataset Search Strategy

**Where the search started.** The search started from the requirements of Section 2, not from datasets already known
to the team, so that the questions decided what was looked for [1]. Its keywords came from the requirement matrix:
student completion, dropout and withdrawal; interaction with a learning management system or virtual learning
environment (VLE), the online platform on which students open materials and submit work; assessment submission;
clickstream, the record of each click a student makes on such a platform; higher education; learning analytics; and
massive open online course (MOOC) dropout.

**Where the team searched.** The search covered the sources the brief suggests [1]; the University of California,
Irvine (UCI) Machine Learning Repository; data repositories that assign a digital object identifier (DOI), a permanent
reference to a dataset, such as figshare, Harvard Dataverse and Zenodo; the pages of the research groups that publish
datasets; and general web search.

**Three rules for every hit.** Three rules applied to every dataset found, as the brief asks [1]. First, the team read
the documentation and the license before judging the data. Second, a dataset found on Kaggle, a blog or another
copy was traced back to the provider that published it. Third, re-uploads without a known origin were rejected.

**What the search found.** The search log in Appendix I records 16 queries and the hits each produced, including the
rejected ones: copies of a data descriptor already held, superseded web addresses, third-party re-uploads of the KDD
Cup 2015 data and secondary descriptions of datasets. Seven candidates remained, more than the three the brief
requires, each documented from its official page or descriptor. Table 3.1 summarises them: who provides each, which
population it describes, its unit of analysis, its outcome and how it records time within a course.

**Table 3.1. Candidate open datasets**

| Candidate | Provider and source | Population | Unit | Outcome | Timing within the course |
| :---- | :---- | :---- | :---- | :---- | :---- |
| A. OULAD | The Open University (UK); provider page and data descriptor [2], [3] | Students of seven distance-learning modules, 2013–2014 [3] | Student–module–run [3] | Final result, including Withdrawal with a dated unregistration [3] | Assessment due and submission days; daily clicks [3] |
| B. UCI 697 Dropout and Academic Success | Polytechnic Institute of Portalegre; UCI page and descriptor [4], [5] | Undergraduates of one institution, 2008–2019 [5] | Student [4] | Degree dropout, still enrolled, or graduate [4] | Semester totals only [5] |
| C. UCI 320 Student Performance | Two Portuguese secondary schools; UCI page [6] | Secondary-school pupils [6] | Student–subject [6] | Grade from 0 to 20 [6] | Three grades per school year [6] |
| D. UCI 856 Higher Education Students Performance Evaluation | One collection in 2019; UCI page [7] | Students of two faculties [7] | Questionnaire answer [7] | Letter grade [7] | None [7] |
| E. XuetangX MOOC dropout data | Tsinghua University, MOOCData [8], [9] | Users of a Chinese MOOC platform, 2015–2017 [8] | User–course [8] | Dropout, yes or no [8] | Timestamped actions [8] |
| F. HarvardX Person-Course 2013 | HarvardX, Harvard Dataverse [10] | HarvardX learners, 2012–2013 [10] | Person–course summary [10] | Certification | Only the first and last activity [10] |
| G. xAPI-Edu-Data | Data from the Kalboard 360 platform; the authors' Kaggle listing [11] | Students of several countries [11] | Student [11] | Grade band [11] | None documented |

The table already shows the main difference between the candidates. Only OULAD and the XuetangX data record when
students did things within a course, which AQ2 and AQ3 need, and only OULAD combines that timing with an outcome that
includes withdrawal and with dated assessments. Section 4 tests this impression against the gates and the brief's
criteria.
