import json
import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from plotnine import ggplot, aes, geom_point, geom_line
from plotnine.themes import theme_minimal


def main():
    linear_r_model()


def get_data():
    with open("all-data-unfiltered.json", "r") as f:
        result = json.load(f)
        for listing in result:
            listing["collection_set"] = listing.pop("collection_date")
            if listing["collection_set"] == "2022-09-03":
                listing["collection_set"] = 1
            elif listing["collection_set"] == "2022-09-11":
                listing["collection_set"] = 2
            elif listing["collection_set"] == "2022-09-19":
                listing["collection_set"] = 3
            elif listing["collection_set"] == "2022-09-26":
                listing["collection_set"] = 4
            elif listing["collection_set"] == "2022-10-03":
                listing["collection_set"] = 5
            else:
                print(listing["collection_set"])
                raise ValueError("Unrecognised data")
    return result


def linear_r_model():
    dataset = get_data()
    ds = pd.DataFrame(dataset)
    df = ds[["rent", "rooms"]]
    print(ds.describe())
    y = ds.rent
    X = ds[["rooms"]]
    model_lr = LinearRegression()
    model_lr.fit(X, y)

    # results
    print("model_lr.coef_: ", end="")
    print(model_lr.coef_)
    print("model_lr.intercept_: ", end="")
    print(model_lr.intercept_)

    # predictions
    print("model_lr.predict: ", end="")
    print(model_lr.predict(ds[["rent"]]))

    # Variance explained
    print("r2_score: ", end="")
    print(r2_score(
        y_true=df.rent,
        y_pred=model_lr.predict(df["rooms"])
    ))
    ds["fitted"] = model_lr.predict(df[["rent"]])
    print(ds.describe())
    ds[["rent", "rooms"]].plot.scatter(x="rooms", y="rent")
    ds[["fitted", "rooms"]].plot.scatter(x="rooms", y="fitted", color="r")
    plt.show()
    # print(ggplot(aes("rooms", "rent"), df)\
    #     + geom_point(alpha=0.5, color="#2c3e50")\
    #     + geom_line(aes(y="fitted"), color="blue")\
    #     + theme_minimal())


if __name__ == '__main__':
    main()