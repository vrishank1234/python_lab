def count_upper_lower_letters(input_string):
    # Initialize counters
    upper_count = 0
    lower_count = 0

    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is an uppercase letter
        if char.isupper():
            upper_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
string_test = 'Today is My Best Day'
upper, lower = count_upper_lower_letters(string_test)

print("Original String:", string_test)
print("Number of Upper-case Letters:", upper)
print("Number of Lower-case Letters:", lower)

