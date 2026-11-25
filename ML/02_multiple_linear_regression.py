# Experiment 2: Multiple Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Features: area (sq ft), bedrooms, age (years); target: house price (lakhs)
X = np.array([
    [800, 2, 10], [1000, 2, 8], [1200, 3, 5], [1500, 3, 4],
    [1800, 4, 3], [2000, 4, 2], [900, 2, 12], [1600, 3, 6]
], dtype=float)
y = np.array([32, 38, 48, 58, 70, 78, 30, 60], dtype=float)

model = LinearRegression().fit(X, y)
pred = model.predict(X)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("MSE:", mean_squared_error(y, pred))
print("R2:", r2_score(y, pred))
print("Estimated price:", model.predict([[1400, 3, 5]])[0], "lakhs")
