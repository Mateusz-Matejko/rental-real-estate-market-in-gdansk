import json

import pandas as pd


def main():
    result = get_result()
    df = pd.DataFrame(result)
    print(df.listing_no[df.rent_extra >= 5000])


def get_result():
    with open("all-data-filtered.json", "r") as f:
        return json.load(f)


if __name__ == '__main__':
    main()