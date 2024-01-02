# Input: Get an email address from the user
email_address = input("Enter an email address: ")

# Split the email address into username and domain
username, domain = email_address.split('@', 1)

# Form a tuple of username and domain
email_tuple = (username, domain)

# Print the tuple
print("Tuple of username and domain:", email_tuple)


