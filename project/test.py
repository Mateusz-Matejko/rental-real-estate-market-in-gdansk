import json


with open("data-operations.json", "r") as json_file:
    data = json.load(json_file)

for listing in data:
    listing["Rodzaj zabudowy"] = listing["Rodzaj zabudowy"].strip()
    # try: listing["Powierzchnia"] = int(listing["Powierzchnia"])
    # except: listing["Powierzchnia"] = float(listing["Powierzchnia"])

with open("data-operations.json", "w") as json_file:
    json.dump(data, json_file, indent=2)