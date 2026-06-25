purchase_amount = int(input("Enter the total amount:"))

if purchase_amount>5000:
    print("Premium User")

elif (purchase_amount>=2000) and (purchase_amount<=5000):
    print("Regular User")

else:
    print("New User")        