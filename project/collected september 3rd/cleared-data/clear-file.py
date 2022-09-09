import json

with open("../../calculations/sep3.json", "r") as json_file:
    data = json.load(json_file)

for listing in data:
    if listing["level"] == None:
        print(listing)
    # if "level" not in listing:
    #     print(listing)

# try:
#     with open("../../calculations/sep3.json", "w") as json_file:
#         json.dump(data, json_file, indent=2, sort_keys=True)
# except:
#     print("Unsuccessfully written")
# print("Success")