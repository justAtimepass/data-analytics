import pandas as pd


students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Aarav", "Priya", "Rahul", "Sneha", "Aman"],
    "Department": ["IT", "CS", "IT", "CS", "IT"]
})

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Marks": [85, 92, 78, 95, 88],
    "Attendance": [90, 95, 80, 92, 85]
})

print("Students DataFrame:")
print(students)

print("\nMarks DataFrame:")
print(marks)



merged_df = pd.merge(students, marks, on="Student_ID")

print("\n--- Merged DataFrame ---")
print(merged_df)



students_part1 = pd.DataFrame({
    "Student_ID": [101, 102, 103],
    "Name": ["Aarav", "Priya", "Rahul"],
    "Marks": [85, 92, 78]
})

students_part2 = pd.DataFrame({
    "Student_ID": [104, 105, 106],
    "Name": ["Sneha", "Aman", "Riya"],
    "Marks": [95, 88, 82]
})

concatenated_df = pd.concat(
    [students_part1, students_part2],
    ignore_index=True
)

print("\n--- Concatenated DataFrame ---")
print(concatenated_df)



grouped = merged_df.groupby("Department")

print("\n--- GroupBy: Mean Marks by Department ---")
print(grouped["Marks"].mean())



aggregation = merged_df.groupby("Department")["Marks"].agg(
    ["sum", "mean", "count", "min", "max"]
)

print("\n--- Aggregate Values by Department ---")
print(aggregation)



pivot = pd.pivot_table(
    merged_df,
    values="Marks",
    index="Department",
    columns="Name",
    aggfunc="mean"
)

print("\n--- Pivot Table ---")
print(pivot)