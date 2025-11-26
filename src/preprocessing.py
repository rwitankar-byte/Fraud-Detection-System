import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Separate features and target
    X = df.drop("Class", axis=1)
    y = df["Class"]

    # Scale the 'Amount' column
    scaler = StandardScaler()
    X["Amount"] = scaler.fit_transform(X["Amount"].values.reshape(-1,1))

    print("Preprocessing completed!")
    print("Fraud cases in dataset:", sum(y))
    print("Non-fraud cases:", len(y) - sum(y))

    return X, y

if __name__ == "__main__":
    df = pd.read_csv("data/raw/creditcard.csv")
    preprocess_data(df)
