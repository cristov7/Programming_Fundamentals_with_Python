item_with_prices = input().split("|")
budget = float(input())
ticket_train = 150
price_per_purchased_items = []
for element in item_with_prices:
    current_element = element.split("->")
    type_item = current_element[0]
    price_item = float(current_element[1])
    if type_item == "Clothes" and price_item <= 50:
        if budget - price_item >= 0:
            budget -= price_item
            price_per_purchased_items.append(price_item)
        else:
            continue
    elif type_item == "Shoes" and price_item <= 35:
        if budget - price_item >= 0:
            budget -= price_item
            price_per_purchased_items.append(price_item)
        else:
            continue
    elif type_item == "Accessories" and price_item <= 20.50:
        if budget - price_item >= 0:
            budget -= price_item
            price_per_purchased_items.append(price_item)
        else:
            continue
    else:
        continue
price_per_sold_item = []
for items in price_per_purchased_items:
    new_price_item = items * 1.4
    price_per_sold_item.append(new_price_item)
    print(f"{new_price_item:.2f}", end=" ")
total_purchased_price = sum(price_per_purchased_items)
total_sold_items = sum(price_per_sold_item)
profit = abs(total_purchased_price - total_sold_items)
print(f"\nProfit: {profit:.2f}")
save_money_for_ticket = budget + total_sold_items
if save_money_for_ticket >= ticket_train:
    print("Hello, France!")
else:
    print("Not enough money.")


# itemsList = input().split("|")
# budget = float(input())
# oldPriceList = []
# newPriceList = []
# for item in itemsList:
#     current_item = item.split("->")
#     type_item = current_item[0]
#     price = float(current_item[1])
#     if "Clothes" in type_item and price <= 50:
#         if budget - price >= 0:
#             budget -= price
#             oldPriceList.append(price)
#     elif "Shoes" in type_item and price <= 35:
#         if budget - price >= 0:
#             budget -= price
#             oldPriceList.append(price)
#     elif "Accessories" in type_item and price <= 25.5:
#         if budget - price >= 0:
#             budget -= price
#             oldPriceList.append(price)
# for i in oldPriceList:
#     newPrice = i * 1.4
#     newPriceList.append(newPrice)
#     print(f"{newPrice:.2f}", end=" ")
# profit = sum(newPriceList) - sum(oldPriceList)
# print()
# print(f"Profit: {profit:.2f}")
# if budget + sum(newPriceList) >= 150:
#     print("Hello, France!")
# else:
#     print("Not enough money.")
