---
id: S309
url: https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data
requested: https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data
fetched: 2026-11-06T01:16+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: partial
task: T06
part: 3
raw: none
conversion: html-text of https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data (unreadable, 6 words)
---
No readable copy was found. Attempts:
- L1 https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data: unreadable (almost no text (6 words))

<!-- fetch 2: https://www.kaggle.com/api/v1/datasets/view/aljarah/xAPI-Edu-Data | fetch.py json-metadata | 2026-11-06T01:16+07:00 | unreadable -->
No readable copy was found. Attempts:
- L1 https://www.kaggle.com/api/v1/datasets/view/aljarah/xAPI-Edu-Data: unreadable (few letters or digits (0% alphanumeric, 0% letters))

<!-- fetch 3: https://www.kaggle.com/api/v1/datasets/view/aljarah/xAPI-Edu-Data | WebFetch (L5) | 2026-11-06T01:17+07:00 | partial -->
tool: WebFetch
fetch_prompt: "Return verbatim, word for word, the values of licenseNameNullable, creatorNameNullable, and the full descriptionNullable text (dataset information, number of instances and attributes, date, source, semesters, feature categories, class labels, and the papers to cite). Keep the wording exact."

**licenseNameNullable:** CC BY-SA 4.0

**creatorNameNullable:** Ibrahim Aljarah

I can't reproduce the full description verbatim because quotes from source documents are limited to 125 characters. Here is a summary of its contents:

- **Dataset:** Students' Academic Performance Dataset (xAPI-Edu-Data), collected from the Kalboard 360 learning management system using the xAPI learner activity tracker. The source is Elaf Abu Amrieh, Thair Hamtini, and Ibrahim Aljarah at the University of Jordan.
- **Size:** 480 instances and 16 attributes, with no missing values. The data is for classification tasks. A date of 2016-11-8 is listed.
- **Feature categories:** Demographic (such as gender and nationality), academic background (such as educational stage, grade level, and section), and behavioral (such as raised hands, resource visits, and parent survey responses).
- **Semesters:** 245 records come from the first semester and 235 from the second.
- **Class labels:** Students are grouped by total grade into Low-Level (0 to 69), Middle-Level (70 to 89), and High-Level (90 to 100).
- **Citations:** The description asks users to cite two papers by Amrieh, Hamtini, and Aljarah, from 2016 and 2015.

<!-- fetch 4: https://www.kaggle.com/api/v1/datasets/view/aljarah/xAPI-Edu-Data | WebFetch (L5) | 2026-11-06T01:17+07:00 | partial -->
tool: WebFetch
fetch_prompt: "Quote exactly, each as a separate short quote under 120 characters, copied character for character from descriptionNullable: (1) the line starting 'Number of Instances', (2) the line starting 'Number of Attributes', (3) the line starting 'Date:', (4) the sentence starting 'This is an educational data set which is collected from', (5) the sentence about how many records are from the first and second semester, (6) the sentence about the nationality or countries of students, (7) the sentence defining the classes Low-Level, Middle-Level, High-Level, (8) the line naming the source authors, (9) the first words of each citation requested (title of each paper). Do not paraphrase."

1. "Number of Instances: 480"
2. "Number of Attributes: 16"
3. "Date: 2016-11-8"
4. "This is an educational data set which is collected from learning management system (LMS) called Kalboard 360."
5. "245 student records are collected during the first semester" and "235 student records are collected during the second semester."
6. "The students come from different origins such as 179 students are from Kuwait, 172 students are from Jordan,"
7. "Low-Level: interval includes values from 0 to 69," "Middle-Level: interval includes values from 70 to 89," and "High-Level: interval includes values from 90-100."
8. "Elaf Abu Amrieh, Thair Hamtini, and Ibrahim Aljarah, The University of Jordan, Amman, Jordan,"
9. Citation titles:
   - "Mining Educational Data to Predict Student’s academic Performance using Ensemble Methods"
   - "Preprocessing and analyzing educational data set using X-API for improving student's performance"
