# Experiment 8: Time Series Forecasting and Trend Lines
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    "Month": pd.date_range("2024-01-01", periods=12, freq="MS"),
    "Sales": [100, 110, 108, 120, 125, 130, 128, 140, 145, 150, 158, 165]
})
x = np.arange(len(df))
slope, intercept = np.polyfit(x, df["Sales"], 1)
df["Trend"] = slope * x + intercept
df["Moving_Average"] = df["Sales"].rolling(window=3).mean()
print(df)
plt.plot(df["Month"], df["Sales"], marker="o", label="Actual")
plt.plot(df["Month"], df["Trend"], label="Linear trend")
plt.plot(df["Month"], df["Moving_Average"], label="3-month moving average")
plt.xlabel("Month"); plt.ylabel("Sales"); plt.title("Sales Trend Analysis")
plt.legend(); plt.xticks(rotation=45); plt.tight_layout(); plt.show()
# Power BI/Tableau: use Analytics pane for trend line/forecast; configure date as continuous.
