"""Composite clinical risk scoring for patient monitoring dashboards."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import pandas as pd


RISK_WEIGHTS: dict[str, float] = {
    "age": 0.10,
    "heart_rate": 0.12,
    "systolic_bp": 0.13,
    "spo2": 0.13,
    "temperature_c": 0.10,
    "cholesterol": 0.12,
    "blood_glucose": 0.12,
    "bmi": 0.08,
    "family_history": 0.06,
    "smoking_status": 0.04,
}


@dataclass(frozen=True)
class RiskBand:
    label: str
    priority: int
    color: str


def _clip(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(value, upper))


def _factor_risks(patient: Mapping[str, object]) -> dict[str, float]:
    """Return normalized 0-1 risk contributions for supported variables."""

    age = float(patient.get("age", 0) or 0)
    heart_rate = float(patient.get("heart_rate", 0) or 0)
    systolic_bp = float(patient.get("systolic_bp", 0) or 0)
    spo2 = float(patient.get("spo2", 100) or 100)
    temperature_c = float(patient.get("temperature_c", 37) or 37)
    cholesterol = float(patient.get("cholesterol", 0) or 0)
    blood_glucose = float(patient.get("blood_glucose", 0) or 0)
    bmi = float(patient.get("bmi", 0) or 0)

    family_history = str(patient.get("family_history", "no")).strip().lower()
    smoking_status = str(patient.get("smoking_status", "never")).strip().lower()

    return {
        "age": _clip((age - 35) / 50),
        "heart_rate": _clip(abs(heart_rate - 75) / 65),
        "systolic_bp": _clip((systolic_bp - 110) / 80),
        "spo2": _clip((96 - spo2) / 12),
        "temperature_c": _clip(abs(temperature_c - 37.0) / 4),
        "cholesterol": _clip((cholesterol - 170) / 130),
        "blood_glucose": _clip((blood_glucose - 90) / 180),
        "bmi": _clip(abs(bmi - 24) / 22),
        "family_history": 1.0 if family_history in {"yes", "true", "1"} else 0.0,
        "smoking_status": {"never": 0.0, "former": 0.45, "current": 1.0}.get(smoking_status, 0.0),
    }


def score_patient(patient: Mapping[str, object]) -> float:
    """Calculate a composite patient risk score from 0 to 100."""

    factor_risks = _factor_risks(patient)
    weighted_score = sum(factor_risks[factor] * weight for factor, weight in RISK_WEIGHTS.items())
    return round(weighted_score * 100, 1)


def classify_risk(score: float) -> RiskBand:
    """Map a 0-100 score to a clinician-friendly risk band."""

    if score >= 75:
        return RiskBand("Critical", 4, "#b91c1c")
    if score >= 55:
        return RiskBand("High", 3, "#ea580c")
    if score >= 35:
        return RiskBand("Moderate", 2, "#ca8a04")
    return RiskBand("Low", 1, "#15803d")


def score_patients(patients: pd.DataFrame) -> pd.DataFrame:
    """Attach risk score, severity, priority, and color columns to patient rows."""

    scored = patients.copy()
    scored["risk_score"] = scored.apply(lambda row: score_patient(row.to_dict()), axis=1)
    bands = scored["risk_score"].apply(classify_risk)
    scored["risk_level"] = bands.apply(lambda band: band.label)
    scored["priority"] = bands.apply(lambda band: band.priority)
    scored["risk_color"] = bands.apply(lambda band: band.color)
    return scored.sort_values(["priority", "risk_score"], ascending=[False, False])
