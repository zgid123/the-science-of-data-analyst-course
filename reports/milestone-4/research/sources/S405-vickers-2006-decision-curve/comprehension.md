# S405 – Decision curve analysis: a novel method for evaluating prediction models (Vickers & Elkin, Medical Decision Making 2006)

## Summary in my own words

Decision curve analysis evaluates a prediction model by its consequences without needing external cost data. The threshold probability pt at which one would act encodes how much worse a false negative is than a false positive; from it, net benefit = TP/n − FP/n × pt/(1 − pt). Plotting net benefit across a range of thresholds and comparing it with the default strategies "treat all" and "treat none" shows the range of thresholds where the model is useful. The method also compares several models and simple decision rules on the same validation data, and net benefit can be read as the net number of true positives per 100 people.

## Key facts

- Purpose – "We sought a method for evaluating prediction models that incorporates consequences and so can be used to make decisions about whether to use a model at all or which of several models to use."
- Threshold encodes preferences – "the threshold probability of a disease or event at which a patient would opt for treatment is informative of how the patient weighs the relative harms of a false-positive and a false-negative prediction."
- Net benefit formula explained – "we subtract the proportion of all patients who are false-positive from the proportion who are true-positive, weighting by the relative harm of a false-positive and a false-negative result."
- Author-reported worked example – "The net benefit is therefore (65/902) – (225/902) × (0.1/0.9) = 0.0443."
- Range – "the theoretical range of net benefit is from negative infinity to the incidence of disease."
- Default comparators – "if the net benefit for the prediction model is positive, it is better to use the model than to assume that everyone is negative."
- Useful range – "In between these two extremes there is a range of pt where the prediction model is of value."
- Comparing models and a rule – "it can be used to compare several different models. To illustrate this we compare the basic prediction model with an expanded model and with a simple clinical decision rule."
- No extra data needed – "this method does not require information on the costs or effectiveness of treatment or how patients value different health states."
- Interpretation – "The net benefit of 0.062 at a pt of 5% can be interpreted in terms that use of the model, compared with assuming that all patients are negative, leads to the equivalent of a net 6.2 true-positive results pe"
- Net benefit attributed to Peirce C.S. (Science 1884) – "first attributed to Peirce14"

## Used in

04-03-metrics-success.md, 04-01-evaluation-cards.md

## Against reference.md

Extends the outline's metrics bullet "comparison with the rule": decision curves compare a model with a simple rule and with "contact all"/"contact none" on the same evaluation data. The OULAD setting is capacity-limited (3–5 contacts per group of about 20), so a fixed top-k rule, not a probability threshold, sets the action; net benefit applies only once the team states an exchange rate between a missed and an unnecessary contact. No direct contradiction; the capacity framing is a condition on its use.

## Reliability

Primary; methods paper by Vickers A.J. and Elkin E.B. (Memorial Sloan-Kettering Cancer Center); Medical Decision Making 26(6):565–574 (2006); open copy PMC2577036. Citation traction: 5986 Crossref / 6594 OpenAlex citations as of 2026-11-06. Original method paper; later tutorials extend it, but the definition of net benefit is unchanged as of November 2026.

## Open questions

How to adapt net benefit to a fixed contact budget (top-k per group) is not covered; the report should state its own adaptation as a design choice.
