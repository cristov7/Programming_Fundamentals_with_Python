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
