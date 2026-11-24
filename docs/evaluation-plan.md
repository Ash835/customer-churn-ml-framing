# Evaluation Plan: Customer Churn Prediction

## 1. Objective

The objective of this evaluation plan is to define how a proposed customer churn prediction system should be assessed before any real-world deployment.

The evaluation will consider predictive performance, business usefulness, reliability, and responsible use.

## 2. Business Metrics

The proposed system should be evaluated using:

- Customer retention rate: Percentage of customers who remain active during the evaluation period.
- Outreach efficiency: Number of customers successfully reached compared with total outreach attempts.
- Retention-team workload: Number of customers requiring manual review.
- Retention campaign cost: Resources spent on customer outreach and incentives.

These are proposed business metrics. Their actual values and effectiveness cannot be established using the supplied dataset alone.

## 3. Model Evaluation Metrics

| Metric | Purpose |
|---|---|
| Accuracy | Measures overall correct predictions |
| Precision | Measures how many predicted churn cases actually churned |
| Recall | Measures how many actual churn cases were identified |
| F1-score | Balances precision and recall |
| PR-AUC | Evaluates precision-recall performance across thresholds |

Recall is important because missing customers who are genuinely at risk may result in missed retention opportunities.

Precision is also important because excessive false positives increase outreach costs and may annoy customers.

Accuracy should not be used alone, particularly when class distributions are imbalanced.

## 4. Cost of Prediction Errors

### False Positive

A customer is predicted to churn but does not churn.

Potential consequences:
- Unnecessary customer outreach.
- Increased operational costs.
- Customer inconvenience.

### False Negative

A customer is predicted not to churn but subsequently churns.

Potential consequences:
- Missed retention opportunities.
- Potential revenue loss.
- Reduced effectiveness of customer support efforts.

The final decision threshold should balance these two costs according to business priorities.

## 5. Baseline Evaluation

A simple rule-based baseline will be evaluated before introducing machine learning.

Proposed rule:

- Flag a customer if `last_login_days >= 14` AND `support_tickets >= 3`.
- Otherwise, classify the customer as normal risk.

These thresholds are illustrative and have not been validated.

The baseline will provide a transparent reference point for future model comparisons.

## 6. Future Machine Learning Evaluation

If a sufficiently large and appropriately labelled dataset becomes available:

1. Separate training and testing data using a time-aware split where timestamps permit.
2. Prevent customer-level and temporal data leakage.
3. Compare suitable classification algorithms.
4. Evaluate precision, recall, F1-score, and PR-AUC.
5. Compare model performance against the rule-based baseline.
6. Evaluate performance across appropriate customer groups where lawful data is available.

Model selection should consider reliability, interpretability, and operational costs rather than accuracy alone.

## 7. Abstention and Human Review

Predictions with insufficient confidence or invalid input data should be marked for manual review.

The system should not force a prediction when the available information is inadequate.

High-risk predictions should be reviewed before customer outreach.

## 8. Monitoring and Rollback

A future deployed model should be monitored for:

- Changes in predictive performance.
- Data quality issues.
- Data distribution drift.
- Unfair performance differences.
- Unexpected increases in false positives.
- Customer complaints and human-review overrides.

The system should be suspended if it becomes unreliable or causes unacceptable harm. A manual or rule-based process should be used until the issue is resolved.

## 9. Current Evaluation Limitations

The supplied dataset contains only 12 records, with 5 churned and 7 non-churned customers.

This is insufficient for a reliable train-test split, meaningful model validation, or generalization claims.

The current project will therefore focus on exploratory analysis, responsible problem framing, and a transparent baseline rather than claiming successful ML prediction.

## 10. Conclusion

A machine learning model should only be considered justified if it demonstrates measurable improvement over a transparent baseline and provides sufficient business value without introducing unacceptable risks.

The availability of a dataset does not automatically justify using machine learning.