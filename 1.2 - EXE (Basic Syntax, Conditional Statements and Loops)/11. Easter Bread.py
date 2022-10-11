budget = float(input())
count_easter_bread = 0
count_coloured_eggs = 0
price_per_one_kg_flour = float(input())
price_per_one_pack_eggs = 0.75 * price_per_one_kg_flour
price_per_one_milk = (1.25 * price_per_one_kg_flour) / 4
price_per_one_easter_bread = price_per_one_pack_eggs + price_per_one_kg_flour + price_per_one_milk
while budget >= price_per_one_easter_bread:
    budget -= price_per_one_easter_bread
    count_easter_bread += 1
    count_coloured_eggs += 3
    if count_easter_bread % 3 == 0:
        count_lost_eggs = count_easter_bread - 2
        count_coloured_eggs -= count_lost_eggs
print(f"You made {count_easter_bread} loaves of Easter bread! Now you have {count_coloured_eggs} eggs and {budget:.2f}BGN left.")


# budget = float(input())
# price_per_one_kg_flour = float(input())
# price_per_one_eggs_pack = 0.75 * price_per_one_kg_flour
# price_per_one_liter_milk = (1.25 * price_per_one_kg_flour) / 4
# price_per_one_easter_bread = price_per_one_kg_flour + price_per_one_eggs_pack + price_per_one_liter_milk
# counter_easter_bread = int(budget // price_per_one_easter_bread)
# money_left_over = budget - (counter_easter_bread * price_per_one_easter_bread)
# counter_colored_eggs = 0
# count_eggs_process = 0
# for easter_bread in range(1, counter_easter_bread + 1):
#     counter_colored_eggs += 3
#     count_eggs_process += 1
#     if easter_bread % 3 == 0:
#         count_lost_eggs = count_eggs_process - 2
#         counter_colored_eggs -= count_lost_eggs
#     else:
#         continue
# print(f"You made {counter_easter_bread} loaves of Easter bread! Now you have {counter_colored_eggs} eggs and {money_left_over:.2f}BGN left.")
