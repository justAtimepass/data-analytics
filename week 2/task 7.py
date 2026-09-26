import pandas as pd
import numpy as np

data = {
    "Name": ["Aarav", "Priya", "Rahul", "Sneha", "Aman", "Riya"],
    "Age": [20, 21, np.nan, 20, 22, np.nan],
    "Marks": [85, np.nan, 68, 95, np.nan, 88],
    "City": ["Delhi", "Mumbai", "Delhi", np.nan, "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

print("Dataset Before Handling Missing Values:")
print(df)

print("\nMissing Values (True/False):")
print(df.isnull())

print("\nMissing Values using isna():")
print(df.isna())

print("\nCount of Missing Values in Each Column:")
print(df.isnull().sum())

df_removed = df.dropna()

print("\nDataset After Removing Rows with Missing Values:")
print(df_removed)

df_filled = df.copy()

df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())

df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())

df_filled["City"] = df_filled["City"].fillna(df_filled["City"].mode()[0])

print("\nDataset After Filling Missing Values:")
print(df_filled)