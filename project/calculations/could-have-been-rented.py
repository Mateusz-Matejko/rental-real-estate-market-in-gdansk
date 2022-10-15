import json
from datetime import datetime, timedelta

requirement_name = "rooms"
requirement_value = 1

pairs = [
    [
        {"file1": "sep3.json", "file1_date": "2022-09-03", "file2": "sep11.json", "file2_date": "2022-09-11", "days": 8},
        {"file1": "sep3.json", "file1_date": "2022-09-03", "file2": "sep19.json", "file2_date": "2022-09-19", "days": 16},
        {"file1": "sep3.json", "file1_date": "2022-09-03", "file2": "sep26.json", "file2_date": "2022-09-26", "days": 23},
    ],
    [
        {"file1": "sep11.json", "file1_date": "2022-09-11", "file2": "sep19.json", "file2_date": "2022-09-19", "days": 8},
        {"file1": "sep11.json", "file1_date": "2022-09-11", "file2": "sep26.json", "file2_date": "2022-09-26", "days": 15},
        {"file1": "sep11.json", "file1_date": "2022-09-11", "file2": "oct3.json", "file2_date": "2022-10-03", "days": 22},
    ],
    [
        {"file1": "sep19.json", "file1_date": "2022-09-19", "file2": "sep26.json", "file2_date": "2022-09-26", "days": 7},
        {"file1": "sep19.json", "file1_date": "2022-09-19", "file2": "oct3.json", "file2_date": "2022-10-03", "days": 14},
        {"file1": "sep19.json", "file1_date": "2022-09-19", "file2": "oct11.json", "file2_date": "2022-10-10", "days": 22},
    ]
        ]


# {"file1": "sep3.json", "file2": "sep11.json", "file2_date": "2022-09-11", "days":},
# {"file1": "sep3.json", "file2": "sep11.json", "file2_date": "2022-09-11", "days":},
# {"file1": "sep11.json", "file2": "sep19.json", "file2_date": "2022-09-19"},
# {"file1": "sep19.json", "file2": "sep26.json", "file2_date": "2022-09-26"},
# {"file1": "sep26.`json", "file2": "oct3.json", "file2_date": "2022-10-03"}`


# get info specific from dictionary
for inside in pairs:
    for pair in inside:
        file_name_1st = pair["file1"]
        file_name_2nd = pair["file2"]
        f2_y, f2_m, f2_d = pair["file2_date"].split("-")
        f1_y, f1_m, f1_d = pair["file1_date"].split("-")
        days = pair["days"]
        date2_minus_30 = datetime(int(f2_y), int(f2_m), int(f2_d)) - timedelta(30)

        possible_counter = 0
        links = []
        no_rented = 0

        with open(file_name_1st, "r") as f:
            result_file_1 = json.load(f)

        for listing in result_file_1:
            if listing[requirement_name] != requirement_value:
                continue
            file1_year, file1_month, file1_day = listing["publish_date"].split("-")
            date1 = datetime(int(file1_year), int(file1_month), int(file1_day))
            if date1 >= date2_minus_30:
                possible_counter += 1
                links.append(listing["link"])

        with open(file_name_2nd, "r") as f:
            result_file_2 = json.load(f)

        for listing in result_file_2:
            if listing["link"] in links:
               no_rented += 1


        def get_percentage(num1, num2):
            return f"{round((num1 / num2) * 100, 2)}%"

        rented = possible_counter - no_rented

        print()
        print(f"For data collected in {pair['file1_date']}")
        print(f"Could have been rented in {days} days: {possible_counter}")
        print(f"Haven't been rented {days} days: {no_rented}, {get_percentage(no_rented, possible_counter)}")
        print(f"Successfully rented in {days} days: {rented}, {get_percentage(rented, possible_counter)}")





