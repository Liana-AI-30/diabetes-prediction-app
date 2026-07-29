 🩺 Diabetes Prediction App

A lightweight, interactive Streamlit web application that predicts the likelihood of a patient having diabetes based on clinical health metrics.



### 📊 Project Overview
Goal: Predict diabetes risk (High Risk / Low Risk).
Machine Learning Model: Logistic Regression (Standardized via `StandardScaler`).
Deployment: Streamlit Cloud with custom Glassmorphism UI styling.

 📥 Clinical Input Features
* **Pregnancies: Number of times pregnant
* **Glucose:** Plasma glucose concentration (mg/dL)
* **Blood Pressure:** Diastolic blood pressure (mm Hg)
* **Skin Thickness:** Triceps skinfold thickness (mm)
* **Insulin:** 2-Hour serum insulin (mu U/ml)
* **BMI:** Body Mass Index
* **Diabetes Pedigree Function:** Genetic influence score
* **Age:** Patient age in years

 🛠️ Built With* `Python` | `Pandas` | `Scikit-Learn` | `Streamlit` | `Joblib` | `CSS`

 📁 Project Structure
diabetes-prediction-app/
│── app.py                  # Main Streamlit Web Application
│── style.css               # Custom Glassmorphism UI Styling
│── diabetes_model.pkl      # Trained Logistic Regression Model
│── scaler.pkl              # Fitted StandardScaler File
│── requirements.txt        # Python Dependencies
└── README.md               # Project Documentation

