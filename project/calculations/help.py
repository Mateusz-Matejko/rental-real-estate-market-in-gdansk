import json

with open("all-data-unfiltered.json", "r") as f:
    result = json.load(f)

for lisitng in result:
    if lisitng["furnished"] == "Nie":
        lisitng["furnished"] = False

with open("all-data-unfiltered.json", "w") as f:
    json.dump(result, f, indent=2, sort_keys=True)