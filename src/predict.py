import pandas as pd
import pickle

def load_model(path):
    with open(path, "rb") as f:
        return pickle.load(f)

def predict_transaction(model_path, input_data):
    model = load_model(model_path)

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]

    if prediction == 1:
        return "⚠️ Fraudulent Transaction Detected"
    else:
        return "✓ Legit Transaction"

if __name__ == "__main__":
    sample = {
        "Time": 50000,
        "V1": -1.2,
        "V2": 0.3,
        "V3": 0.1,
        "V4": 0.5,
        "V5": -0.2,
        "V6": 1.1,
        "V7": -0.3,
        "V8": 0.2,
        "V9": 0.0,
        "V10": -0.1,
        "V11": 0.4,
        "V12": 0.6,
        "V13": -1.0,
        "V14": -0.5,
        "V15": 0.3,
        "V16": 0.1,
        "V17": -0.4,
        "V18": 0.2,
        "V19": -0.3,
        "V20": 0.1,
        "V21": -0.2,
        "V22": 0.3,
        "V23": 0.4,
        "V24": 0.0,
        "V25": -0.1,
        "V26": 0.2,
        "V27": -0.05,
        "V28": 0.01,
        "Amount": 100.00
    }

    print(predict_transaction("models/fraud_model_rf.pkl", sample))
