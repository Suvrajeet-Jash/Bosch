import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
 
# Sample data
data = {
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 5, 4, 5]
}
 
df = pd.DataFrame(data)
print(df)
 
 
X = df[["x"]]   # Features must be 2D
y = df["y"]     # Target
 
model = LinearRegression()
model.fit(X, y)
 
 
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
 
 
y_pred = model.predict(X)
print("Predictions:", y_pred)
 
 
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, y_pred, color="red", label="Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()