# ML Problem Framing Memo: Customer Churn Prediction

## 1. Problem Statement

Customer churn occurs when customers stop using a company's products or services. Identifying customers who may be at risk of leaving can help a business prioritize timely support and retention efforts.

The objective of this project is to investigate whether machine learning can help identify customers who are at risk of churning and support better customer-retention decisions.

## 2. Decision to Be Supported

The proposed system will help a customer-retention team prioritize which customers should receive proactive support or follow-up.

The prediction will support human decision-making. It will not automatically penalize customers, restrict services, or make final decisions about them.

## 3. Prediction Target

**Proposed target:** Whether a customer will churn within the next 30 days.

The supplied dataset contains a `churned` column, but its exact label definition and observation period have not yet been confirmed. Therefore, the 30-day horizon is a proposed design choice, not an established property of the dataset.

## 4. Unit of Observation

One record represents one customer.

For a production-ready prediction system, each record should represent a customer's information at a clearly defined prediction date.

## 5. Available Features

- `tenure_months`: Customer's tenure.
- `support_tickets`: Number of support tickets.
- `monthly_spend_inr`: Monthly customer spending.
- `last_login_days`: Days since the customer's last login.
- `plan_type`: Customer's subscription plan.
- `customer_id`: Customer identifier; excluded from predictive features.

The target variable is `churned`.

## 6. Proposed Action Window

- Day 0: Generate a churn-risk assessment.
- Day 0: Retention team reviews flagged customers.
- Days 1–3: Conduct appropriate customer outreach.
- Day 30: Assess whether the customer churned.

This timeline is a proposed workflow and requires validation against actual business operations.

## 7. Non-ML Baseline

Before using machine learning, a simple rule-based approach will be evaluated.

For example, customers with at least 14 days of inactivity and at least 3 support tickets may be flagged for review.

These thresholds are illustrative and are not validated business rules.

## 8. Why Consider Machine Learning?

Machine learning may identify patterns across multiple customer attributes that are difficult to capture using fixed rules.

However, the available dataset contains only 12 records. This is insufficient for reliable model training, validation, or generalization. A larger, representative, properly labelled dataset would be required before making claims about model performance.

## 9. Key Assumptions and Limitations

- The meaning and time horizon of the churn label must be confirmed.
- The original data source and collection process are not documented.
- The dataset is too small for reliable predictive modelling.
- Features must be verified to ensure they were available at prediction time.
- Customer outreach effectiveness cannot be established from prediction accuracy alone.

## 10. Initial Recommendation

Proceed with exploratory analysis and a transparent rule-based baseline. Do not deploy a machine-learning model until the dataset's provenance, label definition, sample size, and suitability have been established.