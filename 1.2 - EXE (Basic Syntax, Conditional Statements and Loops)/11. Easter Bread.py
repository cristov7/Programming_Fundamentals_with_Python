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
