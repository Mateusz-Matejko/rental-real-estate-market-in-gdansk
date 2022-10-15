import json

files = ["oct3.json", "sep3.json", "sep11.json", "sep19.json", "sep26.json"]

for file_name in files:
    with open(file_name) as file:
        result = json.load(file)

    for listing in result:
        if listing["furnished"] == "Nie":
            listing["furnished"] = False

    with open(file_name, "w") as file:
        json.dump(result, file)