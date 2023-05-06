import json

def main():
        raw_data_cleaner(
        filepath_raw_input = 'original-data-oct20.json',
        filepath_cleaned_output = 'xxxxxxx.json',
        day_of_collecting = 1111,
        month_of_collecting = 22222,
        year_of_collecting = 33333,
        collection_set = 444444
                        )


def raw_data_cleaner(
    filepath_raw_input :str,
    filepath_cleaned_output :str,
    day_of_collecting :int,
    month_of_collecting :int,
    year_of_collecting :int,
    collection_set :int
                     ):

    # get the raw data to perform data cleaning
    with open(filepath_raw_input, "r") as file:
        result = json.load(file)

    # Step 0 - delete duplicates
    links = set()
    new_result = []
    for listing in result:
        if listing["link"] not in links:
            new_result.append(listing)
            links.add(listing["link"])
    result = new_result

    # 1. STRIP IT
    for listing in result:
        for key, val in listing.items():
            if type(val) == str:
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
        elif listing["level"] == "Poddasze":
            listing["level"] = "4"
        elif listing["level"] is None:
            continue
        try:
            listing["level"] = int(listing["level"])
        except:
            print(listing["level"])
            input("level problem -> line 97 ")

    # 5. Furnished, surface, rooms
    for listing in result:

        # furnished variable handling
        if listing["furnished"] == "Tak":
            listing["furnished"] = True
        elif listing["furnished"] == "Nie":
            listing["furnished"] = False

        # manual error handler for further improvement
        else:
            print(listing["furnished"])
            input("furnished variable creation problem -> line 109")

        # rooms variable handling & clearing
        if listing["rooms"] == "Kawalerka":
            listing["rooms"] = "1"

        listing["rooms"] = listing["rooms"].split(" ")[0]
        listing["rooms"] = int(listing["rooms"])

        # surface variable handling & clearing
        listing["surface"] = listing["surface"].split(" ")[0].replace(",", ".")
        listing["surface"] = int(round(float(listing["surface"])))


    # 6. Publish date handling
    for listing in result:
        try:
            day, month, year = listing["publish-date"].split(" ")
            day = int(day)
            year = int(year)
            month = {
                "sierpnia": 8,
                "września": 9,
                "października": 10,
                "listopada": 11,
            }.get(month, ValueError)
        except ValueError:
            day = day_of_collecting
            month = month_of_collecting
            year = year_of_collecting
        listing["publish-date"] = f"{year:02}-{month:02}-{day:02}"

    # 7. Building type handling
    for i, listing in enumerate(result):
        building_type = {
            "Pozostałe": 0,
            "Dom wolnostojący": 1,
            "Kamienica": 2,
            "Szeregowiec": 3,
            "Blok": 4,
            "Apartamentowiec": 5,
            "Loft": 6,
            "Suterena": 7
        }.get(listing["building-type"], None)

        # Check if building type is valid
        if building_type is None:
            print(listing["building-type"])
            input("Building type problem, line -> 14999999")

    # 8. Final polishing with change of variable

    counter = 1
    for listing in result:
        listing["listing_no"] = counter
        counter += 1
        listing["publish_date"] = listing.pop("publish-date")
        listing["building_type"] = listing.pop("building-type")
        listing["rent_extra"] = listing.pop("rent-extra")
        listing["rent_full"] = listing.pop("rent-full")
        listing["collection_set"] = collection_set


    # Save the final cleaned file
    try:
        with open(filepath_cleaned_output, "w") as file:
            json.dump(result, file, indent=2, sort_keys=True)
        print("Success")
    except:
        print("Failed")

if __name__ == '__main__':
    main()