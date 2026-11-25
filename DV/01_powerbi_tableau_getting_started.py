# Experiment 1: Getting started with Power BI / Tableau
# Companion Python practice: load a CSV and create basic table, bar, and line views.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Category": ["A", "B", "A", "B", "A"],
    "Sales": [120, 150, 170, 160, 210]
})
print("Data preview:\n", df)
print("\nSummary:\n", df.describe(include="all"))
df.groupby("Category")["Sales"].sum().plot(kind="bar", title="Sales by Category")
plt.ylabel("Sales"); plt.tight_layout(); plt.show()
df.plot(x="Month", y="Sales", kind="line", marker="o", title="Monthly Sales")
plt.ylabel("Sales"); plt.tight_layout(); plt.show()
# Power BI/Tableau: Get Data -> Text/CSV -> select columns -> create Table, Bar and Line charts.
