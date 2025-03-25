#!/usr/bin/python3
"""
### **Exercise 3: Encapsulation**
Create a class `BankAccount` with:
Private attributes: `__balance`
Methods:
`deposit(amount)` (add to the balance)
`withdraw(amount)` (subtract from the balance if sufficient funds are available)
`get_balance()` (return the current balance)
Test the class by creating an account, performing deposits and withdrawals, and accessing the balance."""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   #esto para hacer privado el atributo balance
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())