# File: bank_module.py

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Amount ${amount} deposited successfully. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Amount ${amount} withdrawn successfully. New balance: ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal unsuccessful."
