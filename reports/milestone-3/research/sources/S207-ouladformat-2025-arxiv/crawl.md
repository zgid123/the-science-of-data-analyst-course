---
id: S207
url: https://arxiv.org/html/2501.08366
requested: arXiv:2501.08366
fetched: 2026-11-06T08:27+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T05
part: 3
raw: raw.html (435 KB)
conversion: html-text of https://arxiv.org/html/2501.08366 (readable, 4820 words)
---
title: ouladFormat R Package: Preparing the Open University Learning Analytics Dataset for Analysis

Skip to main content

#####

Why HTML?

Back to Abstract

Download PDF

-
-
-

-
-
-
-
-

-

-
-

-
-
-

License: CC BY 4.0

arXiv:2501.08366v2 [stat.CO] 16 Jan 2025

# ouladFormat R Package: Preparing the Open University Learning Analytics Dataset for Analysis

Emma Howard

Affiliation: Trinity College Dublin

Email: emhoward@tcd.ie

###### Abstract

Analysing educational data sets is fundamental to many fields of research focusing on improving student learning. However, large educational data sets are complex and can involve intensive preprocessing. These obstacles can be overcome through the development of educational tools which simplifies the preprocessing stages of analysis. The Open University Learning Analytics Dataset (OULAD), available online, contains data from 32,593 students across 22 module presentations at the Open University. This paper introduces the R software package ouladFormat; which loads and formats the OULAD for data analysis. The paper summarizes the ouladFormat R package and explains the different functions within the package. In addition, two case studies are provided which discuss how the OULAD and ouladFormat R package could be used when preparing for an educational study, and in the early identification of at-risk students. The package increases the accessibility of the OULAD for researchers, practitioners, and educators, and supports reproducibility and comparability of educational studies.

## 1 Introduction

Educational research is broadly defined as seeking ‘to describe, understand, and explain how learning takes place throughout a person’s life and how formal and informal contexts of education affect all forms of learning’ (American Educational Research Association, (\bibnodate)). A number of different areas of educational research have developed; each with their own specific goals, methodologies or population of interest. Those which focus on analysing, acquiring or harnessing insights from educational data sets include Academic Analytics, Educational Data Science, Educational Data Mining, and Learning Analytics (LA). For example, Motz et al. ((2023), p. 1) set forth the criteria of LA research to be research which uses data from learners engaged in education systems, which measures student learning, and improves the learning environments. Furthermore, Motz et al. ((2023)) analysed LA research from two main sources of publication, the Learning Analytics and Knowledge (LAK) conference and the Journal of Learning Analytics, to see if the studies were meeting these criteria. They found that 37.4% of studies reviewed did not analyze data from learners in an education system.

To further the education field, it is essential that researchers and practitioners have access to real learner data. Mihaescu & Popescu ((2021)) identified 41 publicly available educational data sets. These include the Student Performance Dataset (Cortez & Silva, (2008)), User Knowledge Modeling Data Set (Kahraman et al., (2013)), Student Academics Performance Data Set (Hussain et al., (2018)) and the Open University Learning Analytics Dataset (OULAD) (Kuzilek et al., (2017)). Studies which conduct the same statistical analysis on the these complex data sets may acquire different results owing to how the data are cleaned and preprocessed. Hadavand et al. ((2019)) highlight the complexity of massive open online course data and call for more tools to support researchers in analysing these data sets.

The OULAD comes from the Open University, a world leader in providing distance learning. Based in the United Kingdom, in 2022/23, the Open University taught 150,619 students (The Open University, (2024)). The OULAD (Kuzilek et al., (2017)) contains anonymized data from 22 presentations from 7 modules (courses). This includes demographic and registration information, assessment information and results, and Virtual Learning Environment (VLE) interactions represented by daily summaries of student clicks from 32,593 students. The OULAD is available online (Kuzilek et al., (\bibnodate)) across seven files under a database schema (see Figure 1). Kuzilek et al. ((2017)) provides definitions for each variable of the OULAD. To conduct statistical analysis, preprocessing is required. According to Mihaescu & Popescu ((2021)), this intensive preprocessing is the main limitation of the OULAD. Hence, the ouladFormat R package (Howard, (2024)) was created to load, clean and format the OULAD for analysis as a single flat file (data set). Apart from streamlining the process of preparing the OULAD, the ouladFormat R package helps towards reproducibility and comparability of studies.

Figure 1: Figure from Kuzilek, Hlosta, and Zdrahal (n.d.) detailing the OULAD Database Schema

This paper explains how the ouladFormat R package can be used to prepare data for analysis. Section 2 summarizes the ouladFormat R package and explains the different functions within the package. In section 3, two case studies are provided where the ouladFormat is used to prepare data for subsequent data analysis. Section 4 concludes the paper.

## 2 The ouladFormat package

### 2.1 Overview

The ouladFormat R package loads, cleans and formats the OULAD for data analysis. The overall aim of the package is to return the Open University data as a single flat data set/table/dataframe where each observation is a student. The package can be installed from CRAN using the command install.packages(“ouladFormat”). The package consists of ten functions (see Table 1). The functions have been grouped according to their purpose: 1) loading support, 2) loads specific data, 3) VLE format conversion, and 4) combines data sets (main function). The OULAD data can be considered under four data categories (demographics, assessment, registration, and VLE). The ouladFormat allows the user to load individual categories of data (see loads specific data functions) or for combination of data categories to be loaded (see combines data sets function) as a single flat file. The returned format of the data is a tibble (Müller & Wickham, (2023)), a type of dataframe. The main function, combined_\_dataset(), draws on the other nine functions to return the formatted data for analysis. Hence, owing to this hierarchical structure, a user might only ever call upon the combined_\_dataset() function. The other functions are useful for additionally flexibility. The ouladFormat R package does not provide functions for data analysis but the output can be combined with other packages for this purpose (see Section 3).

While the OULAD includes data from 22 presentations across 7 modules (Kuzilek et al., (2017)), this paper will predominately show results from the ‘2013J’ presentation of the STEM module ‘DDD’. There were 1,503 students who have data available across the four data categories for the DDD-2013J presentation. Depending on the data categories requested by the user, the number of students per data set for a presentation will change. For example, for the DDD-2013J presentation, there are 1,938 students with registration data available. Student 3733 unregistered on day -8 (eight days before the start of the teaching semester), and therefore, there are no assessment data available for student 3733. When the data requested includes assessment data, student 3733 will not feature in the returned data set. There are 1,507 students with assessment data available. There are 1,507 students who have both assessment and registration data available.

Table 1: Description of Functions in the ouladFormat R Package

| Function Name
| Description edited from the R Package Help File
| Function Purpose

| load_\_github_\_modified
|

| Loads .RData files directly from a GitHub repository.

| Loading support

| path_\_to_\_file
|

| ouladFormat comes bundled with the sample student VLE data

| in its directory. This function makes it easy to access.

| Loading support

| dataset_\_demographics
|

| Load and formats the studentInfo file from the OULAD

| for data analysis.

| Loads specific data

| dataset_\_registration
|

| Load and formats the studentRegistration file from the

| OULAD for data analysis.

| Loads specific data

| dataset_\_assessment
|

| Load, combines and formats the assessment and

| studentAssessment files from the OULAD for data analysis.

| Loads specific data

| dataset_\_VLE_\_time
|

| Load and formats the studentVLE file from the OULAD

| for data analysis.

| Loads specific data

| dataset_\_VLE_\_activity
|

| Load and formats the studentVLE and vle files from the

| OULAD for data analysis.

| Loads specific data

| convert_\_VLE
|

| Converts the data format of VLE data from total view counts

| to binary, standardised or logarithmic view count data.

|

| VLE format

| conversion

| VLE_\_learning_\_classification
|

| Transform Open University VLE activities to classifications

| under either the FSLM, FSLSM, VARK or OLS mapping.

|

| VLE format

| conversion

| combined_\_dataset
|

| Main function. Combines multiple OULAD files into one

| tibble that is formatted for data analysis and where each row

| represents a unique student.

| Combines data sets

### 2.2 Loading Support Functions

The ouladFormat R package does not store the OULAD. Instead, the package features two functions (see Table 1) which help to load the OULAD into R. The user does not need to use these functions directly as they are called as part of the other package functions. For use of this package, the OULAD is stored as a series of .RData files on Github according to a database schema (see Figure 1). The load_\_github_\_modified(), based on the Rfssa function (Haghbin et al., (2022)), which is based on a Stack Overflow post (Hartman, (2016)), loads the .RData to a specified environment. The function was modified to allow the user to choose the environment in which the .RData files are loaded to. When a function, for example dataset_\_demographics(), calls on the corresponding .RData, the data will be loaded into the local (function) environment rather than to the global environment. Functions return the requested subset of the OULAD as a formatted tibble.

A subset of the OULAD studentVle data comes bundled with the package (5,000 rows from the AAA-2013J presentation). The path_\_to_\_file() function is adapted from the readxl_\_example() function contained in the readxl R package (Wickham & Bryan, (2023)) and loads in the sample VLE data. The sample VLE data are used for VLE examples as manipulating the full VLE data takes longer than the recommended time for a CRAN package example.

### 2.3 Loading Specific Data Functions

The five functions for loading specific data sets (see Table 1) are designed to have a similar structure through their sharing of three core parameters; module, presentation and repeat_\_students. Kuzilek et al. ((2017)) specifies that the OULAD consists of three Social Sciences modules (AAA, BBB and GGG) and four STEM modules (CCC, DDD, EEE and FFF). The module parameter can specify an individual module or call upon all modules using the argument ‘All’. Each module has between two and four presentations present in the dataset. The presentations consist of 2013B, 2013J, 2014B, 2014J (B indicates a February start date and J indicates an October start date). Similarly, all presentations can be called upon using the argument ‘All’. The ouladFormat package will give an error if a selected presentation does not exist for a selected module. In the case of loading VLE data, there is no option to load ‘All’ presentations of a module owing to the function design. This can be circumvented by loading each presentation individually and combining the outputs. The repeat_\_students parameter indicates whether repeat students should be removed or kept. Each of the five loading specific data functions will be discussed in subsequent paragraphs.

The dataset_\_demographics() and dataset_\_registration() functions, apart from returning the core arguments as outputs, return the OULAD studentInfo and studentRegistration data respectively. Minimal changes are made to the OULAD studentInfo and studentRegistration data.

⬇

# Example code for using the dataset_demographics()

# and dataset_registration() functions:

# Return demographic data for students in module DDD and presentation 2013J:

dataset_demographics(module = "DDD", presentation = "2013J",

repeat_students = "remove")

# Return demographic data for students in module DDD (all presentations):

dataset_demographics(module = "DDD", presentation = "All",

repeat_students = "remove")

# Return registration data for students who undertook a module with a presentation 2013J:

dataset_registration(module = "All", presentation = "2013J",

repeat_students = "keep")

The dataset_\_assessment() function, apart from having the three core parameters, has the parameters week_\_begin, week_\_end and na.rm. These parameters give the user greater flexibility over the output by allowing the user to specify the period in the semester that the returned assessment data relates to. For example, the user may wish to only include assessments in the returned tibbles that had due dates in the first 10 weeks of the module (see example code below).

⬇

# Example code and output for using the dataset_assessment()

# function:

> dataset_assessment(module = "DDD", presentation = "2013J",

+ repeat_students = "remove", week_begin = 1, week_end=10,

+ na.rm = FALSE)

$assessment_data

# A tibble: 2,379 X 11

id_student code_module code_presentation id_assessment assessment_type

<chr> <fct> <fct> <fct> <fct>

1 102850 DDD 2013J 25349 TMA

2 102850 DDD 2013J 25348 TMA

3 103800 DDD 2013J 25348 TMA

4 103800 DDD 2013J 25349 TMA

5 104643 DDD 2013J 25349 TMA

6 104643 DDD 2013J 25348 TMA

7 104772 DDD 2013J 25348 TMA

8 104772 DDD 2013J 25349 TMA

9 105523 DDD 2013J 25348 TMA

10 105523 DDD 2013J 25349 TMA

# 2,369 more rows

# 6 more variables: date <dbl>, weight <dbl>, date_submitted <dbl>,

# is_banked <fct>, score <dbl>, reactivity <dbl>

# Use ‘print(n = ...)‘ to see more rows

$assessments

# A tibble: 7 x 7

code_module code_p... id_a... assessment_type date weight week

<chr> <chr> <int> <chr> <int> <dbl> <dbl>

1 DDD 2013J 25348 TMA 25 10 4

2 DDD 2013J 25349 TMA 53 12.5 8

3 DDD 2013J 25350 TMA 88 17.5 13

4 DDD 2013J 25351 TMA 123 20 18

5 DDD 2013J 25352 TMA 165 20 24

6 DDD 2013J 25353 TMA 207 20 30

7 DDD 2013J 25354 Exam 261 100 38

$assessment_performance

# A tibble: 1,271 X 4

id_student ‘25349‘ ‘25348‘ average_CA_score

<dbl> <dbl> <dbl> <dbl>

1 102850 97 68 84.1

2 103800 56 63 59.1

3 104643 81 77 79.2

4 104772 56 67 60.9

5 105523 69 81 74.3

6 1080206 81 93 86.3

7 108789 NA 27 12

8 1103608 87 84 85.7

9 114558 81 81 81

10 1187586 92 84 88.4

# 1,261 more rows

# Use ‘print(n = ...)‘ to see more rows

$assessment_reactivity

# A tibble: 1,271 X 3

id_student ‘25349‘ ‘25348‘

<chr> <dbl> <dbl>

1 102850 0 8

2 103800 0 0

3 104643 1 5

4 104772 1 1

5 105523 0 0

6 1080206 6 5

7 108789 NA -2

8 1103608 7 3

9 114558 1 8

10 1187586 2 6

# 1,261 more rows

# Use ‘print(n = ...)‘ to see more rows

$module

[1] "DDD"

$presentation

[1] "2013J"

$repeat_students

[1] "remove"

The dataset_\_assessment() function returns a list of the three core parameters and the four tibbles: 1) assessment_\_data, 2) assessments, 3) assessment_\_performance, and 4) assessment_\_reactivity. The assessment_\_data, assessment_\_performance, and assessment_\_reactivity are all filtered based on the week_\_begin and week_\_end parameters. The assessment_\_data is a tibble based on the combined OULAD files of studentAssessment and assessments (see Figure 1), and filtered based on the inputs. The assessments tibble, as seen above, returns the full list of assessments for the selected module-presentation combination. This tibble is particularly beneficial for the user in learning about the module as continuous assessment drives engagement. For DDD-2013J, there were six continuous assessments; all marked by a tutor. These were weighted 10%, 12.5%, 17.5%, 20%, 20% and 20%, and were due in weeks 4, 8, 13, 18, 24, and 30 respectively. The assessment_\_performance tibble is a tibble where each row represents a unique student and their scores in the range of 0-100 for different assessment items (see id_\_assessment in the assessments tibble). When a specific module presentation is called, for example DDD-2013J, the ouladFormat package calculates students’ average weighted continuous assessment (CA) score based on the CA variables included in the filtered data and returns it as part of the assessment_\_performance tibble. Any (end-of-semester) examination data is not included in the calculation. According to Kuzilek et al. ((2017)), if a student does not submit the assessment, a NA is recorded for that assessment. For this calculation, the NAs may be excluded or replaced by 0 (default) through using the na.rm parameter. The fourth tibble, the assessment_\_reactivity tibble, returns the reactivity for each assessment. Treuiller & Boyer ((2021)) define reactivity for the OULAD as the delay between the date the assessment is returned and the deadline (in days). Negative numbers indicate overdue assessments.

The OULAD studentVle file provides information on how many times a specific resource (coded as the variable id_\_site) for a specific date was accessed by a student. Using the OULAD vle file, the classification of the resource can be identified (e.g., homepage, oucontent, and forumng). Formatted VLE data can be returned using the dataset_\_VLE_\_activity() and dataset_\_VLE_\_time() functions. dataset_\_VLE_\_time() returns tibbles of the number of times students accessed VLE resources per day and per week. dataset_\_VLE_\_activity() returns a tibble of the number of times students accessed VLE resources by activity classification. In addition to the core parameters, both these functions have the parameters week_\_begin, week_\_end and example_\_data (see Section 2.2). Similar to the dataset_\_assessment() function, week_\_begin and week_\_end allow the user to control what period, or weeks of the semester, the VLE data relates to in the returned tibbles.

⬇

# Example code for using the dataset_VLE_time() and

# dataset_VLE_activity() functions:

# See Section 2.2 on example student VLE data

# (subset of AAA-2013J):

dataset_VLE_time(example = TRUE)

# Return all VLE data available for students in module DDD and presentation 2013J:

dataset_VLE_time(module = "DDD", presentation = "2013J",

repeat_students = "keep", week_begin = -4, week_end = 39,

example_data = FALSE)

# Return VLE data for students in module BBB and presentation 2013J for weeks 1-13:

dataset_VLE_time(module = "BBB", presentation = "2013J",

repeat_students = "remove", week_begin = 1, week_end = 13,

example_data = FALSE)

# Return VLE activity data for students in DDD-2013J with weeks prior to module start excluded:

dataset_VLE_activity(module = "DDD", presentation = "2013J",

repeat_students = "keep", week_begin = 1, week_end = 39,

example_data = FALSE)

Apart from returning tibbles, the dataset_\_VLE_\_activity() and dataset_\_VLE_\_time() return the core arguments as well as values for week_\_begin and week_\_end. However, the returned values for week_\_begin and week_\_end may differ from the inputted values. The inputted values represent the time period of VLE data that users request be returned in the outputted tibbles. The returned values represent the week_\_begin and week_\_end period that is in the returned tibbles. In the example below, the code requests VLE data for DDD-2013J for between week -6 (six weeks before the start date) and week 2 of the semester inclusive. However, students only started accessing the module VLE in week -3, and therefore the returned value for week_\_begin is -3; this is evident in the tibbles outputted as well.

⬇

# Example code and output for using the dataset_VLE_time()

# function:

> dataset_VLE_time(module = "DDD", presentation = "2013J",

+ repeat_students = "remove", week_begin = -6,

+ week_end = 2, example_data = FALSE)$filtered_data

# A tibble: 110,953 x 6

id_student code_module code_presentation id_site date sum_click

<chr> <fct> <fct> <int> <dbl> <dbl>

1 102850 DDD 2013J 674078 -2 2

2 102850 DDD 2013J 674186 -2 1

3 102850 DDD 2013J 673740 -2 5

4 102850 DDD 2013J 674054 10 1

5 102850 DDD 2013J 673981 -2 2

6 102850 DDD 2013J 673537 -2 1

7 102850 DDD 2013J 673724 -12 1

8 102850 DDD 2013J 674075 -2 1

9 102850 DDD 2013J 674158 -2 1

10 102850 DDD 2013J 674306 -2 1

# 110,943 more rows

# Use ‘print(n = ...)‘ to see more rows

$daily_data

# A tibble: 1,472 x 33

id_student ‘-18‘ ‘-17‘ ‘-16‘ ‘-15‘ ‘-14‘ ‘-13‘ ‘-12‘ ‘-11‘

<chr> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl>

1 1103608 105 0 17 28 1 11 0 0

2 122739 11 0 0 0 0 1 0 0

3 123957 14 5 3 0 0 0 7 0

4 126394 47 0 0 0 0 0 0 0

5 130467 2 4 16 0 0 0 0 4

6 130671 10 7 10 10 34 26 7 1

7 130837 63 0 0 0 0 0 0 0

8 131222 20 26 0 0 5 1 0 0

9 1345808 16 0 0 0 0 0 0 0

10 1440467 66 30 50 0 0 0 0 0

# 1,462 more rows

# 24 more variables: ‘-10‘ <dbl>, ‘-9‘ <dbl>, ‘-8‘ <dbl>,

# ‘-7‘ <dbl>,‘-6‘ <dbl>, ‘-5‘ <dbl>, ‘-4‘ <dbl>, ‘-3‘ <dbl>,

# ‘-2‘ <dbl>, ‘-1‘ <dbl>, ‘0‘ <dbl>, ‘1‘ <dbl>, ‘2‘ <dbl>,

# ‘3‘ <dbl>, ‘4‘ <dbl>, ‘5‘ <dbl>, ‘6‘ <dbl>, ‘7‘ <dbl>,

# ‘8‘ <dbl>, ‘9‘ <dbl>, ‘10‘ <dbl>, ‘11‘ <dbl>, ‘12‘ <dbl>,

# ‘13‘ <dbl>

# Use ‘print(n = ...)‘ to see more rows

$weekly_data

# A tibble: 1,472 x 6

id_student ‘Week_pre-3‘ ‘Week_pre-2‘ ‘Week_pre-1‘ Week1 Week2

<chr> <dbl> <dbl> <dbl> <dbl> <dbl>

1 104643 5 70 32 61 36

2 104772 7 66 35 61 186

3 1103608 150 18 257 75 75

4 114558 22 66 41 187 80

5 118887 7 2 0 0 0

6 122739 11 1 24 10 52

7 123957 22 11 28 86 31

8 124387 14 0 0 42 0

9 126394 47 0 0 0 0

10 126812 17 115 106 106 9

# 1,462 more rows

# Use ‘print(n = ...)‘ to see more rows

$module

[1] "DDD"

$presentation

[1] "2013J"

$repeat_students

[1] "remove"

$week_begin

[1] -3

$week_end

[1] 2

### 2.4 VLE Format Conversion Functions

The defaults of dataset_\_VLE_\_activity() and dataset_\_VLE_\_time() are to return tibbles with the number of times students accessed resources per day, per week or per activity type. However, a number of statistical methods (e.g., kk-means) are sensitive to variances across variables, and other data formats may be needed. convert_\_VLE() quickly converts the VLE data to either binary, standardised by variable, standardised globally, or logarithmic format. Some studies have mapped the OULAD activities to different classifications. For example, Balti et al. ((2023)) mapped the activity classifications to the VARK Learning Style Model (Fleming & Mills, (1992)). The VLE_\_learning_\_classification() function maps the VLE activities according to different studies (see function’s help file), and returns the mapping as well as a tibble of the VLE data according to the chosen mapping.

⬇

# Example code for using the convert_VLE() and

# VLE_learning_classification functions:

# Loads and standardises sample VLE data by variable

VLE_data = dataset_VLE_activity(example_data = TRUE)$resource_data

convert_VLE(VLE_data, conversion = "standardise1")

# Loads sample VLE data and maps activities under the

# Felder-Silverman Learning Style Model:

VLE_data = dataset_VLE_activity(example_data = TRUE)$resource_data

VLE_learning_classification(VLE_data, classification = "VARK")

# See more mappings

?VLE_learning_classification

### 2.5 Combines Data Sets (Main Function)

The main function of the ouladFormat package is combined_\_dataset(), and this function calls on the other nine functions in the package to allow the user to easily return their required data set as a single tibble. In addition to the parameters previously seen, the demographics, registration, assessment and VLE parameters allow the user to specify if each of the corresponding data categories should be included in the returned tibble, and in the case of the VLE parameter further flexibility is provided; with even more flexibility possible through the VLE_\_clicks parameter. Additionally, there is a withdrawn_\_students parameter to indicate whether withdrawn students should be removed. When set to ‘remove’, this does not necessarily remove all students who withdrew from the module, rather it removes students who withdrew from the module up to and including the week indicated by the week_\_end argument (see Section 3.2 for example). Note for the combined_\_dataset(), repeat students are always removed when presentation set to ‘All’.

⬇

# Usage of combined_dataset():

combined_dataset(

module = c("AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"),

presentation = c("2013J", "2014J", "2013B", "2014B", "All"),

repeat_students = c("remove", "keep"),

withdrawn_students = c("remove", "keep"),

demographics = FALSE,

registration = FALSE,

VLE = c("omit", "daily", "weekly", "activity", "FSLM", "FSLSM",

"OLS", "VARK"),

VLE_clicks = c("total", "binary", "standardise1", "standardise2",

"logarithmic"),

week_begin = -4,

week_end = 39,

assessment = FALSE,

na.rm = FALSE,

example_data = FALSE

)

## 3 Case Studies

### 3.1 Case Study 1: Preparation for an educational study

Researchers, or institution staff, may wish to conduct an educational study. Pre-registration of data analysis plans are becoming more common, and any data to be collected should be determined in advance of conducting a study. In preparation, researchers, through exploring the OULAD, can improve their data analytics skills, learn about relationships underpinning educational data to inform their data collection and knowledge, and gather evidence for their own educational hypotheses for ethics or funding applications. For example, a researcher may wish to examine whether extra supports for students from low-income backgrounds would decrease student drop out and failure rates. To acquire funding for this project, researchers may need to show evidence that there exists a difference in achievement levels between students from low-income and high-income backgrounds. One source of evidence could be showing the relationship between the OULAD final_\_result and imd_\_band variables. The imd_\_band variable gives the index of multiple deprivation (imd) band of the place where the student lived during a module-presentation (Kuzilek et al., (2017)). Figure 2 shows that of those students who withdrew or failed, a higher proportion came from lower imd bands. The significance of the relationship between the final result and the imd band is confirmed by a χ2\chi^{2} statistic of 161.74 with 27 degrees of freedom.

Figure 2: Heatmap illustrating for each final result category, the proportion of students within each imd band. Darker colours indicate a higher proportion of students.

⬇

# Load ouladFormat

require(ouladFormat)

# Load the demographic data

case1 <- dataset_demographics(module = ’DDD’, presentation = ’All’,

repeat_students = ’keep’)$studentInfo

# Format final result variable

# (makes Figure 2 nicer as categories ordered)

case1$final_result = factor(case1$final_result,

levels = c("Distinction", "Pass", "Fail", "Withdrawn"))

# Examine the relationship between final result and the index of

# multiple deprivation band of the place where the student lived

# during the presentation

cross_tab = table(case1$final_result, case1$imd_band)

cross_tab

chisq.test(cross_tab) # Run X^2 test

# Creates Figure 2

heatmap(cross_tab, Rowv = NA, Colv = NA, scale = "row", cexRow = 1.3)

### 3.2 Case Study 2: Early identification of at-risk students

An early warning system in education involves identifying students at risk of failing or dropping out of a module/course and providing them with an intervention to help support them in their studies. Ideally, at-risk students would be identified as early as possible in the teaching semester in order to provide effective interventions (Howard et al., (2018)). At-risk students may be identified by academic staff or through statistical methods such as prediction modelling. While many studies have applied prediction modelling to the OULAD for various motivations (Jin et al., (2024)), Drousiotis et al. ((2021)) aimed to identify at-risk students by predicting students’ final results (withdrawn, fail, pass and distinction) as early as possible in the teaching semester. To achieve this, they used the explanatory variables of first assessment mark, highest educational level achieved, number of VLE clicks until the module starts, registration date, age, disability, gender, and number of previous attempts. Then they applied a 70%/30% split for training/test data and used the prediction algorithms of Decision Tree classifier, Random Forest, and Bayesian Additive Regression Trees. The code below demonstrates the approach taken by Drousiotis et al. ((2021)) for the DDD-2013J presentation using the Decision Tree Classifier and Random Forest algorithms. Overall, the Decision Tree classifier achieves the higher accuracy (0.5262 versus 0.5011). If the intention was to provide at-risk students with interventions, the Decision Tree classifier could be used to identify at-risk students (those predicted to fail or withdraw) in the next iteration of the module and subsequently interventions provided.

Researchers may be interested in finding the best prediction model for identifying at-risk students and use the OULAD for this. The ouladFormat R package can aid comparisons between models as it makes it easier for studies to use the same data from the OULAD.

⬇

# Load required packages for case study

require(ouladFormat)

require(tidyverse)

require(randomForest)

require(caret)

require(party)

# Load in the DDD-2013J data, match variables used by

# Drousiotis, Shi and Maskell (2021) and remove

# redundant variables:

case2 <- combined_dataset(module = ’DDD’, presentation = ’2013J’,

withdrawn_students = "remove", repeat_students = ’keep’,

demographics = TRUE, assessment= TRUE, registration = TRUE,

VLE = "weekly", VLE_clicks = ’total’,

week_begin = -4, week_end = 4)$dataset_combined %>%

mutate(clicks = ‘Week_pre-3‘+‘Week_pre-2‘+‘Week_pre-1‘) %>%

rename(CA1 = ‘25348‘) %>% # Rename first assessment variable

select(!c(id_student:code_presentation, date_unregistration,

region, imd_band, studied_credits, average_CA_score:Week4))

# Remove incomplete student records

case2 <- case2[complete.cases(case2),]

# Set seed to ensure reproducibility of results

set.seed(123)

# Implement 70%/30% data split

trainIndex <- createDataPartition(case2$final_result,

p = 0.7, list = FALSE)

trainData <- case2[trainIndex, ] %>% as.data.frame()

testData <- case2[-trainIndex, ] %>% as.data.frame()

# Implement Random Forest approach

Model1 <- randomForest(final_result ~ ., data = trainData,

ntree=50)

predictions1 <- predict(Model1, newdata = testData)

confMatrix1 <- confusionMatrix(predictions1, testData$final_result)

print(confMatrix1)

# Implement Decision Tree approach

Model2 <- ctree(final_result ~ ., data = trainData)

predictions2 <- predict(Model2, newdata = testData)

confMatrix2 <- confusionMatrix(predictions2, testData$final_result)

print(confMatrix2)

## 4 Conclusion

Educational research benefits by having large real-life data sets, such as the OULAD (Kuzilek et al., (2017)), freely available. However, large educational data sets are complex and can be a challenge for those working with them (Hadavand et al., (2019)). Similar to the crsra R package (Hadavand et al., (2019)), which supports researchers in cleaning and analysing Coursera’s research data exports, the ouladFormat R package is a flexible tool to help researchers load and format the OULAD for analysis. The main function, combined_\_dataset(), allows the user to easily return a subset of the OULAD as a single data set. The parameters of combined_\_dataset() are designed to give the user flexibility.

While the two case studies presented in Section 3 focused on examples of researchers or practitioners making use of the OULAD, the OULAD may also be of interest to educators teaching statistical analysis and methods. For example, a subset of the OULAD could be used as a data set for a multivariate analysis or machine learning module, or for a final year undergraduate project. For educators, we hope that the ouladFormat R package makes the OULAD accessible for teaching. For researchers, we hope the ouladFormat R package helps support reproducibility of studies and comparability of results across studies.

## Acknowledgments

I would like to thank Dr Arthur White and Dr Jason Wyse for their support in the development of the ouladFormat R package.

## References

- American Educational Research Association ((\bibnodate))

American Educational Research Association.

(\bibnodate).

What is Education Research?

https://www.aera.net/About-AERA/What-is-Education-Research

- Balti et al. ((2023))

Balti, R., Hedhili, A., Chaari, W. & Abed, M.

(2023).

Hybrid analysis of the learner’s online behavior based
on learning style.

Education and Information
Technologies 28 12465–12504.

doi:https://doi.org/10.1007/s10639-023-11595-x

- Cortez & Silva ((2008))

Cortez, P. & Silva, A.M.G.

(2008).

Using data mining to predict secondary school student
performance.

: EUROSIS-ETI.

- Drousiotis et al. ((2021))

Drousiotis, E., Shi, L. & Maskell, S.

(2021).

Early predictor for student success based on
behavioural and demographical indicators.

In A.I. Cristea & C. Troussas (Eds.), Intelligent tutoring systems ( 161–172).

Cham: Springer International Publishing.

- Fleming & Mills ((1992))

Fleming, N.D. & Mills, C.

(1992).

Not another inventory, rather a catalyst for reflection.

To Improve the Academy: A Journal of Educational
Development 11 137-155.

doi:https://digitalcommons.unl.edu/podimproveacad/246

- Hadavand et al. ((2019))

Hadavand, A., Muschelli, J. & Leek, J.

(2019).

Analysis of student behavior using the r package crsra.

Journal of Learning Analytics 6 2 140-152.

https://learning-analytics.info/index.php/JLA/article/view/6189

doi:10.18608/jla.2019.62.10

- Haghbin et al. ((2022))

Haghbin, H., Trinka, J., Najibi, S.M. & Maadooliat, M.

(2022).

Package ’Rfssa’ [
https://cran.r-project.org/web/packages/Rfssa/Rfssa.pdf

- Hartman ((2016))

Hartman, R.

(2016).

Importing data into R (.rData) from Github [
https://stackoverflow.com/questions/24846120/importing-data-into-r-rdata-from-github

- Howard ((2024))

Howard, E.

(2024).

ouladFormat: Loads and
formats the Open University Learning Analytics Dataset for data
analysis [

- Howard et al. ((2018))

Howard, E., Meehan, M. & Parnell, A.

(2018).

Contrasting prediction methods for early warning
systems at undergraduate level.

The Internet and Higher Education 37 66-75.

doi:https://doi.org/10.1016/j.iheduc.2018.02.001

- Hussain et al. ((2018))

Hussain, S., Dahan, N.A., Ba-Alwi, F.M. & Ribata, N.

(2018).

Educational data mining and analysis of
students’ academic performance using weka.

Indonesian Journal of Electrical Engineering and
Computer Science 9 2 447–459.

doi:10.11591/ijeecs.v9.i2.pp447-459

- Jin et al. ((2024))

Jin, L., Wang, Y., Song, H. & So, H-J.

(2024).

Predictive
modelling with the Open University Learning Analytics dataset (OULAD): A
systematic literature review.

In A.M. Olney, I-A. Chounta, Z. Liu, O.C. Santos & I.I. Bittencourt (Eds.), Artificial intelligence in education. posters and late
breaking results, workshops and tutorials, industry and innovation tracks,
practitioners, doctoral consortium and blue sky (p.  477-484).

Cham: Springer Nature Switzerland.

doi:https://doi.org/10.1007/978-3-031-64315-6˙46

- Kahraman et al. ((2013))

Kahraman, H.T., Sagiroglu, S. & Colak, I.

(2013).

The development of intuitive
knowledge classifier and the modeling of domain dependent data.

Knowledge-Based Systems 37 283-295.

doi:https://doi.org/10.1016/j.knosys.2012.08.009

- Kuzilek et al. ((\bibnodate))

Kuzilek, J., Hlosta, M. & Zdrahal, Z.

(\bibnodate).

Open university
learning analytics dataset.

https://analyse.kmi.open.ac.uk/open_dataset#examples

- Kuzilek et al. ((2017))

Kuzilek, J., Hlosta, M. & Zdrahal, Z.

(2017).

Open
university learning analytics dataset.

Scientific Data 4 1-8.

doi:https://doi.org/10.1038/sdata.2017.171

- Mihaescu & Popescu ((2021))

Mihaescu, M.C. & Popescu, P.S.

(2021).

Review on publicly available datasets for educational data
mining.

WIREs Data Mining and Knowledge
Discovery 11 3 e1403.

doi:https://doi.org/10.1002/widm.1403

- Motz et al. ((2023))

Motz, B.A., Bergner, Y., Brooks, C.A., Gladden, A., Gray, G., Lang, C.Quick, J.D.

(2023).

A lak of direction:
Misalignment between the goals of learning analytics and its research
scholarship.

Journal of Learning Analytics 10 2 1-13.

doi:10.18608/jla.2023.7913

- Müller & Wickham ((2023))

Müller, K. & Wickham, H.

(2023).

tibble: Simple data
frames [ https://tibble.tidyverse.org/

- The Open University ((2024))

The Open University.

(2024).

Financial statements for the year ended 31 July 2023.

https://www5.open.ac.uk/foi/main/sites/www.open.ac.uk.foi.main/files/files/Financial_Report_2023_FINAL_Online.pdf

- Treuiller & Boyer ((2021))

Treuiller, C. & Boyer, A.

(2021).

Identification of class-representative learner personas.

In Proceedings of la4sle 2021 - learning analytics
for smart learning environments (p.  38-45).

Bolzano, Italy: .

- Wickham & Bryan ((2023))

Wickham, H. & Bryan, J.

(2023).

readxl: Read excel
files [ https://readxl.tidyverse.org,https://github.com/tidyverse/readxl

##

-

<!-- fetch 2: arXiv:2501.08366 | fetch.py none | 2026-11-06T08:28+07:00 | error -->
No readable copy was found. Attempts:

