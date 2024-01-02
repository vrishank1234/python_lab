# File: main_script.py

# Import the bank_module module
from bank_module import BankAccount

# Function to perform banking operations
def perform_banking_operations(account):
    print("\nBank Operations Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Current Balance: ${account.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(account.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == '4':
            print("Exiting Bank Operations. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Example usage:

# Create a BankAccount object
account_number = input("Enter your account number: ")
user_account = BankAccount(account_number)

# Perform banking operations
perform_banking_operations(user_account)
