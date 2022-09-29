import json
import pprint

"""
Important notes: 
unfiltered file - has repetitions of listing, although it has the number of set it was collected in
filtered file - is just the all amount of unique listings,
it is because the listing collected in set on 3september may also be available on set collected in sep 19th, 
because the listing life on olx site is limited to 30days. 

IF CREATING FILTERED - REMEMBER TO REMOVE collection_set key 
IF CREATING UNFILTERED - BE SURE collection_set is in it

REMEMBER TO READ AND WRITE TO SAME FILE 
"""


# ALL DATA CREATION
list_of_file = ["sep3.json", "sep11.json", "sep19.json", "sep26.json"]
direction_file = "all-data-unfiltered.json.json"


all_results = []


for file in list_of_file:
    with open(file, "r") as f:
        result = json.load(f)
        for listing in result:
            listing["collection_date"] = listing.pop("collection_set")
            if file == "sep3.json":
                listing["collection_date"] = "2022-09-03"
            elif file == "sep11.json":
                listing["collection_date"] = "2022-09-11"
            elif file == "sep19.json":
                listing["collection_date"] = "2022-09-19"
            elif file == "sep26.json":
                listing["collection_date"] = "2022-09-26"
            all_results.append(listing)

counter = 0
for listing in all_results:
    counter += 1
    listing["listing_no"] = counter


with open("all-data-unfiltered.json", "w") as file:
# input("You remembered to set same file to read from and write to? ")
    json.dump(all_results, file, indent=2, sort_keys=True)















