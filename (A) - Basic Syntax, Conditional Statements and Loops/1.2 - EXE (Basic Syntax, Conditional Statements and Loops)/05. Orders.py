total_price = 0
count_orders = int(input())
for order in range(count_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00\
            and 1 <= days <= 31\
            and 1 <= needed_capsules_per_day <= 2000:
        price_per_one_coffee = price_per_capsule * days * needed_capsules_per_day
        print(f"The price for the coffee is: ${price_per_one_coffee:.2f}")
        total_price += price_per_one_coffee
    else:
        continue
print(f"Total: ${total_price:.2f}")


# total_price_per_all_orders = 0
# count_orders = int(input())
# for order in range(1, count_orders + 1):
#     price_per_one_capsule = float(input())
#     days = int(input())
#     count_capsules_per_one_day = int(input())
#     if 0.01 <= price_per_one_capsule <= 100 and 1 <= days <= 31 and 1 <= count_capsules_per_one_day <= 2000:
#         total_price_per_order = price_per_one_capsule * count_capsules_per_one_day * days
#         print(f"The price for the coffee is: ${total_price_per_order:.2f}")
#         total_price_per_all_orders += total_price_per_order
#     else:
#         continue
# else:
#     print(f"Total: ${total_price_per_all_orders:.2f}")
