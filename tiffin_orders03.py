
total_tiffins = 0
total_bill = 0

while True:
    customer_name = input("Enter customer name (or 'stop' to finish): ")

    if customer_name.lower() == "stop":
        break

    tiffins = int(input("Enter number of tiffins: "))

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

    if tiffins >= 10:
        pass  # bulk discount to be added later

    bill = tiffins * price

    total_tiffins += tiffins
    total_bill += bill

    print("\nOrder Successful!")
    print("Customer Name:", customer_name)
    print("Plan:", plan_name)
    print("Number of Tiffins:", tiffins)
    print("Order Bill: ₹", bill)

    if total_tiffins >= 20:
        print("Kitchen full")
        break

print("\n========== FINAL SUMMARY ==========")
print("Total Tiffins Ordered:", total_tiffins)
print("Total Bill: ₹", total_bill)


# OUTPUT:
# Enter customer name (or 'stop' to finish): ABC
# Enter number of tiffins: 3
# Enter plan number: 1
#
# Order Successful!
# Customer Name: ABC
# Plan: Regular
# Number of Tiffins: 3
# Order Bill: ₹ 180
#
# Enter customer name (or 'stop' to finish): PQR
# Enter number of tiffins: 2
# Enter plan number: 9
# Error: Invalid plan number!
#
# Enter customer name (or 'stop' to finish): XYZ
# Enter number of tiffins: 12
# Enter plan number: 2
#
# Order Successful!
# Customer Name: XYZ
# Plan: Jain
# Number of Tiffins: 12
# Order Bill: ₹ 840
#
# Enter customer name (or 'stop' to finish): stop
#
# ========== FINAL SUMMARY ==========
# Total Tiffins Ordered: 15
# Total Bill: ₹ 1020
