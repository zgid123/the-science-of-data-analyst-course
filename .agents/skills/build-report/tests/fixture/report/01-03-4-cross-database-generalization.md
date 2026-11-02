### 1.3.4. Cross-Database Generalisation

Every family in Sections 1.3.1 to 1.3.3 is evaluated on datasets, and the way it is tested decides what its numbers mean. In intra-dataset testing, training and test data are sampled from the same dataset and share a similar domain distribution; in cross-dataset testing, a model is trained on one or several source datasets and tested on unseen target datasets with a shifted domain [35]. Cross-dataset results are commonly reported with the half total error rate (HTER), the average of the false acceptance rate (FAR) and the false rejection rate (FRR) [35].

Generalisation is the central open problem of the field because the two settings diverge sharply. Methods that perform well within one database cannot generalise well when training and testing data come from different domains, because they learn database-biased features [42]. Most methods over-fit the training set and fail on unseen attacks and environments [41]. Adding more training databases does not close the gap either, since even a combination of multiple databases cannot deal with attack types absent from the training data [30].

Two benchmark designs make this problem measurable. The OULU-NPU dataset, published in 2017, contains 4,950 real access and attack videos of 55 subjects, recorded with the front cameras of six smartphones in three sessions with different illumination and backgrounds [43]. Its four protocols each hold one factor out of training, as Table 1.10 shows [43].

**Table 1.10. OULU-NPU evaluation protocols**

| Protocol | Unseen in testing |
| :---- | :---- |
| Protocol I | Environmental conditions: illumination and background scene [43] |
| Protocol II | Attack instruments: printers or displays [43] |
| Protocol III | Input sensor: one camera left out [43] |
| Protocol IV | Environment, attack instruments and sensors combined [43] |

The second design crosses whole datasets. The O/C/I/M leave-one-out protocol uses OULU-NPU, CASIA-FASD, Idiap Replay-Attack and MSU-MFSD, where CASIA-FASD also appears as CASIA-MFSD in some papers [42]: one dataset is selected as the unseen target and the remaining three serve as training sources, which gives four tasks scored by HTER and the area under the receiver operating characteristic curve (AUC) [42].

The numbers show the size of the gap. Within one dataset, many deep methods reach an ACER below 5%, yet when trained on Replay-Attack and tested on CASIA-FASD most deep models exceed 20% HTER because of lighting and camera-resolution variations [35]. On the four O/C/I/M tasks, the colour-texture method of Section 1.3.1 scores between 28.09% and 63.59% HTER and a binary CNN between 29.25% and 34.88%, while domain-generalisation methods reduce the error, MADDG to between 17.69% and 27.98% [44] and SSDG-R to between 7.38% and 15.61% [42]. These domain-generalisation methods are the starting point of the third era in Section 2.3.
