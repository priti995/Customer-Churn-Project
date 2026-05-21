import streamlit as st
import joblib
import pandas as pd

# =========================
# LOAD TRAINED MODEL
# =========================

model = joblib.load(
    r"C:\Users\pawar\OneDrive\Documents\customer-churn-project\models\churn_model.pkl"
)

# =========================
# CREATE EMPTY DATAFRAME
# =========================

sample = pd.DataFrame(
    columns=model.feature_names_in_
)

sample.loc[0] = 0

# =========================
# APP TITLE
# =========================

st.title("Customer Churn Prediction System")

st.write("Enter customer details below")

# =========================
# USER INPUTS
# =========================

tenure = st.number_input(
    "Customer Tenure (months)",
    min_value=0,
    max_value=100,
    value=1
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=500.0,
    value=50.0
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

# =========================
# STORE INPUTS
# =========================

sample['tenure'] = tenure

sample['MonthlyCharges'] = monthly_charges

# =========================
# CONTRACT ENCODING
# =========================

if contract == "One year":

    sample['Contract_One year'] = 1

elif contract == "Two year":

    sample['Contract_Two year'] = 1

# Month-to-month stays default 0

# =========================
# PREDICTION BUTTON
# =========================

if st.button("Predict Churn"):

    # Predict
    prediction = model.predict(sample)

    # Probability
    probability = model.predict_proba(sample)

    # Risk Score
    risk_score = probability[0][1] * 100

    # =========================
    # SHOW RESULT
    # =========================

    if prediction[0] == 1:

        st.error("Customer is likely to churn")

    else:

        st.success("Customer is not likely to churn")

    # =========================
    # SHOW RISK SCORE
    # =========================

    st.write(f"Risk Score: {risk_score:.2f}%")

    # =========================
    # RECOMMENDED ACTION
    # =========================

    if risk_score > 70:

        st.warning(
            "Recommended Action: Assign support manager"
        )

    elif risk_score > 40:

        st.info(
            "Recommended Action: Send retention email"
        )

    else:

        st.success(
            "Recommended Action: Normal engagement"
        )