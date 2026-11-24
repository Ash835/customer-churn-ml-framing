
def predict_churn_risk(last_login_days, support_tickets):
    """
    Assign a simple churn-risk category using transparent rules.

    High risk:
        At least 14 days of inactivity AND at least 3 support tickets.

    Normal risk:
        Does not meet both conditions.
    """

    if last_login_days >= 14 and support_tickets >= 3:
        return "High"

    return "Normal"


def add_risk_predictions(df):
    """
    Add rule-based churn-risk predictions to a copy
    of the supplied customer DataFrame.
    """

    result = df.copy()

    result["predicted_risk"] = result.apply(
        lambda row: predict_churn_risk(
            row["last_login_days"],
            row["support_tickets"]
        ),
        axis=1
    )

    result["predicted_churn"] = (
        result["predicted_risk"] == "High"
    ).astype(int)

    return result
