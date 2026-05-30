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

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(forecast["Company"], forecast["5_Day_Forecast"])
ax.set_title("5 Day Forecast by Company")
ax.set_ylabel("Forecast Close Price")
st.pyplot(fig)
