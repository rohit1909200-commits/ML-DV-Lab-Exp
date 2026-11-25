# Experiment 2: Data Cleaning and Transformation
import pandas as pd

df = pd.DataFrame({
    " customer ": ["Asha", "Ravi", "Asha", None, "Meera"],
    "sales": ["100", "200", None, "150", "250"],
    "region": ["north", "south", "north", "east", None]
})
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df["customer"] = df["customer"].fillna("Unknown").str.strip().str.title()
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["sales"] = df["sales"].fillna(df["sales"].median())
df["region"] = df["region"].fillna("Not specified").str.title()
df["sales_band"] = df["sales"].apply(lambda x: "High" if x >= 180 else "Low")
print("Cleaned data:\n", df)
# Power Query equivalent: Trim/Clean, Replace Values, Change Type, Fill, Add Conditional Column.
