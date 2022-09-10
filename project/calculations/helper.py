@average_decorator
def get_average_specific(data, return_key, condition_k, condition_v):
    list_of_results = []
    for listing in data:
        print(listing)
        if listing[condition_k] == condition_v:
            list_of_results.append(listing[return_key])
    # [list_of_results.append(listing[return_key]) for listing in data if listing[condition_k] == condition_v]
    return list_of_results, return_key