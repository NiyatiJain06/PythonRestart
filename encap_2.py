class BankAccount:
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
acc1.__balance = 100000
print("After deposit 5000", acc1.get_balance())
acc1.withdraw(2000)
print("After withdraw 2000", acc1.get_balance())

