available_items = {}
while True:
    info = input()
    if info == "statistics":
        print("Products in stock:")
        for product, quantity in available_items.items():
            print(f"- {product}: {quantity}")
        count_all_products = len(available_items.keys())
        print(f"Total Products: {count_all_products}")
        sum_all_quantities = sum(available_items.values())
        print(f"Total Quantity: {sum_all_quantities}")
        break
    else:
        info_list = info.split(": ")
        product = info_list[0]
        quantity = info_list[1]
        if product not in available_items.keys():
            available_items[product] = int(quantity)
        else:
            available_items[product] += int(quantity)


# stock = {}
# while True:
#     command = input()
#     if command == "statistics":
#         break
#     else:
#         command_list = command.split(": ")   # available_product, available_quantity = command.split(": ")
#         available_product = command_list[0]
#         available_quantity = int(command_list[1])
#         if available_product in stock.keys():   # if available_product in stock:
#             stock[available_product] += available_quantity
#         else:
#             stock[available_product] = available_quantity
# print("Products in stock:")
# for product, quantity in stock.items():
#     print(f"- {product}: {quantity}")
# print(f"Total Products: {len(stock)}")
# print(f"Total Quantity: {sum(stock.values())}")


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
