# Prompt: Download and Setup 7 Educational Benchmark Datasets

Copy and paste the prompt below to your AI coding assistant (Antigravity, Cursor, Claude, ChatGPT, etc.) to automatically download, extract, and verify all 7 education datasets for the final project.

---

```markdown
Please download, extract, and organize the following 7 educational benchmark datasets into `the-science-of-data-analyst-course/final-project/datasets/`:

### 1. OULAD (Open University Learning Analytics Dataset)
- Target Folder: `datasets/oulad/`
- Direct Download URL: `https://ndownloader.figshare.com/files/8606371`
- Action: Download `anonymisedData.zip`, unzip to extract all 7 CSV tables:
  - `courses.csv`
  - `assessments.csv`
  - `vle.csv`
  - `studentInfo.csv`
  - `studentRegistration.csv`
  - `studentAssessment.csv`
  - `studentVle.csv` (433 MB clickstream log)

### 2. FFF Dataset (OULAD Benchmark STEM Module)
- Target Folder: `datasets/fff/`
- Context: In educational data mining and learning analytics research, module `FFF` is the benchmark STEM course in OULAD across 4 cohorts (2013B, 2013J, 2014B, 2014J) with 7,762 students.
- Action: Write and execute a Python script to filter OULAD's tables for `code_module == 'FFF'` (and corresponding assessment and VLE site IDs) and output the filtered CSVs into `datasets/fff/`:
  - `courses.csv` (4 cohorts)
  - `assessments.csv` (52 assessments)
  - `vle.csv` (1,967 learning activities)
  - `studentInfo.csv` (7,762 students)
  - `studentRegistration.csv` (7,762 registrations)
  - `studentAssessment.csv` (54,815 assessment results)
  - `studentVle.csv` (4,014,499 clickstream interactions)

### 3. EdNet (Santa AI Tutoring Platform)
- Target Folder: `datasets/ednet/`
- Prerequisites: Requires `gdown` (`pip install gdown`).
- Action:
  - **Contents Metadata**: Download using `python3 -m gdown --id 117aYJAWG3GU48suS66NPaB82HwFj6xWS -O contents.zip` and unzip to extract `questions.csv`, `lectures.csv`, `payments.csv`, `coupons.csv`.
  - **KT1 Student Response Logs**: Download using `python3 -m gdown --id 1AmGcOs5U31wIIqvthn9ARqJMrMTFTcaw -O ednet_kt1.zip` and unzip into `KT1/` (contains 784,309 student sequence CSVs: `u{user_id}.csv`).

### 4. MOOCCubeX (Tsinghua University / XuetangX)
- Target Folder: `datasets/mooccubex/`
- Base CDN: `https://lfs.aminer.cn/misc/moocdata/data/mooccube2/`
- Action:
  - Clone repository: `git clone https://github.com/THU-KEG/MOOCCubeX.git mooccubex`
  - Download core entities into `mooccubex/data/entities/`:
    - `course.json` (43 MB)
    - `teacher.json` (8.7 MB)
    - `school.json` (613 KB)
  - Download core relations into `mooccubex/data/relations/`:
    - `course-field.json`, `course-teacher.txt`, `concept-course.txt`, `concept-other.txt`, `concept-problem.txt`, `concept-comment.txt`, `user-xiaomu.json`, `user-reply.txt`, `comment-reply.txt`.

### 5. College Scorecard (U.S. Department of Education)
- Target Folder: `datasets/college-scorecard/`
- Action: Download and unzip:
  - Institutional Data: `https://ed-public-download.scorecard.network/downloads/Most-Recent-Cohorts-Institution_06102026.zip` (extracts `Most-Recent-Cohorts-Institution.csv`, 95 MB)
  - Field-of-Study Data: `https://ed-public-download.scorecard.network/downloads/Most-Recent-Cohorts-Field-of-Study_06102026.zip` (extracts `Most-Recent-Cohorts-Field-of-Study.csv`, 146 MB)

### 6. PISA 2022 (OECD)
- Target Folder: `datasets/pisa-2022/`
- Direct File Server Base: `https://webfs.oecd.org/pisa2022/` (use `webfs.oecd.org` directly to avoid Cloudflare bot protection on the main OECD website).
- Action: Download and unzip:
  - School Questionnaire: `https://webfs.oecd.org/pisa2022/SCH_QQQ_SPSS.zip` (extracts `CY08MSP_SCH_QQQ.SAV`, 19 MB)
  - Teacher Questionnaire: `https://webfs.oecd.org/pisa2022/TCH_QQQ_SPSS.zip` (extracts `CY08MSP_TCH_QQQ.SAV`, 101 MB)
  - Socioeconomic Trends: `https://webfs.oecd.org/pisa2022/escs_trend.zip` (extracts `escs_trend.csv`, 74 MB)

### 7. TALIS 2024 (OECD)
- Target Folder: `datasets/talis-2024/`
- Direct File Server Base: `https://webfs.oecd.org/talis/2024/core/` (use `webfs.oecd.org` directly).
- Action: Download and unzip:
  - Principal Questionnaires (CSV): `https://webfs.oecd.org/talis/2024/core/TALIS2024_principals_NoESE_CSV.zip` (extracts `acgintt4.csv`, `bcgintt4.csv`, `ccgintt4.csv`, `tcgintt4.csv`)
  - Teacher Questionnaires (CSV): `https://webfs.oecd.org/talis/2024/core/TALIS2024_teachers_NoESE_CSV.zip` (extracts `atgintt4.csv`, `btgintt4.csv`, `ctgintt4.csv`, `ttgintt4.csv`, 1.2 GB uncompressed)
- *Optimization Tip:* Because `webfs.oecd.org` throttles single HTTP connections to ~60 KB/s, use a multi-threaded HTTP Range request script with 8–16 workers to accelerate the 150 MB teacher archive download.

### Final Verification
When finished, print an inventory of all 7 datasets showing file counts, paths, and total sizes to confirm they are all non-empty and valid.
```
