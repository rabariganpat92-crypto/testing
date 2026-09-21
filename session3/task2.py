price = input("Enter the price of your Zomato order: ")
price = float(price)
gst = price * 0.18
final_bill = price + gst
print("Final bill amount:", final_bill)
