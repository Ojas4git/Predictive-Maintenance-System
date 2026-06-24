🔧 AI Predictive Maintenance System
🚀 Live Demo

Streamlit App:
https://predictive-maintenance-system-ai.streamlit.app/

📌 Project Overview

Machine failures in industrial environments can lead to production downtime, maintenance costs, and operational losses.

This project uses Machine Learning (XGBoost) to predict machine failures based on operational parameters such as temperature, rotational speed, torque, and tool wear, enabling predictive maintenance and proactive decision-making.

The solution is deployed as an interactive Streamlit dashboard where users can enter machine parameters and instantly receive failure predictions and risk assessments.

🎯 Problem Statement

Traditional maintenance approaches often rely on scheduled servicing or reactive repairs after failures occur.

The objective of this project is to:

Predict machine failures before they occur
Reduce unplanned downtime
Improve maintenance planning
Increase operational efficiency
Support predictive maintenance strategies
📊 Dataset

Dataset: AI4I 2020 Predictive Maintenance Dataset

The dataset contains operational data collected from industrial machines.

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
1. Exploratory Data Analysis (EDA)
Data understanding
Distribution analysis
Outlier detection
Failure vs Healthy machine analysis
Correlation analysis
2. Data Preprocessing
Removed irrelevant columns
Label Encoding
Train-Test Split
Feature Scaling
3. Model Building

The following machine learning models were trained and evaluated:

Logistic Regression
Decision Tree
Random Forest
XGBoost
4. Hyperparameter Tuning

Used GridSearchCV to optimize:

max_depth
learning_rate
n_estimators
🤖 Final Model
XGBoost Classifier

XGBoost was selected as the final model because it achieved the best balance between:

Accuracy
Recall
F1 Score
False Negative Reduction
📈 Model Performance
Metric	Score
Accuracy	98.35%
Recall	62%
Precision	79%
F1 Score	0.70
Why Recall Matters

For predictive maintenance, missing a machine failure can result in:

Unexpected breakdowns
Production losses
Higher maintenance costs

Therefore, Recall was prioritized over Accuracy during model selection.

🔍 Feature Importance Analysis

Top contributing features identified by XGBoost:

Torque [Nm]
Rotational Speed [rpm]
Air Temperature [K]
Tool Wear [min]
Process Temperature [K]
Machine Type
Key Insight

Higher torque, lower rotational speed, and increased tool wear were strongly associated with machine failure risk.

💻 Streamlit Dashboard Features
Dashboard Capabilities

✅ Machine Failure Prediction

✅ Failure Probability Estimation

✅ Risk Assessment

✅ Interactive User Interface

✅ Industrial Monitoring Style Dashboard

Input Parameters
Machine Type
Air Temperature
Process Temperature
Rotational Speed
Torque
Tool Wear
Outputs
Machine Healthy / Failure Prediction
Failure Probability
Risk Level Assessment
🧰 Technologies Used
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
Classification Models
Model Evaluation
Hyperparameter Tuning
Feature Importance Analysis
Streamlit Deployment
End-to-End Machine Learning Workflow
👨‍💻 Author

Ojas Savkar

Mechanical Engineering Student | AI/ML & Data Science Enthusiast

GitHub: https://github.com/Ojas4git

⭐ Future Improvements
Real-time sensor integration
IoT-based monitoring
Advanced anomaly detection
Cloud database integration
Maintenance scheduling recommendations
