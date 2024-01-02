# Input: Get the range from the user
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Create a dictionary of cubes for odd numbers in the range
cube_dict = {num: num ** 3 for num in range(start_range, end_range + 1) if num % 2 != 0}

# Print the dictionary
print("Dictionary of cubes for odd numbers:", cube_dict)
