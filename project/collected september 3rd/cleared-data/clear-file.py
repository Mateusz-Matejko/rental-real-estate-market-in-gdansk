import json

with open("cleared-data.json", "r") as json_file:
    data = json.load(json_file)

for listing in data:
    listing["publish-date"] = listing["publish-date"].strip()
    day, month, year = listing["publish-date"].split()
    if month == "sierpnia":
        month = 8
    elif month == "września":
        month = 9
    day = int(day)
    year = int(year)
    listing["publish-date"] = year, month, day
    print(listing["publish-date"])

# try:
#     with open("cleared-data.json", "w") as json_file:
#         json.dump(data, json_file, indent=2, sort_keys=True)
# except:
#     print("Unsuccessfully written")
# print("Success")