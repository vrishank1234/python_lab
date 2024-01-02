# File: main_script.py

# Import the my_module module
import my_module

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Use the add_numbers function from my_module
result = my_module.add_numbers(num1, num2)

# Display the result
print(f"The sum of {num1} and {num2} is: {result}")
