import re
regex = r">>([A-Za-z]+)<<([\d]+[\.\d]*)!([\d]+)\b"
names_list = []
total_price_list = []
while True:
    command = input()
    if command == "Purchase":
        break
    else:
        info_list = re.findall(regex, command)
        if len(info_list) == 1:
            info = info_list[0]
            if len(info) == 3:
                furniture_name = info[0]
                names_list.append(furniture_name)
                price = float(info[1])
                quantity = int(info[2])
                total_price = price * quantity
                total_price_list.append(total_price)
            else:
                continue
        else:
            continue
print("Bought furniture:")
[print(name) for name in names_list]
total_money_spend = sum(total_price_list)
print(f"Total money spend: {total_money_spend:.2f}")


# import re
# regex = r">>([A-Za-z]+)<<([\d]+[\.\d]*)!([\d]+)\b"
# furniture_list = []
# total_price = 0
# while True:
#     command = input()
#     if command == "Purchase":
#         break
#     else:
#         info = re.search(regex, command)
#         if info:
#             # furniture_name, price, quantity = info.groups()   # strings
#             furniture_name = info.group(1)
#             furniture_list.append(furniture_name)
#             price = float(info.group(2))
#             quantity = int(info.group(3))
#             total_price += (price * quantity)
#         else:
#             continue
# print("Bought furniture:")
# [print(name) for name in furniture_list]
# print(f"Total money spend: {total_price:.2f}")


# import re
# names_list = []
# total_price_list = []
# while True:
#     command = input()
#     if command == "Purchase":
#         break
#     else:
#         furniture_name_list = re.findall(r">>([A-Za-z]+)<<\b", command)
#         price_list = re.findall(r"<<([\d]+[\.\d]*)!\b", command)
#         quantity_list = re.findall(r"!([\d]+)\b", command)
#         if len(furniture_name_list) == 1 and len(price_list) == 1 and len(quantity_list) == 1:
#             names_list.extend(furniture_name_list)
#             current_price = float(*price_list)
#             current_quantity = int(*quantity_list)
#             total_price = current_price * current_quantity
#             total_price_list.append(total_price)
#         else:
#             continue
# print("Bought furniture:")
# [print(name) for name in names_list]
# total_money_spend = sum(total_price_list)
# print(f"Total money spend: {total_money_spend:.2f}")
