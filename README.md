# 🚀 Fraud Detection System (Machine Learning + FastAPI)

A complete end-to-end **Fraud Detection System** that identifies fraudulent financial transactions using **Machine Learning**, **Random Forest**, and an easy-to-use **FastAPI backend**.

This project includes:
- Data preprocessing  
- Model training (Logistic Regression + Random Forest)  
- API for real-time prediction  
- Clean project structure for deployment  
- Production-ready environment setup  

---

## 📌 Features

### ✅ 1. Data Preprocessing  
- Handles imbalance (fraud vs. non-fraud)  
- Scales numerical features  
- Removes noise  
- Splits dataset into train/test sets  

### ✅ 2. Machine Learning Models  
Two models trained and compared:
- **Logistic Regression**
- **Random Forest Classifier (final selected model)**  

### Model Metrics (Random Forest)
| Metric | Score |
|--------|--------|
| Precision | 0.81 |
| Recall | 0.82 |
| F1 Score | 0.81 |
| Accuracy | 99% |

---

## 🌐 3. FastAPI Backend (Real-Time Prediction)

Endpoint:
POST /predict

css
Copy code

Request JSON:
```json
{
  "Time": 1000,
  "V1": -1.23,
  "V2": 0.45,
  "V3": 1.89,
  "V4": -0.30,
  "V5": 0.12,
  "V6": 0.80,
  "V7": -1.10,
  "V8": 0.10,
  "V9": 0.56,
  "V10": -0.22,
  "V11": -1.56,
  "V12": 1.22,
  "V13": -0.80,
  "V14": 0.40,
  "V15": 0.33,
  "V16": -0.22,
  "V17": 0.87,
  "V18": -0.11,
  "V19": 0.65,
  "V20": -0.90,
  "V21": 0.12,
  "V22": 0.33,
  "V23": -0.44,
  "V24": 0.52,
  "V25": -0.22,
  "V26": 0.66,
  "V27": -0.11,
  "V28": 0.12,
  "Amount": 150.55
}
Response:

json
Copy code
{
  "prediction": "Legit" 
}
📂 Project Structure
css
Copy code
FraudDetectionSystem/
│── app.py
│── data/
│── models/
│── notebooks/
│── README.md
│── requirements.txt
│── src/
│── venv/
🛠 Installation & Setup
1️⃣ Clone the repository
bash
Copy code
git clone https://github.com/rwitankar-byte/Fraud-Detection-System.git
cd Fraud-Detection-System
2️⃣ Create Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
nginx
Copy code
pip install -r requirements.txt
4️⃣ Run FastAPI Server
lua
Copy code
uvicorn app:app --reload
Server will start at:

cpp
Copy code
http://127.0.0.1:8000
Swagger Docs:

arduino
Copy code
http://127.0.0.1:8000/docs
📊 Model Training
Training scripts are located in:

bash
Copy code
src/preprocessing.py
src/train_model.py
src/train_random_forest.py
Models are saved in:

bash
Copy code
models/fraud_model.pkl
models/fraud_model_rf.pkl
Random Forest is the final model used for predictions.

📜 License
This project is for educational purposes and can be extended for production.

🙌 Author
Rwitankar Pal
Fraud Detection System – Capstone Project

