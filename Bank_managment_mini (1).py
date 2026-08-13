class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise   InsufficientBalanceError("Not enough balance")
        self.balance -= amount
        print("Withdraw Succesful")

try:
    acc = BankAccount(2000)
    acc.withdraw(4000)

except InsufficientBalanceError as e:
    print("Transaction failed", e)            