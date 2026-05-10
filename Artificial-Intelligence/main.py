from model import train_model

model = train_model()

prediction = model.predict([[6]])

print("AI Prediction:", prediction)
