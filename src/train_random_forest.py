import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

def train_random_forest():
    df = pd.read_csv("data/raw/creditcard.csv")

    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\nRandom Forest Model Training Completed!")
    print(classification_report(y_test, y_pred))

    with open("models/fraud_model_rf.pkl", "wb") as f:
        pickle.dump(model, f)

    print("\nModel saved at: models/fraud_model_rf.pkl")

if __name__ == "__main__":
    train_random_forest()
