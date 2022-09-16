def main():
    result = get_result()
    # stats_square_meter = price_per_square_meter(result)
    # pprint.pprint(stats_square_meter)

    # avg_surface_per_room = universal_stat_specific_range(
    #     result=result, msg_to_avg="average_surface_any_rooms",
    #     msg_avg_spec="average_surface", return_question="surface",
    #     condition_question="rooms", dest_range=5)
    # pprint.pprint(avg_surface_per_room)
    # avg_full_per_room = universal_stat_specific_range(
    #     result=result, msg_to_avg="avg_full_price_any_room",
    #     msg_avg_spec="avg_full_price", return_question="rent-full",
    #     condition_question="rooms", dest_range=5)
    # pprint.pprint(avg_full_per_room)
    # avg_rent_extra_per_room = universal_stat_specific_range(
    #     result=result, msg_to_avg="avg_rent_extra_any_room",
    #     msg_avg_spec="avg_rent_extra", return_question="rent-extra",
    #     condition_question="rooms", dest_range=5)
    # pprint.pprint(avg_rent_extra_per_room)
    # avg_rent_per_room = universal_stat_specific_range(
    #     result=result, msg_to_avg="avg_rent_any_room",
    #     msg_avg_spec="avg_rent", return_question="rent",
    #     condition_question="rooms", dest_range=5)
    # pprint.pprint(avg_rent_per_room)

    # counter = 0
    # for listing in result:
    #     if listing["building-type"] == "Blok":
    #         counter += 1
    #     print(counter)
    # for _ in range(1, 5):
    #     print(get_average_specific_2_keys(
    #         result, "rent-full", "building-type", "Blok", "rooms", _))
    universal_stat_any_range(
        result=result, msg_to_avg="avg_price_per_blok", msg_avg_spec="avg_price_per_blok",
        return_question="rent-full", condition_k1="building-type", condition_v1="Blok",
        condition_k2="rooms",condition_v2=None
    )


def universal_stat_any_range(result, msg_to_avg, msg_avg_spec, return_question,
                             condition_k1, condition_v1, condition_k2, condition_v2):
    stats = {}
    for _ in range(1, 5):
        answear = get_average_specific_2_keys(data=result, return_key=return_question,
                                        condition_k1=condition_k1, condition_v1=condition_v1,
                                        contidion_k2=condition_k2, condition_v2=_)
    stats[f"{msg_avg_spec}_{_}_{condition_k2}"] = round(answear, 2)
    return stats


def universal_stat_specific_range(
        result, msg_to_avg, msg_avg_spec, return_question, condition_question, dest_range=None):
    stats = {}
    pass
    stats[msg_to_avg] = round(get_average(result, return_question), 2)
    for _ in range(1, dest_range):
        answear = get_average_specific(result, return_question, condition_question, _)
        stats[f"{msg_avg_spec}_{_}_{condition_question}"] = round(answear, 2)
    return stats


def price_per_square_meter(result):
    stats = {}
    rent_full_any_room = get_average(result, "rent-full")
    surface_any_room = get_average(result, "surface")
    stats["average_square_meter_price_any_room"] = round(rent_full_any_room/surface_any_room, 2)
    for _ in range(1,5):
        rent = get_average_specific(result, "rent-full", "rooms", _)
        surface = get_average_specific(result, "surface", "rooms", _)
        stats[f"average_square_meter_price_{_}_room"] = round(rent/surface, 2)
    return stats


def average_decorator(base_func):
    def wrapper(*args, **kwargs):
        total_cost = 0
        xlist, what_check = base_func(*args, *kwargs)
        amount_of_result = len(xlist)
        for cost in xlist:
            try:
                total_cost += int(cost)
            except TypeError:
                amount_of_result -= 1
        result = float(total_cost / amount_of_result)
        # print(f"Average {what_check} is {result}")
        return result
    return wrapper


def get_result():
    with open("sep3.json", "r") as file:
        result = json.load(file)
    return result


@average_decorator
def get_average(data, key):
    list_of_results = []
    for listing in data:
        list_of_results.append(listing[key])
    return list_of_results, key

@average_decorator
def get_average_specific(data, return_key, condition_k, condition_v):
    list_of_results = []
    for listing in data:
        if listing[condition_k] == condition_v:
            list_of_results.append(listing[return_key])
    # [list_of_results.append(listing[return_key]) for listing in data if listing[condition_k] == condition_v]
    return list_of_results, return_key

@average_decorator
def get_average_specific_2_keys(
        data, return_key, condition_k1, condition_v1, condition_k2, condition_v2):
    list_of_results = []
    for x in data:
        data = dict(data)
        for listing in data:
            if listing[condition_k1] == condition_v1 and listing[condition_k2] == condition_v2:
                list_of_results.append(listing[return_key])
    return list_of_results, return_key



if __name__ == '__main__':
    main()