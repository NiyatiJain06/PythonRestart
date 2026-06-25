Amount = int(input("Enter total amount:"))

if Amount >=5000:
    print("Eligible for discount")

    print("Enter Mode of payment:")
    mode = input("A- Cash, B- Card, C- UPI:")
    if mode == "B":
        print("Discount Appiled")
    elif mode == "A" or "C":
        print("Discount not applied")
    else:
        print("In-valid input")        
     

elif (Amount>0) and (Amount<5000):
    print("Not eligible")

else:
    print("Please do shopping")    

