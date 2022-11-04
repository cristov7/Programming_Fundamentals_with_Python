stock = {}
while True:
    command = input()
    if command == "statistics":
        break
    else:
        command_list = command.split(": ")   # available_product, available_quantity = command.split(": ")
        available_product = command_list[0]
        available_quantity = int(command_list[1])
        if available_product in stock.keys():   # if available_product in stock:
            stock[available_product] += available_quantity
        else:
            stock[available_product] = available_quantity
print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")


# stock = {}
# while True:
#     command = input()
#     if command == "statistics":
#         print("Products in stock:")
#         for product, quantity in stock.items():
#             print(f"- {product}: {quantity}")
#         break
#     else:
#         command_list = command.split(": ")
#         available_product = command_list[0]
#         available_quantity = int(command_list[1])
#         if available_product in stock.keys():
#             stock[available_product] += available_quantity
#         else:
#             stock[available_product] = available_quantity
# print(f"Total Products: {len(stock)}")
# print(f"Total Quantity: {sum(stock.values())}")
