item = input()
qty = int(input())
price = float(input())

total = qty * price

# TODO: put the values into these three lines with f-strings.
# The total must show exactly two digits after the decimal point.
print("Item:", item)
print("Quantity:", qty)
print(f"Total: ${total:.2f}")
