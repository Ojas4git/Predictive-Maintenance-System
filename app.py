import streamlit as st
import pandas as pd
import joblib

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="🔧",
    layout="wide"
)

# ---------------------------------
# Custom CSS
# ---------------------------------

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.metric-card {
    padding: 15px;
    border-radius: 10px;
    background-color: #f0f2f6;
    text-align: center;
}

.big-font {
    font-size: 22px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Load Model
# ---------------------------------

model = joblib.load("machine_failure_xgb.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------------------------
# Header
# ---------------------------------

st.title("🔧 AI Predictive Maintenance Dashboard")

st.markdown("""
Predict machine failures before they happen using **XGBoost Machine Learning Model**.
""")

st.divider()

# ---------------------------------
# Input Layout
# ---------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("⚙️ Machine Parameters")

    machine_type = st.selectbox(
        "Machine Type",
        ["H", "L", "M"]
    )

    rpm = st.number_input(
        "Rotational Speed (RPM)",
        min_value=1000,
        max_value=3000,
        value=1500
    )

    torque = st.number_input(
        "Torque (Nm)",
        min_value=0.0,
        max_value=100.0,
        value=40.0
    )

    tool_wear = st.number_input(
        "Tool Wear (min)",
        min_value=0,
        max_value=300,
        value=100
    )

with col2:

    st.subheader("🌡️ Temperature Parameters")

    air_temp = st.number_input(
        "Air Temperature (K)",
        value=300.0
    )

    process_temp = st.number_input(
        "Process Temperature (K)",
        value=310.0
    )

# ---------------------------------
# Predict Button
# ---------------------------------

if st.button("🚀 Predict Machine Status"):

    # Encoding

    type_mapping = {
        "H": 0,
        "L": 1,
        "M": 2
    }

    machine_type_encoded = type_mapping[machine_type]

    # DataFrame

    input_df = pd.DataFrame(
        [[
            machine_type_encoded,
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear
        ]],
        columns=[
            "Type",
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]"
        ]
    )

    # Scale

    input_scaled = scaler.transform(input_df)

    # Prediction

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    st.divider()

    # ------------------------------
    # Result Section
    # ------------------------------

    st.subheader("📊 Prediction Result")

    col3, col4 = st.columns(2)

    with col3:

        if prediction == 1:

            st.error(
                "⚠️ MACHINE FAILURE PREDICTED"
            )

        else:

            st.success(
                "✅ MACHINE HEALTHY"
            )

    with col4:

        st.metric(
            "Failure Probability",
            f"{probability*100:.2f}%"
        )

    # ------------------------------
    # Risk Level
    # ------------------------------

    st.subheader("🚨 Risk Assessment")

    if probability < 0.30:

        st.success("🟢 LOW RISK")

    elif probability < 0.70:

        st.warning("🟡 MEDIUM RISK")

    else:

        st.error("🔴 HIGH RISK")

# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.title("📌 Project Information")

st.sidebar.markdown("""
### Model Used
XGBoost Classifier

### Features

- Machine Type
- Air Temperature
- Process Temperature
- RPM
- Torque
- Tool Wear

### Performance

Accuracy: 98.35%

Recall: 62%

F1 Score: 0.70

### Developer

Ojas Savkar
""")

# ---------------------------------
# Footer
# ---------------------------------

st.divider()

st.caption(
    "AI Predictive Maintenance using Machine Learning and XGBoost"
)