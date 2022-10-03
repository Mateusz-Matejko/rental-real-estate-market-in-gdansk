import json

filename = "cleared-data-3oct-backup.json"
day_of_collecting = 3
month_of_collecting = 10
year_of_collecting = 2022
collection_set = 5

with open(filename, "r") as file:
    result = json.load(file)

for lisitng in result:
    lisitng["collection_set"] = lisitng.pop("colection_set")

try:
    with open(filename, "w") as file:
        json.dump(result, file, indent=2, sort_keys=True)
    print("Success")
except:
    print("Failed")