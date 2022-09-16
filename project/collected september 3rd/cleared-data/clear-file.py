import json

with open("../../calculations/sep3.json", "r") as json_file:
    data = json.load(json_file)

number = 1
for listing in data:
    listing["listing_no"] = number
    number += 1
    # if "level" not in listing:
    #     print(listing)
    print(listing)


try:
    with open("cleared-data-3sep.json", "w") as json_file:
        json.dump(data, json_file, indent=2, sort_keys=True)
except:
    print("Unsuccessfully written")
print("Success")