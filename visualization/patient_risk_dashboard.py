from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from clinical_risk import RISK_WEIGHTS, score_patients


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "patient_risk_sample.csv"


st.set_page_config(
    page_title="Patient Risk Dashboard",
    layout="wide",
)


@st.cache_data
def load_patient_data(uploaded_file=None) -> pd.DataFrame:
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    return pd.read_csv(DEFAULT_DATA)


def risk_gauge(score: float) -> go.Figure:
    return go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "/100"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#0f766e"},
                "steps": [
                    {"range": [0, 35], "color": "#dcfce7"},
                    {"range": [35, 55], "color": "#fef9c3"},
                    {"range": [55, 75], "color": "#ffedd5"},
                    {"range": [75, 100], "color": "#fee2e2"},
                ],
                "threshold": {"line": {"color": "#111827", "width": 3}, "value": score},
            },
        )
    )


st.title("Patient Risk Dashboard")

uploaded = st.sidebar.file_uploader("Upload patient CSV", type=["csv"])
patients = score_patients(load_patient_data(uploaded))

wards = sorted(patients["ward"].dropna().unique())
selected_wards = st.sidebar.multiselect("Wards", wards, default=wards)
risk_levels = ["Critical", "High", "Moderate", "Low"]
selected_levels = st.sidebar.multiselect("Risk levels", risk_levels, default=risk_levels)

filtered = patients[
    patients["ward"].isin(selected_wards) & patients["risk_level"].isin(selected_levels)
]

critical_count = int((filtered["risk_level"] == "Critical").sum())
high_count = int((filtered["risk_level"] == "High").sum())
avg_score = filtered["risk_score"].mean() if not filtered.empty else 0
max_score = filtered["risk_score"].max() if not filtered.empty else 0

kpi_a, kpi_b, kpi_c, kpi_d = st.columns(4)
kpi_a.metric("Patients", len(filtered))
kpi_b.metric("Critical", critical_count)
kpi_c.metric("High risk", high_count)
kpi_d.metric("Average score", f"{avg_score:.1f}")

left, right = st.columns([1.05, 1])

with left:
    st.subheader("Risk Triage Queue")
    display_cols = [
        "patient_id",
        "name",
        "ward",
        "risk_level",
        "risk_score",
        "heart_rate",
        "systolic_bp",
        "spo2",
        "temperature_c",
        "last_update",
    ]
    st.dataframe(
        filtered[display_cols],
        hide_index=True,
        use_container_width=True,
        column_config={
            "risk_score": st.column_config.ProgressColumn("Risk score", min_value=0, max_value=100),
            "spo2": st.column_config.NumberColumn("SpO2", format="%d%%"),
            "temperature_c": st.column_config.NumberColumn("Temp C", format="%.1f"),
        },
    )

with right:
    st.subheader("Composite Risk Load")
    st.plotly_chart(risk_gauge(max_score), use_container_width=True)

chart_a, chart_b = st.columns(2)

with chart_a:
    st.subheader("Ward Risk Distribution")
    ward_chart = (
        filtered.groupby(["ward", "risk_level"], as_index=False)
        .size()
        .rename(columns={"size": "patients"})
    )
    fig = px.bar(
        ward_chart,
        x="ward",
        y="patients",
        color="risk_level",
        category_orders={"risk_level": risk_levels},
        color_discrete_map={
            "Critical": "#b91c1c",
            "High": "#ea580c",
            "Moderate": "#ca8a04",
            "Low": "#15803d",
        },
    )
    st.plotly_chart(fig, use_container_width=True)

with chart_b:
    st.subheader("Vitals Risk Map")
    fig = px.scatter(
        filtered,
        x="systolic_bp",
        y="heart_rate",
        size="risk_score",
        color="risk_level",
        hover_name="name",
        hover_data=["ward", "spo2", "temperature_c", "blood_glucose"],
        category_orders={"risk_level": risk_levels},
        color_discrete_map={
            "Critical": "#b91c1c",
            "High": "#ea580c",
            "Moderate": "#ca8a04",
            "Low": "#15803d",
        },
    )
    fig.update_layout(xaxis_title="Systolic BP", yaxis_title="Heart rate")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Risk Factor Weighting")
weights = pd.DataFrame(
    [{"factor": factor.replace("_", " ").title(), "weight": weight} for factor, weight in RISK_WEIGHTS.items()]
)
fig = px.bar(weights, x="weight", y="factor", orientation="h", color="weight", color_continuous_scale="Teal")
fig.update_layout(yaxis={"categoryorder": "total ascending"}, coloraxis_showscale=False)
st.plotly_chart(fig, use_container_width=True)
