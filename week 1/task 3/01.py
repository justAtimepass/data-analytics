num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
else:
    division = "Cannot divide by zero"
    modulus = "Cannot calculate modulus by zero"