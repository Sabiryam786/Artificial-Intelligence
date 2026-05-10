from sklearn.linear_model import LinearRegression
import numpy as np

# training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# model
model = LinearRegression()

# train
model.fit(X, y)

# prediction
prediction = model.predict([[6]])

print("Prediction:", prediction)
