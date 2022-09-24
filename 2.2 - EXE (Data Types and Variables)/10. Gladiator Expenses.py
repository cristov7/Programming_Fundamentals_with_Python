count_lose_battles = int(input())
price_per_one_helmet = float(input())
price_per_one_sword = float(input())
price_per_one_shield = float(input())
price_per_one_armour = float(input())
expenses = 0
counter = 0
for lose in range(1, count_lose_battles + 1):
    if lose % 2 == 0:
        expenses += price_per_one_helmet
    if lose % 3 == 0:
        expenses += price_per_one_sword
    if lose % 2 == 0 and lose % 3 == 0:   # if lose % 6 == 0:
        expenses += price_per_one_shield
        counter += 1
        if counter == 2:
            expenses += price_per_one_armour
            counter = 0
        else:
            continue
print(f"Gladiator expenses: {expenses:.2f} aureus")


# count_lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armour_price = float(input())
# count_helmets = count_lost_fights // 2
# count_swords = count_lost_fights // 3
# count_shields = count_lost_fights // 6   # count_lost_fights // (2 * 3)
# count_armours = count_shields // 2
# expenses_per_helmets = count_helmets * helmet_price
# expenses_per_swords = count_swords * sword_price
# expenses_per_shields = count_shields * shield_price
# expenses_per_armours = count_armours * armour_price
# total_expenses = expenses_per_helmets + expenses_per_swords + expenses_per_shields + expenses_per_armours
# print(f"Gladiator expenses: {total_expenses:.2f} aureus")
