shopping_cart = []
#you need to purchase five items.
#at end you need to display five items.
total_items = int(input("Enter the number of items: "))
for i in range(total_items):
    item = input(f"Enter item:{i + 1} ")
    shopping_cart.append(item)
print("All items are :")
for i in range(total_items):
    print(f"{shopping_cart[i]}")
