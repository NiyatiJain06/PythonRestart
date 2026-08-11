"""
Bank account managment without encapsulation
balance not private
"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance= balance

account1 = BankAccount("Pappu", 10000)
print(account1.name)
account1.balance = 5000000   
print(account1.balance)     