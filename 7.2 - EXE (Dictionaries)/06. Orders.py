orders = {}
while True:
    command = input()
    if command == "buy":
        break
    else:
        # name, price, quantity = command.split()
        info_list = command.split()
        name = info_list[0]
        price = float(info_list[1])
        quantity = int(info_list[2])
        if name not in orders.keys():   # if name not in orders:
            orders[name] = [price, quantity]
        else:
            orders[name][0] = price
            orders[name][1] += quantity
for product_name, price_and_quantity in orders.items():
    total_price = price_and_quantity[0] * price_and_quantity[1]
    print(f"{product_name} -> {total_price:.2f}")


# orders_dict = {}
# while True:
#     command = input()
#     if command == 'buy':
#         break
#     product, price, quantity = command.split()
#     if product not in orders_dict:
#         orders_dict[product] = {'price': 0.00, 'quantity': 0}
#     orders_dict[product]['price'] = float(price)
#     orders_dict[product]['quantity'] += int(quantity)
# for product_name, data in orders_dict.items():
#     total_price = data['price'] * data['quantity']
#     print(f"{product_name} -> {total_price:.2f}")
