import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(marks)

data = {
    "Name": ["Aarav", "Priya", "Rahul", "Sneha", "Aman"],
    "Age": [20, 21, 19, 20, 22],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

print("\nColumn Names:")
print(df.columns)

print("\nIndex:")
print(df.index)

df["Grade"] = ["B", "A", "C", "A", "B"]

print("\nUpdated DataFrame:")
print(df)