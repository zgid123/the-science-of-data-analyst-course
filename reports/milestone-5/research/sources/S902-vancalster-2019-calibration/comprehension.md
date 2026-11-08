# S902 – Calibration: the Achilles heel of predictive analytics (Van Calster et al., BMC Medicine 2019)

## Summary in my own words

The paper argues that calibration – agreement between predicted risks and observed event rates – is assessed far less often than discrimination, although decisions are made on the predicted risk and miscalibrated risks can mislead or harm. It defines four levels of calibration (mean, weak, moderate, strong) and links each to a measure: calibration-in-the-large/intercept (target 0), calibration slope (target 1), and a flexible calibration curve (loess or splines). It recommends against the Hosmer–Lemeshow test, suggests about 200 events and 200 non-events for a precise calibration curve, and advises focusing on the slope at internal validation and on curve, intercept and slope at external validation. When calibration is poor, the model should be updated (recalibrated) rather than discarded, provided enough data are available.

## Key facts

- Calibration neglected – "The assessment of calibration performance of risk prediction models based on regression or more flexible machine learning algorithms receives little attention."
- Good AUC is not enough – "estimated risks can be unreliable even when the algorithms have good discrimination."
- Four levels – "models can be calibrated in the mean, weak, moderate, or strong sense"
- Mean calibration – "the average predicted risk is compared with the overall event rate."
- Slope – "The calibration slope evaluates the spread of the estimated risks and has a target value of 1. A slope < 1 suggests that estimated risks are too extreme"
- Intercept – "The calibration intercept, which is an assessment of calibration-in-the-large, has a target value of 0; negative values suggest overestimation, whereas positive values suggest underestimation."
- Curve – "This is assessed with a flexible calibration curve to show the relation between the estimated risk (on the x-axis) and the observed proportion of events (y-axis), for example, using loess or spline functions."
- Intercept and slope are not sufficient – "a calibration intercept close to 0 and a calibration slope close to 1 do not guarantee that the flexible calibration curve is close to the diagonal"
- Sample size for a curve – "a minimum of 200 patients with and 200 patients without the event has been suggested"
- Small data – "In small datasets, it is defendable to evaluate only weak calibration by calculating the calibration intercept and slope."
- Against Hosmer–Lemeshow – "we recommend against using the Hosmer–Lemeshow test to assess calibration."
- Internal validation – "At internal validation, focus on the calibration slope as a part of the assessment of statistical overfitting"
- External validation – "At external validation, focus on the calibration curve, intercept and slope"
- Updating – "Model updating should be considered in case of poor calibration; re-estimating the model entirely requires sufficient data"
- Cites Van Calster B. & Vickers A.J. (Med Decis Making 2015) on the decision-analytic cost of miscalibration – "Calibration of risk prediction models: impact on decision-analytic performance."

## Used in

09-01-validation-success.md, 11-05-decision-support.md (Milestone 5; reused by T07 from the Milestone 4 trail).

## Against reference.md

Extends Section 9 of the Milestone 5 outline ("Metrics"): calibration is a required metric when risk scores drive decisions, not only discrimination.

## Reliability

Primary; methodological debate article by Van Calster B., McLernon D.J., van Smeden M., Wynants L., Steyerberg E.W. on behalf of the STRATOS initiative Topic Group 6; BMC Medicine 17:230 (2019); open access PMC6912996. Citation traction: 2757 Crossref / 2966 OpenAlex citations as of 2026-11-06. Current as of November 2026 (no updated version; its recommendations are carried into TRIPOD+AI, S400).

## Open questions

The paper does not discuss the Brier score; that measure is taken from PROBAST+AI (S401). The 200/200 guideline is "suggested" and comes from Van Calster et al. 2016 (J Clin Epidemiol), not fetched.
