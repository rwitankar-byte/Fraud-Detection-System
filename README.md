# 🚀 Fraud Detection System (Machine Learning + FastAPI)

A machine-learning powered **Fraud Detection System** that predicts whether a financial transaction is **Legit** or **Fraudulent**.  
Built using **Python, scikit-learn, FastAPI, Random Forest**, and the **Kaggle Credit Card Fraud Dataset**.

---

## 📖 Overview
Financial fraud is a major modern risk. This project uses machine learning models to analyze transaction data and determine whether a given transaction is suspicious.

This system:
- Trains models using real financial transaction data
- Exposes a REST API for prediction
- Returns JSON responses such as:
```json
{
  "prediction": "Legit"
}
🧰 Tech Stack

Python 3.13+

FastAPI (API layer)

Uvicorn (server)

scikit-learn (ML models)

pandas, numpy (data handling)

📁 Folder Structure
FraudDetectionSystem/
│── data/
│    └── creditcard.csv
│── models/
│    ├── fraud_model.pkl
│    └── fraud_model_rf.pkl
│── src/
│    ├── load_data.py
│    ├── preprocessing.py
│    ├── train_model.py
│    ├── train_random_forest.py
│    ├── api.py
│    └── utils.py
│── venv/
│── requirements.txt
│── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/rwitankar-byte/FraudDetectionSystem.git
cd FraudDetectionSystem

2️⃣ Create Virtual Environment (Mac)
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the API

Start the FastAPI server:

uvicorn src.api:app --reload


API will run at:

http://127.0.0.1:8000


Interactive documentation (Swagger UI):

http://127.0.0.1:8000/docs

🧪 API Usage
POST /predict

Send JSON like:

{
  "Time": 12,
  "V1": -1.23,
  "V2": 0.56,
  "V3": -0.78,
  "Amount": 120.50
}

Response:
{
  "prediction": "Legit"
}

📊 Model Details
Models Trained

Logistic Regression

Random Forest ✅ (Selected as final model)

Performance Highlights

High accuracy

Strong recall on fraud class (~82%)

Model stored in models/fraud_model_rf.pkl

📜 How It Works

Load and preprocess dataset

Train ML models

Save best model

API loads model on startup

User sends JSON → model predicts → returns result

🚧 Future Enhancements

Dashboard for monitoring predictions

Real-time fraud streaming engine

Cloud deployment (Render/AWS)

Deep learning (Autoencoders, LSTM)

🙍‍♂️ Author

Rwitankar Pal
