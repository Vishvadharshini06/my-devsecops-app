import random

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = random.randint(100000, 999999)
        print(f"Account created for {self.account_holder} with Account Number: {self.account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        print(f"Account Balance: {self.balance}")

    def account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

# Example Usage
account = BankAccount("Alice", 1000)
account.account_info()
account.deposit(500)
account.withdraw(300)
account.get_balance()
account.withdraw(1500)  # Should show insufficient funds
