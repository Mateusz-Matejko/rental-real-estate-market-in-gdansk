import json

with open("cleared-data-3sep.json", "r") as json_file:
    data = json.load(json_file)

for listing in data:
    x = listing["building-type"]
    if x == "Blok":
        listing["building-type"] = 4
    elif x == "Apartamentowiec":
        listing["building-type"] = 5
    elif x == "Kamienica":
        listing["building-type"] = 2
    elif x == "Dom wolnostojący":
        listing["building-type"] = 1
    elif x == "Szeregowiec":
        listing["building-type"] = 3
    elif x == "Pozostałe":
        listing["building-type"] = 0
    elif x not in [0, 1, 2, 3, 4, 5]:
        print(listing["building-type"])
        input()


try:
    with open("cleared-data-3sep.json", "w") as json_file:
        json.dump(data, json_file, indent=2, sort_keys=True)
except:
    print("Unsuccessfully written")
print("Success")