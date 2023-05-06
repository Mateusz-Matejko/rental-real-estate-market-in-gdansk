def raw_data_cleaner(
        raw_data_filepath='xxxxx',
        cleared_data_filepath='xxxx',
        collection_set=9,
        day_of_collecting=999,
        month_of_collecting=999,
        year_of_collecting=999,
):
    with open(raw_data_filepath, "r") as file:
        result = json.load(file)

    # 0. Delete duplicates
    result = [dict(t) for t in {tuple(d.items()) for d in result}]

    # 1. STRIP IT
    for listing in result:
        for key, value in listing.items():
            if isinstance(value, str):
                listing[key] = value.strip()

    # 2. "rent", "negotiable"
    for listing in result:
        rent = listing["rent"]
        negotiable = "do negocjacji" in rent
        listing["negotiable"] = negotiable
        rent = rent.rstrip("do negocjacji").rstrip("zł").replace(" ", "")
        listing["rent"] = int(rent)

    # 3. Listing clear/ keys / negotiable/ private
    for listing in result:
        listing["level"] = listing.pop("Poziom", None)
        listing["furnished"] = listing.pop("Umeblowane", None)
        listing["rent-extra"] = listing.pop("Czynsz (dodatkowo)", None)
        listing["surface"] = listing.pop("Powierzchnia", None)
        listing["rooms"] = listing.pop("Liczba pokoi", None)
        listing["building-type"] = listing.pop("Rodzaj zabudowy", None)
        listing["private"] = listing.pop("Prywatne", False)

    # 4. level, rent-full, private, rent-extra
    for listing in result:
        rent_extra = listing["rent-extra"]
        rent_extra = rent_extra.split("zł")[0].strip().replace(",", ".")
        rent_extra = int(round(float(rent_extra)))
        rent_full = listing["rent"] + rent_extra
        private = listing["private"] == "Tak"
        level = listing["level"]
        if level == "Parter":
            level = "0"
        elif level == "Powyżej 10":
            level = "11"
        elif level == "Poddasze":
            level = "4"
        try:
            level = int(level)
        except ValueError:
            level = None
        listing.update(rent_extra=rent_extra, rent_full=rent_full, private=private, level=level)

    # 5. furnished, surface, rooms
    for listing in result:
        furnished = listing["furnished"]
        furnished = furnished == "Tak"
        rooms = listing["rooms"]
        if rooms == "Kawalerka":
            rooms = "1"
        rooms = rooms.split(" ")[0]
        rooms = int(rooms)
        surface = listing["surface"]
        surface = surface.split(" ")[0].replace(",", ".")
        surface = int(round(float(surface)))
        listing.update(furnished=furnished, rooms=rooms, surface=surface)

    # 6. Publish date
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

    # 7. Building type
    # Combine loops and use dictionary lookup for building type
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
            input("Building type problem, line -> 109")

        # Update listing with new keys and values
        listing.update({
            "listing_no": i + 1,
            "publish_date": listing.pop("publish-date"),
            "building_type": building_type,
            "rent_extra": listing.pop("rent-extra"),
            "rent_full": listing.pop("rent-full")
        })

    # 8. Counter
    # Use enumerate() to get index and update listing with new key-value pair
    for i, listing in enumerate(result):
        listing["listing_no"] = i + 1

    # 9. Save result to file
    try:
        with open(cleared_data_filepath, "w") as file:
            # Save result to file as formatted JSON
            json.dump(result, file, indent=2, sort_keys=True)
            print("Success")
    except:
        print("Failed")