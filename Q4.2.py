def get_user_details(*args, **kwargs):
    # Extract values from *args and **kwargs
    name = args[0] if args and len(args) >= 1 else kwargs.get('name', None)
    email = args[1] if args and len(args) >= 2 else kwargs.get('email', None)
    age = args[2] if args and len(args) >= 3 else kwargs.get('age', None)

    return name, email, age

# Get user input for details
user_name = input("Enter your name: ")
user_email = input("Enter your email: ")
user_age = int(input("Enter your age: "))

# Call the function with user input using positional and keyword arguments
name_arg, email_arg, age_arg = get_user_details(user_name, user_email, user_age)
name_kwarg, email_kwarg, age_kwarg = get_user_details(name=user_name, email=user_email, age=user_age)

# Print the results
print("\nUsing *args:")
print(f"Name: {name_arg}, Email: {email_arg}, Age: {age_arg}")

print("\nUsing **kwargs:")
print(f"Name: {name_kwarg}, Email: {email_kwarg}, Age: {age_kwarg}")
