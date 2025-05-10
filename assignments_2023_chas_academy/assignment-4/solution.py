# Your code goes here
from datetime import datetime

def extract_datetime(entry): # Var entry is a parameter
        timestamp_str = entry.split(":")[0] + ":" + entry.split(":")[1] + ":" + entry.split(":")[2]
        return datetime.strptime(timestamp_str.strip(), "%Y-%m-%d %H:%M:%S.%f")

class BankAccount():

    def __init__(self, account_number, account_holder, balance): # Constructor parameters.
        self.account_number = account_number # attribute_1 (self.account_number)
        self.account_holder = account_holder # attribute_2
        self.balance = balance               # attribute_3
        self.transaction_history = [f"{datetime.now()}: +{balance}$"]

    def deposit(self, amount): # method_1: add money to balance.
        self.balance = self.balance + amount
        self.transaction_history.append(f"{datetime.now()}: -{amount}$")
        return "Deposit complete"

    def withdraw(self, amount): # method_2: remove money from balance.
        if self.balance < amount:
            raise ValueError("Not enouch money in your bank account.")
        self.balance = self.balance - amount
        self.transaction_history.append(f"{datetime.now()}: +{amount}$")
        return "Withdraw complete"

    def get_balance(self): # method_3: return the current balance of the account.
        return f"Balance: {self.balance}$"

    def display_account_info(self): # method_4: return account number, account holder's name, and current balance.
        return f"Account number: {self.account_number}, account holder: {self.account_holder}, current balance: {self.balance}$"

    def display_transaction_history(self):
        return f"Transaction history: {self.transaction_history}"

    def merge_account(self, other_account):
        if self.account_holder == other_account.account_holder:
            print("Same account holder, merging the bank accounts.")
            self.balance += other_account.balance

            combined = self.transaction_history + other_account.transaction_history
            combined.sort(key=extract_datetime)
            self.transaction_history = combined
            return "Merging the two bank account has been completed."
        else:
            return "Not same account holder, cancelling the merge."


x = BankAccount(123456789, "Alexander Lindholm", 500.0) # Arguments for BankAccount class.
y = BankAccount(7654321, "Alexander Lindholm", 600.0)
BankAccount.deposit(x, 300.0)

BankAccount.merge_account(x, y)

print(BankAccount.display_account_info(x))
print(BankAccount.display_transaction_history(x))


#class Bank():
#
#    def __init__(self, name, owner, location, bank_accounts):
#        self.name = name
#        self.owner = owner
#        self.location = location
#        self.bank_accounts = bank_accounts


#    def create_bank_account(self):
#
#    def add_bank_account(self):
#    
#    def close_bank_account(self):
#    
#    def generate_accounts_report(self):
#
#    def get_accounts_for_person(self):


#class Person():
#
#    def __init__(self):
#        pass