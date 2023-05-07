import json
import pprint

all_data_paths_by_dict = [
    {"month": "sep", "day":"3",   "month_int": 9, "collection_set": 1},
    {"month": "sep", "day": "11", "month_int": 9,"collection_set": 2},
    {"month": "sep", "day": "19", "month_int": 9,"collection_set": 3},
    {"month": "sep", "day": "26", "month_int": 9,"collection_set": 4},
    {"month": "oct", "day": "3",  "month_int": 10,"collection_set": 5},
    {"month": "oct", "day": "11", "month_int": 10,"collection_set": 6},
    {"month": "oct", "day": "20", "month_int": 10,"collection_set": 7},
    {"month": "oct", "day": "27", "month_int": 10,"collection_set": 8},
    {"month": "nov", "day": "3",  "month_int": 9,"collection_set": 9},
]


def main():

    # created universal path to cover all data clearing with loop
    for key in all_data_paths_by_dict:

        # get month and day from dict to use it in path
        month_str = key["month"]
        day_str = key["day"]

        # create raw data filepath witch schema
        filepath_raw_input = f"time-series-and-original-data/collected-{month_str}-{day_str}/original-data/" \
                             f"original-data-{month_str}{day_str}.json"

        # create cleaned data filepath with schema
        filepath_cleaned_output = f"time-series-and-original-data/collected-{month_str}-{day_str}/cleared-data/" \
                                  f"cleared-data-{month_str}-{day_str}.json"

        # get data to future cleaning
        day_of_collecting = int(day_str)
        month_of_collecting = key["month_int"]
        year_of_collecting = 2022
        collection_set = key["collection_set"]

        # read raw data
        result = read_raw_data(filepath=filepath_raw_input)

        # delete duplicate values
        result = step_0_delete_duplicates(result)

        counter = 0
        for listing in result:
            # handle clearing of:
                # listing_no, collection_set,
            counter += 1
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


def read_raw_data(filepath):
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
    pprint.pprint(listing)
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
    elif listing["level"] == "Suterena":
        listing["level"] = "0"
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
    try:
        listing["building_type"] = building_type_dictionary[listing["building_type"]]
# Check if building type is valid
    except:
        if listing["building_type"] not in building_type_dictionary:
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