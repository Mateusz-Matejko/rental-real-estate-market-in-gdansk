import json
from datetime import datetime, timedelta

pairs = [
    {"file1": "sep3.json", "file2": "sep11.json", "file2_date": "2022-09-11"},
    {"file1": "sep11.json", "file2": "sep19.json", "file2_date": "2022-09-19"},
    {"file1": "sep19.json", "file2": "sep26.json", "file2_date": "2022-09-26"},
]

for pair in pairs:
    file_name_1st = pair["file1"]
    file_name_2nd = pair["file2"]
    f2_y, f2_m, f2_d = pair["file2_date"].split("-")
    date2_minus_30 = datetime(int(f2_y), int(f2_m), int(f2_d)) - timedelta(30)

    possible_counter = 0
    links = []
    unrented_counter = 0

    with open(file_name_1st, "r") as f:
        result_file_1 = json.load(f)

    for listing in result_file_1:
        file1_year, file1_month, file1_day = listing["publish_date"].split("-")
        date1 = datetime(int(file1_year), int(file1_month), int(file1_day))
        if date1 >= date2_minus_30:
            possible_counter += 1
            links.append(listing["link"])

    with open(file_name_2nd, "r") as f:
        result_file_2 = json.load(f)

    for listing in result_file_2:
        for link in links:
            if link == listing["link"]:
                unrented_counter += 1


    def get_percentage(num1, num2):
        return f"{round((num1 / num2) * 100, 2)}%"

    rented = possible_counter - unrented_counter

    print(f"Could have been rented: {possible_counter}")
    print(f"Haven't been rented: {unrented_counter}, {get_percentage(unrented_counter, possible_counter)}")
    print(f"Successfully rented: {rented}, {get_percentage(rented, possible_counter)}")





