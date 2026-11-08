# S607 – scikit-learn: Common pitfalls and recommended practices (data leakage)

## Summary in my own words

The scikit-learn user guide (section 12, version 1.9.1 as fetched) defines data leakage as using information that would not be available at prediction time when building the model, which gives over-optimistic performance estimates and poorer performance on new data. Its practical rules: split into train and test first, before any preprocessing; never call fit or fit_transform on test data; learn every transformation (for example the mean used for normalisation) on the training subset only and apply it with transform to both subsets; use a Pipeline so that cross-validation and tuning refit preprocessing inside each fold. It shows that feature selection on the full data optimistically biases results.

## Key facts

- Definition – "Data leakage occurs when information that would not be available at prediction"
- Consequence – "This results in overly optimistic"
- Test data and model choices – "Test data should never be used to make choices about the model."
- General rule – "The general rule is to never call fit on the test data."
- Transformations are learnt from training data only – "it is important that these transformations are only learnt from the training data."
- Normalisation example – "the average should be the average of the train subset, not the average of all the data"
- Split first – "Always split the data into train and test subsets first, particularly"
- Pipelines prevent leakage in cross-validation – "The scikit-learn pipeline is a great way to prevent data"
- Version fetched – "scikit-learn 1.9.1 documentation"

## Used in

06-03-split-leakage.md (transforms fitted on the training partition only; split before preprocessing).

## Against reference.md

Confirms the outline's rule "transforms fitted on the training partition" word for word in substance, and adds the order: split before any preprocessing (imputation, scaling, encoding, feature selection).

## Reliability

Primary technical documentation of the library the pipeline uses (scikit-learn developers), version 1.9.1, fetched 2026-11-06. Not peer-reviewed, but the authoritative statement of the library's intended use.

## Open questions

None.
