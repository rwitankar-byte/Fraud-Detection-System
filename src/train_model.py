import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle

def train_model():
    # Load preprocessed data
    df = pd.read_csv("data/raw/creditcard.csv")

    # Separate features and target
    X = df.drop("Class", axis=1)
    y = df["Class"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Logistic Regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    print("\nModel Training Completed!")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Save model
    with open("models/fraud_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("\nModel saved at: models/fraud_model.pkl")

if __name__ == "__main__":
    train_model()
