import json
import pprint
import pandas as pd


def main():
    all_results = get_results()
    for listing in all_results:
        for k, v in listing.items():
            # clear the nan
            if type(v) == float:
                listing[k] = None
    write_results_write(destination_file="average-results.json", results=all_results)


def get_results():
    list_of_base_files = ["sep3.json", "sep11.json", "sep19.json", "sep26.json", "oct3.json", "all-data-filtered.json"]
    all_results = []
    for file in list_of_base_files:
        result_partial = {}
        result = get_result(file)
        df = pd.DataFrame(result)
        result_partial = price_per_square_meter(brave="rent_full", divisor="surface", df=df,
                                                partial_result=result_partial)
        result_partial = price_per_square_meter(brave="rent_full", divisor="surface", df=df,
                                                partial_result=result_partial, buildings=True)
        result_partial = average_by_rooms(key_to_return="surface", df=df, result=result_partial)
        result_partial = average_by_rooms(key_to_return="rent_full", df=df, result=result_partial)
        result_partial = average_by_rooms(key_to_return="rent_extra", df=df, result=result_partial)
        result_partial = average_by_rooms(key_to_return="rent", df=df, result=result_partial)
        for i in range(7):
            result_partial = average_by_rooms_and_condition(key_to_return="rent_full", df=df,
                                                            condition_key="building_type", condition_v=i,
                                                            result=result_partial)
        for i in range(12):
            result_partial = average_by_rooms_and_condition(key_to_return="rent_full", df=df, condition_key="level",
                                                            condition_v=i, result=result_partial)
        if file == "sep3.json":
            result_partial.update({"collection_date": "2022-09-03"})
        elif file == "sep11.json":
            result_partial.update({"collection_date": "2022-09-11"})
        elif file == "sep19.json":
            result_partial.update({"collection_date": "2022-09-19"})
        elif file == "sep26.json":
            result_partial.update({"collection_date": "2022-09-26"})
        elif file == "oct3.json":
            result_partial.update({"collection_date": "2022-10-03"})
        elif file == "all-data-filtered.json":
            result_partial.update({"collection_date": "all_data_average"})
        all_results.append(result_partial)
    return all_results


def price_per_square_meter(brave, divisor, df, partial_result, buildings=False,):
    for i in range(1, 5):
        if buildings:
            for b in range(6):
                outcome = df[(df.rooms == i) & (df.building_type == b)]
                df_price = outcome[brave].mean()
                df_surface = outcome[divisor].mean()
                result = df_price / df_surface
                partial_result[f"average_price_per_square_meter_in_{i}_rooms_and_building_type_=_{b}"] = round(result, 2)
        else:
            outcome = df[df.rooms == i]
            df_price = outcome[brave].mean()
            df_surface = outcome[divisor].mean()
            result = df_price/df_surface
            partial_result[f"average_price_per_square_meter_in_{i}_rooms"] = round(result, 2)
    return partial_result


def average_by_rooms(key_to_return, df, result):
    for i in range(1, 5):
        outcome = df[df.rooms == i]
        outcome = outcome[key_to_return].mean()
        result[f"average_{key_to_return}_per_{i}_rooms"] = round(outcome, 2)
    return result


def average_by_rooms_and_condition(key_to_return, df, condition_key, condition_v, result):
    for i in range(1, 5):
        outcome = df[(df.rooms == i) & (df[condition_key] == condition_v)]
        outcome = outcome[key_to_return].mean()
        result[f"average_{key_to_return}_per_{i}_rooms_if_{condition_key}_=_{condition_v}"] = round(outcome, 2)
    return result


def get_result(file):
    with open(file, "r") as file:
        result = json.load(file)
    return result


def write_results_append(destination_file, results):
    with open(destination_file, "a") as f:
        json.dump(results, f, indent=2)


def write_results_write(destination_file, results):
    with open(destination_file, "w") as f:
        json.dump(results, f, indent=2)


if __name__ == '__main__':
    main()