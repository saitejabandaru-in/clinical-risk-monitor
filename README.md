# Clinical Risk Monitor

A real-time clinical risk stratification project for monitoring patient acuity across hospital wards. The repository now includes a runnable Streamlit dashboard, sample patient data, and a composite scoring engine for clinical triage demos.

## What It Does

- Scores patients from 0 to 100 using weighted clinical risk factors.
- Classifies patients into Low, Moderate, High, and Critical risk bands.
- Presents a triage queue sorted by urgency.
- Visualizes ward-level risk distribution and vital-sign risk patterns.
- Supports uploading a custom patient CSV for exploratory monitoring.

## Dashboard Preview

Run the Streamlit app to open the patient risk dashboard:

```bash
pip install -r requirements.txt
streamlit run visualization/patient_risk_dashboard.py
```

## Project Structure

```text
clinical_risk/
  __init__.py
  risk_scoring.py

data/
  patient_risk_sample.csv

visualization/
  patient_risk_dashboard.py

tests/
  test_risk_scoring.py

requirements.txt
README.md
```

## Risk Scoring Inputs

The composite score uses these patient variables:

| Factor | Weight |
| --- | ---: |
| Age | 0.10 |
| Heart rate | 0.12 |
| Systolic blood pressure | 0.13 |
| SpO2 | 0.13 |
| Temperature | 0.10 |
| Cholesterol | 0.12 |
| Blood glucose | 0.12 |
| BMI | 0.08 |
| Family history | 0.06 |
| Smoking status | 0.04 |

## Data Format

The dashboard expects a CSV with columns matching `data/patient_risk_sample.csv`:

```text
patient_id,name,ward,age,heart_rate,systolic_bp,spo2,temperature_c,cholesterol,blood_glucose,bmi,family_history,smoking_status,last_update
```

## Run Tests

```bash
pip install -r requirements.txt
pytest
```

## Notes

This project is for analytics and portfolio demonstration purposes. It is not a medical device and should not be used for clinical decisions without validation, governance, and regulatory review.

## Author

Sai Teja Bandaru

https://www.saitejabandaru.com/

## License

MIT License
