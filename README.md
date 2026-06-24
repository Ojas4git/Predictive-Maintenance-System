🔧 AI Predictive Maintenance System

🚀 Machine Failure Prediction using XGBoost & Streamlit

Live Demo:
👉 https://predictive-maintenance-system-ai.streamlit.app/


📌 Project Overview

Machine failures in industrial environments can result in:

Production Downtime
Increased Maintenance Costs
Operational Losses
Reduced Efficiency

This project uses Machine Learning (XGBoost) to predict machine failures based on machine operating conditions such as temperature, rotational speed, torque, and tool wear.

The solution is deployed as an interactive Streamlit Dashboard that allows users to enter machine parameters and receive real-time failure predictions and risk assessments.

🎯 Problem Statement

Traditional maintenance strategies are often:

Reactive (repair after failure)
Time-based (scheduled maintenance)

These approaches can lead to unnecessary maintenance costs or unexpected breakdowns.

Objective

Build a predictive maintenance system capable of:

✅ Predicting machine failures before they occur

✅ Reducing unplanned downtime

✅ Improving maintenance planning

✅ Increasing operational efficiency

✅ Supporting Industry 4.0 practices

📊 Dataset
AI4I 2020 Predictive Maintenance Dataset

The dataset contains operational sensor data collected from industrial machines.

Features Used
Feature	Description
Type	Machine Type (H, M, L)
Air Temperature [K]	Ambient Air Temperature
Process Temperature [K]	Machine Process Temperature
Rotational Speed [rpm]	Machine Rotational Speed
Torque [Nm]	Applied Torque
Tool Wear [min]	Tool Usage Time
Machine Failure	Target Variable
🛠️ Project Workflow
1️⃣ Exploratory Data Analysis (EDA)
Distribution Analysis
Failure vs Healthy Machine Analysis
Outlier Detection
Correlation Analysis
Feature Understanding
2️⃣ Data Preprocessing
Removed irrelevant columns
Label Encoding
Train-Test Split
Feature Scaling
3️⃣ Model Building

The following classification models were trained and evaluated:

Logistic Regression
Decision Tree
Random Forest
XGBoost
4️⃣ Hyperparameter Tuning

Used GridSearchCV to optimize:

max_depth
learning_rate
n_estimators

for improved recall and overall performance.

🤖 Final Model
XGBoost Classifier

XGBoost was selected as the final model because it achieved the best balance between:

Accuracy
Recall
Precision
F1 Score

while minimizing false negatives.

📈 Model Performance
Metric	Score
Accuracy	98.35%
Precision	79%
Recall	62%
F1 Score	0.70
Why Recall Matters?

For predictive maintenance:

Missing a failure is far more expensive
than inspecting a healthy machine.

Therefore Recall was prioritized during model evaluation and model selection.

🔍 Feature Importance Analysis

Top features identified by XGBoost:

Rank	Feature
1	Torque [Nm]
2	Rotational Speed [rpm]
3	Air Temperature [K]
4	Tool Wear [min]
5	Process Temperature [K]
6	Machine Type
Key Insights
Higher Torque increases failure risk.
Lower RPM is associated with machine failures.
Increased Tool Wear contributes significantly to failures.
Temperature variations affect machine reliability.
💻 Streamlit Dashboard
Features

✅ Machine Failure Prediction

✅ Failure Probability Estimation

✅ Risk Assessment

✅ Interactive Dashboard

✅ Real-Time User Inputs

Dashboard Preview

Add a screenshot here after deployment.

Example:

![Dashboard](dashboard.png)
🧰 Tech Stack
Programming Language
Python
Libraries
Pandas
NumPy
Scikit-Learn
XGBoost
Joblib
Streamlit
Matplotlib
Seaborn
Deployment
GitHub
Streamlit Cloud
📂 Project Structure
Predictive-Maintenance-System/
│
├── app.py
├── machine_failure_xgb.pkl
├── scaler.pkl
├── requirements.txt
├── Predictive_Maintenance_System.ipynb
├── ai4i2020.csv
└── README.md
🎓 Learning Outcomes

Through this project, I gained hands-on experience in:

Exploratory Data Analysis
Feature Engineering
Machine Learning Classification
Hyperparameter Tuning
Model Evaluation
Feature Importance Analysis
Streamlit Deployment
End-to-End ML Workflow
🔮 Future Improvements
IoT Sensor Integration
Real-Time Monitoring
Cloud Database Connectivity
Maintenance Scheduling Recommendations
Advanced Anomaly Detection
👨‍💻 Author
Ojas Savkar

Mechanical Engineering Student | AI/ML & Data Science Enthusiast

🔗 GitHub: https://github.com/Ojas4git

🚀 Live App: https://predictive-maintenance-system-ai.streamlit.app/
