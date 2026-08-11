class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Processing payment of:", self.amount)

class CreditCardPayment(Payment):
    def pay(self):
        print("Credit Card payment of:", self.amount, ":+ 2% Processing fee")

class UPIPayment(Payment):
    def pay(self):
        print("UPI Payment of", self.amount, "With Noo Fee")

p1 = CreditCardPayment(500)
p1.pay()

p2 =UPIPayment(1000)
p2.pay()