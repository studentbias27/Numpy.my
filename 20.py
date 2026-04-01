"""project"""

import pandas as pd
import numpy as numpy

#loading the dataset
df = pd.read_csv("/home/ayush-bora/Pandas/data.CSv")
print(df.head())
print("missing data",df.isnull().sum())
df["age"] = df["age"].fillna(df["age"].mean())
print(df)
df["income"] = df["income"].fillna(df["income"].mean())
print(df)