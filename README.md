<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,100:2C5364&height=200&section=header&text=Clinical%20Risk%20Monitor&fontSize=40&fontColor=E6EEF3&animation=fadeIn&fontAlignY=40" />
</p>

<p align="center">
  🏥 Clinical Intelligence &nbsp;|&nbsp; 📊 Patient Risk Dashboard &nbsp;|&nbsp; ⚡ Real-Time Triage Monitoring
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/Data-Pandas%20%7C%20NumPy-lightgrey?style=flat-square"/>
  <img src="https://img.shields.io/badge/Visualization-Plotly-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Architecture-Risk%20Scoring-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square"/>
</p>

---

# 🏥 Clinical Risk Monitor

A **real-time clinical risk stratification system** designed to support **patient triage, ward-level monitoring, and healthcare decision analytics** through a runnable **Streamlit patient risk dashboard**.

This project demonstrates how a modern clinical decision support prototype can combine **patient data, weighted risk scoring, and interactive visualization** into one deployable analytics workflow.

---

## 🧠 Overview

The **Clinical Risk Monitor** integrates multiple dimensions of patient data:

- 🫀 Vital signs and oxygen saturation
- 🧪 Laboratory-style risk indicators
- 🧬 Family history and clinical background
- 🏃 Lifestyle and smoking status
- 👤 Demographic context

Using a **weighted composite scoring model**, the system produces:

✔ Patient-level risk scores from 0 to 100
✔ Severity bands: Low, Moderate, High, Critical
✔ A clinician-friendly triage queue
✔ Ward-level risk distribution charts
✔ Interactive vital-sign risk mapping
✔ CSV upload support for custom patient cohorts

---

## ⚙️ Core Features

### 🔬 Multi-Factor Risk Assessment
- 10 clinical variables across vitals, labs, demographics, lifestyle, and history
- Weighted scoring model for transparent risk contribution
- Normalized factor scoring with bounded 0-100 composite output

### ⏱️ Patient Triage Dashboard
- Streamlit-based interactive dashboard
- KPI cards for total patients, critical patients, high-risk patients, and average score
- Sortable triage table with progress-style risk score display

### 🌡️ Vitals Risk Map
- Plotly scatter visualization for heart rate and systolic blood pressure
- Bubble size reflects composite risk score
- Hover details include ward, SpO2, temperature, and blood glucose

### 📊 Ward Risk Distribution
- Color-coded severity breakdown by ward
- Fast comparison across ICU, Emergency, Cardiology, and General units

### 🎯 Composite Risk Gauge
- Aggregated patient risk load visualization
- Dynamic thresholds for low → critical risk bands

---

## 🧬 System Workflow

```text
Patient CSV Data
↓
Data Loading Layer
↓
Risk Scoring Engine
↓
Composite Risk Score + Severity Band
↓
Streamlit Dashboard
↓
Triage Queue + Charts + Clinical Monitoring Views
```

---

## 🗂️ Project Structure

```text
clinical_risk/
├── __init__.py
└── risk_scoring.py

data/
└── patient_risk_sample.csv

visualization/
└── patient_risk_dashboard.py

tests/
└── test_risk_scoring.py

requirements.txt
README.md
```

---

## 📊 Risk Scoring Methodology

| Category     | Variables                                 | Weight |
|--------------|-------------------------------------------|--------|
| Vital        | Heart Rate, Blood Pressure, SpO2, Temp    | 0.48   |
| Lab          | Cholesterol, Blood Glucose                | 0.24   |
| Demographic  | Age Factor                                | 0.10   |
| Physical     | BMI Index                                 | 0.08   |
| Genetic      | Family History                            | 0.06   |
| Lifestyle    | Smoking Status                            | 0.04   |

📌 Generates a **composite patient risk score** for dashboard-based clinical prioritization.

---

## 📁 Sample Data Format

The dashboard includes `data/patient_risk_sample.csv` and supports uploaded CSV files with the same columns:

```text
patient_id,name,ward,age,heart_rate,systolic_bp,spo2,temperature_c,cholesterol,blood_glucose,bmi,family_history,smoking_status,last_update
```

---

## 🚀 Quick Start

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the patient risk dashboard

```bash
streamlit run visualization/patient_risk_dashboard.py
```

### Run tests

```bash
pytest
```

---

## 🧪 Tech Stack

* Python 3.10+
* Streamlit
* Pandas / NumPy
* Plotly
* Pytest

---

## 📈 What This Project Demonstrates

✔ Healthcare analytics dashboarding
✔ Patient risk stratification logic
✔ Interactive clinical monitoring workflows
✔ Data-driven triage prioritization
✔ Portfolio-ready Streamlit application design
✔ Testable Python scoring utilities

---

## ⚠️ Disclaimer

This project is for analytics, education, and portfolio demonstration purposes. It is **not a medical device** and should not be used for real clinical decisions without validation, governance, and regulatory review.

---

## 👨‍💻 Author

**Sai Teja Bandaru**
*Data Scientist & AI Researcher*

🌐 [https://www.saitejabandaru.com/](https://www.saitejabandaru.com/)
💼 LinkedIn
💻 GitHub

---

## 📄 License

MIT License — see `LICENSE` for details.

---

## ⭐ Support

If you find this useful:

⭐ Star the repo
🍴 Fork it
📢 Share it

---

> Building intelligent systems that bring data-driven precision into healthcare.
