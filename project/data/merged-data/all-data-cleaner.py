import json

with open("merged-data.json", "r") as f:
    result = json.load(f)

counter = 1
links = set()
new_result = []

for listing in result:
    if listing["link"] not in links:
        new_result.append(listing)
        links.add(listing["link"])
    result = new_result
    listing["listing_no"] = counter
    counter += 1


with open("merged-data.json", "w") as f:
    json.dump(result, f, indent=2, sort_keys=True)
