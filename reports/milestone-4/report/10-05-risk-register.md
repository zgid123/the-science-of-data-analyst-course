## Appendix V – Risk Register and Risk Notes

### 1. Risk Register

The register follows the four functions of the NIST AI Risk Management Framework, which organises risk work as
govern, map, measure and manage [39]. Each row names where a risk arises in this project, the control that the
proposal builds in, the check that shows whether the control works, and the risk that remains. Table A.18 lists the
sixteen risks.

**Table A.18. Risk register**

| # | Risk | Where it arises | Control | Check | Residual |
| :---- | :---- | :---- | :---- | :---- | :---- |
| R1 | Target leakage | A predictor that carries information from after the cut-off | Predictors dated on or before the cut-off; target-derived flags outside the predictor list (Milestone 3) | Predictor legitimacy at the time of use [41]; validation of the prepared views | Low |
| R2 | Train–test contamination | Preprocessing or tuning that sees validation or test rows | Refit inside each fold; one test scoring after the second freeze | Logged test access [26]; pipeline review [22] | Low |
| R3 | Selection bias in model choice | The chosen configuration's fold score is optimistic | Nested tuning; choice by a margin fixed in advance; fold results never reported as performance | Fold-level results kept for the record [30] | Low to medium |
| R4 | Shift between years and to the university | 2014 runs differ from 2013; UK distance learning differs from a Vietnamese program | Temporal test; paired and unpaired runs apart; local validation before any use | Per-run metrics; a failed calibration check leads to ranks only, and recalibration only on a run after the 2014 test runs [33] | Medium |
| R5 | Unseen module | Module CCC appears only in 2014 | Module terms as deviations; unseen module scored with the average | CCC runs reported apart | Medium for CCC |
| R6 | Few-cluster inference | 13 test runs of unequal size | Paired two-level bootstrap with a sign-flip test; per-run results | Wins, ties and losses reported | Medium |
| R7 | Selective reporting | Many test variants | One primary comparison declared; variants cannot change the verdict | First and second freeze records [26] | Low |
| R8 | Run list versus tutor capacity | One run-wide list stands in for tutors' lists | Capacity expressed as a share of the run; limitation stated | Tutor-level check in the pilot | Medium |
| R9 | Misreading coefficients as causes | AQ2 estimates and AQ3 reasons read as effects | Association wording rule with a text review; unadjusted and adjusted estimates side by side | Review of all result wording against the brief | Low |
| R10 | Claiming that contact works | The list read as proof that contacting helps | No effect claim; randomised pilot proposed [44] | Wording review of tutor materials before the pilot | Medium until a pilot |
| R11 | Unequal errors across groups | Lower recall for disabled, deprived or older students | Separation as primary criterion; confirmatory check (Appendix IV) | Shortfall rule of Table A.17 | Medium for small groups |
| R12 | Proxies for excluded attributes | Activity, history or credits carry group information | Proxy check by group | Score and predictor means by group | Medium |
| R13 | Automation bias | Tutors follow the list without judgement | Tutor decides; can override any entry; reasons shown [47] | Scripted tutor walk-through before the pilot; overrides recorded | Medium |
| R14 | Labelling and stereotyping | A flag that follows a student | Flags lead to support and expire with the run [45] | Review of list use [46] | Medium |
| R15 | Feedback after deployment | Contacts change the outcomes the next model learns from | Contacts logged with outcomes before any retraining [52] | Monitoring of later cohorts [39] | Medium |
| R16 | Legal status and privacy at the university | Ranking learners is listed as high-risk in Vietnam [50]; university records are personal data [51] | Pilot only after risk classification and the duties of the AI law [49]; OULAD never linked to other data | Conformity assessment, the procedure that assesses a high-risk AI system before it is put into use [49]; data protection review | Depends on the university |

### 2. Leakage, Overfitting and Interpretability

Section 5.1 summarises these risks to the validity of the evaluation; this section treats each in full.

**Leakage.** Following the notes of Table 5.1, the first group of risks concerns the validity of the evaluation.
Leakage covers three failures that matter here: an unclean separation of training and test data, including
preprocessing fitted on the whole dataset; features that act as proxies of the outcome; and temporal leakage, or
dependence between training and test samples [22]. The modeller should not see information beyond the point that
separates training from testing [40]. The 2014 outcomes therefore stay unopened until the single test, AQ2 waits for it (Change Log entry C14, Appendix VII), and every learned step is refitted inside each fold. Predictors must have been available at the moment the
model is used [41], which the dated feature views ensure and the labels-available variant checks, since the outcomes of the
October 2013 runs are not yet known when the February 2014 runs reach their cut-offs.

**Overfitting.** Overfitting also enters through the choice of model: a fold score that was tuned on the same folds is
optimistic [30], so fold results serve only the choice between candidates and are never reported as performance.
Published comparisons of machine learning with logistic regression are often biased by flaws in validation and silent
on calibration [18], which the frozen validation of Section 4.2 is designed to avoid.

**Interpretability.** Interpretability is built into the choice of model rather than added afterwards. Each student's
reasons come from the same logistic model that ranks the student, which avoids explanations made afterwards that can
mislead [11]. Many different models, with different coefficients, fit about equally well [5]; the chosen
model's coefficients are one of many sets that fit the data, so no coefficient is read as a cause, and AQ2's
mutually adjusted estimates are shown beside the unadjusted gaps. The final model is to be documented in a model card,
which states its intended and out-of-scope uses with its performance by group [42], and the prepared data in a
datasheet, which records their composition, collection and recommended uses [43].

**Data constraints.** The data limit what can be claimed: 9 training runs from 6 modules, one module (CCC) seen only
in 2014, and distance learning in the UK in 2013–2014. Any use at a Vietnamese university therefore
starts with validation on the university's own records.

### 3. Causal Limits, Fairness and High-Stakes Use

Section 5.2 summarises the risks of using the list on real students; this section treats each in full.

**Causal limits.** Beyond the validity risks of Section 5.1, the list will shape decisions about real students. Its
first limit is causal. The effect of an intervention is best answered by a randomised experiment, which observational
data can at most emulate [44], and estimating for whom a contact helps needs randomised or unconfounded data on
treatment [9], which OULAD lacks. Risk and benefit can also diverge: the students at highest risk do not always benefit
most, as field experiments in customer retention showed [20]. The choice of contact, and any ranking by the expected benefit of a contact, therefore stay deferred; AQ4
supplies only the list of whom to contact first (D1), and the next step is a randomised pilot whose time zero, the
moment from which every student in the pilot is followed, is the cut-off at which students become eligible for the list [44], with contacts and outcomes logged together.

**Fairness.** Fairness has a second limit: a score cannot have equal predictive value and equal error rates across
groups whose non-completion rates differ [36], so separation leads (Section 4.4). A flag leads to support and expires
with the run, because flagged students should be able to prove the prediction wrong [45], and labels must not bias how
staff see a student [46].

**High-stakes and regulated use.** The use is high-stakes, and it is regulated. The EU AI Act, a
reference standard here rather than a law that binds a Vietnamese university, lists as high-risk the systems that
evaluate learning outcomes or steer learning, and requires that people can oversee and override them [47]; its main
obligations for these systems apply from 2 December 2027 under Regulation (EU) 2026/1744, according to a legal commentary [48]. Vietnam's Law on AI, No. 134/2025/QH15, applies from 1 March 2026 and requires human control over decisions made with AI
[49]; Decision 33/2026/QĐ-TTg lists as high-risk in education the systems that rank learners or analyse learner
behaviour [50]; and processing personal data with AI must be classified by level of risk [51]. Such a list at a
Vietnamese university is therefore likely to be high-risk, a reading that the university's legal staff must confirm
from the official texts before a pilot. A pilot needs a risk classification first, and tutors keep
the final say, can override any entry and see the reasons behind it.

**Feedback after use.** Once tutors act on the lists, the outcomes partly reflect the contacts, a performative effect
in which a prediction changes what it predicts [52], so contacts are logged with outcomes before any model is
retrained.
