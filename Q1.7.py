# Input: Get a number from the user
num = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Print the factorial of the number
print(f"The factorial of {num} is: {factorial}")
