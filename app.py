import warnings
warnings.filterwarnings("ignore")  # 🔥 remove warnings

import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from src.recommend import get_recommendations

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Student Dashboard", layout="wide")

# -------------------------
# LOAD MODEL
# -------------------------
model = pickle.load(open("models/model.pkl", "rb"))

st.title("🎓 Student Performance Dashboard")

# -------------------------
# SIDEBAR INPUTS
# -------------------------
input_dict = {
    "study_hours": st.sidebar.slider("Study Hours", 1.0, 10.0, 5.0),
    "attendance": st.sidebar.slider("Attendance", 50.0, 100.0, 75.0),
    "previous_score": st.sidebar.slider("Previous Score", 40.0, 100.0, 70.0),
    "sleep_hours": st.sidebar.slider("Sleep Hours", 4.0, 9.0, 6.0),
    "internet_usage": st.sidebar.slider("Internet Usage", 1.0, 8.0, 4.0),
    "extracurricular": st.sidebar.selectbox("Extracurricular", [0, 1]),
    "parent_education": st.sidebar.selectbox("Parent Education", [1, 2, 3])
}

# -------------------------
# PREDICTION
# -------------------------
input_df = pd.DataFrame([input_dict])
prediction = model.predict(input_df)[0]

# -------------------------
# KPI SECTION
# -------------------------
k1, k2, k3 = st.columns(3)

k1.metric("Score", round(prediction, 2))
k2.metric("Study Hours", input_dict["study_hours"])
k3.metric("Attendance", input_dict["attendance"])

# -------------------------
# SMALL CHART FUNCTION
# -------------------------
def small_chart():
    fig, ax = plt.subplots(figsize=(2, 1))  # 🔥 small size
    return fig, ax

# -------------------------
# DASHBOARD (SINGLE ROW)
# -------------------------
c1, c2, c3, c4 = st.columns(4)

# -------------------------
# Feature Importance
# -------------------------
with c1:
    st.write("FI")

    if hasattr(model, "feature_importances_"):
        fig, ax = small_chart()
        ax.barh(list(input_dict.keys()), model.feature_importances_)
        ax.tick_params(labelsize=5)
        st.pyplot(fig)

# -------------------------
# Input Profile
# -------------------------
with c2:
    st.write("Input")

    fig, ax = small_chart()
    ax.bar(list(input_dict.keys()), list(input_dict.values()))
    ax.tick_params(axis='x', labelrotation=90, labelsize=5)
    st.pyplot(fig)

# -------------------------
# Comparison
# -------------------------
with c3:
    st.write("Compare")

    try:
        df = pd.read_csv("data/student_data.csv")
        avg = df.mean()

        fig, ax = small_chart()
        ax.bar(["You"], [prediction])
        ax.bar(["Avg"], [avg.mean()])
        ax.tick_params(labelsize=5)
        st.pyplot(fig)

    except:
        st.write("No data")

# -------------------------
# Score Chart
# -------------------------
with c4:
    st.write("Score")

    fig, ax = small_chart()
    ax.bar(["Score"], [prediction])
    ax.set_ylim(0, 100)
    ax.tick_params(labelsize=5)
    st.pyplot(fig)

# -------------------------
# RECOMMENDATIONS
# -------------------------
st.markdown("### 🤖 Tips")

recs = get_recommendations(input_dict)

if recs:
    for r in recs[:2]:
        st.write("✔️", r)
else:
    st.write("Good performance 👍")