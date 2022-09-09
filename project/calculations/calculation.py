import json


def main():
    result = get_result()
    template(key="level", result=result)

def average_decorator(base_func):
    def wrapper(*args, **kwargs):
        total_cost = 0
        xlist, what_check = base_func(*args, *kwargs)
        amount_of_result = len(xlist)
        for cost in xlist:
            total_cost += cost
        result = float(total_cost / amount_of_result)
        print(f"Average full {what_check} is {result:.2f} PLN")
        return result
    return wrapper


def get_result():
    with open("sep3.json", "r") as file:
        result = json.load(file)
    return result


@average_decorator
def rent(result):
    rent_full_list = []
    for listing in result:
        rent_full_list.append(listing["rent-full"])
    return rent_full_list

@average_decorator
def template(key, result):
    list_of_results = []
    for listing in result:
        print(listing[key])
        list_of_results.append(listing[key])
    return list_of_results, key

if __name__ == '__main__':
    main()