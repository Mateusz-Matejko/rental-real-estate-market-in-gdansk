import json
import pprint
import pandas as pd


def main():
    result = get_result()
    df = pd.DataFrame(result)
    result_4_rooms = df[(df["rooms"] == 4) & (df["rent-full"] >= 4000)].describe()
    # result_4_rooms = result_4_rooms.reset_index()
    print(result_4_rooms.loc["mean"].to_dict())
    variable_x = result_4_rooms.loc["mean"].reset_index()
    variable_x.columns = ["asd", "3"]
    variable_y = variable_x.copy()
    variable_y.columns = ["asd", "4"]
    # print(variable_y)
    merge = variable_x.merge(variable_y, how="inner", on=["asd"])
    print(merge)
    print((merge["3"] - merge["4"]) / merge["3"])


def get_result():
    with open("sep3.json", "r") as file:
        result = json.load(file)
    return result


if __name__ == '__main__':
    main()