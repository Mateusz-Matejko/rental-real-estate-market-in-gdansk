import json
import pprint
import pandas as pd

global result_final
result_final = []


def main():
    result = get_result("sep3.json")
    df = pd.DataFrame(result)
    average_by_rooms(key_to_return="surface", df=df)
    average_by_rooms(key_to_return="rent-full", df=df)
    average_by_rooms(key_to_return="rent-extra", df=df)
    average_by_rooms(key_to_return="rent", df=df)
    for i in range(6):
        average_by_rooms_and_condition(key_to_return="rent-full", df=df, conditionkey="building-type", codnitionv=i)
    for i in range(12):
        average_by_rooms_and_condition(key_to_return="rent-full", df=df, conditionkey="level", codnitionv=i)
    pprint.pprint(result_final)
    print(result_final)


def average_by_rooms(key_to_return, df):
    for i in range(1, 5):
        outcome = df[df.rooms == i]
        outcome = outcome[key_to_return].mean()
        score = {f"average_{key_to_return}_per_{i}_rooms": round(outcome,2)}
        result_final.append(score)


def average_by_rooms_and_condition(key_to_return, df, conditionkey, codnitionv):
    for i in range(1, 5):
        outcome = df[ (df.rooms == i) & (df[conditionkey] == codnitionv)]
        outcome = outcome[key_to_return].mean()
        score = {f"average_{key_to_return}_per_{i}_rooms_if_{conditionkey}_=_{codnitionv}": round(outcome,2)}
        result_final.append(score)


def get_result(file):
    with open(file, "r") as file:
        result = json.load(file)
    return result


if __name__ == '__main__':
    main()