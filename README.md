# 🔧 AI Predictive Maintenance System

## 🚀 Live Demo

🔗 Streamlit App:  
https://predictive-maintenance-system-ai.streamlit.app/

---

## 📌 Project Overview

Machine failures in industrial environments can lead to production downtime, maintenance costs, and operational losses.

This project uses Machine Learning (XGBoost) to predict machine failures based on operational parameters such as temperature, rotational speed, torque, and tool wear. The solution enables predictive maintenance by identifying potential failures before they occur.

The project is deployed as an interactive Streamlit dashboard where users can enter machine parameters and instantly receive failure predictions along with risk assessments.

---

## 🎯 Problem Statement

Traditional maintenance approaches are generally:

- Reactive (repair after failure)
- Scheduled (maintenance at fixed intervals)

Both approaches can result in unnecessary costs or unexpected machine breakdowns.

### Objectives

- Predict machine failures before they occur
- Reduce unplanned downtime
- Improve maintenance planning
- Increase operational efficiency
- Support predictive maintenance strategies

---

## 📊 Dataset

**Dataset:** AI4I 2020 Predictive Maintenance Dataset

The dataset contains operational data collected from industrial machines.

### Features Used

| Feature | Description |
|----------|-------------|
| Type | Machine Type (H, M, L) |
| Air Temperature [K] | Ambient Air Temperature |
| Process Temperature [K] | Machine Process Temperature |
| Rotational Speed [rpm] | Machine Rotational Speed |
| Torque [Nm] | Applied Torque |
| Tool Wear [min] | Tool Usage Time |
| Machine Failure | Target Variable |

---

## 🛠️ Project Workflow

### 1. Exploratory Data Analysis (EDA)

- Distribution Analysis
- Outlier Detection
- Failure vs Healthy Machine Analysis
- Correlation Analysis
- Feature Understanding

### 2. Data Preprocessing

- Removed irrelevant columns
- Label Encoding
- Train-Test Split
- Feature Scaling

### 3. Model Development

The following machine learning models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

### 4. Hyperparameter Tuning

Used GridSearchCV to optimize:

- Max Depth
- Learning Rate
- Number of Estimators

### 5. Model Evaluation

Models were compared using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 🤖 Final Model

### XGBoost Classifier

XGBoost was selected as the final model because it achieved the best balance between:

- Accuracy
- Precision
- Recall
- F1 Score

while minimizing false negatives, which is critical in predictive maintenance systems.

---

## 📈 Model Performance

| Metric | Score |
|---------|---------|
| Accuracy | 98.35% |
| Precision | 79% |
| Recall | 62% |
| F1 Score | 0.70 |

### Why Recall Matters

In predictive maintenance, missing an actual machine failure can lead to:

- Unexpected breakdowns
- Production downtime
- Increased maintenance costs
- Operational losses

Therefore, Recall was prioritized during model selection.

---

## 🔍 Feature Importance Analysis

The XGBoost model identified the following features as most influential:

| Rank | Feature |
|--------|---------|
| 1 | Torque [Nm] |
| 2 | Rotational Speed [rpm] |
| 3 | Air Temperature [K] |
| 4 | Tool Wear [min] |
| 5 | Process Temperature [K] |
| 6 | Machine Type |

### Key Insights

- Higher torque significantly increases failure risk.
- Lower rotational speed is associated with machine failures.
- Increased tool wear contributes to failure probability.
- Temperature variations influence machine reliability.

---

## 💻 Streamlit Dashboard Features

### Dashboard Capabilities

- Machine Failure Prediction
- Failure Probability Estimation
- Risk Assessment
- Interactive User Interface
- Real-Time Input Parameters

### Input Parameters

- Machine Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

### Outputs

- Machine Health Status
- Failure Prediction
- Failure Probability
- Risk Level Assessment

---

## 🧰 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit
- Matplotlib
- Seaborn

### Deployment

- GitHub
- Streamlit Cloud

---

## 📂 Project Structure

```text
Predictive-Maintenance-System/
│
├── app.py
├── machine_failure_xgb.pkl
├── scaler.pkl
├── requirements.txt
├── Predictive_Maintenance_System.ipynb
├── ai4i2020.csv
└── README.md
```

## 🎓 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning Classification
- Hyperparameter Tuning
- Model Evaluation
- Feature Importance Analysis
- Model Deployment
- Streamlit Application Development

---

## 🔮 Future Improvements

- IoT Sensor Integration
- Real-Time Monitoring
- Cloud Database Connectivity
- Maintenance Scheduling Recommendations
- Advanced Anomaly Detection

---

## 👨‍💻 Author

**Ojas Savkar**

Mechanical Engineering Student | AI/ML & Data Science Enthusiast

GitHub: https://github.com/Ojas4git

Live Application: https://predictive-maintenance-system-ai.streamlit.app/

---

⭐ If you found this project interesting, consider giving the repository a star.
