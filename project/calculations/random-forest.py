import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


with open("/Users/mateusz/Documents/Code/Final-Project/project/calculations/sample_cleared_results.json", "r") as f:
    result = json.load(f)


df = pd.DataFrame(result)
print(df.isnull().sum().sum())
df.dropna(inplace=True)
print(df.isnull().sum().sum())
plt.hist(df["rent"])
plt.xlabel("rent")
plt.ylabel("rent_full")
plt.show()
X = df[["rooms", "building_type", "collection_set", "level"]]
# X = df.iloc[:, :-1]
y = df.rent
# y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(y_pred)
res = pd.DataFrame([y_pred, y_test])