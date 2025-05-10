# Episode 4: The Sinister Bank Corp Plot

In the dark corners of the secret underground lair, Commander Lambda, the brilliant and evil genius, hatches a new plan. This time, it's not world domination or world destruction, but something far more devious: infiltrating the Evil Bank Corp! The plan is to manipulate their financial systems and extract a fortune. The key to success? A specially crafted Python program and a secret agent (you) who can build it.

Mission Briefing:

Commander Lambda has devised a cunning scheme to infiltrate several banks at the company Evil Bank Corp. It involves creating a piece of code with a few difference classes in Python.

This piece of code is the first step to create a virus that can infiltrate real banks to slowly chip away rounding errors in the transfer calculations. This will be the ultimate tool for money manipulation, and it's your mission to build it.


## Problem/Solution

Create a class BankAccount

Required attributes:
 - account_number (a unique identifier for each account, this identifier should be unique generated for each account)
 - account_holder (the name of the person account holder)
 - balance (the current balance in the account)
 - transaction_history: Some data structure that tracks when and how much each transaction was

Required Methods to implement:

 - __init__ This method is the constructor and should initialize the attributes when a new account is created. The account_number should be generated automatically and unique for each account.
 - deposit: This method should allow the account holder to deposit a specified amount into their account. It should update the account's balance accordingly.
 - withdraw: This method should allow the account holder to withdraw a specified amount from their account, provided they have sufficient funds. It should update the account's balance accordingly.
 - get_balance: This method should return the current balance of the account.
 - display_account_info: This method should display the account information, including the account number, account holder's name, and current balance.
 - merge_account: If provided with another BankAccount, if it belongs to the same account holder, they should be merged together into one bank account. Note here that how do you verify/validate that two accounts with the same name really is the exact same person?

-----

Create a class Bank

Required attributes
 - bank_accounts: Some way of tracking all bank accounts

Required methods to implement
 - __init__ This methods create a new bank. Each bank has a name, a owner and location where it exists (thinkk street address)
 - create_bank_account: Creates a new bank account given all reuqired information for a bank account
 - add_bank_account: The ability to add an existing BankAccount object to this bank. You need to validate that the new account do not conflict with any existing bank account
 - close_bank_account: Closes and removes the BankAccount from this bank. Think about what happens to deposited money in this case.
 - generate_accounts_report: This method should take all BankAccounts and generate a CSV report with all relevant information that a bank manager might want to look at. This output should be written to the filename "accounts_report.csv"
 - get_accounts_for_person: Given a person or person identifier data, return all BankAccounts for this person

-----

Create a class Person. You need to have the capability to track an individual physical person and use this object when you create a bank account, or even to represent the Bank owner. A unique identifier schema must be sorted so that the same firstname + lastname for two different persons can be distribugished between eachother. Methods that needs to be possible to run from this class is "get_all_bank_accounts" & "get_total_balance". Note here that one Person can have many different accounts in many different Banks all at once. One final method that Commander Lambda wants to be implemented is that you should be able to compare two Person objects with eachother with the syntax `if person_one == person_two`, `if person_one != person_two` in order to make the comparison between two different person objects simpler.

-----

Additional Instructions:

Implement error checking in the withdraw method to ensure that the account holder cannot withdraw more than the available balance.

Error checking should be implemented where ever it is resonable to be added

Implement a way to generate unique account_number values. Each new account should have a unique account number, and this number should be automatically generated when a new account is created. This do not need to be perfect, just very very very unlikley to not collide.

Add comments to your code to explain the purpose of each method and attribute.



## Verification script

```python
python3 verification.py
```

If this script do not throw an error, the script succeeds and the test cases within it works.

I will attempt to write my own test code from your submited solution in order to verify a few known corner-cases and to see if your submited code fullfills the requirements or not.


## Hints and help

You will have to write your own test code from scratch. No pre-existing test code will be provided and you have to extract all relevant value and constraints from the assignment text

Note that you might need to implement additional attributes and methods in order to fullfill all requirements for this problem.

Some methods and solutions do not need to be perfectly implemented. Sometimes even just documenting or knowing about a corner case even if it still exists, is okey to have around.

You are free to add additional functionality outside this specification. If you do, it must be documented well what it is, how it works and the purpose of it and why we need that functionality for the future.


## Constraints and additional requirements

Bank, BankAccount, Person must be a python class

Creating a good and unique account identifier is important. There are a few good built-in solutions in the python std lib that is commonly used. This identifier do not require to be guaranteed to never have duplicate entries, it should just be very very very unlikley that it happens

You must write a full documentation for your project in a `README.md` file in this folder. It should include installation instructions, how to run the code, how to run the test code, and a description of the purpose of why this code exists. This task requires you to make assumptions and trade-off:s based on incomplete and infomration not provided. These assumptions and things should be written down.

If you use external dependencies, they must be documented in a file named "requirements.txt"

Submit an example file accounts_report.csv that you have generated on your machine with any test data

Test code needs to be separated into smaller independant test functions using pythons built-in "Unittest" framework. A tip here is to look at and possibly implement the use of "pytest" when writing your test cases

Bonus points if you use and document how to install and run the code within a virtualenv

If you add anything outside the scope of what is really required, if this is a new value, helper method, or anything similar, it expected to contain all documentation from installation instrucitons, all the way to top level documentation for us to consume
