import joblib
import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Diabetes Risk Analyzer",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

@st.cache_resource
def load_assets():
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_assets()

st.markdown(
    """
    <style>
    /* General App Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* Glassmorphism Form Card */
    div[data-testid="stForm"] {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
    }

    /* Result Card Formatting */
    .result-card {
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    .status-positive {
        background: linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%);
        border: 1px solid #ef4444;
    }
    .status-negative {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        border: 1px solid #10b981;
    }
    
    .result-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .result-desc {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("🩺 Diabetes Risk Prediction Assessment")
st.markdown(
    "Please enter the patient's clinical parameters below to evaluate the risk of Diabetes."
)
st.divider()

with st.form(key="diabetes_assessment_form"):
    st.subheader("📋 Patient Clinical Metrics")
    
    col1, col2 = st.columns(2, gap="large")

    with col1:
        pregnancies = st.number_input("Pregnancies (Count)", min_value=0, max_value=20, value=1)
        glucose = st.slider("Glucose Level (mg/dL)", min_value=0, max_value=300, value=100)
        blood_pressure = st.slider("Blood Pressure (mmHg)", min_value=0, max_value=180, value=70)
        skin_thickness = st.slider("Skin Thickness (mm)", min_value=0, max_value=100, value=20)

    with col2:
        insulin = st.slider("Insulin Level (mu U/ml)", min_value=0, max_value=900, value=80)
        bmi = st.slider("BMI (Body Mass Index)", min_value=0.0, max_value=70.0, value=24.5, step=0.1)
        dpf = st.slider("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.47, step=0.01)
        age = st.number_input("Age (Years)", min_value=1, max_value=120, value=25)

    st.write("")
    submit_button = st.form_submit_button(label="📊 Run Health Assessment", use_container_width=True)


if submit_button:
    glucose_bmi = glucose * bmi
    glucose_age = glucose * age

    raw_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age,
        "GlucoseBMI": glucose_bmi,
        "GlucoseAge": glucose_age,
    }
    
    input_df = pd.DataFrame([raw_data])

    if hasattr(scaler, "feature_names_in_"):
        input_df = input_df[scaler.feature_names_in_]
        
    scaled_data = scaler.transform(input_df)

\    prediction = model.predict(scaled_data)[0]
    probability = (
        model.predict_proba(scaled_data)[0][1]
        if hasattr(model, "predict_proba")
        else None
    )

    st.divider()
    
    if prediction == 1:
        prob_text = f"Risk Factor Score: **{probability:.1%}**" if probability is not None else ""
        st.markdown(
            f"""
            <div class="result-card status-positive">
                <div class="result-title">⚠️ High Risk Detected</div>
                <div class="result-desc">The analysis indicates a high probability of diabetes. {prob_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        prob_text = f"Health Score (No-Risk): **{(1 - probability):.1%}**" if probability is not None else ""
        st.markdown(
            f"""
            <div class="result-card status-negative">
                <div class="result-title"> Low Risk Detected</div>
                <div class="result-desc">The analysis indicates a low probability of diabetes. {prob_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

\    if probability is not None:
        st.write("")
        st.caption("Risk Probability Scale")
        st.progress(float(probability))
