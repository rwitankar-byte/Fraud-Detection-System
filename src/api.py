from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

def load_model():
    with open("models/fraud_model_rf.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

@app.get("/")
def home():
    return {"message": "Fraud Detection System API is running"}

@app.post("/predict")
def predict_transaction(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    result = "Fraud" if prediction == 1 else "Legit"
    return {"prediction": result}
