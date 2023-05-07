
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

original_path = "project/data/time-series-and-original-data/collected-nov-3"

for key in all_paths_by_dict:
    month_str = key["month"]
    day_str = key["day"]
    collection_set = key["collection_set"]
    filepath_raw_input = f"time-series-and-original-data/collected-{month_str}-{day_str}/original-data/" \
                         f"original-data-{month_str}{day_str}.json"
    filepath_cleaned_output = f"time-series-and-original-data/collected-{month_str}-{day_str}/cleaned-data/" \
                              f"cleared-data-{month_str}-{day_str}.json"
    day_of_collecting = int(day_str)
    month_of_collecting = key["month_int"]
    print(filepath_raw_input)

