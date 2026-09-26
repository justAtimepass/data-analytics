import pandas as pd


output_file = "processed_student_performance.csv"

df.to_csv(output_file, index=False)

print("DataFrame exported successfully!")
print("File name:", output_file)

verified_df = pd.read_csv(output_file)

print("\nVerified Exported Data:")
print(verified_df)

print("\nNumber of rows:", verified_df.shape[0])
print("Number of columns:", verified_df.shape[1])

print("\nMissing Values in Exported File:")
print(verified_df.isnull().sum())

print("\nCSV file is ready for submission.")