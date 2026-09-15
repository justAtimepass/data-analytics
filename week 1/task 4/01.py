
marks = float(input("Enter the marks: "))

if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
else:
    grade = 'Fail'

print(f"The grade for {marks} marks is: {grade}")