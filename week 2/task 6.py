import pandas as pd

data = {
    "Name": ["Aarav", "Priya", "Rahul", "Sneha", "Aman", "Riya"],
    "Age": [20, 21, 19, 20, 22, 19],
    "Marks": [85, 92, 68, 95, 78, 88],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSelected Columns (Name and Marks):")
print(df[["Name", "Marks"]])

print("\nSelected Rows (first 3 rows):")
print(df.iloc[0:3])

print("\nStudents with Marks greater than 80:")
print(df[df["Marks"] > 80])

print("\nStudents with Marks greater than 80 and Age less than 21:")
print(df[(df["Marks"] > 80) & (df["Age"] < 21)])

print("\nStudents sorted by Marks (Ascending):")
print(df.sort_values(by="Marks", ascending=True))

print("\nStudents sorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))