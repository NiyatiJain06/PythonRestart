"""
Bank account managment with encapsulation
we make balance private variable
customer use only requrid data - modify, deposit, withdraw
"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -=amount
        else:
            print("In-valid withdrawl")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Pappu", 10000)
print("1st", acc1.get_balance())
acc1.deposit(5000)
acc1.__balance = 100000 # use this line in code and run the code, code will not be change because (__balance) is private variable.
print("After deposit 5000", acc1.get_balance())
acc1.withdraw(2000)
print("After withdraw 2000", acc1.get_balance())

