import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def main():
    data = get_data()
    df = pd.DataFrame(data)
    print(df.isnull().sum().sum())
    df.dropna(inplace=True)
    print(df.isnull().sum().sum())
    plt.hist(df["listing_no"])
    plt.xlabel("rent")
    plt.ylabel("rent_full")
    plt.show()
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)
    X_train.shape()
    y_train.shape()
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    print(y_pred)


def get_data():
    with open("sample_cleared_results.json", "r") as f:
        result = json.load(f)
    return result


if __name__ == '__main__':
    main()