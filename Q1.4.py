n = int(input("Enter the value of n: "))

# Calculate the sum of the first n natural numbers
sum_of_numbers = n * (n + 1) // 2

# Print the first n natural numbers
print("First", n, "natural numbers:", list(range(1, n + 1)))

print("Sum of the first", n, "natural numbers:", sum_of_numbers)
