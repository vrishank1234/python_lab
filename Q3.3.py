# Get user input for the list
user_input = input("Enter elements separated by spaces: ")
user_list = [int(element) for element in user_input.split()]

# Create a new list with distinct elements
distinct_elements_list = []
for element in user_list:
    if element not in distinct_elements_list:
        distinct_elements_list.append(element)

# Print the result
print("Original List:", user_list)
print("List with Distinct Elements:", distinct_elements_list)
