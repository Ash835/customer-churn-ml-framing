# Responsible ML Problem Framing: Customer Churn Prediction

## Overview

This project explores whether machine learning is justified for identifying customers who may be at risk of churning.

Rather than immediately training a model, the project focuses on defining the business decision, understanding the dataset, evaluating a transparent rule-based baseline, and documenting responsible AI considerations.

The project follows a responsible ML workflow that prioritizes data quality, explainability, privacy, and human oversight.

## Problem Statement

Customer churn occurs when customers stop using a company's products or services.

The proposed system aims to help customer-retention teams identify potentially at-risk customers and prioritize supportive outreach.

The proposed prediction target is customer churn within the next 30 days. However, the supplied dataset's exact churn-label definition and observation period have not been confirmed.

## Dataset Overview

The supplied dataset contains:

- 12 customer records
- 7 columns
- 5 churned customers
- 7 non-churned customers
- No missing values in the initial inspection
- No duplicate rows in the initial inspection

### Features

| Feature | Description |
|---|---|
| customer_id | Customer identifier |
| tenure_months | Customer tenure |
| support_tickets | Number of support tickets |
| monthly_spend_inr | Monthly spending |
| last_login_days | Days since last login |
| plan_type | Subscription plan |
| churned | Target variable |

`customer_id` is excluded from predictive features.

## Project Structure

```text
customer-churn-ml-framing/
├── data/
│   └── customer-churn-training.csv
├── docs/
│   ├── problem-framing.md
│   ├── data-card.md
│   ├── risk-register.md
│   └── evaluation-plan.md
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   └── 02_baseline_evaluation.ipynb
├── src/
│   └── baseline_rules.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Baseline Approach

A transparent rule-based baseline was implemented.

A customer is flagged as high risk when both conditions are satisfied:

- `last_login_days >= 14`
- `support_tickets >= 3`

Otherwise, the customer is classified as normal risk.

The thresholds are illustrative and have not been validated as business rules.

## Baseline Evaluation Results

The baseline was evaluated against the supplied dataset's churn labels.

| Metric | Result |
|---|---:|
| Accuracy | 91.67% |
| Precision | 100% |
| Recall | 80% |
| F1-score | 88.89% |

### Confusion Matrix

| | Predicted: No Churn | Predicted: Churn |
|---|---:|---:|
| Actual: No Churn | 7 | 0 |
| Actual: Churn | 1 | 4 |

The baseline identified four of the five churned customers and missed one. It generated no false-positive predictions on these 12 records.

**Important limitation:** These are in-sample results on a very small dataset. They do not demonstrate generalization or production readiness.

## Responsible AI Considerations

The project documents:

- Data provenance and permitted use.
- Consent and privacy considerations.
- Sensitive attributes and potential proxy variables.
- Missingness and data quality.
- Potential data leakage.
- False-positive and false-negative costs.
- Abstention and human-review strategies.
- Monitoring and rollback conditions.

Predictions are intended only to support human-reviewed, supportive customer outreach. They should not be used to penalize customers or automatically restrict services.

## Key Limitations

- The dataset contains only 12 records.
- Original data provenance and collection methodology are not documented.
- The exact churn-label definition and prediction horizon are unconfirmed.
- No independent test dataset is available.
- The baseline thresholds are illustrative.
- Real-world retention impact cannot be inferred from these results.

A larger, representative, appropriately authorized dataset is required before reliable ML training or deployment can be considered.

## Conclusion

This project demonstrates that responsible ML development begins with understanding the decision, data, risks, and baseline alternatives—not simply training a model.

The current findings support exploratory analysis and a transparent rule-based approach. There is not enough evidence to justify deploying a machine learning model.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Git and GitHub

## How to Run

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Open the project in VS Code or Jupyter Notebook.
4. Run `01_dataset_exploration.ipynb`.
5. Run `02_baseline_evaluation.ipynb`.

## Project Deliverables

- ML problem-framing memo
- Responsible data card
- Dataset exploration notebook
- Rule-based baseline implementation
- Baseline evaluation notebook
- Risk register
- Evaluation plan
