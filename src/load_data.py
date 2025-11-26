import pandas as pd

def load_data():
    path = "data/raw/creditcard.csv"
    df = pd.read_csv(path)
    print("Dataset loaded successfully!")
    print(df.head())
    print("\nShape:", df.shape)
    return df

if __name__ == "__main__":
    load_data()
