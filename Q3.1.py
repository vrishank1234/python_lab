# Given list
original_list = [1, 2, 3]

# i. By using + operator
extended_list_operator = original_list + [4, 5, 6]

# ii. By using append()
extended_list_append = original_list.copy()  # Create a copy to avoid modifying the original list
extended_list_append.append(4)
extended_list_append.append(5)
extended_list_append.append(6)

# iii. By using extend()
extended_list_extend = original_list.copy()  # Create a copy to avoid modifying the original list
extended_list_extend.extend([4, 5, 6])

# Print the results
print("Original List:", original_list)
print("i. Extended List using + operator:", extended_list_operator)
print("ii. Extended List using append():", extended_list_append)
print("iii. Extended List using extend():", extended_list_extend)
