# Responsible Data Card: Customer Churn Dataset

## 1. Dataset Overview

**Dataset name:** Customer Churn Training Dataset

**Purpose:** Explore customer attributes and assess their potential usefulness for identifying churn risk.

**Number of records:** 12

**Number of columns:** 7

**Target variable:** `churned`

**Target interpretation:** 1 = Churned, 0 = Not churned. The precise label definition and observation period have not been confirmed.

## 2. Data Provenance

The dataset was supplied as part of the internship assignment.

The original data provider, collection process, collection dates, and underlying population are currently unknown.

These details must be obtained from the provider before the dataset is used for real-world model development or deployment.

## 3. Consent and Permitted Use

The dataset was provided as part of the internship assignment, which explicitly requires the completed project to be published in a public GitHub repository.

Therefore, public repository publication is an intended part of the assignment.

The dataset is used for educational exploration, ML problem framing, and responsible data documentation.

The project does not use the dataset for commercial purposes or real-world customer decisions.

The dataset should be used within the scope of the assignment's stated sharing permission.

## 4. Data Fields

| Feature | Description | Potential concern |
|---|---|---|
| customer_id | Customer identifier | Direct identifier; exclude from model |
| tenure_months | Customer tenure | Verify measurement date |
| support_tickets | Number of support tickets | Verify tickets existed before prediction |
| monthly_spend_inr | Monthly spending | Verify measurement period |
| last_login_days | Days since last login | Verify calculation date |
| plan_type | Subscription plan | Check for unfair proxy effects |
| churned | Churn outcome | Confirm label definition and time horizon |

## 5. Sensitive Attributes

No explicit sensitive demographic attributes are present in the supplied schema.

However, the absence of such fields does not guarantee fairness. Features such as subscription plan or spending may indirectly reflect differences between customer groups.

Legitimate fairness evaluation would require appropriate, lawfully obtained data and privacy safeguards.

## 6. Missingness and Data Quality

Initial exploratory analysis found:

- Missing values: 0
- Duplicate rows: 0
- Unique customer IDs: 12
- Total records: 12

Although no missing values were observed, the small sample size limits confidence in the dataset's representativeness.

## 7. Potential Data Leakage

Potential leakage risks include:

- Support tickets recorded after the prediction date.
- Login inactivity calculated using information from after the prediction date.
- Spending values collected after the prediction cutoff.
- Churn labels derived from events occurring outside the intended prediction window.
- Customer IDs being used as predictive inputs.

All features must be checked to ensure they were available at the time the prediction would have been made.

## 8. Data Limitations

- Extremely small sample size.
- Unknown original source and collection methodology.
- Unknown consent and redistribution permissions.
- Unconfirmed churn-label definition.
- No documented timestamps or observation window.
- Unknown representativeness of the customer population.

## 9. Responsible Use Recommendations

- Exclude customer identifiers from model training.
- Verify data provenance and permissions.
- Avoid collecting unnecessary personal information.
- Use predictions only to prioritize supportive human outreach.
- Do not automatically deny services or penalize customers.
- Review model performance and fairness before deployment.
- Restrict access to customer-level data.

## 10. Overall Assessment

The dataset is suitable for a limited educational exploration of responsible ML problem framing and basic data analysis.

It is not sufficient for reliable model training, deployment, or real-world customer decisions.

A larger, representative, documented, and appropriately authorized dataset is required before proceeding to production-level machine learning.