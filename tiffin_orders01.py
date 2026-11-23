
total_tiffins = 0
total_bill = 0

while True:
    customer_name = input("Enter customer name (or 'stop' to finish): ")

    if customer_name.lower() == "stop":
        break

    number_of_tiffins = int(input("Enter number of tiffins: "))

    print("\nTiffin Plans:")
    print("1. Regular - ₹60")
    print("2. Jain - ₹70")
    print("3. Special - ₹90")

    plan_number = int(input("Enter plan number: "))

    if plan_number == 1:
        price = 60
        plan_name = "Regular"
    elif plan_number == 2:
        price = 70
        plan_name = "Jain"
    elif plan_number == 3:
        price = 90
        plan_name = "Special"
    else:
        print("Error: Invalid plan number!")
        continue

    bill = number_of_tiffins * price

    total_tiffins += number_of_tiffins
    total_bill += bill

    print("\n Order Successful!")
    print("Customer Name:", customer_name)
    print("Plan:", plan_name)
    print("Number of Tiffins:", number_of_tiffins)
    print("Order Bill: ₹", bill)

print("\n========== FINAL SUMMARY ==========")
print("Total Tiffins Ordered:", total_tiffins)
print("Total Bill: ₹", total_bill)
