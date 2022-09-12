"""
"building-type": ["Blok", "Kamienica", "Dom wolnostojący", "Apartamentowiec"]
"furnished": true, false
"level": 0-10, if 11 is more than 10, null if no info.
"link": some link,
"listing_no": number of listing,
"negotiable": true, false
"private": true, false
"publish-date": "YYYY-MM-DD",
"rent": standard price,
"rent-extra": shared rent,
"rent-full": full-rent,
"rooms": 1-3, if 4 is 4 or more.
"surface": square meters
"title": "Title of listing"
"""

"MORE IN "
"/Users/mateusz/Documents/Code/Final Project/project/"
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