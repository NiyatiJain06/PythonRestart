price = float(input("Enter product price:"))
quantity = float(input("Enter product quatity:"))

total_price = price*quantity
gst = total_price*18/100
final_amount = total_price+gst

print("Total_price:", total_price)
print("GST:",gst)
print("Final_amount:",final_amount) 