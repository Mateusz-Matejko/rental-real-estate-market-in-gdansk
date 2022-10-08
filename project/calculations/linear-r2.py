import pandas as pd
import matplotlib.pyplot as plt
import json


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
    result = get_data()
    data = pd.DataFrame(result)
    data = data["rooms" == 1]
    data = data[["rent", "collection_set"]]
    print(data)
    plt.scatter(data.collection_set, data.rent)
    plt.show()


def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].rent
        y = points.iloc[i].score
        total_error += (y - (m * x + b)) ** 2
    total_error / float(len(points))


if __name__ == '__main__':
    main()