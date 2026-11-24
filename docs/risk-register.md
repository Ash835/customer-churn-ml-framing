# Risk Register: Customer Churn Prediction

## 1. Purpose

This risk register identifies potential technical, operational, privacy, and fairness risks associated with a proposed customer churn prediction system.

The system is intended to support customer-retention teams by prioritizing supportive outreach. Predictions must not be treated as definitive judgments about customers.

## 2. Identified Risks

| ID | Risk | Potential impact | Mitigation |
|---|---|---|---|
| R1 | False positives | Customers receive unnecessary outreach, causing annoyance and additional staff workload | Use human review before outreach |
| R2 | False negatives | Customers at risk of leaving may not receive timely support | Monitor recall and review missed churn cases |
| R3 | Data leakage | Model performance appears artificially high and fails in real use | Verify that all features are available before prediction time |
| R4 | Small dataset | Model results are unreliable and may not generalize | Obtain a larger, representative dataset |
| R5 | Privacy exposure | Customer information may be accessed or shared improperly | Apply access controls and minimize personal data |
| R6 | Bias or unfair treatment | Certain customer groups may receive unequal treatment | Evaluate performance across appropriate groups where lawful data is available |
| R7 | Incorrect or outdated data | Customers may receive inappropriate risk assessments | Validate inputs and monitor data quality |
| R8 | Over-reliance on predictions | Staff may treat predictions as certain outcomes | Provide explanations and require human judgment |

## 3. False Positive and False Negative Costs

### False Positive

A customer is flagged as high risk but does not churn.

Potential costs:
- Unnecessary outreach.
- Increased retention-team workload.
- Customer annoyance.
- Unnecessary retention incentives.

### False Negative

A customer is not flagged as high risk but subsequently churns.

Potential costs:
- Missed opportunity for timely assistance.
- Potential loss of customer revenue.
- Reduced effectiveness of retention efforts.

The business must balance these costs when selecting an operating threshold.

## 4. Abstention Strategy

The system should abstain from making a prediction when:

- Required customer information is missing.
- Input values are invalid or outside expected ranges.
- The model's confidence is insufficient.
- The customer record differs significantly from the data used during model development.

Abstained cases should be referred for manual review rather than automatically classified.

## 5. Human Review

- High-risk predictions must be reviewed by an authorized retention-team member.
- Staff should consider the customer's actual circumstances before contacting them.
- Customers must not be penalized based solely on model predictions.
- Human reviewers should be able to override recommendations.

## 6. Monitoring Plan

If a model is developed in the future, monitor:

- Precision and recall.
- False-positive and false-negative rates.
- F1-score and PR-AUC.
- Changes in input data distributions.
- Data quality and missing values.
- Performance across appropriate customer groups, where lawful and feasible.
- Human-review overrides and customer complaints.

Monitoring frequency should be established before deployment.

## 7. Rollback Conditions

The system should be suspended and returned to a manual or rule-based process if:

- Model performance falls below predefined acceptance thresholds.
- Significant data drift is detected.
- Unfair or harmful patterns are identified.
- A privacy or security incident occurs.
- Data pipelines produce invalid or unreliable inputs.
- The model cannot provide sufficiently reliable predictions.

## 8. Current Risk Assessment

The supplied dataset contains only 12 records. Consequently, no reliable ML model can currently be validated or deployed.

The proposed safeguards describe requirements for a future system and have not been tested in production.

A transparent rule-based baseline and human review are recommended for the current educational exercise.