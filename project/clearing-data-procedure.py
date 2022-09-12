"""
Creation of data:

"building-type": ["Blok", "Kamienica", "Dom wolnostojący", "Apartamentowiec"]
"furnished": true, false
"level": 0-10, if 11 level is higher than 10, None if no info.
"link": listing link,
"listing_no": number of listing,
"negotiable": true, false
"private": true, false
"publish-date": "YYYY-MM-DD",
"rent": standard price,
"rent-extra": shared rent,
"rent-full": full-rent,
"rooms": 1-3, 4 if is 4 or more.
"surface": square meters
"title": "Title of listing"
"""

"""
Procedure of cleaning: All in
1. STRIP IT
1. "rent", "negotiable"
2. Listing clear/ keys / negotiable/ private
3. level, rent-full, private, rent-extra
4. furnished, surface, rooms
5. counter, repetition
6. Publish date
"""

#DETAILED

# # 1. STRIP IT
# for listing in result:
#     for key,v in listing.items():
#         if type(v) == str:
#             listing[key] = listing[key].strip()

# # 2. "rent", "negotiable"
# for listing in result:
#     if "do negocjacji" in listing["rent"]:
#         listing["negotiable"] = True
#     else:
#         listing["negotiable"] = False
#     listing["rent"] = listing["rent"].rstrip("do negocjacji").strip()
#     listing["rent"] = listing["rent"].rstrip("zł").strip()
#     listing["rent"] = listing["rent"].replace(" ","")
#     listing["rent"] = int(listing["rent"])
#     print(listing["rent"])

# # 3. Listing clear/ keys / negotiable/ private
# for listing in result:
#     if "Poziom" not in listing:
#         listing["Poziom"] = None
#     listing["level"] = listing.pop("Poziom")
#     listing["furnished"] = listing.pop("Umeblowane")
#     listing["rent-extra"] = listing.pop("Czynsz (dodatkowo)")
#     listing["surface"] = listing.pop("Powierzchnia")
#     listing["rooms"] = listing.pop("Liczba pokoi")
#     listing["building-type"] = listing.pop("Rodzaj zabudowy")
#     if "Prywatne" not in listing:
#         listing["Prywatne"] = False
#     listing["private"] = listing.pop("Prywatne")
#     if "Firmowe" in listing:
#         del listing["Firmowe"]

# # 4. level, rent-full, private, rent-extra
# for listing in result:
#     listing["rent-extra"] = listing["rent-extra"].split("zł")[0].strip().replace(" ","").replace(",",".")
#     listing["rent-extra"] = int(round(float(listing["rent-extra"])))
#     listing["rent-full"] = listing["rent-extra"] + listing["rent"]
#     if listing["private"] == "Tak":
#         listing["private"] = True
#     else:
#         listing["private"] = False
#     if "level" not in listing:
#         listing["level"] = None
#     elif listing["level"] == "Parter":
#         listing["level"] = "0"
#     elif listing["level"] == "Powyżej 10":
#         listing["level"] = "11"
#     try:
#         listing["level"] = int(listing["level"])
#     except:
#         print(listing["level"])

# # 5. furnished, surface, rooms
# for listing in result:
#     if listing["furnished"] == "Tak":
#         listing["furnished"] = True
#     if listing["rooms"] == "Kawalerka":
#         listing["rooms"] = "1"
#     listing["rooms"] = listing["rooms"].split(" ")[0]
#     listing["rooms"] = int(listing["rooms"])
#     listing["surface"] = listing["surface"].split(" ")[0].replace(",",".")
#     listing["surface"] = int(round(float(listing["surface"])))
#     print(listing["surface"])

# # 6. counter, repetition
# counter = 0
# links = []
#
# for listing in result:
#     if listing["link"] in links:
#         del listing
#         continue
#     links.append(listing["link"])
#     counter += 1
#     listing["listing_no"] = counter
#     print(listing["listing_no"])

# # 7. Publish date
# for listing in result:
#     try:
#         day, month, year = listing["publish-date"].split(" ")
#         day = int(day)
#         year = int(year)
#         if month == "sierpnia":
#             month = 8
#         elif month == "września":
#             month = 9
#     except ValueError:
#         day = 11
#         month = 9
#         year = 2022
#     listing["publish-date"] = f"{year:02}-{month:02}-{day:02}"