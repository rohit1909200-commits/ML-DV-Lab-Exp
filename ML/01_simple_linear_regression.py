# Experiment 1: Simple Linear Regression
# Dataset: synthetic study-hours vs marks data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]], dtype=float)
y = np.array([35, 40, 50, 55, 65, 70, 75, 85], dtype=float)

model = LinearRegression().fit(X, y)
pred = model.predict(X)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("MSE:", mean_squared_error(y, pred))
print("R2:", r2_score(y, pred))
print("Predicted marks for 9 study hours:", model.predict([[9]])[0])

plt.scatter(X, y, label="Actual data")
plt.plot(X, pred, color="red", label="Regression line")
plt.xlabel("Study hours"); plt.ylabel("Marks")
plt.title("Simple Linear Regression"); plt.legend(); plt.show()
