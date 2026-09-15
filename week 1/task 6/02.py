def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print("\nEnter three numbers to calculate their average:")
user_avg_num1 = float(input("Enter the first number: "))
user_avg_num2 = float(input("Enter the second number: "))
user_avg_num3 = float(input("Enter the third number: "))

average_result = calculate_average(user_avg_num1, user_avg_num2, user_avg_num3)
print(f"The average of {user_avg_num1}, {user_avg_num2}, and {user_avg_num3} is: {average_result}")