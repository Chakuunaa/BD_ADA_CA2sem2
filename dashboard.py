import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Forecast Dashboard", layout="wide")

st.title("Stock Forecast Dashboard")

forecast = pd.read_csv("/home/chakuunaa/BD_ADA_CA2sem2/data/five_company_forecast_1_3_5_days.csv")
model = pd.read_csv("/home/chakuunaa/BD_ADA_CA2sem2/data/five_company_model_comparison.csv")

st.subheader("1, 3 and 5 Day Forecasts")
st.dataframe(forecast)

st.subheader("Model Comparison")
st.dataframe(model)

forecast_cols = ["1_Day_Forecast", "3_Day_Forecast", "5_Day_Forecast"]
rmse_cols = ["ARMA_RMSE", "ARIMA_RMSE", "SARIMA_RMSE"]

for col in forecast_cols:
    forecast[col] = pd.to_numeric(forecast[col], errors="coerce")

for col in rmse_cols:
    model[col] = pd.to_numeric(model[col], errors="coerce")

st.subheader("5 Day Forecast by Company")

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(forecast["Company"], forecast["5_Day_Forecast"])
ax.set_title("5 Day Forecast by Company")
ax.set_ylabel("Forecast Close Price")
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.subheader("Full Forecast Comparison")

fig2, ax2 = plt.subplots(figsize=(10, 6))
forecast.set_index("Company")[forecast_cols].plot(kind="bar", ax=ax2)
ax2.set_title("1, 3 and 5 Day Forecasts for Five Companies")
ax2.set_ylabel("Forecast Close Price")
ax2.set_xlabel("Company")
ax2.tick_params(axis="x", rotation=45)
plt.tight_layout()
st.pyplot(fig2)

st.subheader("RMSE Comparison")

fig3, ax3 = plt.subplots(figsize=(10, 6))
model.set_index("Company")[rmse_cols].plot(kind="bar", ax=ax3)
ax3.set_title("RMSE Comparison by Company")
ax3.set_ylabel("RMSE")
ax3.set_xlabel("Company")
ax3.tick_params(axis="x", rotation=45)
plt.tight_layout()
st.pyplot(fig3)

st.success("Dashboard loaded successfully")
