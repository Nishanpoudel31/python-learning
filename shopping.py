# # print("Welcome to my shopping app.")
# # total_items = int(input("enter how many items: "))
# # total_price = 0

# # for i in range(1,total_items + 1):
# #     price = float(input(f"enter price for {i}: "))
# #     total_price = total_price + price


# # print(f"Total price for {total_items} items is RS.{total_price}")


print("welcome to Nishan's shopping app.")
total_price = 0
is_shopping = True
while is_shopping:
    price = float(input("enter price: "))
    total_price = total_price + price
    choice= print("Do you want to add more items: [yes/no]")
    if choice.lower() == "yes":
        

