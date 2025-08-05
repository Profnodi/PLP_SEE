# Simple calculator program

# Get user input
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter an operation (+, -, *, /): ")

# Convert numbers to float (to handle decimals as well)
num1 = float(num1)
num2 = float(num2)

# Perform the selected operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
