# Experiment 4: Interactive Dashboard with filters/slicers
# Run: pip install pandas plotly
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Category": ["Furniture", "Technology", "Office", "Furniture", "Technology", "Office"],
    "Date": pd.to_datetime(["2025-01-10", "2025-02-12", "2025-03-15",
                            "2025-04-10", "2025-05-12", "2025-06-15"]),
    "Sales": [1200, 1800, 900, 1500, 2200, 1100]
})
fig = px.bar(df, x="Region", y="Sales", color="Category",
             animation_frame=df["Date"].dt.month.astype(str),
             title="Sales by Region and Category")
fig.show()
print("Use Region, Category and Date as slicers/filters in Power BI or Tableau.")
