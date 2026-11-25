# Experiment 3: Bar and Line Charts for Series Data
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Date": pd.date_range("2025-01-01", periods=6, freq="MS"),
    "Product": ["A", "B", "A", "B", "A", "B"],
    "Sales": [120, 90, 150, 110, 170, 140]
})
category_sales = df.groupby("Product")["Sales"].sum()
category_sales.plot(kind="bar", title="Total Sales by Product")
plt.xlabel("Product"); plt.ylabel("Sales"); plt.tight_layout(); plt.show()

monthly = df.groupby("Date")["Sales"].sum()
monthly.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month"); plt.ylabel("Sales"); plt.grid(True); plt.tight_layout(); plt.show()
