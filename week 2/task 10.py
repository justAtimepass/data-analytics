
import numpy as np
import pandas as pd


data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Aarav", "Priya", "Rahul", "Sneha", "Aman", "Riya", "Karan", "Neha"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Department": ["IT", "CS", "IT", "CS", "IT", "CS", "IT", "CS"],
    "Age": [20, 21, np.nan, 20, 22, 19, 21, np.nan],
    "Marks": [85, 92, 68, 95, np.nan, 88, 78, 90],
    "Attendance": [90, 95, 80, 92, 85, np.nan, 88, 94]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)



print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())



print("\nMissing Values in Each Column:")
print(df.isnull().sum())



df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nDataset After Handling Missing Values:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())



print("\nSelected Columns - Name, Department and Marks:")
print(df[["Name", "Department", "Marks"]])



print("\nStudents Scoring 85 or More:")
print(df[df["Marks"] >= 85])

print("\nIT Students with Marks 80 or More:")
print(df[(df["Department"] == "IT") & (df["Marks"] >= 80)])



print("\nStudents Sorted by Marks - Highest to Lowest:")
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)



group_analysis = df.groupby("Department").agg(
    Average_Marks=("Marks", "mean"),
    Maximum_Marks=("Marks", "max"),
    Minimum_Marks=("Marks", "min"),
    Average_Attendance=("Attendance", "mean"),
    Student_Count=("Student_ID", "count")
)

print("\nGroupBy Analysis by Department:")
print(group_analysis)



pivot_table = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print("\nPivot Table - Average Marks by Department and Gender:")
print(pivot_table)



average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

top_student = df.loc[df["Marks"].idxmax(), "Name"]

department_average = df.groupby("Department")["Marks"].mean()
highest_department = department_average.idxmax()

print("\n========== USEFUL INSIGHTS ==========")

print("Overall Average Marks:", round(average_marks, 2))
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Top Performing Student:", top_student)
print("Department with Highest Average Marks:", highest_department)

print("======================================")



output_file = "processed_student_performance.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset exported successfully!")
print("File Name:", output_file)



verified_df = pd.read_csv(output_file)

print("\nVerified Exported Dataset:")
print(verified_df)

print("\nRows:", verified_df.shape[0])
print("Columns:", verified_df.shape[1])

print("\nMissing Values in Exported Dataset:")
print(verified_df.isnull().sum())

print("\nCSV file is ready for submission.")