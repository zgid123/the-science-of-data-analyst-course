---
id: S301
url: https://api.openalex.org/works/doi:10.1016/j.jclinepi.2019.02.004
requested: 10.1016/j.jclinepi.2019.02.004
fetched: 2026-11-06T23:05+07:00
tool: fetch.py (curl + json-metadata; ladder L4)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T05
part: 3
raw: raw.json (32 KB)
conversion: json-metadata of https://api.openalex.org/works/doi:10.1016/j.jclinepi.2019.02.004 (metadata, 161 words)
---
source: OpenAlex
title: A systematic review shows no performance benefit of machine learning over logistic regression for clinical prediction models
authors: Evangelia Christodoulou; Jie Ma; Professor Gary S. Collins; Ewout Willem Steyerberg; Jan Yvan Jos Verbakel; Ben VAN CALSTER
institutions: KU Leuven; Leiden University Medical Center; Oxford University Hospitals NHS Trust; University of Oxford
venue: Journal of Clinical Epidemiology
publication date: 2019-02-11
volume: 110
issue: None
pages: 12–22
doi: https://doi.org/10.1016/j.jclinepi.2019.02.004
cited_by_count (OpenAlex): 2180
type: review
location: https://doi.org/10.1016/j.jclinepi.2019.02.004 (open access: False)
location: https://pubmed.ncbi.nlm.nih.gov/30763612 (open access: False)
location: https://research.birmingham.ac.uk/en/publications/9f559fe6-124a-4ba5-89b2-b23e59621707 (open access: False)
location: https://ora.ox.ac.uk/objects/uuid:4167c905-5171-4fc7-b157-ff36d56a73db (open access: False)
location: http://hdl.handle.net/1887/121093 (open access: False)
location: https://scholarlypublications.universiteitleiden.nl/handle/1887/121093 (open access: False)
location: https://lirias.kuleuven.be/handle/123456789/634049 (open access: True)
location: http://hdl.handle.net/1887/121093 (open access: False)
location: https://hdl.handle.net/1887/121093 (open access: False)

<!-- fetch 2: https://pubmed.ncbi.nlm.nih.gov/30763612/ | fetch.py html-text | 2026-11-06T23:05+07:00 | blocked -->
No readable copy was found. Attempts:
- L1 https://pubmed.ncbi.nlm.nih.gov/30763612/: blocked (blocking page (cookies must be enabled))

<!-- fetch 3: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.jclinepi.2019.02.004&resultType=core&format=xml | fetch.py html-text | 2026-11-06T23:06+07:00 | readable -->
title: A systematic review shows no performance benefit of machine learning over logistic regression for clinical prediction models.Journal of clinical epidemiology

6.91DOI:10.1016/j.jclinepi.2019.02.004core*25false30763612MED3076361210.1016/j.jclinepi.2019.02.004Christodoulou E, Ma J, Collins GS, Steyerberg EW, Verbakel JY, Van Calster B.Christodoulou EEvangeliaChristodoulouE0000-0001-7900-5952Department of Development & Regeneration, KU Leuven, Herestraat 49 box 805, Leuven, 3000 Belgium.Ma JJieMaJ0000-0002-3900-1903Centre for Statistics in Medicine, Nuffield Department of Orthopaedics, Rheumatology and Musculoskeletal Sciences, Botnar Research Centre, University of Oxford, Windmill Road, Oxford, OX3 7LD UK.Collins GSGary SCollinsGS0000-0002-2772-2316Centre for Statistics in Medicine, Nuffield Department of Orthopaedics, Rheumatology and Musculoskeletal Sciences, Botnar Research Centre, University of Oxford, Windmill Road, Oxford, OX3 7LD UK; Oxford University Hospitals NHS Foundation Trust, Oxford, UK.Steyerberg EWEwout WSteyerbergEWDepartment of Biomedical Data Sciences, Leiden University Medical Centre, Albinusdreef 2, Leiden, 2333 ZA The Netherlands.Verbakel JYJan YVerbakelJY0000-0002-7166-7211Department of Development & Regeneration, KU Leuven, Herestraat 49 box 805, Leuven, 3000 Belgium; Department of Public Health & Primary Care, KU Leuven, Kapucijnenvoer 33J box 7001, Leuven, 3000 Belgium; Nuffield Department of Primary Care Health Sciences, University of Oxford, Woodstock Road, Oxford, OX2 6GG UK.Van Calster BBenVan CalsterB0000-0003-1613-7450Department of Development & Regeneration, KU Leuven, Herestraat 49 box 805, Leuven, 3000 Belgium; Department of Biomedical Data Sciences, Leiden University Medical Centre, Albinusdreef 2, Leiden, 2333 ZA The Netherlands. Electronic address: ben.vancalster@kuleuven.be.0000-0001-7900-59520000-0002-2772-23160000-0002-3900-19030000-0002-7166-72110000-0003-1613-7450altmetrics11028186252019 Jun620192019-06-01J Clin EpidemiolJ Clin Epidemiol88013830895-43561878-5921201912-22<h4>Objectives</h4>The objective of this study was to compare performance of logistic regression (LR) with machine learning (ML) for clinical prediction modeling in the literature.<h4>Study design and setting</h4>We conducted a Medline literature search (1/2016 to 8/2017) and extracted comparisons between LR and ML models for binary outcomes.<h4>Results</h4>We included 71 of 927 studies. The median sample size was 1,250 (range 72-3,994,872), with 19 predictors considered (range 5-563) and eight events per predictor (range 0.3-6,697). The most common ML methods were classification trees, random forests, artificial neural networks, and support vector machines. In 48 (68%) studies, we observed potential bias in the validation procedures. Sixty-four (90%) studies used the area under the receiver operating characteristic curve (AUC) to assess discrimination. Calibration was not addressed in 56 (79%) studies. We identified 282 comparisons between an LR and ML model (AUC range, 0.52-0.99). For 145 comparisons at low risk of bias, the difference in logit(AUC) between LR and ML was 0.00 (95% confidence interval, -0.18 to 0.18). For 137 comparisons at high risk of bias, logit(AUC) was 0.34 (0.20-0.47) higher for ML.<h4>Conclusion</h4>We found no evidence of superior performance of ML over LR. Improvements in methodology and reporting are needed for studies that compare modeling algorithms.Department of Development & Regeneration, KU Leuven, Herestraat 49 box 805, Leuven, 3000 Belgium.ppublishengPrint-ElectronicComparative StudyResearch Support, Non-U.S. Gov'tSystematic ReviewJournal Article27294Cancer Research UKCRUK_016895Cancer Research UKCRUK_0C24/15/037KU Leuven05529/A16895Cancer Research UKCRUK_0NIHR Biomedical Research Centre0NIHR-RMFI-2014-05-05-101National Institute for Health Research (NIHR)0G0B4716NFWO0NHumansNArea Under CurveYLogistic ModelsNSensitivity and SpecificityNPredictive Value of TestsNAlgorithmsYModels, TheoreticalYSupervised Machine LearningNOutcome Assessment, Health CareLogistic regressioncalibrationReportingAucMachine LearningClinical Prediction ModelsIMIndex MedicusFreeFpdfUnpaywallhttps://ora.ox.ac.uk/objects/uuid:4167c905-5171-4fc7-b157-ff36d56a73db/files/m0c822b1760523fd587b9a6769e616049Subscription requiredSdoiDOIhttps://doi.org/10.1016/j.jclinepi.2019.02.00431425736MEDJ Clin Epidemiol. 2019 Dec;116:137-138. doi: 10.1016/j.jclinepi.2019.08.002.Comment in131425737MEDJ Clin Epidemiol. 2019 Dec;116:136-137. doi: 10.1016/j.jclinepi.2019.08.003.Comment in2NNNNNN1268NYYNYNNNNN2020-05-182019-02-152019-02-152026-03-252019-02-112019-02-11
