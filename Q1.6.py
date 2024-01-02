# Input: Get a number from the user
num = int(input("Enter a number: "))

# Convert the number to a string to find the number of digits
num_str = str(num)

# Calculate the number of digits in the number
num_digits = len(num_str)

# Calculate the sum of the digits, each raised to the power of the number of digits
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

# Check if the number is an Armstrong number
if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
