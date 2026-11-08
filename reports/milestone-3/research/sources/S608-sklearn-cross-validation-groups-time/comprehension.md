# S608 – scikit-learn: Cross-validation, grouped data and time series

## Summary in my own words

The scikit-learn cross-validation guide warns that the i.i.d. assumption behind KFold and ShuffleSplit rarely holds. When samples come from a time-dependent process a time-aware scheme is safer, and when samples share a group (for example several records from the same patient) the validation fold must contain only groups absent from the training fold (GroupKFold and related splitters). For time series it recommends evaluating on "future" observations (TimeSeriesSplit). For OULAD, a student who appears in several presentations is a group, and a later presentation is "the future".

## Key facts

- i.i.d. rarely holds; time-dependent data need a time-aware scheme – "it is safer to"
- Group structure needs group-wise CV – "it is safer to use group-wise cross-validation."
- Grouped validation definition – "ensure that all the samples in the validation fold come from groups that are"
- Group example – "medical data collected from multiple patients, with multiple samples taken from"
- Random splits on time-dependent data correlate training and test – "would result in unreasonable correlation"
- Evaluate on future observations – "to evaluate our model for time series data on the “future” observations"

## Used in

06-03-split-leakage.md (entity split by id_student; time split by presentation).

## Against reference.md

Confirms the outline's "entity and time split" rule: group-wise validation keeps one student's records on one side, and evaluation on later observations matches train 2013 → test 2014.

## Reliability

Primary technical documentation (scikit-learn developers, user guide section 3.1, version as served on 2026-11-06). General ML guidance, not specific to education data.

## Open questions

No education-specific source on time-based splits was fetched; S605 (OU trains on previous presentations) supplies the domain practice.
