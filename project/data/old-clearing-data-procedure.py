import json
import pprint



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

    counter = 1
    for listing in result:
        listing["listing_no"] = counter
        counter += 1

    # 1) STRIP IT since its very dirty data
        for key, val in listing.items():
            if type(val) == str:
                listing[key] = listing[key].strip()


     # negotiable variable handling
        if "do negocjacji" in listing["rent"]:
            listing["negotiable"] = True
        else:
            listing["negotiable"] = False


    # rent variable handling & cleaning
        listing["rent"] = int(listing["rent"].rstrip("do negocjacji").strip().rstrip("zł").strip().replace(" ", ""))


    # level variable handling & cleaning
        if "Poziom" not in listing:
            listing["Poziom"] = None
        listing["level"] = listing.pop("Poziom")
        if "level" not in listing:
            listing["level"] = None
        elif listing["level"] == "Poddasze":
            listing["level"] = None
        elif listing["level"] is None:
            listing["level"] = None
        elif listing["level"] == "Parter":
            listing["level"] = "0"
        elif listing["level"] == "Powyżej 10":
            listing["level"] = "11"
        try:
            if listing["level"] is None:
                listing["level"] = None
            else:
                listing["level"] = int(listing["level"])
        except:
            print(listing["level"])
            input("Unrecognized level: ")

        # publish_date variable handling & cleaning
        listing["publish_date"] = listing.pop("publish-date")
        try:
            day, month, year = listing["publish_date"].split(" ")
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
        listing["publish_date"] = f"{year:02}-{month:02}-{day:02}"

    # furnished variable handling
        listing["furnished"] = listing.pop("Umeblowane")
        if listing["furnished"] == "Tak":
            listing["furnished"] = True
        elif listing["furnished"] == "Nie":
            listing["furnished"] = False
            # manual error handling for furnished variable
        else:
            print(listing["furnished"])
            input("furnished variable creation problem -> line 109")


    # rent_extra variable handling & cleaning
        listing["rent_extra"] = listing.pop("Czynsz (dodatkowo)")
        listing["rent_extra"] = int(
            round(float(listing["rent_extra"].split("zł")[0].strip().replace(" ", "").replace(",", "."))))


    # rent_full variable handling & cleaning
        listing["rent_full"] = listing["rent_extra"] + listing["rent"]


    # surface variable handling & clearing
        listing["surface"] = listing.pop("Powierzchnia")
        listing["surface"] = int(round(float(listing["surface"].split(" ")[0].replace(",", "."))))


    # rooms variable handling & clearing
        listing["rooms"] = listing.pop("Liczba pokoi")
        if listing["rooms"] == "Kawalerka":
            listing["rooms"] = "1"
        listing["rooms"] = int(listing["rooms"].split(" ")[0])


    # building_type handling & cleaning
        listing["building_type"] = listing.pop("Rodzaj zabudowy")
        building_type_dictionary = {
            "Pozostałe": 0,
            "Dom wolnostojący": 1,
            "Kamienica": 2,
            "Szeregowiec": 3,
            "Blok": 4,
            "Apartamentowiec": 5,
            "Loft": 6,
            "Suterena": 7}
        listing["building_type"] = building_type_dictionary[listing["building_type"]]
        # Check if building type is valid
        if listing["building_type"] is str:
            print(listing["building_type"])
            input("Unrecognized building type: ")

    # private_seller handling & cleaning
        if "Prywatne" in listing.keys():
            listing["private_seller"] = listing.pop("Prywatne")
        if "Firmowe" in listing:
            listing["private_seller"] = False
            del listing["Firmowe"]
        if listing["private_seller"] == "Tak":
            listing["private_seller"] = True
        else:
            listing["private_seller"] = None




if __name__ == '__main__':
    main()