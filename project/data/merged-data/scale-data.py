import json

all_paths_by_dict = [
    {"month": "sep", "day":"3",   "month_int": 9, "collection_set": 1},
    {"month": "sep", "day": "11", "month_int": 9,"collection_set": 2},
    {"month": "sep", "day": "19", "month_int": 9,"collection_set": 3},
    {"month": "sep", "day": "26", "month_int": 9,"collection_set": 4},
    {"month": "oct", "day": "3",  "month_int": 10,"collection_set": 5},
    {"month": "oct", "day": "11", "month_int": 10,"collection_set": 6},
    {"month": "oct", "day": "20", "month_int": 10,"collection_set": 7},
    {"month": "oct", "day": "27", "month_int": 10,"collection_set": 8},
    {"month": "nov", "day": "3",  "month_int": 9,"collection_set": 9},
]

final_result = []

for key in all_paths_by_dict:
    month_str = key["month"]
    day_str = key["day"]
    filepath_input = f"../time-series-and-original-data/collected-{month_str}-{day_str}/cleared-data/" \
                              f"cleared-data-{month_str}-{day_str}.json"

    with open(filepath_input, "r") as f:
        result = json.load(f)

    print(len(final_result))
    for listing in result:
        final_result.append(listing)

with open("merged-data.json", "w") as f:
    json.dump(final_result, f, indent=2, sort_keys=True)