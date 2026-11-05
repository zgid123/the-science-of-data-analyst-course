---
id: S006
url: https://api.openalex.org/works/doi:10.1007/s11423-019-09685-0
requested: 10.1007/s11423-019-09685-0
fetched: 2026-11-02T00:47+07:00
tool: fetch.py (curl + json-metadata; ladder L4)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T03
part: 5
raw: raw.json (20 KB)
conversion: json-metadata of https://api.openalex.org/works/doi:10.1007/s11423-019-09685-0 (metadata, 224 words)
---
source: OpenAlex
title: A large-scale implementation of predictive learning analytics in higher education: the teachers’ role and perspective
authors: Christothea Herodotou; Bart Rienties; Avinash Boroowa; Zdeněk Zdráhal; Martin Hlosta
institutions: The Open University
venue: Educational Technology Research and Development
publication date: 2019-07-02
volume: 67
issue: 5
pages: 1273–1306
doi: https://doi.org/10.1007/s11423-019-09685-0
cited_by_count (OpenAlex): 188
type: article
location: https://link.springer.com/content/pdf/10.1007/s11423-019-09685-0.pdf (open access: True)
location: https://oro.open.ac.uk/62191/1/Herodotou2019_Article_ALarge-scaleImplementationOfPr.pdf (open access: False)

abstract:
By collecting longitudinal learner and learning data from a range of resources, predictive learning analytics (PLA) are used to identify learners who may not complete a course, typically described as being at risk. Mixed effects are observed as to how teachers perceive, use, and interpret PLA data, necessitating further research in this direction. The aim of this study is to evaluate whether providing teachers in a distance learning higher education institution with PLA data predicts students’ performance and empowers teachers to identify and assist students at risk. Using principles of Technology Acceptance and Academic Resistance models, a university-wide, multi-methods study with 59 teachers, nine courses, and 1325 students revealed that teachers can positively affect students’ performance when engaged with PLA. Follow-up semi-structured interviews illuminated teachers’ actual uses of the predictive data and revealed its impact on teaching practices and intervention strategies to support students at risk.

<!-- fetch 2: https://web.archive.org/web/2id_/https://oro.open.ac.uk/62191/1/Herodotou2019_Article_ALarge-scaleImplementationOfPr.pdf | fetch.py pdfkit | 2026-11-02T00:49+07:00 | readable -->
<!-- page 1 -->
Education Tech Research Dev
https://doi.org/10.1007/s11423-019-09685-0
DEVELOPMENT ARTICLE
A large‑scale implementation of predictive learning analytics
in higher education: the teachers’ role and perspective
Christothea Herodotou1
Martin Hlosta2
· Bart Rienties1 · Avinash Boroowa1 · Zdenek Zdrahal2
·
© The Author(s) 2019
Abstract
By collecting longitudinal learner and learning data from a range of resources, predictive
learning analytics (PLA) are used to identify learners who may not complete a course, typically described as being at risk. Mixed effects are observed as to how teachers perceive,
use, and interpret PLA data, necessitating further research in this direction. The aim of
this study is to evaluate whether providing teachers in a distance learning higher education
institution with PLA data predicts students’ performance and empowers teachers to identify and assist students at risk. Using principles of Technology Acceptance and Academic
Resistance models, a university-wide, multi-methods study with 59 teachers, nine courses,
and 1325 students revealed that teachers can positively affect students’ performance when
engaged with PLA. Follow-up semi-structured interviews illuminated teachers’ actual uses
of the predictive data and revealed its impact on teaching practices and intervention strategies to support students at risk.
Keywords Predictive learning analytics · Teachers · Student performance · Retention ·
Higher education
Introduction
With the increased availability of large datasets, powerful analytics engines (Joksimović
et al. 2015; Macfadyen and Dawson 2010; Romero et al. 2013), and skilfully designed visualisations of analytics (Ali et al. 2012; Dyckhoff et al. 2012; González-Torres et al. 2013),
institutions and teachers may be able to use the experience of the past to create supportive, insightful models of primary (and perhaps real-time) learning processes (Ferguson and
Buckingham Shum 2012; Mor et al. 2015; Papamitsiou and Economides 2014). In recent
years, several institutions have started to adopt predictive learning analytics (PLA) using
a range of advanced computational techniques (e.g., Bayesian modelling, cluster analysis,
* Christothea Herodotou
christothea.herodotou@open.ac.uk
1
Institute of Educational Technology, The Open University, Walton Hall, Milton Keynes MK7 6AA,
UK
2
Knowledge Media Institute, The Open University, Walton Hall, Milton Keynes MK7 6AA, UK
Vol.:(0123456789)
1 3

<!-- page 2 -->
C. Herodotou et al.
predictive modelling) to identify which students are going to pass a course, and which of
them are at-risk (Calvert 2014; Gasevic et al. 2016; Joksimović et al. 2015; Tempelaar
et al. 2015; Wolff et al. 2014), yet little evidence exist about their wide adoption in higher
education (Viberg et al. 2018). PLA data may provide useful, complementary information
to teachers to help them identify students at-risk while also allowing them to support other
groups of students and maximise their potential.
As recognised by recent learning analytics research (Dyckhoff et al. 2012; Rienties et al.
2016; van Leeuwen et al. 2014; Verbert et al. 2013) and wider literature on the role of
teachers in blended learning settings (e.g., Mazzolini and Maddison 2003; Norton et al.
2005; Rienties et al. 2013), teachers have an essential role to play in transforming insights
gathered from PLA into actionable support and interventions that help students. Yet, for
many teachers, it is a challenge to be able to filter relevant information from the virtual
learning environment (VLE) in PLA tools, and access predictive data about each of their
students. In particular, a lack of competence has been observed in extracting relevant information from learning analytics visualisations as well as taking corresponding pedagogical
actions (van Leeuwen 2018). While we recognise that VLE and PLA tools provide rich and
detailed information about student progression, they may also lead to information overload
which may restrict teachers’ abilities to provide effective support to learners (van Leeuwen
et al. 2014). Also, PLA data can negatively impact learning if their applications are not
well-routed into existing educational theory (Gasevic et al. 2015). A well-known application of PLA in education, Course Signals (Tanes et al. 2011), identified students ‘at-risk’
and provided warning signals to teachers and students. The authors analysed the content of
feedback messages sent to students as a response to the signals received by the system. The
type of feedback most often given to students was summative whereas instructive or process feedback on how to overcome difficulties was almost absent. Aligning with existing
research, summative feedback had no effect on students’ learning.
Although PLA might provide teachers with some powerful tools, several researchers
(Gasevic et al. 2016; Greller and Drachsler 2012; Tempelaar et al. 2015) indicate that most
institutions and teachers in particular may not be ready for PLA results. Indeed, recently
several researchers reported mixed effects about providing PLA data and visualisations to
teachers (Rienties et al. 2016; van Leeuwen et al. 2014, 2015). While these studies provide important insights about how teachers in relatively small-scale settings used simple
learning analytics visualisations to identify groups of learners that were less active, to the
best of our knowledge, no study has yet unpacked how teachers are using actual PLA data
across large distance learning courses as well as the impact this activity may have on student learning outcomes.
This study reports on a university-wide implementation of PLA consisting of 59 teachers facilitating nine courses (N
=
9) in a distance learning higher education institution. A
multi-methods research was conducted to first, measure the impact of teachers’ use of PLA
on students’ performance. Such understanding is essential as it can provide insights about
whether any reported usage of PLA by teachers has an impact or not on students’ performance, thus concluding on whether PLA tools, when used by teachers, are successful or
not in terms of benefiting students and their learning. Also, it can inform our understanding
and interpretation of qualitative data collected from interviews with teachers about PLA
perceptions and usage patterns. For instance, if PLA usage is found to improve learning,
understanding how teachers make use of it could provide evidence of best practice as to
how PLA tools could be used to support learning. Alternatively, if PLA usage is found not
to improve learning, we could seek to understand whether actual uses (e.g., approaches and
frequency of contacting students at risk) may explain the lack of any learning improvement
1 3

<!-- page 3 -->
A large-scale implementation of predictive learning analytics…
thus informing future evaluations of PLA. Second, using semi-structured interviews, we
aimed to unpack whether and how participating teachers made use of PLA data to support
students and identify the underlying reasons explaining teaching practices. We made use
of two theoretical lenses, the Technology Acceptance (Davis 1989; Šumak et al. 2011) and
Academic Resistance Models (Piderit 2000; Rienties 2014), that may explain why some
teachers pro-actively engaged with PLA while others chose not to do so. The Technology Acceptance model (TAM) explains users’ intention to use a technology by the extent
to which the user believes that the technology is beneficial (perceived usefulness) and
whether the technology is easy to use (perceived easy-of-use). Previous research has consistently found that one common factor as to why teachers start and continue to use technology in their practice is their acceptance of technology (Rienties et al. 2016; Šumak et al.
2011; Teo 2010; Teo and Zhou 2016), in particular technology’s perceived ease of use and
perceived usefulness.
The academic resistance model (ARM) explains organisational adaptation or resistance in terms of employees’ attitudes. Attitudes are perceived as a multidimensional concept comprised of: (a) cognitive attitudes referring to whether a technology is positively,
negatively or neutrally evaluated by users, (b) emotional attitudes referring to feelings and
emotions experienced when using the technology, and (c) intentional attitudes referring
to intention to resist or plan to use the technology in the future. Different reactions may
characterise each dimension, for example, a strongly positive cognitive attitude maybe
accompanied by a strongly negative emotional response. Tensions between cognitive and
emotional attitudes may inhibit adoption of online interventions by teachers and lead to
AR (Rienties 2014). Resistance was originally suggested as influencing change in organisational structures. According to Piderit (2000, p. 783), “[s]uccessful organisational adaptation is increasingly reliant on generating employee support and enthusiasm for proposed
changes, rather than merely overcoming resistance.(p. 783)” Some teachers may embrace
new technologies and PLA approaches in particular while others may be more reticent,
which may be explained by the above models.
In order to address our overall research aim of unpacking how the engagement of teachers with PLA might positively or negatively support students’ performance, we will first
provide a review of literature on PLA, TAM, and AR. Second, we will explain the OU
Analyse system, which is the in-house built PLA system by the Open University UK.
Providing predictive learning analytics (PLA) to teachers in online
learning settings
An often cited model of visualisation of learning analytics tools (Dyckhoff et al. (2012)
distinguishes four different stages of use: (a) data-gathering of students’ activities in VLE,
(b) data collection and data mining using learning analytics techniques, (c) visualisation
of student activities in a widget, application, or VLE, and (d) reflection by the teacher.
Teachers are expected to quickly interpret visualisations, understand their impact on teaching and learning, and judge their effectiveness (Dyckhoff et al. (2012, p. 60). Ideally, PLA
visualisation should lead teachers to action in terms of teaching interventions, yet there is
no guarantee that teachers will be able to make informed teaching interventions and act
accordingly (Rienties et al. 2016).
There is a limited understanding as to how teachers make use of learning analytics
visualisation (van Leeuwen et al. (2015, p. 28). In a small experimental study of 28 high
1 3

<!-- page 4 -->
C. Herodotou et al.
school and student teachers, van Leeuwen et al. (2014) found that teachers who received
learning analytics visualisations of collaboration activities (i.e., authentic student data
were converted into simulation vignettes of students who had participation or discussion
problems) were better able to identify participation problems. Furthermore, these teachers
intervened more often with “problematic” groups as opposed to a control group of teachers who did not receive learning analytics visualisations. Yet, a follow-up study with 40
teachers visualisation (van Leeuwen et al. (2015, p. 28) showed that teachers with access
to learning analytics data were not better at detecting problematic groups but they could
provide more support to students experiencing problems. In a qualitative study, van Leeuwen (2018) examined the perceptions of seven teachers when weekly learning analytics
reports were made available to them. Learning analytics insights were found to influence
teachers’ behaviour, by opening up interaction and communication between the teachers
and students, leading to pedagogical interventions. In a four-year study of fine-grained data
collection amongst 34 teachers, McKenney and Mor (2015) indicated that the teachers’
professional development was enhanced (i.e., they learn from the process) by engaging
with learning analytics software and that teachers were able to develop better curriculum
materials.
In distance learning settings, the role of teachers in providing support through PLA data
is crucial. The teachers’ guidance and assistance are found to significantly impact learning
outcomes in particular, completion of students’ learning activities (Ma et al. 2015). While
distance learning teachers may have access to a lot of fine-grained clicking data to support them in comparison to teachers in face-to-face or blended settings (Richardson 2013;
Wolff et al. 2013), they will often not receive visual and oral clues about their students as
teachers in face-to-face or blended settings (Simpson 2013). Research indicated that VLE
engagement, in particular engagement with assessment activities, was positively predicting
performance (Calvert 2014), while Bayesian modelling indicated that the learning paths of
successful students were significantly different from those of “failing” students (Kuzilek
et al. 2015; Wolff et al. 2014). At the same time, in many distance learning settings most
teachers are recruited externally given the sheer scale of operations (contract-based). These
conditions may place obstacles to teachers and their continuous monitoring of PLA data.
Technology acceptance
A range of studies have found that users’ technology-acceptance, as conceptualised in the
technology acceptance model (TAM) by Davis et al. (1989), can have a substantial impact
on the adoption of information systems. TAM is a widely used model and has proved to
be highly informative in explaining teachers’ uptake of educational technology (Šumak
et al. 2011; Teo and Zhou 2016). Developed models have successfully been applied to
educational settings (Pynoo et al. 2011; Sanchez-Franco 2010; Šumak et al. 2011). The
TAM model is founded on the well-established theory of Planned Behaviour (Ajzen 1991),
which states that human behaviour is directly preceded by the intention to perform this
behaviour. In turn, three factors are found to influence intentions: personal beliefs about
one’s own behaviour, one’s norms, and the (perceived) amount of behavioural control an
individual has.
Building on this theory, TAM states that a user’s intention to use technology is influenced by two main factors: perceived usefulness (PU: e.g., the extent to which a teacher
believes the use of PLA dashboards will, for example, enhance the quality of their teaching
or increase academic retention) and perceived ease of use (PEU: e.g., the perceived effort
1 3

<!-- page 5 -->
A large-scale implementation of predictive learning analytics…
needed to use PLA). The influence of PU and PEU has consistently been shown in educational research (Pynoo et al. 2011; Teo 2010; Teo and Zhou 2016; Ali et al. 2013; Pituch
and Lee 2006; Sanchez-Franco 2010). For example, Teo (2010) found that PU and PEU
were key determinants of the attitudes towards computer use of 239 pre-service teachers.
Also, Rienties et al. (2018) identified that, out of 95 teaching staff, the great majority (68%)
perceived learning analytics visualisations as being useful (PU), yet only 34% as easy to
use (PEU) and this is more likely due to the number of tools examined concurrently and
their early level of development. These insights indicate the teachers’ recognition of the
significance of using analytics to support students yet they also raised the need for additional support and teacher training that can facilitate usage.
Academic resistance model
A second main reason why some teachers might be more willing to adopt PLA may be a
resistance or ambivalence towards change. According to Piderit (2000, p. 783), “[s]uccessful organisational adaptation is increasingly reliant on generating employee support and
enthusiasm for proposed changes, rather than merely overcoming resistance.” As argued by
Hanson (2009, p. 557), many studies tend “to blame the individual academic and attribute
delays or failure in implementation to an oversimplification of negative attributes, ill-will,
indolence, ineptitude or indiscipline on the part of those at whom the change is aimed … or
to portray resistance to change as irrational.”
In her review of “resistance” literature, Piderit (2000) argued that the ambivalence of
academics, in particular towards change, needs to be understood against three dimensions
of attitudes: cognitive, emotional, and intentional. Academic resistance models (ARM)
explain resistance (or having mixed feelings) about PLA in terms of cognitive (e.g., beliefs
about PLA that may help to accurately identify students at risk), emotional (e.g., feelings
about being followed by PLA systems; being assessed about how well a teacher provides
support to students; anxiety towards a future where PLA could replace teachers) and intentional attitudes (i.e., teachers’ plans to take an action). The ARM could help illuminate
teachers’ perceptions about the use of learning analytics and whether these relate to specific beliefs, feelings, or future plans. For example, in a large-scale organisational change
implementation across 629 courses from paper to online student evaluation, Rienties
(2014) found that the vast majority of academics were negative about this organisational
change. This finding was rather surprising given that, from a cognitive perspective, participants recognised that student evaluations were provided faster, with comparable evaluation
scores for teachers, yet with three times more qualitative feedback. Follow-up interviews
revealed that academics were at the same time experiencing anxiety (i.e., emotional dimension) with the idea that senior management could more intensively monitor their behaviour
and use this for promotion/demotion.
In this study, ARM and TAM are used in combination as they complement each other
and can provide unique insights in relation to the reasons potentially explaining usage of
PLA by teachers. In particular, TAM advocates that usage is explained by technology’s
easy-of-use and perceived usefulness whereas ARM explains usage in terms of cognitive,
emotional and intentional resistance to change. TAM is more focused on the design and
use of a technology whereas ARM on individuals’ attitudes to change. One may argue that
there is also a degree of overlap between the two models with, for example, perceived usefulness being an example of a cognitive attitude (ARM), and anxiety when using PLA due
1 3

<!-- page 6 -->
C. Herodotou et al.
to complexity of visualisations explained by both TAM through “perceived easy-of-use”
and ARM as an indication of emotional resistance.
PLA at a distance learning institution: OU analyse
Learning analytics dashboards have been discussed in the literature in relation to their
potential benefits to providing feedback opportunities and supporting learning (Bodily and
Verbert 2017). Yet, few studies have examined their actual impact on behaviour, achievement and skills (Bodily and Verbert 2017; Verbert et al. 2013). For example, Gutiérrez
et al. (2018) generated evidence about the effectiveness of learning analytics dashboards
for academic advising and support of decision-making processes. In particular, experts
advisers were found to assess more and difficult cases of students who failed their courses
while inexperienced advisers were shown to make informed decision in the same amount
of time as experienced ones. Towards this direction, in this study we aim to generate evidence about the effectiveness of OU analyse (OUA).
OUA is a PLA system designed at the Open University UK, which uses a range of
advanced statistical and machine learning approaches to predict students at-risk so that
cost-effective interventions can be made. The primary objective of OUA is the early identification of students who may fail to submit their next teacher marked assessment (TMA).
Four to six TMAs per course are typically requested from students. Combining predictions
about whether a student will submit their next TMA, the system also provides information about whether students will complete a course. This is the ‘overall’ system prediction
about a student’s performance. OUA was designed as a tool that would inform teachers
about their students’ behaviour and motivate them towards taking an action when students
are at-risk of not submitting their next assignment. The broader objective was to increase
students’ retention and completion of their studies.
Predictions of students at-risk of not submitting their next TMA are constructed by
machine learning algorithms that make use of two types of data: (a) static data: demographics, such as age, gender, geographic region, previous education, and (b) behavioural
data: students’ interactions within the VLE hosting a course. These sources of data were
shown to be significant indicators of predicting students’ assignment submission (Kuzilek
et al. 2015; Wolff et al. 2013, 2014). The resources a student may interact with have semantic labels called “activity types.” Examples of activity types are: forum, content, resource,
glossary, and wiki. All students’ interactions with the VLE are recorded and saved in a
database.
OUA employs three machine learning methods: (1) Naïve Bayes classifier (NB), (2)
Classification and regression tree (CART), (3) k-Nearest Neighbours (k-NN). Those are
used to develop four predictive models: (1) NB, (2) CART, (3) k-NN with demographic
data, and (4) k-NN with VLE data. Combining results from these four models was shown
to improve overall predictive performance. Two versions of k-NN was used due to the different nature of the values measured, i.e. numeric VLE data and categorical demographic
data. These four models consider different properties of student data and complement
each other. Each model classifies each student into classes: (a) will/will-not submit next
assessment and (b) will fail/pass the course. The final verdict of the prediction is done by
combining the outcomes and using voting techniques from all four models (Kuzilek et al.
2015; Wolff et al. 2013, 2014). In brief, the result of the prediction is ‘will-not submit next
assignment’ if three or all four models give a prediction of ‘will-not submit’. The result of
the prediction is ‘will submit’ if zero, one, or two models only vote ‘will-not submit’.
1 3

<!-- page 7 -->
A large-scale implementation of predictive learning analytics…
Fig. 1 Precision, recall, F-measure and accuracy of OUA
Predictions are calculated in two steps. First, predictive models are constructed by
machine learning methods from legacy data recorded in the previous presentation of the
same course. Second, student performance is predicted by the predictive models and the
student data of the current presentation. Machine learning methods aim at constructing
predictive models that capture data patterns for e.g., succeeding, failing or withdrawing
in formative/summative assessments and the course. OUA algorithms make use of weekly
aggregates. The system applies weekly information theoretic criteria to select 4–6 activity
types with the minimum redundancy and maximum information content and most informative about the outcome of the next assessments. These activity types are used to build predictive models. Moreover, the frequency of learners’ use of activities with selected activity
types indicates which study material learners visited and how many times. Activity types
that are not used point to a potential gap in knowledge and are used by the system as an
input for individualised study recommender.
To assess the quality of predictions by OUA, in each week confusion matrix values (True Positive, True Negative, False Positive, False Negative) for all the courses are
summed up, creating one confusion matrix per week. From this matrix, the performance
metrics, such as accuracy, are computed. By doing this, the courses with larger number of
students have higher impact on the performance metrics. Precision, Recall, F-measure, and
Accuracy for the courses under study are then constructed (see Fig. 1). Precision denotes
the proportion of students that OUA correctly identified as “not submit” out of all students
identified as “not submit”. Recall is the proportion of those students correctly identified as
“not submit” of all students that have not submitted an assignment; F-Score is a harmonic
mean of Precision and Recall, and Accuracy is the proportion of all correct predictions
to the total number of students. The class under examination is students “at risk” (‘willnot submit next assignment’); in each week, only students who do not submit their assignments are subject to predictions. Teachers can see all the students in the dashboard, yet
1 3

<!-- page 8 -->
C. Herodotou et al.
Fig. 2 A section of the OUA dashboard illustrating the average performance of the whole cohort of students in a respective course. The current course presentation (yellow) is compared to the previous one (dark
blue). The bars show the average assignment scores, while the lines indicate the average number of clicks
per student per week in VLE activities (Color figure online)
no predictions are produced for those who submit the coming teacher-mark assignment
as the result of this submission is already known (i.e., they submitted). In Fig. 1, “number
of students” refers to students who have not submitted their next assignment, that is the
assignment that is currently being predicted. Precision increases the closer the assignment
submission deadline is. Recall increases after the deadline as the model can identify more
students due to their low activity. Accuracy is relatively the same across presentations and
increases in the end of a course presentation, more likely due to the more information the
system knows about students as well as the fact that more courses that are easier to predict
remain in the analysis. F-measure, the harmonic mean of precision and recall, increases
towards the middle and end of course presentations.
Teachers access OUA data through the OUA dashboard (Figs. 2, 3, 4). Accessing the
dashboard is separate to accessing any other information about students that is hosted in
the University’s management system. The dashboard provides teachers with information
about how their course compares to the previous year’s presentation in terms of students’
engagement with VLE. Also, by combing evidence from the VLE and demographics, it
gives teachers access to predictions about whether their students would submit their next
assignment. Contact with students takes place outside the OUA dashboard, either by emailing, texting, or phoning students. Information about the process of getting in touch and the
responsiveness of students is recorded in the University’s management system.
Aim of this study
While several researchers in the learning analytics field have indicated a need for professional development, training, and support for teachers to help them use the complex and
1 3

<!-- page 9 -->
A large-scale implementation of predictive learning analytics…
Fig. 3 A section of OUA Dashboard showing the overall statistics of the current course presentation
(trends). At the bottom part, a list of all students with their TMA predictions in a given week is presented.
Predictions are generated for all students who have not yet submitted their next TMA in the given week.
Predictions are not generated the week a student submits their assignment. Such students (e.g., Student7)
are flagged as S (submitted)
dynamic insights from learning analytics (Ali et al. 2012; McKenney and Mor 2015; Rienties and Toetenel 2016; van Leeuwen et al. 2014), few studies have unpacked how teachers
perceive and use insights from predictive analytics in their daily practice as well as how
teachers’ PLA practices may relate to specific student outcomes (e.g., passing or failing
a course). Such insight would be valuable as existing studies suggest that teaching practices can have a positive impact on student performance in online settings. For example,
examining more than 500 students, Liu and Cavanaugh (2012) found a significant influence of teachers’ comments and timely and constructive feedback on students’ final scores
in online algebra modules. In another study, Ma et al. (2015) analysed log data from 900
courses and found that the teachers’ guidance has a significant effect on the completion
of students’ learning activities. In a recent systematic review, Viberg et al. (2018) noted
improvements from using learning analytics in student learning outcomes and the teaching
practice (support), yet these are very limited.
In this paper, we adopted a two-phase multi-methods methodology to understand how
teachers used, interpreted and integrated OUA into their teaching practices. In Phase 1,
1 3

<!-- page 10 -->
C. Herodotou et al.
Fig. 4 The individual student view of OUA dashboard showing dynamic information about individual students. The target visualises similarity between the selected student and their nearest neighbours measured
in terms of VLE activities (horizontal axes) and demographic parameters (vertical axes). In the table with
scores, the previous predictions of the student in the current presentation are shown along with the actual
score if their assignment has been marked
we explored from a quantitative perspective how the performance of 1325 students was
influenced by the use of OUA by 59 teachers across nine online courses. Building on previous PLA research (e.g., Herodotou et al. 2017, 2019; Rienties et al. 2016), we specifically
considered for learners’ characteristics, such as age, gender, previous grades, ethnicity, successful completion of previous courses [e.g., (e.g., Hachey et al. 2014)], VLE design and
course-specific characteristics (e.g., Gasevic et al. 2016; Rienties and Toetenel 2016), and
the teacher’s role and interaction with students (e.g., Arbaugh 2014).
In this study, we expected that the successful prediction of student performance could
be achieved with:
(a) (b) (c) student demographic data: gender, age, disability, ethnicity, education level, Index
of Multiple Deprivation (IMD band),1 students’ previous experience of studying at a
university (new versus continuous student), best previous course score achieved, and
sum of previous credits achieved,
design differences across participating courses, and
teaching features, including number of course presentations each teacher completed,
workload as measured by the number of students per course presentation assigned to
each teacher, and the average weekly usage of OUA dashboard per teacher.
Therefore, our first Research Question (RQ1) explored the potential impact of teachers’
usage of OUA on students’ performance:
RQ1 To what extent does engagement of teachers with OUA predict students’ performance (i.e., pass and completion rates)?2
1
2
IMD band is a UK measure of deprivation indicating deprived areas in English local councils.
Completion refers to submitting the final assignment of a course. Pass refers to passing the course that is
achieving at least 40%.
1 3

<!-- page 11 -->
A large-scale implementation of predictive learning analytics…
In Phase 2, in line with (Boyatzis 1998; Herodotou et al. 2017), we took a fine-grained,
qualitative perspective to better understand how teachers made sense of PLA in their daily
practice. Using the two lenses of TAM and AR, we explored the experiences of six teachers who used OUA during those courses to unpack why some teachers actively used the
system, while others might not have actively engaged with it. By triangulating the OUA
experiences of those teachers with their actual OUA usage data, we explored the following
two Research Questions:
RQ2 How do teachers make use of OUA data and visualisations to support teaching and
RQ3 learning?
Using TAM and ARM as theoretical lenses, which factors might explain teachers’
use of OUA?
Methodology
Nine distance learning, year 1 (Level 1) courses (N
=
9) took part in this multi-methods
study. Some of the courses have optional face-to-face elements, such as meetings between
students and teachers to discuss course-related issues. A range of activities is featured in
these courses including assimilative activities, finding and handling information, communication, productive, experiential, interactive activities, and assessment. Each course
emphasises some or most of these activities. Assessment criteria vary between courses,
and include formative and summative assignments and examinations (Nguyen et al. 2017).
Participating courses were self-selected. Courses expressing interest in participating were
included in this study.
Each course has a number of teachers, so-called Associate Lecturers (ALs), who support students at a distance. Each AL is responsible for a group of 15–20 students and their
role is to provide support and guidance to students in their group when needed. ALs are
required to know how to use information communication technology for teaching and supporting students, accessing information in relation to students, facilitating contact with academic units, and dealing with administrative responsibilities. Data were collected from the
cohort of students registered at the nine courses under study in 2015–2016. Participating
teachers were volunteers interested in joining the project. Oral consent by teachers was
gained by accepting to join the project. In terms of students’ consent, the OU Policy on
Ethical use of Student Data for Learning Analytics (Open University UK 2014) informs
students that their interactions are captured and may be used where there is likely to be an
expected benefit to learning. Informed consent applies at the point of reservation or registration on to a course or qualification.
Participating teachers were offered the option of joining online briefing sessions about
what predictive analytics are, what tools including OUA are available, and how they could
be used to support the teaching practice. Yet, participation was very limited in the range of
5–6%, despite scheduling the sessions well in advance.
Sample
Participating teachers (see Table 1) were self-selected with the obvious (self-selecting)
biases (Rienties et al. 2016; Torgerson and Torgerson 2008). No financial incentives
were offered to participating teachers. Logging in data from 59 teachers with access to
1 3

<!-- page 12 -->
C. Herodotou et al.
Table 1 Number of courses,
teachers, and students
participating in the study
No Course/year Teachers Students
1 Arts—2015 3 55
2 Social science—2015 3 69
3 Education—2015 11 262
4 Health care—2015 2 24
5 Maths—2015 8 186
6 Engineering—2015 6 152
7 Technology—2015 11 239
8 Technology—2016 6 92
9 Law—2015 9 246
Total 59 1325
Fig. 5 Percentage of teachers accessing the OUA dashboard per week per course. X axis indicates the
respective week of the term for participating courses. Y axis indicates the nine participating courses
OUA dashboard were collected. These data can provide us with insights about teachers’
usage patterns and their relation (if any) to student performance.
Methods of data collection and analysis
Phase 1: quantitative impact of OUA on students’ performance
In Phase 1, binary logistic regression analysis was performed to identify whether teachers’ engagement with PLA through the OUA dashboard significantly predicts pass and
completion rates (RQ1). Our unit of analysis were students (N
=
1325). Course and
teacher predictor indicators were group-level measures, created by combining data
between the student and teacher/course levels. In particular, teacher-level data was
constant within a group of students that was managed by a single teacher. Similarly,
course-level data was constant within all students attending a single course. On the contrary, individual-level variables such as age and gender varied across all cases i.e., 1325
participating students. A binary logistic regression was used as dependent variables
of completion (i.e., completed/not completed) and pass (i.e., passed/failed) rates were
dichotomous (Gliner et al. 2011).
1 3

<!-- page 13 -->
A large-scale implementation of predictive learning analytics…
The average weekly usage of OUA dashboard was captured by measuring the logging
in activity of participating teachers (i.e., how often and when teachers accessed the system). Weekly usage statistics were gathered and aggregated on a course level to guarantee
anonymity of respective teachers (see Fig. 5). Seven (n
=
7) teachers did not access the
dashboard at all. It is noted that this type of log file data entails certain limitations such as
not informing about the OUA features teachers accessed and the amount of time they spend
on the system; teachers may have identical numbers of OUA visits, yet differ in these other
dimensions. Figure 5 shows the number of visits to the dashboard per week per course.
The two courses with the highest frequency of access were Technology-2015 (i.e., course
ran in year 2015) and Education. Substantially lower use was observed for Law, Maths,
Social sciences, Technology-2016, Engineering (week 12 onwards), and Education (week
16 onwards). This trend indicates that, although teachers had access to OUA they did not
access OUA predictions regularly.
Correlation analysis was performed before entering the variables into the regression to
examine for multicollinearity. No variables were found to correlate highly or significantly.
Phase 2: qualitative experiences of teachers using OUA
In Phase 2, six individual semi-structured interviews with teachers who made use of
OUA were conducted in order to explore RQ2 and RQ3. Emails were sent to all course
chairs of the participating courses requesting for teachers-volunteers who could take
part in the interviews. Teachers were invited to individual semi-structured interviews
expected to last approximately 45 min. Interview participants were self-selected.
Only six (N
=
6) individuals from the engineering (n
=
3), math (n
=
2) and technology (n
=
1) courses were willing to participate in an interview. This response rate might
be explained by the fact that teachers at the university under study work on a part-time
basis for distance learning courses and therefore other responsibilities might have inhibited their participation in this study. In addition, teachers’ employment contracts do not
foresee any contributions to research activities. It is acknowledged that the interview
sample was relatively small and self-selected, and thus accompanied by the obvious
potential biases. It is also noted that participating teachers may be individuals who consider themselves as ‘technology-savvy’, or particularly interested in using PLA in their
practice, or even sceptical teachers with strong opinions as to how best to support learners. Therefore, any interest in using OUA (see “Thematic analysis” section) should be
analysed considering for the above factor and its possible impact on teachers’ perceptions about PLA use. A more representative sample selection would enable us to collect
and compare the perspectives of teachers who are/are not technology enthusiastic and
are/are not particularly interested in OUA, resulting in a multidimensional understanding of how and why OUA is used in the teaching practice. Insights should be treated as
preliminary, and beginning to shed light on PLA adoption in higher education.
Yet, the in-depth nature of interviewing allowed us to identify and report the perceptions of participating teachers about the use of OUA in their practice. Interviews were
conducted by the first author who had no prior involvement in the respective courses to
minimize biases. All six interviewees chose to have a Skype interview. Oral informed
consent was gained prior to the initiation of the interview by all interviewees. Interviews lasted between 25 and 45 min.
An interview protocol was devised and piloted prior to the interviews. Interview questions were open-ended and aimed to detail the experiences and perceptions of teachers
1 3

<!-- page 14 -->
C. Herodotou et al.
about OUA. In addition, we hypothesized that TAM and ARM could potentially explain
teachers’ practices and, in particular, why some teachers adopted and used OUA whereas
some others not. Therefore, we also added questions about issues such as easy of using
OUA, perceived OUA effectiveness, feelings towards OUA and future intentions (as
described in the two models). Interview questions were organised in the following four pillars (see Table 2): (1) teachers’ background, (2) the impact of OUA on teaching, (3) teachers’ concerns and feelings about OUA, and (4) future use and intentions. Apart from capturing the impact of OUA on teaching, the second set of questions (see (2) above) aimed
to identify how TAM may relate to teaching practice. Similarly, the third and fourth set of
questions (see (3) and (4) above) aimed to identify whether and how ARM may relate to
OUA usage.
Interview data were entered to the NVivo software. Thematic analysis (Kvale 1996) was
used to identify emerging themes related to the aims of this study, including the actual use
of OUA by teachers, specific interventions towards students at risk, teachers’ perceptions
of use, and factors explaining usage (see Table 3). The first author, who was not previously involved in OUA activities with teachers, coded the first interview, which was then
independently coded and analysed by the second author to ensure inter-rater reliability. The
inter-rater percentage agreement, which equalled to 90%, was calculated by dividing the
number of times both researchers agreed by the total number of times coding was possible
(Boyatzis 1998). Areas of disagreement referred to renaming codes to enhance comprehension and splitting one code into two sub-categories. Agreement was reached between the
two coders and changes were fed into the coding of the rest of the transcripts. The final
coding scheme and analyses were conducted by the first author. The third author who was
involved in delivering OUA training sessions to teachers, was not involved in determining
the final list of themes, yet he reviewed drafts of the analysis and improved the interpretation of the outcomes by providing contextual information related to teachers and their practice. Figure 6 presents the times per week each interviewee accessed the OUA dashboard.
These data were discussed in the interview analysis (see “Phase 2: qualitative experiences
of teachers using OUA” section).
Results
Phase 1: quantitative impact of OUA on students’ performance
Tables 4 and 5 present descriptive statistics about the continuous and categorical variables entered in the model, including the two dependent variables (pass and completion). In
categorical variables with more than two options (see Table 5), reference categories were
mixed race, postgraduate qualification, and Health Care.
In relation to RQ1, two binary logistic regression analyses were performed with dependent variables completion and pass indicators. In terms of completion, a test of the full
model against a constant only model was statistically significant, indicating that the predictors as a set reliably distinguished between students who complete and students who do not
complete a course (Χ2(24)
=
80.84, p < .001). Nagelkerke’s R2 of .181 indicated a moderately weak relationship between prediction and grouping (18% of variance explained by the
proposed model in completion rates). Prediction success overall was 72.9% (25.4% for not
completing a course and 92.4% for completing a course). The Wald criterion demonstrated
that only OUA weekly usage (p
=
.003) and students’ best previous course score (p
=
.003)
1 3

<!-- page 15 -->
1 3
Table 2 Interview questions
No Pillars Sample questions Theoretical models
1 Teachers’ background Which courses do you teach?
What are the objectives?
2 The impact of OUA on teaching What are your first impressions of using OUA? Was it easy to understand and use it?
Did you make any changes to your teaching approach because of the
insights gained from OUA?
Has OUA backed up your own intuition as to who may be at risk?
Did you take any action when a student was flagged as at-risk?
3 Teachers’ concerns and feelings about OUA How did you feel about using OUA in your practice?
Do you have any concerns around its use?
Do you foresee any problems?
4 Future use and intentions Would you use OUA in the future and if so, how?
Is it something you would use systematically in your practice?
TAM (PEU/PU)
ARM (cognitive attitudes)
ARM (emotional attitudes)
TAM (PU)
ARM (intentions)
A large-scale implementation of predictive learning analytics…

<!-- page 16 -->
C. Herodotou et al.
Table 3 Emerging themes identified through thematic analysis
Emerging themes Sub-categories of themes
OUA features Perceived usefulness of OUA Approaching students at risk Informing learning design Improvements to OUA Intention to use OUA in the future Features of the OUA dashboard that are used by teachers
Frequency of use
Ease of use
Teachers’ perceptions of OUA as being useful or not
In what respect OUA supports teaching practices
How teachers react to students flagged as being at risk
What intervention strategies they devise to support students
How OUA could be used to inform the design of a course
Teachers’ suggestions for improving OUA
Teachers’ intentions to use OUA in the future
Fig. 6 Number of times per week each interviewee accessed the OUA dashboard. X axis indicates the
respective week of the term for participating courses. Y axis indicates individual interviewees (n
=
6)
made a significant contribution to prediction. All other predictors were not significant. To
evaluate the performance of the classification for completion, the Area Under the ROC
Curve was examined. This was statistically significant and calculated as .737 (p < .001),
suggesting that the accuracy of the proposed classification is fair or acceptable.
In terms of effect size, the odds ratio was examined. Exp (B) value indicates that
when OUA usage is raised by one unit, that is a teacher is accessing OUA .1 or 10%
more of the duration of the course weeks, the odds ratio is 7,4 times as large and therefore students are 7,4 times more likely to complete the course (see Table 6). These findings indicate that increasing engagement with OUA predictions and greater best overall previous score were associated with an increase in the likelihood of completing a
course. It is yet noted that a low percentage of prediction suggests that additional variables are likely to explain variability in the outcome variable. One such variable may
be the teacher’s general engagement with students (i.e., interactions to provide support,
resolve questions). For example, a proactive teacher who does not make use of OUA
may have students with better performance outcomes compared to teachers that are less
supportive and systematically engaged with students.
In terms of passing the course, a similar picture was revealed (Χ2 (24)
=
84.83,
p < .001). Nagelkerke’s R2 of .177 indicated a moderately weak relationship between
prediction and grouping. The model explains 18% of the variance in passing rates and
correctly classified over 69% of the cases. In particular, prediction success overall was
1 3

<!-- page 17 -->
1 3
Table 4 Descriptive statistics of continuous variables entered in the regression model
Variable Description Min Max M SD N
Teacher variables
OUA weekly usage Usage of OUA relative to length of each course; Percentage of course weeks
.0 .91 .22 .21 1325
OUA was accessed at least once.
Course presentations per teacher Number of (any) course presentations a teacher completed 1 119 26 21 1325
Students per course presentation Number of students assigned to a teacher 10 32 21 4 1325
Student variables
Age Student age 13 79 33 11 1325
Sum of previous credits Sum of the credits previously achieved and linked to the current qualification 0 340 32 66 1249
Best overall previous score Best overall course score from previous study 0 98 51 34 642
A large-scale implementation of predictive learning analytics…

<!-- page 18 -->
C. Herodotou et al.
Table 5 Descriptive statistics (%)
for categorical data entered in the
regression model
Pass rates
Passed 802 60.5%
Failed 523 39.5%
Total 1325 100%
Completion rates
Completion 63.8%
Non-completion 28.9%
Total 1325 100%
Gender
Male 53.7%
Female 46.3%
Total 1325 100%
Disability
Yes 17.5%
No 82.5%
Total 1325 100%
Ethnicity
Asian 4.5%
Black 3.9%
Mixed 2.2%
White 86.9%
Total 1325 100%
Qualifications
A Level or Equivalent to two A levels 45.1%
HE qualification. 13%
Lower than A level 36.5%
No formal qualification 2.9%
Postgraduate qualification 2.3%
Missing 0.2%
Total 1325 100%
IMD band
0–25% 22%
25–50% 26.3%
50–75% 24.5%
75–100% 23.2%
Total 1274 100%
New/continuous
New 54.8%
Continuous 45.2%
Total 1325 100%
Courses
Arts 4.2%
Social science 5.2%
Education 19.8%
Health care 1.8%
Maths 14%
Engineering 11.5%
1 3

<!-- page 19 -->
A large-scale implementation of predictive learning analytics…
Table 5 (continued) Technology (2015) 18%
Technology (2016) 7%
Law 18.6%
Total 1325 100%
Table 6 Logistic regression model estimating effects of independent variables on completion (N
=
1325)
Variable B SE Wald p value Exp(B)
OUA weekly usage 1.998 .667 8.987 .003* 7.377
Couse presentations per teacher .003 .006 .315 .575 1.003
Students per course presentation −
.016 .027 .349 .554 .984
Age .010 .010 .916 .339 1.010
Disability .000 .000 2.389 .122 1.000
Sum of previous credits .004 .002 2.456 .117 1.004
Best overall previous score .012 .004 8.808 .003* 1.012
New −
.545 .374 2.130 .144 .580
Gender −
.098 .233 .178 .673 .906
Arts −
.749 1.199 .391 .532 .473
Social science −
.547 1.240 .195 .659 .579
Maths −
.213 1.153 .034 .854 .808
Engineering −
Technology (× presentations) −
Law .953 1.179 .653 .419 .386
.973 1.170 .692 .406 .378
.071 1.154 .004 .951 1.074
Education course .117 1.159 .010 .920 1.124
Ethnicity Asian 1.026 .938 1.199 .274 2.791
Ethnicity Black −
.667 .741 .810 .368 .513
Ethnicity White −
.356 .618 .331 .565 .701
IMD band .063 .092 .463 .496 1.065
A Level or Equiv. 1.161 .684 2.883 .090 3.193
No formal qualification −
.162 .842 .037 .847 .850
HE qualification 1.049 .706 2.208 .137 2.856
Lower than A level .671 .678 .978 .323 1.956
(constant) −
.112 1.618 .005 .945 .894
Model χ2
=
80.84, df
=
24, p < .001
69.5% (35.5% for not passing a course and 87.6% for passing a course). The Wald criterion demonstrated that only OUA weekly usage (p
=
.001) and students’ best previous
course score (p
=
.001) made a significant contribution to prediction. Odds ratio value
indicated that when OUA usage is raised by one unit, the odds ratio is 7.5 times as large
and therefore students are 7.5 times more likely to pass the course (see Table 7). In line
with existing studies suggesting that the instructor’s role (e.g., Arbaugh 2014; Ma et al.
2015) and students’ success in previous courses (e.g., Hachey et al. 2014) are predicting
performance, these findings indicate that the increasing engagement of teachers with
OUA predictions along with the students’ greater best overall previous score are associated with an increase in the likelihood of passing a course. To evaluate the performance
1 3

<!-- page 20 -->
C. Herodotou et al.
Table 7 Logistic regression model estimating effects of independent variables on pass rates (N
=
1325)
Variable B S.E. Wald p value Exp(B)
OUA weekly usage 2.010 .617 10.595 .001* 7.461
Couse presentations per teacher .002 .005 .111 .739 1.002
Students per course presentation .002 .026 .008 .928 1.002
Age .009 .009 .932 .334 1.009
Disability .000 .000 3.067 .080 1.000
Sum of previous credits .002 .002 .865 .352 1.002
Best overall previous score .012 .004 10.084 .001* 1.012
New/continuous −
.740 .369 4.029 .045 .477
Gender −
.191 .220 .750 .386 .826
Arts −
1.110 1.180 .884 .347 .330
Social science −
.300 1.212 .061 .805 .741
Maths −
.272 1.144 .057 .812 .762
Engineering −
Technology (× presentations) −
Law −
1.007 1.170 .741 .389 .365
1.720 1.158 2.207 .137 .179
.113 1.144 .010 .921 .893
Education course −
.292 1.145 .065 .799 .747
Ethnicity Asian .912 .842 1.174 .278 2.490
Ethnicity Black −
.317 .699 .206 .650 .728
Ethnicity White −
.287 .569 .255 .614 .750
IMD band .024 .086 .076 .783 1.024
A Levels or Equiv. 1.158 .617 3.518 .061 3.183
No formal qualification .249 .796 .098 .754 1.283
HE qualification 1.132 .637 3.160 .075 3.102
Lower than A level .745 .614 1.474 .225 2.107
(constant) −
.205 1.553 .017 .895 .814
Model χ2
=
84.83, df
=
24, p < .001
of the classification (passing), the area under the ROC Curve was examined. This was
statistically significant and calculated as .724 (p < .001), suggesting that the accuracy of
the proposed classification is fair or acceptable.
The following examples of students exemplify further the outcomes of the regression
analysis: (a) Low OUA usage—Low previous performance: “Student 857” is female,
41 years old, attending an education course. Her previous best score is 14% and her teacher
accessed OUA 2% of the weeks of the course (approx. 1 week out of 40). This student
is more likely to fail their studies as both predictors of performance are relatively low.
(b) High OUA usage—Low previous performance: “Student 869” is female, 34 years old
attending an education course. Her teacher has accessed OUA 46% of the weeks of the
course (approx. 16 weeks out of 40) and her previous best score is 28%. Despite the low
previous score, this student may complete and pass their studies given the teacher’s usage
of OUA.
1 3

<!-- page 21 -->
A large-scale implementation of predictive learning analytics…
Phase 2: qualitative experiences of teachers using OUA
Access to OUA dashboard
In order to address RQ2 and RQ3, we analysed data from six interviews with teachers who
used OUA in their teaching practice. Figure 6 shows the times per week each of the six
interviewees logged into the dashboard. The majority of the participating teachers did not
access the dashboard regularly (i.e., every week when predictions were updated), yet they
accessed it throughout a course presentation at selected weeks. Some of them were found
to be more active in the first few weeks of the course, in particular, interviewees 1, 4 and
5, who logged in the dashboard more than once per week. Logging in activity was found
to decline after the first few weeks of a course presentation. The selected use of the dashboard might suggest that teachers chose to check OUA data at certain points, such as near
an assignment submission week (i.e., 4–6 times per course). This infrequent access to OUA
data by teachers might have limited the potential effectiveness of OUA interventions.
Thematic analysis
OUA features The two main functions teachers found more interesting and helpful when
they made use of the OUA dashboard were the OUA colour-coded system indicating students “at risk” (i.e., Fig. 3) and students’ activity in the VLE (i.e., Fig. 2). Interviewed teachers mostly gave attention to students who were flagged as red or amber rather than those
flagged as green (indicating no risk). However, one teacher indicated that: “I found it quite
encouraging to look at the ones who are doing well and then sending emails and encouraging those […] it’s quite a good tool to use on both ends of the spectrum” (Interviewee 1,
male). In addition, the level of the VLE activity comprised a major indicator of whether
students were engaged with the course, the materials, and whether they will submit their
next assignment. As explained by Interviewee 2:
“I just drill down to my students and look through for the red […] I won’t look at
the nearest neighbour or anything like that. I generally just have a look at how much
they’ve been interacting on the VLE and with the website” (Interviewee 2, female).
From the teacher analytics data, teachers were found to access OUA rarely usually
before the submission of an assignment. Interviewed teachers stressed the voluntary nature
of their interaction with OUA and the fact that they could individually determine whether
using OUA would be time-consuming or not. The below excerpt also points to the easy
of using the system—“a quick glance” would suffice to identify students at risk (see also
another reference by Interviewee 2 “I think it’s quite straightforward”):
“I think that would depend on how many students were at risk. I think it could be
time consuming but I think it’s as time consuming, as you want it to be perhaps […].
You could use it as a quick glance or you could spend a lot of ‘me drilling down and
having a look at particular students” (Interviewee 2, female).
Overall, the type of interaction with OUA was found to vary and be rather limited to
specific features of OUA. Specifically, teachers were those deciding how and what features of OUA to use, including the colour-coded system and the VLE activity. Other
system features, such as the nearest student functionality, indicating how a student’s
1 3

<!-- page 22 -->
C. Herodotou et al.
performance approaches or deviates from others in different course presentations, were
not used by teachers. In contrast, OUA was perceived as easy to use and straightforward
(see also “Improvements and intention to use OUA in the future”, suggestions for changes
were unrelated to the easy of using OUA). An interesting contradiction is highlighted when
participants’ consistently strong ease-of-use is considered alongside their varied ways of
engaging with OUA features. While the ease-of-use condition proposed by TAM for “technology acceptance” appears to have been met, it appears that users’ perceptions of easeof-use were formed in referenced to different functions, with some interviewees accessing
only specific features of the system and avoiding others.
Usefulness of OUA Participating teachers perceived OUA as a very useful tool for a range
of reasons that often related to existing teaching practices and expertise. For participants
who tended to check on their students often, either through sending emails, or checking
the forums for students’ activity, OUA provided a useful tool that systematized these practices, and made it easier to identify what students were doing at certain times. For other
participants, OUA influenced their teaching practices by making them more proactive in
contacting students when needed and being “on top” of what students were doing at a given
moment. Participating teachers found OUA particularly useful in between the submission of
their assignments, especially for those students who did not engage with forums or online
activities. It could be argued that teachers’ cognitive evaluations of OUA were very positive,
pointing to low levers of academic resistance, as explained by AR, and in relation to the
cognitive dimension of attitudes.
As evidenced previously, many groups of students may not be engaged with discussion forums in terms of posting, but they do read and reflect on contributions by peers
(Macfadyen and Dawson 2010; Mazzolini and Maddison 2003; Romero et al. 2013). These
“ghost” students were relatively invisible to teachers. OUA provided some insights into
their engagement behaviour. This early indicator of students’ activity could prevent a possible non-submission of an assignment as teachers were more inclined to intervene and
support a given student. OUA provided an indication as to when a teacher should intervene
and, as explained by a teacher, “where I need to put my efforts” (Interviewee 6, male).
OUA was perceived as a tool that complemented existing teaching practices, such as contacting students and checking their activities online. As explained by teachers:
“I love it. […] It brings together the things that I would normally do so if I haven’t
heard from a student then I will often have a look to see when they were last online
or have a look see if they’re getting involved on the forums” (Interviewee 2, female).
“One of the things that the OUA a hundred per cent has been made me do is being
much more proactive in sending out messages around in between assignments –
group messages […] I sort of feel that I am on top of what the students are doing”
(Interviewee 5, female).
The OUA predictions as to who might be at-risk of not submitting their next assignment
aligned well with the teachers’ own assumptions of who might be at-risk. Yet, in some
cases OUA provided additional insights as a teacher might have not identified a student
as being at-risk without the support of OUA. In addition, the role of the teachers in interpreting OUA predictions was crucial. As was previously found (Dyckhoff et al. 2012; van
Leeuwen et al. 2014), teachers were aware of the nature and particularities of each course
and were able to judge whether a student “at risk” as predicted by OUA required further
attendance or not:
1 3

<!-- page 23 -->
A large-scale implementation of predictive learning analytics…
“I might be worried about a student because I haven’t heard from them whereas OUA
can tell me that they’ve been getting involved and that it’s quite likely that they will
be okay. […] it generally just confirms my suspicions but with those two cases I had
no idea” (Interviewee 2, female).
“I don’t think that it is always going to be right. I think that with the nature of this
particular course [maths] people can work offline. […] But then it’s down to me and
my opinion to look into it and see if it is right” (Interviewee 2, female).
While generally teachers’ perceptions of OUA usefulness seem to relate to actual uses,
the following excerpts present a contradiction. Interviewee 2 perceived OUA as “not indepth”, while Interviewee 1 stressed a need for a better understanding of the usefulness
of OUA after becoming engaged with additional features, suggesting that a more in-depth
understanding of OUA might more likely lead to better and more effective use. These two
interviewees share a relatively similar pattern of OUA usage, suggesting that greater perceived usefulness of OUA may not relate to greater actual use or “technology acceptance”,
as TAM advocates. Yet, this is a tentative interpretation as differences between interviewees in relation to the amount of time they spend on OUA and the features they access—not
captured in the current study—may explain this contradiction.
“I think it’s quite straightforward. But it’s not in depth for the things I use it for. I
mean I can just go on and look at my students see if they are “at risk” and drill down.
There’s not a lot to use really from my point of view” (Interviewee 2, female).
“The more experience you have of using it the more you understand how valuable
it is and how you can use it for your particular cohorts[…] I did have a look at such
things gender and qualifications to see if that made a deference in with the way that
they were actually working. […]it’s not a steep learning curve” (Interviewee 1, male).
The discussion in this section also points to the emotional attitudes of teachers, as
explained by AR, in particular their positive feelings and emotions when using OUA for
supporting students. Yet, a form of ambivalence between cognitive and emotional attitudes
is observed; the varied patterns of OUA use (see “OUA features” section) indicate a variation in cognitive beliefs, in relation to which features of the system are accessed and perceived as useful. This variation comes to contrast with consistently positive emotional attitudes, and may suggest that interviewees choose to access those features of OUA they feel
comfortable with, rather than features they do not understand well, or they are challenging,
and that could cause negative perceptions about the system.
Approaching students at risk In line with previous research (Ali et al. 2013; Hanson
2009; Herodotou et al. 2019; van Leeuwen et al. 2014), teachers were found to adopt different approaches when a student was flagged as being at-risk, including a referral to student support services, sending an email, texting, calling, or doing nothing (as they were
aware of why a student is offline). For some teachers, referral to student support services
was the first and straightforward option, yet it did involve additional work:
“I was flagging them up to student support services and it was an extra lot of
work” (Interviewee 5, female).
Other teachers chose to send an email, give a call or text students. The reasons behind
a given choice varied. The following two excerpts indicated that teachers have different
perceptions as to what the best way of reaching students might be:
1 3

<!-- page 24 -->
C. Herodotou et al.
“I start off with a couple of emails because I find most students prefer email contact but they haven’t replied and then I do follow up with a phone call” (Interviewee 4, female).
“I prefer to give them a call because I think the highest level of communication
you can get is the best one. If you speak to someone you can read a lot more from
their voice” (Interviewee 2, female).
Reaching students was not always successful. Some teachers faced challenges due to
students not replying to emails, calls, or texts. In such cases, teachers made a reference
to students support services. As explained by a teacher: “It sorts of ties in quite well
with the support—the student support system […][they] can obviously chase up the students from a novel angle” (Interviewee 1, male). Overall, it remains unclear which intervention strategy may be the most effective one in order to motivate and support students
“at risk” and potentially help them complete and pass their studies.
These insights point to an underlying variation in terms of teaching approaches and
perceptions of what the teachers’ role might actually be (Hanson 2009; Mazzolini and
Maddison 2003; Norton et al. 2005; Rienties et al. 2013). Some teachers seemed very
persistent in reaching out to students, while others were less pro-active or persistent.
Others perceived a referral as the action to be taken forward when a student was flagged
at risk. These differences became more apparent when teachers were asked to describe
how they perceived their teaching role in the course they taught. As explained:
“I find a lot of my time is spent encouraging the lesser able students rather than
engaging with the better students to improve their approach to their studies and
things. It’s about maintaining people on the course so that they can have a chance
of progressing to the next level” (Interviewee 6, male).
The ways teachers checked on their students’ performance varied in terms of persistency, pro-activeness, and sources of information accessed. The following excerpts
point to persistent teachers who checked on students regularly:
“I kept looking at their contact history, one of them again I could see nothing […]
but I say okay I will do it one more time. I contacted them. No answer. Left a
voice message for them. That was lost now. Again, I emailed them. Lost now. So
far nothing” (Interviewee 3, female).
“ if I haven’t had contact from a student I’ll search around on the website and
see if they are getting engaged in other ways like in the forums or when they last
logged in but that’s about all I have normally whereas with OU Analyse you can
see how much they are getting involved” (Interviewee 2, female).
Informing learning design Teachers made suggestions as to how information from
OUA could be used to inform the design of their courses, such as the addition of activities to boost students’ motivation:
“If it looked like people were losing motivation at a certain point I would probably try and get an online tutorial together to check on everybody” (Interviewee 2,
female).
“quite often we lose them between the second and third TMA or the third and
fourth TMA so I don’t know if this highlights the need to find some way to engage
them better between TMAs” (Interviewee 4, female).
1 3

<!-- page 25 -->
A large-scale implementation of predictive learning analytics…
Yet others perceived the use of OUA as of help to the teacher per se and not relevant
to improving content:
“It’s just being in touch with the student and picking up the student at earlier stage
[…]. to my knowledge, it won’t help in the content – the course” (Interviewee 3,
female).
Improvements and intention to use OUA in the future Teachers would like OUA to
become more “sensitive” and provide information as to what students were engaged with
at certain times in the VLE, such as which course activities they work on. As explained:
“ If it was more sensitive to what students were accessing or what they were doing
in terms of their literacy and numeracy skills […] I think it could probably influence my teaching and my practise”(Interviewee 5, female).
Teachers asked for improvements in what information can be recorded by teachers
in OUA, such as their own outstanding actions (e.g., follow-up students who have not
replied) and accessing OUA information through a single teacher portal to minimise
workload. One teacher who devised her own strategy to monitoring students’ progress
using excel sheets explained:
“what I do when I get my first batch of students I download the students’ names
into a spreadsheet and from there I add columns so I can record who has done
their TMA, who was doing the group activity etc. Because now OUA was doing
some of that for me I can add actions and updates. I think if that could be developed further I think that could replace the need for me to keep a separate spreadsheet” (Interviewee 4, female).
The proposed changes above could be viewed as manifestations of teachers’ cognitive resistance to using OUA at its current form, which when waived away, could facilitate adoption, and potentially encourage more systematic usage. These cognitive beliefs
are also in contrast to teachers’ intention to using OUA in the future; although a considerable interest for future use was recorded, teachers raised concerns in relation to some
of its functionality that might inhibit use, such as being sensitive to students’ specific
actions online:
“I think I’ve now got to grips with it and when some changes were made I will be
very interested in using it again. Very supportive of it” (Interviewee 5, female).
In terms of academic resistance, as explained by AR, participating teachers expressed
positive emotional and intentional attitudes about OUA, yet these were in contrast to
their cognitive beliefs and the inconsistency observed in relation to OUA features they
choose to use and find useful as well as their suggested changes to the system.
Discussion
In this multi-method study, we described and explored a university-wide implementation of PLA in a distance learning higher education institution in which 59 teachers and
1325 students from nine courses participated. Participating teachers were granted access to
PLA data produced weekly by OUA, a system designed to predict students “at risk” of not
1 3

<!-- page 26 -->
C. Herodotou et al.
submitting their next assignment. Whether and how predictive data should be used was up
to the teachers to decide along with the identification of an intervention strategy to support
students flagged as being at risk.
In our multi-method approach, we first explored the quantitative impact of teachers’
use of OUA on students’ performance. With regards to the extent to which OUA usage by
teachers predicts students’ performance (RQ1), binary logistic regression analysis with student, course, and teacher variables as predictors revealed that engagement with and usage
of OUA, along with the students’ success in previous courses, positively predict students’
pass and completion performance. The more teachers make use of OUA data and the more
successful students were in previous courses, the likelihood of completing and passing a
course increases. These findings emphasise that, in addition to previous student performance, teachers play a crucial role in online learning settings. While other studies emphasised aspects of teaching such as guidance and assistance for completing online activities
(Ma et al. 2015) or teaching presence as perceived by students (Arbaugh 2014), this study
revealed how usage of a predictive system, OUA can contribute positively to students’
performance. At the same time, as indicated by the user statistics of OUA, many teachers
seemed reluctant to frequently engage with the system on a weekly basis.
These findings are significant as they are starting to shed light on our rather limited
understanding of how teachers’ usage of learning analytics may relate to student performance. Existing studies presenting mixed effects (van Leeuwen et al. 2015, p. 28), captured
teachers’ perceptions of analytics in experimental set ups, rather than in naturalistic settings, and in a relatively short period of time. In contrast, in the present study participating
teachers were given access to “live” student data and their participation was monitored
over the duration of a course presentation (long term). These methodological differences
may explain why the present study have reached more conclusive outcomes whereas previous studies have not.
Yet, any causal interpretation of the above findings should be treated with caution, as
additional variables, not captured in the regression analysis may have had an influence
or explain student learning outcomes. For example, teachers who are more engaged with
their students (i.e., interactions to provide support, resolve questions) may have students
with better learning outcomes compared to teachers that are less supportive and engaged
with students (Herodotou et al. 2019). These teachers may well be those actively using
OUA, and this may be a factor mediating the relationship between OUA usage and learning outcomes. Future studies should examine in particular whether PLA-guided support
to students is more effective than less data-intensive approaches such as accessing student information hosted in the University’s management system (e.g., last student log in
date, demographics, TMA score and submission). Towards this direction, Herodotou et al.
(2019) identified that teachers with relatively low or no usage of OUA had worse performing students than teachers with high usage of the system. Also, teachers with average OUA
use had better performing students when using the system, than the year before when they
had no access to OUA (and after controlling for variation in student performance characteristics). These findings suggest that PLA-guided support is actually significantly better than
other less-data intense support approaches devised by teachers. Similarly, the actual design
of different courses (level of difficulty of course material, assessment points etc.) may have
had an impact on students’ engagement with the material affecting the chances of completing and passing their courses. Also, the actions teachers have or have not taken in response
to OUA insights may also relate to student learning outcomes as they may have facilitated
learning or empowered learners to reach course completion.
1 3

<!-- page 27 -->
A large-scale implementation of predictive learning analytics…
Another aspect that should be considered in interpreting these outcomes is the number
of teachers participating in the study (N
=
59) and the mean OUA engagement (M
=
.22;
Max
=
.91). A further examination of the distribution of OUA usage across teachers
showed that the median of use was .13, suggesting that half of the teachers had rather limited access to the system. Therefore, it is likely that a relatively small number of teachers
who demonstrated intensive usage had an outsized impact on the analysis, explaining the
high coefficient of OUA usage in the regression models.
In Phase 2, we explored the experiences of teachers who made use of OUA to improve
our understanding of why some teachers were actively using OUA in their practice, while
others teachers were perhaps reluctant to embrace the system. With regards to the extent to
which participating teachers made use of OUA data and visualisations to help students “at
risk” (RQ2) and the factors that explain teachers’ use of OUA (RQ3), six semi-structured
interviews with teachers-volunteers were conducted building on the theoretical lenses of
TAM (Davis 1989) and ARM (Piderit 2000). Insights revealed how OUA was used and
in what degree. In line with Perceived Usefulness of TAM (Davis 1989; Sanchez-Franco
2010), teachers reported to make use of specific features of OUA only, including the colour-coded system and the VLE activity. The OUA teacher usage data indicated that most
teachers used OUA rather infrequently, primarily for a short period of time just before the
submission of an assignment. In terms of the use of the ‘risk indicators’, teachers reported
that the predictions reaffirmed their suspicions about who might be at risk. Yet, in some
cases, OUA predictions provided additional insights a teacher might not have identified
without the support of the system. In terms of perceived ease of use (Davis 1989; Rienties
et al. 2016), teachers found OUA simple to use, faced no obstacles when accessing data,
and view the tool as not being time-consuming.
OUA was perceived by teachers as either complementing existing student monitoring
practices or influencing proactive engagement with students. For teachers used to checking
on students and their progress often, it systematised their practices and made it easier to
identify what students were doing at certain times. For others, it influenced their practices
positively by making them more proactive in contacting students when there was a need
and illuminated students’ activity in between the submission of assignments, especially for
those students who did not engage with e.g., forums or other online activities. It could
be argued that, even though the perceived usefulness of OUA was subjectively defined,
teachers were not reluctant to use OUA and they found value in its use as complementing
their own existing practices or empowering them to become more proactive with students
(RQ3).
A variation was observed in terms of the type of intervention strategy teachers adopted
to support students at-risk and their level of persistence in reaching students. Each teacher
devised their own approach, including making a phone call, sending an email, or referring
the student to support services. Yet, it remains unclear which intervention strategy was the
most effective one in order to support students “at risk” and potentially help them complete
and pass their studies (Rienties et al. 2016; van Leeuwen et al. 2014). This is the focus of
follow-up studies that take place at the university under study at the moment; a number of
different intervention strategies are piloted to identify which of them effectively supports
‘at-risk’ students.
Overall, teachers expressed interest in using OUA in the future to better support students “at risk” and improve the design of the courses they are teaching by, for example,
designing additional activities when engagement between assignments tails off. In relation
to RQ3, academic resistance, as conceptualised by (Piderit 2000), towards the use of analytics to support teaching activities was shown to relate to cognitive beliefs, in particular
1 3

<!-- page 28 -->
C. Herodotou et al.
teachers’ inconsistency in terms of which features of OUA they access and perceive as useful, as well as certain enhancements to the system that could facilitate adoption. Emotional
and intentional aspects of resistance were shown to align with teachers expressing positive feeling about OUA and declaring their intention to use it in the future. It is noted that
teachers in this study were self-selected, with obvious self-selection limitations. A large
number of teachers seemed to vote with their feet by not engaging with OUA at all or only
close to the assessment deadlines. Previous studies have highlighted that the time window
of opportunity to effectively support students at-risk is relatively short (Gasevic et al. 2016;
Tempelaar et al. 2015), ranging between 2 and 4 weeks.
A paradox is observed between the teachers’ perceptions about the usefulness of OUA
and their actual, rather infrequent use of the system. Although the use of OUA was an
optional activity for teachers, Figs. 5 and 6 show evidence of lack of regular use and ongoing engagement with it. Briefing online sessions about what PLA are, what tools are available, and how they could be used to support the teaching practice were organised and
offered to participating teachers before the start of their courses. While teachers were aware
of the sessions well in advance, actual participation was very limited in the range of 5–6%.
This lack of interest and motivation in using OUA should be examined considering for the
teachers’ contractual agreement with the university and the conditions under which they
teach. Teachers do not hold permanent positions within the university; they are contracted
employees whose contracts renew on a yearly basis. The great majority of them are parttime employees and teaching is not their primary source of income as they usually hold
other full-time positions. These conditions may relate to viewing themselves as temporary
staff of the university for whom professional development is not essential. In addition,
teachers’ contracts do not foresee participation in OUA, or other relevant activities, raising
additional barriers to participation.
The lack of interest in engaging or adopting OUA may also relate to other factors such
as limited time availability to engage with extracurricular, professional development activities, teachers’ ‘trust’ to OUA data as opposed to directly communicating with students, and
teachers’ lack of competency in interpreting OUA insights and taking appropriate action.
These considerations may also explain the above paradox; while expressing an interest in
using OUA in the teaching practice, teachers made limited and rather infrequent use of it.
Given the positive results of logistic regression analysis, it could be argued that usage of
OUA by teachers would benefit students and lead to better learning outcomes. In addition
to effective predictive analytics tools, a clear and supportive management and professional
development structure needs to be in place to empower teachers to pro-actively help students flagged as “at risk” (Herodotou et al. 2019; Mor et al. 2015). Managerial arrangements should provide technical and pedagogical support to teachers when using OUA,
offer teachers training as to how to use OUA on a yearly basis before and/or during a new
course presentation, and set up a virtual space for sharing good practice around the use
of OUA within the teaching community, raise and negotiate concerns and access relevant
sources of information. Also, the use of OUA should be included in contractual agreements as a tool that can support students’ learning and inform the teaching practice. Any
requirements for additional professional development activities related to OUA should be
compensated accordingly.
1 3

<!-- page 29 -->
A large-scale implementation of predictive learning analytics…
Conclusions
This study about the use of OUA by 59 teachers and 1325 students at a distance learning higher education institution has illustrated teachers’ actual uses and practices in relation to OUA data and indicated a variation in teachers’ degree and quality of engagement
with learning analytics. This variation was evidenced in how often predictive data were
accessed, what predictive data teachers looked at and foremost, how teachers acted on this
data to support students. Despite the lack of consensus, greater OUA usage was found
to predict better completion and pass rates, suggesting that systematic engagement with
OUA should become a significant aspect of the teaching practice as it can improve student
performance.
Yet, this may not be a straightforward endeavour. What is required is teachers who are
willing to use and act upon PLA data for the benefit of their students and of the teaching
practice. This study highlights that, at this early stage of OUA development and diffusion
in the teaching and learning practice, access to OUA did not result in systematic use of
OUA. This finding has certain implications in terms of actions that facilitate OUA acceptance and best use including, for example, allowing time for teachers to engage with and
understand the potential of PLA to support learning, designing easy to understand and use
visualisations, and providing teachers with PLA features that are theoretically informed,
unpack learning processes and highlight areas students struggle with. Towards this direction, the PLA system used in this study provides recommendations as to the content areas
a student should engage with in order to cope with course requirements and submit their
next assignment. Successful case-studies of PLA data use by teachers could work as a stepping stone for capturing the teachers’ interest and diverting their efforts towards using PLA
to support students in need. In addition, certain implementations of PLA could facilitate
technology acceptance more than others. As interview data revealed in this study, PLA
provided through the OUA dashboard were perceived as easy to use and useful by teachers, suggesting that OUA is a suitable PLA tool for use by teachers. Yet, further actions are
needed to facilitate adoption, such as ongoing support and appropriate training in interpreting and effectively acting upon OUA data.
Moreover, findings from this study revealed that OUA was a significant source of information for teachers that can enhance and facilitate the teaching practice, especially within
distance learning contexts where teacher-student interactions can be restricted (Mazzolini
and Maddison 2003; Rienties et al. 2013; Simpson 2013). This finding has certain implications in terms of whether and how PLA tools could be used in the teaching practice;
PLA tools can be particularly useful to teachers as they can alert them about students who
may require special attention or support to proceed with their learning, enhance and complement teaching strategies, in particular, within distance learning contexts. Such insights
could lead to proactive teaching practice; teachers approaching students flagged as at risk,
discussing their progress and performance, identifying possible learning difficulties and
providing ‘real-time’, tailored support to accommodate students’ learning needs.
In addition, this study has implications relevant to the design of online courses; PLA
insights could lead to ‘live’ or retrospective changes to a course. This may require adaptations or modifications of teaching activities or lesson plans to host the delivery of additional activities that can scaffold a specific cohort of students and address their learning
needs. Alternatively, PLA could be used retrospectively to inform the design of a course
such as spreading the workload evenly across weeks to ensure that students cope with
requirements and manage to submit assignments on time. It may also entail guidance on
1 3

<!-- page 30 -->
C. Herodotou et al.
how much time is needed to prepare an assignment, how to organise workload and prioritise activities to ensure that deadlines are met and assignments are delivered at the standards required.
While van Leeuwen et al. (2014) found a significant positive impact of providing
learning analytics dashboards to teachers in a small-scale study of 20 teachers, additional
research in large-scale settings across multiple courses and disciplines is needed to measure the impact of teachers’ interventions on students’ progress and retention. Findings from
this study revealed a variation in intervention strategies devised by teachers to support students flagged as at risk, suggesting that more research is needed to identify how, when, and
what interventions to trigger to adequately support students (Rienties et al. 2016; Torgerson and Torgerson 2008). For example, we need to understand whether we must intervene
with a student as soon as they are flagged as “at risk” of not submitting an assignment, or
wait for the next set of predictions before action is taken (Gasevic et al. 2016; Mor et al.
2015; van Leeuwen et al. 2015).
Towards this direction, we have set up the Early Alert Indicators project in order to
examine the impact of specific intervention strategies on students’ retention with teachers
from 25 courses. The two-year project is expected to gather more evidence on the usefulness and effectiveness of using predictive data to support students. It will examine in particular how usage of OUA before an assignment deadline may relate to students’ submitting
(or not) the assignment on time and associated grades. To overcome the self-selecting bias,
predictive data will be shared widely across courses by providing access to all teachers
within a course. Also, it will make use of experimental methodologies including A/B testing and randomised control trials (RCTs) to evaluate the use of predictive data by teachers.
Our overall objective is to identify best practice in the use of predictive data that will assist
teachers to better understand PLA, devise appropriate intervention strategies, and engage
students at-risk with learning prior to failing or not completing their studies.
Compliance with ethical standards
Conflict of interest The authors declare that they have no conflict of interest.
Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creat iveco mmons .org/licen ses/by/4.0/), which permits unrestricted use, distribution,
and reproduction in any medium, provided you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons license, and indicate if changes were made.
References
Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes,
50(2), 179–211. https ://doi.org/10.1016/0749-5978(91)90020 -T.
Ali, L., Asadi, M., Gašević, D., Jovanović, J., & Hatala, M. (2013). Factors influencing beliefs for adoption
of a learning analytics tool: An empirical study. Computers & Education, 62, 130–148. https ://doi.
org/10.1016/j.compe du.2012.10.023.
Ali, L., Hatala, M., Gašević, D., & Jovanović, J. (2012). A qualitative evaluation of evolution of a learning analytics tool. Computers & Education, 58(1), 470–489. https ://doi.org/10.1016/j.compe
du.2011.08.030.
Arbaugh, J. B. (2014). System, scholar, or students? Which most influences online MBA course effectiveness? Journal of Computer Assisted Learning, 30(4), 349–362. https ://doi.org/10.1111/jcal.12048 .
1 3

<!-- page 31 -->
A large-scale implementation of predictive learning analytics…
Bodily, R., & Verbert, K. (2017). Review of research on student-facing learning analytics dashboards and
educational recommender systems. IEEE Transactions on Learning Technologies, 10(4), 405–418.
https ://doi.org/10.1109/TLT.2017.27401 72.
Boyatzis, R. E. (1998). Transforming qualitative information: Thematic analysis and code development.
Thousand Oaks: Sage.
Calvert, C. (2014). Developing a model and applications for probabilities of student success: A case study of
predictive analytics. Open Learning: The Journal of Open, Distance and e-Learning, 29(2), 160–173.
https ://doi.org/10.1080/02680 513.2014.93180 5.
Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319–340.
Davis, F. D., Bagozzi, R. P., & Warshaw, P. R. (1989). User acceptance of computer technology: A comparison of two theoretical models. Management Science, 35(8), 982–1002.
Dyckhoff, A. L., Zielke, D., Bültmann, M., Chatti, M. A., & Schroeder, U. (2012). Design and implementation of a learning analytics toolkit for teachers. Journal of Educational Technology & Society, 15(3),
58–76.
Ferguson, R., & Buckingham Shum, S. (2012). Social learning analytics: Five approaches. Paper presented at the 2nd International Conference on learning analytics and knowledge, Vancouver, British
Columbia.
Gasevic, D., Dawson, S., Rogers, T., & Gasevic, D. (2016). Learning analytics should not promote one size
fits all: The effects of instructional conditions in predicating learning success. Internet and Higher
Education, 28, 68–84. https ://doi.org/10.1016/j.ihedu c.2015.10.002.
Gasevic, D., Dawson, S., & Siemens, G. (2015). Let’s not forget: Learning analytics are about learning.
TechTrends, 59(1), 64–71. https ://doi.org/10.1007/s1152 8-014-0822-x.
Gliner, J. A., Morgan, G. A., & Leech, N. L. (2011). Research methods in applied settings: An integrated
approach to design and analysis. London: Routledge.
González-Torres, A., García-Peñalvo, F. J., & Therón, R. (2013). Human–computer interaction in evolutionary visual software analytics. Computers in Human Behavior, 29(2), 486–495. https ://doi.
org/10.1016/j.chb.2012.01.013.
Greller, W., & Drachsler, H. (2012). Translating learning into numbers: A generic framework for learning
analytics. Journal of Educational Technology and Society, 15(3), 42.
Gutiérrez, F., Seipp, K., Ochoa, X., Chiluiza, K., Laet, T. De, & Verbert, K. (2018). LADA: A learning
analytics dashboard for academic advising. Computers in Human Behavior. https ://doi.org/10.1016/j.
chb.2018.12.004.
Hachey, A. C., Wladis, C. W., & Conway, K. M. (2014). Do prior online course outcomes provide more
information than G.P.A. alone in predicting subsequent online course grades and retention? An
observational study at an urban community college. Computers & Education, 72, 59–67. https ://doi.
org/10.1016/j.compe du.2013.10.012.
Hanson, J. (2009). Displaced but not replaced: The impact of e-learning on academic identities in higher
education. Teaching in Higher Education, 14(5), 553–564. https ://doi.org/10.1080/13562 51090 31867
74.
Herodotou, C., Rienties, B., Boroowa, A., Zdrahal, Z., Hlosta, M., & Naydenova, G. (2017). Implementing
predictive learning analytics on a large scale: The teacher’s perspective. Paper presented at the Proceedings of the Seventh International learning analytics & knowledge conference, Vancouver, British
Columbia.
Herodotou, C., Rienties, B., Verdin, B., & Boroowa, A. (2019). Predictive learning analytics ‘at scale’:
Guidelines to successful implementation in higher education. Journal of Learning Analytics, 6(1),
85–95.
Joksimović, S., Gašević, D., Loughin, T. M., Kovanović, V., & Hatala, M. (2015). Learning at distance:
Effects of interaction traces on academic achievement. Computers & Education, 87, 204–217. https ://
doi.org/10.1016/j.compe du.2015.07.002.
Kuzilek, J., Hlosta, M., Herrmannova, D., Zdrahal, Z., & Wolff, A. (2015). OU analyse: Analysing at-risk
students at The Open University. Learning Analytics Review, LAK15–1, pp. 1–16.
Kvale, S. (1996). Interviews: An introduction to qualitative research interviewing. London: SAGE
Publications.
Liu, F., & Cavanaugh, C. (2012). Factors influencing student academic performance in online high school
algebra. Open Learning: The Journal of Open, Distance and e-Learning, 27(2), 149–167. https ://doi.
org/10.1080/02680 513.2012.67861 3.
Ma, J., Han, X., Yang, J., & Cheng, J. (2015). Examining the necessary condition for engagement in an
online learning environment based on learning analytics approach: The role of the instructor. The
Internet and Higher Education, 24, 26–34. https ://doi.org/10.1016/j.ihedu c.2014.09.005.
1 3

<!-- page 32 -->
C. Herodotou et al.
Macfadyen, L. P., & Dawson, S. (2010). Mining LMS data to develop an “early warning system” for
educators: A proof of concept. Computers & Education, 54(2), 588–599. https ://doi.org/10.1016/j.
compe du.2009.09.008.
Mazzolini, M., & Maddison, S. (2003). Sage, guide or ghost? The effect of instructor intervention on
student participation in online discussion forums. Computers & Education, 40(3), 237–253.
McKenney, S., & Mor, Y. (2015). Supporting teachers in data-informed educational design. British Journal of Educational Technology, 46(2), 265–279. https ://doi.org/10.1111/bjet.12262 .
Mor, Y., Ferguson, R., & Wasson, B. (2015). Editorial: Learning design, teacher inquiry into student
learning and learning analytics: A call for action. British Journal of Educational Technology, 46(2),
221–229. https ://doi.org/10.1111/bjet.12273 .
Nguyen, Q., Rienties, B., Toetenel, L., Ferguson, F., & Whitelock, D. (2017). Examining the designs
of computer-based assessment and its impact on student engagement, satisfaction, and pass rates.
Computers in Human Behavior, 76, 703–714. https ://doi.org/10.1016/j.chb.2017.03.028.
Norton, L., Richardson, T., Hartley, J., Newstead, S., & Mayes, J. (2005). Teachers’ beliefs and intentions concerning teaching in higher education. Higher Education, 50(4), 537–571.
Open University UK. (2014). Ethical use of student data for learning analytics policy. Retrieved June 23,
2016, from http://www.open.ac.uk/stude nts/chart er/essen tial-docum ents/ethic al-use-stude nt-datalearn ing-analy tics-polic y
Papamitsiou, Z., & Economides, A. (2014). Learning analytics and educational data mining in practice:
A systematic literature review of empirical evidence. Educational Technology & Society, 17(4),
49–64.
Piderit, S. K. (2000). Rethinking resistance and recognizing ambivalence: A multidimensional view of
attitudes toward an organizational change. The Academy of Management Review, 25(4), 783–794.
https ://doi.org/10.2307/25920 6.
Pituch, K. A., & Lee, Y.-K. (2006). The influence of system characteristics on e-learning use. Computers
& Education, 47(2), 222–244. https ://doi.org/10.1016/j.compe du.2004.10.007.
Pynoo, B., Devolder, P., Tondeur, J., van Braak, J., Duyck, W., & Duyck, P. (2011). Predicting secondary school teachers’ acceptance and use of a digital learning environment: A cross-sectional study.
Computers in Human Behavior, 27(1), 568–575. https ://doi.org/10.1016/j.chb.2010.10.005.
Richardson, J. T. E. (2013). Approaches to studying across the adult life span: Evidence from distance education. Learning and Individual Differences, 26, 74–80. https ://doi.org/10.1016/j.lindi
f.2013.04.012.
Rienties, B. (2014). Understanding academics’ resistance towards (online) student evaluation. Assessment & Evaluation in Higher Education, 39(8), 987–1001. https ://doi.org/10.1080/02602
938.2014.88077 7.
Rienties, B., Boroowa, A., Cross, S., Kubiak, C., Mayles, K., & Murphy, S. (2016a). Analytics4Action
evaluation framework: A review of evidence-based learning analytics interventions at Open University UK. Journal of Interactive Media in Education, 1(2), 1–12. https ://doi.org/10.5334/jime.394.
Rienties, B., Brouwer, N., & Lygo-Baker, S. (2013). The effects of online professional development
on higher education teachers’ beliefs and intentions towards learning facilitation and technology.
Teaching and Teacher Education, 29, 122–131. https ://doi.org/10.1016/j.tate.2012.09.002.
Rienties, B., Cross, S., & Zdrahal, Z. (2016b). Implementing a learning analytics intervention and evaluation framework: What works? In B. K. Daniel (Ed.), Big data and learning analytics in higher
education: Current theory and practice (pp. 147–166). Heidelberg: Springer.
Rienties, B., Giesbers, S., Lygo-Baker, S., Ma, S., & Rees, R. (2016c). Why some teachers easily learn
to use a new virtual learning environment: A technology acceptance perspective. Interactive Learning Environments, 24(3), 539–552. https ://doi.org/10.1080/10494 820.2014.88139 4.
Rienties, B., Herodotou, C., Olney, T., Schencks, M., & Boroowa, A. (2018). Making sense of learning analytics dashboards: A technology acceptance perspective of 95 teachers. The International
Review of Research in Open and Distributed Learning. https ://doi.org/10.19173 /irrod l.v19i5 .3493.
Rienties, B., & Toetenel, L. (2016). The impact of learning design on student behaviour, satisfaction and
performance: A cross-institutional comparison across 151 modules. Computers in Human Behavior, 60, 333–341. https ://doi.org/10.1016/j.chb.2016.02.074.
Romero, C., López, M.-I., Luna, J.-M., & Ventura, S. (2013). Predicting students’ final performance
from participation in on-line discussion forums. Computers & Education, 68, 458–472. https ://doi.
org/10.1016/j.compe du.2013.06.009.
Sanchez-Franco, M. J. (2010). WebCT—The quasimoderating effect of perceived affective quality on
an extending technology acceptance model. Computers & Education, 54(1), 37–46. https ://doi.
org/10.1016/j.compe du.2009.07.005.
1 3

<!-- page 33 -->
A large-scale implementation of predictive learning analytics…
Simpson, O. (2013). Supporting students for success in online and distance education. New York:
Routledge.
Šumak, B., Heričko, M., & Pušnik, M. (2011). A meta-analysis of e-learning technology acceptance:
The role of user types and e-learning technology types. Computers in Human Behavior, 27(6),
2067–2077. https ://doi.org/10.1016/j.chb.2011.08.005.
Tanes, Z., Arnold, K. E., King, A. S., & Remnet, M. A. (2011). Using signals for appropriate feedback:
Perceptions and practices. Computers & Education, 57(4), 2414–2422. https ://doi.org/10.1016/j.
compe du.2011.05.016.
Tempelaar, D. T., Rienties, B., & Giesbers, B. (2015). In search for the most informative data for feedback generation: Learning analytics in a data-rich context. Computers in Human Behavior, 47,
157–167. https ://doi.org/10.1016/j.chb.2014.05.038.
Teo, T. (2010). A path analysis of pre-service teachers’ attitudes to computer use: Applying and extending the technology acceptance model in an educational context. Interactive Learning Environments,
18(1), 65–79. https ://doi.org/10.1080/10494 82080 22313 27.
Teo, T., & Zhou, M. (2016). The influence of teachers’ conceptions of teaching and learning on their
technology acceptance. Interactive Learning Environments. https ://doi.org/10.1080/10494
820.2016.11438 44.
Torgerson, D. J., & Torgerson, C. (2008). Designing randomised trials in health, education and the
social sciences: An introduction. London: Palgrave Macmillan.
van Leeuwen, A. (2018). Teachers’ perceptions of the usability of learning analytics reports in a flipped
university course: When and how does information become actionable knowledge? Educational
Technology Research and Development. https ://doi.org/10.1007/s1142 3-018-09639 -y.
van Leeuwen, A., Janssen, J., Erkens, G., & Brekelmans, M. (2014). Supporting teachers in guiding
collaborating students: Effects of learning analytics in CSCL. Computers & Education, 79, 28–39.
https ://doi.org/10.1016/j.compe du.2014.07.007.
van Leeuwen, A., Janssen, J., Erkens, G., & Brekelmans, M. (2015). Teacher regulation of cognitive
activities during student collaboration: Effects of learning analytics. Computers & Education, 90,
80–94. https ://doi.org/10.1016/j.compe du.2015.09.006.
Verbert, K., Duval, E., Klerkx, J., Govaerts, S., & Santos, J. L. (2013). Learning analytics dashboard
applications. American Behavioral Scientist, 57(10), 1500–1509. https ://doi.org/10.1177/00027
64213 47936 3.
Viberg, O., Hatakka, M., Bälter, O., & Mavroudi, A. (2018). The current landscape of learning analytics in higher education. Computers in Human Behavior, 89, 98–110. https ://doi.org/10.1016/j.
chb.2018.07.027.
Wolff, A., Zdrahal, Z., Herrmannova, D., Kuzilek, J., & Hlosta, M. (2014). Developing predictive
models for early detection of at-risk students on distance learning modules, Workshop: machine
learning and learning analytics. Paper presented at the learning analytics and knowledge (2014),
Indianapolis.
Wolff, A., Zdrahal, Z., Nikolov, A., & Pantucek, M. (2013). Improving retention: Predicting at-risk students by analysing clicking behaviour in a virtual learning environment. Paper presented at the Proceedings of the Third International Conference on learning analytics and knowledge, Indianapolis.
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional affiliations.
Christothea Herodotou is an Associate Professor at the Open University, UK. She is interested in the evidence-based design and evaluation of technologies for learning (web-based platforms, mobile applications,
digital games) through innovative research methodologies including learning analytics. She is a Senior Fellow of the Higher Education Academy (HEA).
Bart Rienties is Professor of Learning Analytics. He is the programme director of Learning Analytics at the
Institute of Educational Technology, Open University, UK, and head of Data Wranglers, whereby he leads a
group of learning analytics academics who conduct evidence-based research and sense making of Big Data.
Avinash Boroowa is the Project Lead of the Early Alert Indicators Project, a strategic initiative at the Open
University, UK. He leads a multi-disciplinary team of senior academics, data scientists, data analysts and
developers, providing thought leadership in the deployment of predictive analytics to support students.
1 3

<!-- page 34 -->
C. Herodotou et al.
Zdenek Zdrahal is Professor of Knowledge Engineering. He conceived the OU Analyse (2014–present)
concept, which builds on his JISC project RETAIN (2011–2012) and the MSR-OU project with the MS
Research Cambridge.
Martin Hlosta is the technical lead and data scientist of OU Analyse. He has developed the predictive models and he leads the design of OU Analyse, and its integration with OU systems.
1 3
