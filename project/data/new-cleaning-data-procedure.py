import json

original_file_paths = [

#september
    "time-series-and-original-data/collected-september-3rd/original-data/original-data-sep3.json",
    "time-series-and-original-data/collected-september-11th/original-data/original-data-sep11.json",
    "time-series-and-original-data/collected-september-19th/original-data/original-data-sep19.json",
    "time-series-and-original-data/collected-september-26th/original-data/original-data-sep26.json",

#october
    "time-series-and-original-data/collected-october-3rd/original-data/original-data-oct3.json",
    "time-series-and-original-data/collected-october-11th/original-data/original-data-oct11.json",
    "time-series-and-original-data/collected-october-20th/original-data/original-data-oct20.json",
    "time-series-and-original-data/collected-october-27th/original-data/original-data-oct27.json",

#november
    "time-series-and-original-data/collected-november-3rd/original-data/original-data-nov3.json",
]

destination_file_paths = [

#september
    "time-series-and-original-data/collected-september-3rd/cleared-data/cleared-data-sep3.json",
    "time-series-and-original-data/collected-september-11th/cleared-data/cleared-data-sep11.json",
    "time-series-and-original-data/collected-september-19th/cleared-data/cleared-data-sep19.json",
    "time-series-and-original-data/collected-september-26th/cleared-data/cleared-data-sep26.json",

#october
    "time-series-and-original-data/collected-october-3rd/cleared-data/cleared-data-oct3.json",
    "time-series-and-original-data/collected-october-11th/cleared-data/cleared-data-oct11.json",
    "time-series-and-original-data/collected-october-20th/cleared-data/cleared-data-oct20.json",
    "time-series-and-original-data/collected-october-27th/cleared-data/cleared-data-oct27.json",

#november
    "time-series-and-original-data/collected-november-3rd/cleared-data/cleared-data-nov3.json",
]

def main():
        filepath_raw_input = "original-data-oct20.json"
        filepath_cleaned_output = "xxxxxxx.json"
        day_of_collecting = 1111
        month_of_collecting = 22222
        year_of_collecting = 33333
        collection_set = 444444

        # read cleaned data
        print(filepath_raw_input)
        result = read_write_data(filepath=filepath_raw_input)

        # delete duplicate values
        result = step_0_delete_duplicates(result)

        counter = 1
        for listing in result:
            # handle clearing of:
                # listing_no, collection_set,
            step_1_strip_data_and_handle_listing_no_collection_set(listing=listing,
                                                                   counter = counter,
                                                                   collection_set = collection_set)
            # negotiable, furnished, publish_date
            step_2_handle_negotiable_furnished_publish_date(listing=listing,
                                                             day_of_collecting = day_of_collecting,
                                                             month_of_collecting = month_of_collecting,
                                                             year_of_collecting = year_of_collecting)
            # rent, rent_extra, rent_full, surface, rooms
            step_3_handle_rent_rent_extra_rent_full_surface_rooms(listing=listing)

            # building_type, private_seller
            step_4_handle_building_type_private_seller(listing=listing)

        # write cleaned data to its destination
        step_5_write_cleared_file(file_path=filepath_cleaned_output, result=result)


def read_write_data(filepath):
    # get the raw data to perform data cleaning
    with open(file= filepath, mode="r") as file:
        result = json.load(file)
    return result

def step_0_delete_duplicates(result):
    # Step 0 - delete duplicates
    links = set()
    new_result = []
    for listing in result:
        if listing["link"] not in links:
            new_result.append(listing)
            links.add(listing["link"])
    return new_result

def step_1_strip_data_and_handle_listing_no_collection_set(listing, counter, collection_set):

# listing_no variable handling
    listing["listing_no"] = counter
    counter += 1

# collection_set variable handling
    listing["collection_set"] = collection_set

    # additional STRIP cuz the data was really unstructured
    for key, val in listing.items():
        if type(val) == str:
            listing[key] = listing[key].strip()

def step_2_handle_negotiable_furnished_publish_date(listing,
                                                     day_of_collecting,
                                                     month_of_collecting,
                                                     year_of_collecting):

# negotiable variable handling
    if "do negocjacji" in listing["rent"]:
        listing["negotiable"] = True
    else:
        listing["negotiable"] = False

# furnished variable handling
    listing["furnished"] = listing.pop("Umeblowane")
    if listing["furnished"] == "Tak":
        listing["furnished"] = True
    elif listing["furnished"] == "Nie":
        listing["furnished"] = False
# manual error handling for furnished variable
    else:
        print(listing["furnished"])
        input("furnished variable creation problem -> line 89")


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

def step_3_handle_rent_rent_extra_rent_full_surface_rooms(listing):

# rent variable handling & cleaning
    listing["rent"] = int(listing["rent"].rstrip("do negocjacji").strip().rstrip("zł").strip().replace(" ", ""))

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

def step_4_handle_building_type_private_seller(listing):

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

def step_5_write_cleared_file(file_path, result):
    try:
        with open(file=file_path, mode="w") as file:
            json.dump(result, file, indent=2, sort_keys=True)
        print("Success")
    except:
        print("Failed")

if __name__ == '__main__':
    main()