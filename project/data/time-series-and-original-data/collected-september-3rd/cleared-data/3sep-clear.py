import json

filename = "../../../../calculations/sep3.json"
day_of_collecting = 3
month_of_collecting = 9
yeare_of_collecting = 2022

with open(filename, "r") as file:
    result = json.load(file)

for listing in result:
    listing["listing_no"] += 1

try:
    with open(filename, "w") as file:
        json.dump(result, file, indent=2, sort_keys=True)
    print("Success")
except:
    print("Failed")