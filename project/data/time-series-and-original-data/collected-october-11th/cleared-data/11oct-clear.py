import json

filename = "cleared-data-oct11.json"
day_of_collecting = 11
month_of_collecting = 10
year_of_collecting = 2022
collection_set = 6

with open(filename, "r") as file:
    result = json.load(file)

# 0. Delete duplicates
while True:
    links = []
    before = len(result)
    print(before)
    for listing in result:
        if listing["link"] in links:
            result.remove(listing)
        else:
            links.append(listing["link"])
    after = len(result)
    print(after)
    if before == after:
        break

# 1. STRIP IT
for listing in result:
    for key, v in listing.items():
        if type(v) == str:
            listing[key] = listing[key].strip()

# 2. "rent", "negotiable"
for listing in result:
    if "do negocjacji" in listing["rent"]:
        listing["negotiable"] = True
    else:
        listing["negotiable"] = False
    listing["rent"] = listing["rent"].rstrip("do negocjacji").strip()
    listing["rent"] = listing["rent"].rstrip("zł").strip()
    listing["rent"] = listing["rent"].replace(" ", "")
    listing["rent"] = int(listing["rent"])
    print(listing["rent"])

# 3. Listing clear/ keys / negotiable/ private
for listing in result:
    if "Poziom" not in listing:
        listing["Poziom"] = None
    listing["level"] = listing.pop("Poziom")
    listing["furnished"] = listing.pop("Umeblowane")
    listing["rent-extra"] = listing.pop("Czynsz (dodatkowo)")
    listing["surface"] = listing.pop("Powierzchnia")
    listing["rooms"] = listing.pop("Liczba pokoi")
    listing["building-type"] = listing.pop("Rodzaj zabudowy")
    if "Prywatne" not in listing:
        listing["Prywatne"] = False
    listing["private"] = listing.pop("Prywatne")
    if "Firmowe" in listing:
        del listing["Firmowe"]

# 4. level, rent-full, private, rent-extra
for listing in result:
    listing["rent-extra"] = listing["rent-extra"].split("zł")[0].strip().replace(" ", "").replace(",", ".")
    listing["rent-extra"] = int(round(float(listing["rent-extra"])))
    listing["rent-full"] = listing["rent-extra"] + listing["rent"]
    if listing["private"] == "Tak":
        listing["private"] = True
    else:
        listing["private"] = False
    if "level" not in listing:
        listing["level"] = None
    elif listing["level"] == "Parter":
        listing["level"] = "0"
    elif listing["level"] == "Powyżej 10":
        listing["level"] = "11"
    try:
        listing["level"] = int(listing["level"])
    except:
        print(listing["level"])

# 5. furnished, surface, rooms
for listing in result:
    if listing["furnished"] == "Tak":
        listing["furnished"] = True
    elif listing["furnished"] == "Nie":
        listing["furnished"] = False
    if listing["rooms"] == "Kawalerka":
        listing["rooms"] = "1"
    listing["rooms"] = listing["rooms"].split(" ")[0]
    listing["rooms"] = int(listing["rooms"])
    listing["surface"] = listing["surface"].split(" ")[0].replace(",", ".")
    listing["surface"] = int(round(float(listing["surface"])))
    print(listing["surface"])

# 6. Publish date
for listing in result:
    listing["collection_set"] = collection_set
    try:
        day, month, year = listing["publish-date"].split(" ")
        day = int(day)
        year = int(year)
        if month == "sierpnia":
            month = 8
        elif month == "września":
            month = 9
        elif month == "października":
            month = 10
        elif month == "listopada":
            month = 11
    except ValueError:
        day = day_of_collecting
        month = month_of_collecting
        year = year_of_collecting
    listing["publish-date"] = f"{year:02}-{month:02}-{day:02}"

# 7. Building type
for listing in result:
    x = listing["building-type"]
    if x == "Pozostałe":
        listing["building-type"] = 0
    elif x == "Dom wolnostojący":
        listing["building-type"] = 1
    elif x == "Kamienica":
        listing["building-type"] = 2
    elif x == "Szeregowiec":
        listing["building-type"] = 3
    elif x == "Blok":
        listing["building-type"] = 4
    elif x == "Apartamentowiec":
        listing["building-type"] = 5
    elif x == "Loft":
        listing["building-type"] = 6
    elif x == "Suterena":
        listing["building-type"] = 7
    elif x not in [0, 1, 2, 3, 4, 5, 6, 7]:
        print(listing["building-type"])
        input()

# 8. Counter
counter = 1
for listing in result:
    listing["listing_no"] = counter
    counter += 1

try:
    with open(filename, "w") as file:
        json.dump(result, file, indent=2, sort_keys=True)
    print("Success")
except:
    print("Failed")

# 9. Listing keys changed to splitted with _
for listing in result:
    listing["publish_date"] = listing.pop("publish-date")
    listing["building_type"] = listing.pop("building-type")
    listing["rent_extra"] = listing.pop("rent-extra")
    listing["rent_full"] = listing.pop("rent-full")

try:
    with open(filename, "w") as file:
        json.dump(result, file, indent=2, sort_keys=True)
    print("Success")
except:
    print("Failed")