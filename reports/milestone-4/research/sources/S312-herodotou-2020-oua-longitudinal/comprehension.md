# S312 – The Scalable Implementation of Predictive Learning Analytics at a Distance Learning University (Herodotou et al., Internet and Higher Education 2020)

## Summary in my own words

This longitudinal case study describes four years of OU Analyse (OUA), the Open University's predictive system, reaching 1,159 teachers and 23,180 students in 231 courses, and the factors that helped or hindered adoption. OUA predicts weekly whether each student will submit the next tutor-marked assignment, shows teachers a traffic-light risk list, and combines four simple classifiers (naive Bayes, CART and two k-NN models on demographic and VLE data) by voting. Adoption depended on faculty engagement, teacher champions, evidence of impact and digital literacy, more than on model sophistication.

## Key facts

- Scale – "OUA has been accessed by 1,159 unique teachers and reached 23,180 students in 231 undergraduate online courses."
- Weekly prediction target – "OUA predicts on a weekly basis whether a given student will submit or not their next teacher-marked assignment."
- Traffic-light output – "It uses a traffic light system to pinpoint: in red students at risk of not submitting, in amber those with a moderate probability of failing, and in green those who are likely to be successful."
- Simple models – "OUA employs three machine learning methods: (1) Naïve Bayes classifier (NB), (2) Classification and regression tree (CART), (3) k-Nearest Neighbours (k-NN)."
- Voting – "the result of the prediction is ‘will-not submit next assignment’ if three or all four models give a prediction"
- Data used – "(a) static data: demographics, such as age, gender, geographic region, previous education, and (b) behavioural data: students' interactions within the VLE hosting a course."
- Kuzilek J. et al. (2015, OU Analyse paper; not registered) and Wolff A. et al. (2013, LAK; not registered) are cited for the model design – "(Kuzilek et al. 2015; Wolff et al, 2013)"
- Adoption factors – "the faculty's engagement with OUA, teachers as "champions", evidence generation and dissemination, digital literacy, and conceptions about teaching online."

## Used in

02-01-modeling-briefs.md, 03-03-predictive.md, 03-04-ranking-capacity.md

## Against reference.md

Confirms that the outline's AQ3–AQ4 (early risk list for tutors, built from demographics and VLE activity) mirrors the system the OU itself runs on the population OULAD samples. Differs in target: OUA predicts next-assignment submission weekly, while the project predicts non-completion at day 13 and day 27; the report should state this difference. OUA's simple-model ensemble supports starting from simple, interpretable families.

## Reliability

Primary; peer-reviewed article by C. Herodotou, B. Rienties, M. Hlosta, A. Boroowa, C. Mangafa and Z. Zdrahal, *The Internet and Higher Education* 45, 100725 (2020), doi:10.1016/j.iheduc.2020.100725; read from the author-accepted manuscript at the University of Aberdeen repository (some self-citations anonymised as "Author A et al."). OpenAlex cited-by count 127 as of 2026-11-06. Describes OUA as of 2020; current OUA model details (2026) were not checked.

## Open questions

Whether OUA's model set changed after 2020 is unknown.
