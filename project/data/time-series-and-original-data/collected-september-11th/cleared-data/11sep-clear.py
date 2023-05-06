import json

filename = "../../../../calculations/sep11.json"
day_of_collecting = 11
month_of_collecting = 9
yeare_of_collecting = 2022

with open(filename, "r") as file:
    result = json.load(file)


try:
    with open(filename, "w") as file:
        json.dump(result, file, indent=2, sort_keys=True)
    print("Success")
except:
    print("Failed")