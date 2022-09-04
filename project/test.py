import json


with open("data-operations.json", "r") as json_file:
    data = json.load(json_file)

# for listing in data:
#     if listing["Liczba pokoi"] == "Kawalerka":
#         listing["Liczba pokoi"] = 1
#     else:
#         listing["Liczba pokoi"] = listing["Liczba pokoi"][0]
#         listing["Liczba pokoi"] = int(listing["Liczba pokoi"])
#     print(listing["Liczba pokoi"])

with open("data-operations.json", "w") as json_file:
    json.dump(data, json_file, indent=2, sort_keys=True)