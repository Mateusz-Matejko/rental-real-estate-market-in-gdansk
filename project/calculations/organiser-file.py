import json
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
            all_results.append(listing)


# # 0. Delete duplicates
# while True:
#     links = []
#     before = len(result)
#     print(before)
#     for listing in result:
#         if listing["link"] in links:
#             result.remove(listing)
#         else:
#             links.append(listing["link"])
#     after = len(result)
#     print(after)
#     if before == after:
#         break


counter = 0
for listing in all_results:
    counter += 1
    listing["listing_no"] = counter

# ALL DATA OPERATION SAVE
with open("all-data-unfiltered.json", "w") as file:
    # input("You remembered to set same file to read from and write to? ")
    json.dump(result, file, indent=2, sort_keys=True)















