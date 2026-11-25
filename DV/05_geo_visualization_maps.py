# Experiment 5: Geo-Visualization with Maps
# Run: pip install pandas plotly
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Bengaluru", "Chennai", "Kolkata"],
    "Latitude": [28.6139, 19.0760, 12.9716, 13.0827, 22.5726],
    "Longitude": [77.2090, 72.8777, 77.5946, 80.2707, 88.3639],
    "Sales": [120, 180, 150, 100, 90]
})
fig = px.scatter_map(df, lat="Latitude", lon="Longitude", size="Sales",
                     hover_name="City", color="Sales", zoom=3,
                     title="City-wise Sales Map")
fig.show()
# Power BI: use City/Latitude/Longitude fields in Map or Azure Maps visual.
