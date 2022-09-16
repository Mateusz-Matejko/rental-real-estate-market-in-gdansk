import json
import pprint
import pandas as pd


def main():
    result = get_result()
    data_frame = pd.DataFrame(result)


def price_for_room(result):
    data_frame = pd.DataFrame(result)
    for _ in range(1, 5):
        data_frame


def get_result():
    with open("sep3.json", "r") as file:
        result = json.load(file)
    return result


if __name__ == '__main__':
    main()