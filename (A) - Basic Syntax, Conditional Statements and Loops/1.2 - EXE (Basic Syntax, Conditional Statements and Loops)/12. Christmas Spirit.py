quantity_decoration_to_buy_per_day = int(input())
days_to_christmas = int(input())
total_cost = 0
total_spirit = 0
for shopping_day in range(1, days_to_christmas + 1):
    if shopping_day % 11 == 0:
        quantity_decoration_to_buy_per_day += 2
    if shopping_day % 2 == 0:
        price_per_ornament_set = 2
        total_cost += price_per_ornament_set * quantity_decoration_to_buy_per_day
        christmas_spirit = 5
        total_spirit += christmas_spirit
    if shopping_day % 3 == 0:
        price_per_tree_skirt = 5
        total_cost += price_per_tree_skirt * quantity_decoration_to_buy_per_day
        christmas_spirit = 3
        total_spirit += christmas_spirit
        price_per_tree_garland = 3
        total_cost += price_per_tree_garland * quantity_decoration_to_buy_per_day
        christmas_spirit = 10
        total_spirit += christmas_spirit
    if shopping_day % 5 == 0:
        price_per_tree_lights = 15
        total_cost += price_per_tree_lights * quantity_decoration_to_buy_per_day
        christmas_spirit = 17
        total_spirit += christmas_spirit
        if shopping_day % 3 == 0:
            christmas_spirit = 30
            total_spirit += christmas_spirit
    if shopping_day % 10 == 0:
        christmas_spirit = - 20
        total_spirit += christmas_spirit
        price_per_tree_skirt = 5
        total_cost += price_per_tree_skirt
        price_per_tree_garland = 3
        total_cost += price_per_tree_garland
        price_per_tree_lights = 15
        total_cost += price_per_tree_lights
if days_to_christmas % 10 == 0:
    christmas_spirit = - 30
    total_spirit += christmas_spirit
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")


# quantity = int(input())
# days = int(input())
# price_per_one_ornament_set = 2
# points_per_one_ornament_set = 5
# price_per_one_tree_skirt = 5
# points_per_one_tree_skirt = 3
# price_per_one_tree_garland = 3
# points_per_one_tree_garland = 10
# price_per_one_tree_lights = 15
# points_per_one_tree_lights = 17
# total_expenses = 0
# total_spirit = 0
# for day in range(1, days + 1):
#     if day % 11 == 0:
#         quantity += 2
#     if day % 2 == 0:
#         total_expenses += (price_per_one_ornament_set * quantity)
#         total_spirit += points_per_one_ornament_set
#     if day % 3 == 0:
#         total_expenses += (price_per_one_tree_skirt * quantity) + (price_per_one_tree_garland * quantity)
#         total_spirit += points_per_one_tree_skirt + points_per_one_tree_garland
#     if day % 5 == 0:
#         total_expenses += (price_per_one_tree_lights * quantity)
#         total_spirit += points_per_one_tree_lights
#     if day % 3 == 0 and day % 5 == 0:
#         total_spirit += 30
#     if day % 10 == 0:
#         total_spirit -= 20
#         total_expenses += price_per_one_tree_skirt + price_per_one_tree_garland + price_per_one_tree_lights
# if days % 10 == 0:
#     total_spirit -= 30
#     print(f"Total cost: {total_expenses}")
#     print(f"Total spirit: {total_spirit}")
# else:
#     print(f"Total cost: {total_expenses}")
#     print(f"Total spirit: {total_spirit}")
