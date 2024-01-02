# using reverse
# Define a list
my_list = [1, 2, 3, 4, 5]

# Method 1: Using reverse method
reversed_list = list(my_list)  # Create a copy to avoid modifying the original list
reversed_list.reverse()

# Print the reversed list
print("Reversed list using reverse method:", reversed_list)


#using slicing
# Define a list
my_list = [1, 2, 3, 4, 5]

# Method 2: Using slicing
reversed_list_slicing = my_list[::-1]

# Print the reversed list using slicing
print("Reversed list using slicing:", reversed_list_slicing)
