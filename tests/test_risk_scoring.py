import pandas as pd

from clinical_risk import classify_risk, score_patient, score_patients


def test_score_patient_returns_bounded_score():
    patient = {
        "age": 70,
        "heart_rate": 130,
        "systolic_bp": 180,
        "spo2": 88,
        "temperature_c": 39.2,
        "cholesterol": 260,
        "blood_glucose": 240,
        "bmi": 33,
        "family_history": "yes",
        "smoking_status": "current",
    }

    score = score_patient(patient)

    assert 0 <= score <= 100
    assert classify_risk(score).label in {"High", "Critical"}


def test_score_patients_adds_triage_columns():
    patients = pd.DataFrame(
        [
            {"name": "Low", "age": 34, "heart_rate": 72, "systolic_bp": 118, "spo2": 99},
            {"name": "High", "age": 77, "heart_rate": 128, "systolic_bp": 182, "spo2": 89},
        ]
    )

    scored = score_patients(patients)

    assert {"risk_score", "risk_level", "priority", "risk_color"}.issubset(scored.columns)
    assert scored.iloc[0]["risk_score"] >= scored.iloc[1]["risk_score"]
