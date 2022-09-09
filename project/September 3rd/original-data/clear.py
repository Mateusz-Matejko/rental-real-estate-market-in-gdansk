import json

with open("result-backup.json", "r") as json_file:
    data = json.load(json_file)

with open("result-backup.json", "w") as json_file:
    json.dump(data, json_file, indent=2)