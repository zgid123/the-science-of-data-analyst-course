# S417 – scikit-learn User Guide 3.1: Cross-validation: evaluating estimator performance (scikit-learn 1.9.1)

## Summary in my own words

The official scikit-learn guide explains why a test set must be held out even when cross-validation is used for tuning, why preprocessing must be learnt on training folds (Pipeline), and which splitters respect data structure. For grouped data it states that the i.i.d. assumption breaks when samples come in dependent groups and that the validation fold must contain only groups absent from the paired training fold; GroupKFold, StratifiedGroupKFold and LeaveOneGroupOut implement this, with LeaveOneGroupOut holding out one group per split. For time-ordered data, TimeSeriesSplit trains on earlier and tests on later observations.

## Key facts

- Version – "3.1. Cross-validation: evaluating estimator performance — scikit-learn 1.9.1 documentation"
- Tuning leaks – "into the model and evaluation metrics no longer report on generalization performance."
- Hold out a test set – "A test set should still be held out for final evaluation, but the validation set is no longer needed when doing CV."
- Preprocessing – "preprocessing (such as standardization, feature selection, etc.) and similar data transformations similarly should be learnt from a training set and applied to held-out data for prediction"
- Groups break i.i.d. – "The i.i.d. assumption is broken if the underlying generative process yields groups of dependent samples."
- Group rule – "we need to ensure that all the samples in the validation fold come from groups that are not represented at all in the paired training fold."
- GroupKFold – "GroupKFold is a variation of K-fold which ensures that the same group is not represented in both testing and training sets."
- StratifiedGroupKFold – "If class proportions must be balanced across folds, StratifiedGroupKFold is a better option."
- LeaveOneGroupOut – "LeaveOneGroupOut is a cross-validation scheme where each split holds out samples belonging to one specific group."
- Time series – "observations least like those that are used to train the model."

## Used in

04-02-validation-strategy.md

## Against reference.md

Confirms the outline's validation bullet "grouped folds inside the training years": LeaveOneGroupOut with the module run as group implements the leave-one-run-out (LORO) folds over the nine 2013 runs, and the held-out test set corresponds to the 2014 runs. No contradiction.

## Reliability

Primary; official documentation of scikit-learn (scikit-learn developers), version 1.9.1, current stable release as of 2026-11-06. Documentation, not peer-reviewed; used for API behaviour only.

## Open questions

The nested cross-validation example page could not be converted (exploded layout); nested CV evidence comes from Varma & Simon (S408) and Cawley & Talbot (S409).
