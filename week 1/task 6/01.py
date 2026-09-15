def calculate_square(number):
    return number ** 2

user_num_square = float(input("\nEnter a number to calculate its square: "))
square_result = calculate_square(user_num_square)
print(f"The square of {user_num_square} is: {square_result}")