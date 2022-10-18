import json
import pandas as pd
import matplotlib.pyplot as plt

files = ["all-data-filtered.json", "all-data-unfiltered"]


def main():
    result = get_result("all-data-filtered.json")
    df = pd.DataFrame(result)
    index_list = []
    for room in range(1, 5):
        df_raw = pd.DataFrame(result)
        print()
        print(f"Rooms: {room}")
        df_raw = df_raw[df_raw.rooms == room]
        # print(df_raw.describe())
        plot_boxplot(df_raw, "rent_extra")
        # df_raw = df_raw[(df_raw.rent_extra != df_raw.rent)]
        for feature in ["rent", "rent_full", "rent_extra"]:
            index_list.extend(outliers(df_raw, feature))
    index_list = sorted(set(index_list))
    print(index_list)
    print(len(index_list))
    cleared_results = remove_outliers_by_listing_no(index_list)
    cleared_results = clear_listing_no_after_clearing_data(cleared_results)
    new_df = pd.DataFrame(cleared_results)

    print(new_df.rent_extra.max())
    # save_results(cleared_results, path="sample_cleared_results.json")


def get_result(file):
    with open(file, "r") as f:
        return json.load(f)


def plot_boxplot(df, ft):
    df.boxplot(column=[ft])
    plt.grid(False)
    # plt.show()


def outliers(df, ft):
    Q1 = df[ft].quantile(0.15)
    Q3 = df[ft].quantile(0.65)
    IQR = Q3 - Q1

    # cet the lower and upper bound
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    ls = df.listing_no[(df[ft] < lower_bound) | (df[ft] > upper_bound)]
    return ls


def remove_outliers(df, ls):
    df = df.drop(ls)
    return df


def remove_outliers_by_listing_no(ls):
    cleared_results = get_result("all-data-filtered.json")
    for i in range(len(cleared_results)):
        for number in ls:
            if cleared_results[i]["listing_no"] == number:
                print(len(cleared_results))
                del cleared_results[i]
                continue
    return cleared_results


def clear_listing_no_after_clearing_data(results):
    counter = 1
    for listing in results:
        listing["listing_no"] = counter
        counter += 1
    return results




def save_results(results, path):
    with open(path, "w") as f:
        json.dump(results, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()