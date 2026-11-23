
total_tiffins = 0

while True:
    customer_name = input("Enter customer name (or 'stop' to finish): ")

    if customer_name.lower() == "stop":
        break

    number_of_tiffins = int(input("Enter number of tiffins: "))

    total_tiffins += number_of_tiffins

print("\nTotal tiffins ordered:", total_tiffins)
