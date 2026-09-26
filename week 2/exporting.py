import pandas as pd
import numpy as np

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Aarav", "Priya", "Rahul", "Sneha",
             "Aman", "Riya", "Karan", "Neha"],
    "Gender": ["Male", "Female", "Male", "Female",
               "Male", "Female", "Male", "Female"],
    "Department": ["IT", "CS", "IT", "CS",
                   "IT", "CS", "IT", "CS"],
    "Age": [20, 21, np.nan, 20, 22, 19, 21, np.nan],
    "Marks": [85, 92, 68, 95, np.nan, 88, 78, 90],
    "Attendance": [90, 95, 80, 92, 85, np.nan, 88, 94]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nStudents with Marks >= 85:")
print(df[df["Marks"] >= 85])

print("\nData Sorted by Marks:")
print(df.sort_values("Marks", ascending=False))

print("\nGroupBy Analysis:")
print(
    df.groupby("Department")["Marks"]
      .agg(["sum", "mean", "count", "min", "max"])
)

print("\nPivot Table:")
print(
    pd.pivot_table(
        df,
        values="Marks",
        index="Department",
        columns="Gender",
        aggfunc="mean"
    )
)

output_file = "processed_student_performance.csv"
df.to_csv(output_file, index=False)

print("\nData exported successfully to:", output_file)

verified_df = pd.read_csv(output_file)

print("\nVerified Exported Data:")
print(verified_df)

print("\nRows:", verified_df.shape[0])
print("Columns:", verified_df.shape[1])

print("\nMissing Values After Processing:")
print(verified_df.isnull().sum())

print("\nFinal CSV file is ready for submission.")