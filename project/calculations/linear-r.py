import json
import pprint
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def main():
    linear_r_model()


def get_data():
    with open("sample_cleared_results.json", "r") as f:
        result = json.load(f)
        # for listing in result:
        #     listing["collection_set"] = listing.pop("collection_date")
        #     if listing["collection_set"] == "2022-09-03":
        #         listing["collection_set"] = 1
        #     elif listing["collection_set"] == "2022-09-11":
        #         listing["collection_set"] = 2
        #     elif listing["collection_set"] == "2022-09-19":
        #         listing["collection_set"] = 3
        #     elif listing["collection_set"] == "2022-09-26":
        #         listing["collection_set"] = 4
        #     elif listing["collection_set"] == "2022-10-03":
        #         listing["collection_set"] = 5
        #     else:
        #         print(listing["collection_set"])
        #         raise ValueError("Unrecognised data")
    return result


def linear_r_model():
    dataset = get_data()
    df = pd.DataFrame(dataset)
    print(df[df.rooms == 2].describe())
    model_df = df[df.rooms == 1]
    model_df = model_df[["surface", "rent"]]
    print(model_df.describe())
    # print(df.describe())
    y = model_df.rent
    X = model_df[["surface"]]
    model_lr = LinearRegression().fit(X, y)

    # results
    print("model_lr.coef_: ", end="")
    print(model_lr.coef_)
    print("model_lr.intercept_: ", end="")
    print(model_lr.intercept_)

    # predictions
    print("model_lr.predict: ", end="")
    print(model_lr.predict(model_df[["rent"]]))

    # Variance explained
    print("r2_score: ", end="")
    print(r2_score(
        y_true=model_df.rent,
        y_pred=model_lr.predict(model_df[["surface"]])
    ))


#     ds["fitted"] = model_lr.predict(df[["rent"]])
#     print(ds.describe())
#     ds[["rent", "rooms"]].plot.scatter(x="rooms", y="rent")
#     ds[["fitted", "rooms"]].plot.scatter(x="rooms", y="fitted", color="r")


if __name__ == '__main__':
    main()