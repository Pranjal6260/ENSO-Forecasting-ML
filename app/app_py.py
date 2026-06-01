import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(page_title="ENSO Forecast", layout="wide")

st.title("🌊 ENSO 1-Month Ahead Forecast Dashboard")

st.write("""
This dashboard predicts next month's ONI (Oceanic Niño Index)
using atmospheric variables and lag features.
""")

# Load model and feature columns
model = joblib.load("enso_forecast_model.pkl")
feature_columns = joblib.load("enso_feature_columns.pkl")

# Sidebar input
st.sidebar.header("Enter Feature Values")

input_data = {}

for col in feature_columns:
    input_data[col] = st.sidebar.number_input(col, value=0.0)

# Prediction button
if st.sidebar.button("Predict ONI"):

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.subheader(f"📊 Predicted ONI (Next Month): {prediction:.3f}")

    # Phase classification
    if prediction >= 0.5:
        st.success("🔴 Predicted Phase: El Niño")
    elif prediction <= -0.5:
        st.info("🔵 Predicted Phase: La Niña")
    else:
        st.warning("🟢 Predicted Phase: Neutral")

    st.write("### Phase Thresholds")
    st.write("El Niño  ≥  +0.5")
    st.write("La Niña  ≤  -0.5")
    st.write("Neutral  between -0.5 and +0.5")