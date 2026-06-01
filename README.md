# 🌍 ENSO Event Forecasting using Machine Learning & Explainable AI

## Overview
This project predicts ENSO (El Niño Southern Oscillation) events using atmospheric and oceanic variables. Multiple machine learning models were trained and evaluated to forecast future Oceanic Niño Index (ONI) values.

The project also incorporates Explainable AI (XAI) techniques using SHAP to understand feature importance and improve model transparency.

## Objectives
- Forecast future ONI values
- Detect El Niño, La Niña, and Neutral phases
- Compare machine learning models
- Explain predictions using SHAP
- Provide an interactive Streamlit dashboard

## Dataset
- NOAA ONI Dataset
- ERA5 Climate Dataset

Variables Used:
- Temperature
- Relative Humidity
- Specific Humidity
- Wind Components (u, v, w)
- Geopotential Height
- Southern Oscillation Index (SOI)

## Models Used
- Random Forest
- Linear Regression
- XGBoost
- Support Vector Regression (SVR)

## Results

| Model | RMSE | R² |
|---------|---------|---------|
| Random Forest | 0.2787 | 0.6493 |
| Linear Regression | 0.3006 | 0.5920 |
| XGBoost | 0.3255 | 0.5217 |
| SVR | 0.4667 | 0.0169 |

### Best Model
Random Forest achieved the lowest RMSE and highest R² score.

## Explainability
SHAP (SHapley Additive exPlanations) was used to identify the most influential features affecting ENSO predictions.

Top Features:
- ONI_lag1
- ONI_lag6
- Temperature Lag Features
- SOI

## Dashboard Features
- ONI Prediction
- ENSO Event Classification
- Event Duration Detection
- Forecast Visualization

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP
- Streamlit
- Matplotlib

## Repository Structure
```
Data/
app/
notebooks/
images/
report/
README.md
requirements.txt
```

## Author
Pranjal Tamrakar
