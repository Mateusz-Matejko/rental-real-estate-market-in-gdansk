import json

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split


def get_result():
    with open("all-data-filtered.json", "r") as f:
        return json.load(f)


df = pd.DataFrame(get_result())
df_x = pd.DataFrame(df.)
print(df_x.describe())

x_train, x_test, y_train, y_test = train_test_split()