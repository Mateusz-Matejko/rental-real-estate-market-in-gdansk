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
    trying_to_predict_variable = "rooms"
    given_variable = "rent"
    # print(df[df.rooms == 2].describe())
    # model_df = df[df.building_type == 5]
    for i in range(1, 2):
        dataset = get_data()
        df = pd.DataFrame(dataset)
        # model_df = model_df[(model_df.surface < 20) & (model_df.surface > 0)]
        for cs in range(1, 7):
            model_df = df
            # model_df = df[df.rooms == i]
            model_df = model_df[model_df.collection_set == cs]
            model_df = model_df[[given_variable, trying_to_predict_variable]]
            # print(model_df.describe())
            # print(df.describe())
            # !!! #
            y = model_df[[trying_to_predict_variable]]
            X = model_df[[given_variable]]
            model_lr = LinearRegression().fit(X, y)

            # # results
            # print("model_lr.coef_: ", end="")
            # print(model_lr.coef_)
            # print("model_lr.intercept_: ", end="")
            # print(model_lr.intercept_)

            # # predictions
            # print("model_lr.predict: ", end="")
            # print(model_lr.predict(model_df[[given_variable]]))

            # Variance explained
            print(f"r2 score for rooms: {i} and collection_set: {cs} = ", end="")
            print(r2_score(
                # !!! #
                y_true=model_df[[trying_to_predict_variable]],
                y_pred=model_lr.predict(model_df[[given_variable]])
            ))

#     ds["fitted"] = model_lr.predict(df[["rent"]])
#     print(ds.describe())
#     ds[["rent", "rooms"]].plot.scatter(x="rooms", y="rent")
#     ds[["fitted", "rooms"]].plot.scatter(x="rooms", y="fitted", color="r")


if __name__ == '__main__':
    main()