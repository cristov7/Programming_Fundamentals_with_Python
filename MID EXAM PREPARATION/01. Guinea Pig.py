available_food_grams = float(input()) * 1000
available_hay_grams = float(input()) * 1000
available_cover_grams = float(input()) * 1000
weight_guinea_pig_grams = float(input()) * 1000
food_is_enough = True
for day in range(1, 31):
    available_food_grams -= 300
    if day % 2 == 0:
        amount_of_hay_per_every_second_day_grams = available_food_grams * 0.05
        available_hay_grams -= amount_of_hay_per_every_second_day_grams
    if day % 3 == 0:
        quantity_cover_per_every_third_day_grams = weight_guinea_pig_grams * 1 / 3
        available_cover_grams -= quantity_cover_per_every_third_day_grams
    if available_food_grams <= 0 or available_hay_grams <= 0 or available_cover_grams <= 0:
        food_is_enough = False
        break
if food_is_enough:
    # available_food_kg = available_food_grams / 1000
    # available_hay_kg = available_hay_grams / 1000
    # available_cover_kg = available_cover_grams / 1000
    available_food_kg, available_hay_kg, available_cover_kg = available_food_grams / 1000, available_hay_grams / 1000, available_cover_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {available_food_kg:.2f}, Hay: {available_hay_kg:.2f}, Cover: {available_cover_kg:.2f}.")
else:
    print("Merry must go to the pet store!")


# available_food_grams = float(input()) * 1000
# available_hay_grams = float(input()) * 1000
# available_cover_grams = float(input()) * 1000
# weight_guinea_pig_grams = float(input()) * 1000
# count_days = 30
# # used_food_grams = 0
# # used_amount_of_hay_grams = 0
# # used_quantity_cover_grams = 0
# food_is_enough = True
# for day in range(1, count_days + 1):
#     food_per_day_grams = 300
#     if available_food_grams - food_per_day_grams > 0:
#         available_food_grams -= food_per_day_grams
#         # used_food_grams += food_per_day_grams
#         if day % 2 == 0:
#             amount_of_hay_per_every_second_day_grams = available_food_grams * 0.05
#             if available_hay_grams - amount_of_hay_per_every_second_day_grams >= 0:
#                 available_hay_grams -= amount_of_hay_per_every_second_day_grams
#                 # used_amount_of_hay_grams += amount_of_hay_per_every_second_day_grams
#             else:
#                 food_is_enough = False
#                 break
#         if day % 3 == 0:
#             quantity_cover_per_every_third_day_grams = weight_guinea_pig_grams * 1 / 3
#             if available_cover_grams - quantity_cover_per_every_third_day_grams >= 0:
#                 available_cover_grams -= quantity_cover_per_every_third_day_grams
#                 # used_quantity_cover_grams += quantity_cover_per_every_third_day_grams
#             else:
#                 food_is_enough = False
#                 break
#     else:
#         food_is_enough = False
#         break
# if food_is_enough:
#     available_food_kg = available_food_grams / 1000
#     available_hay_kg = available_hay_grams / 1000
#     available_cover_kg = available_cover_grams / 1000
#     print(f"Everything is fine! Puppy is happy! Food: {available_food_kg:.2f}, Hay: {available_hay_kg:.2f}, Cover: {available_cover_kg:.2f}.")
# else:
#     print("Merry must go to the pet store!")


# available_food_kg = float(input())
# available_hay_kg = float(input())
# available_cover_kg = float(input())
# weight_guinea_pig = float(input())
# count_days = 30
# # used_food = 0
# # used_amount_of_hay = 0
# # used_quantity_cover = 0
# food_is_enough = True
# for day in range(1, count_days + 1):
#     food_per_day = 0.300
#     if available_food_kg - food_per_day > 0:
#         available_food_kg -= food_per_day
#         # used_food += food_per_day
#         if day % 2 == 0:
#             amount_of_hay_per_every_second_day = available_food_kg * 0.05
#             if available_hay_kg - amount_of_hay_per_every_second_day >= 0:
#                 available_hay_kg -= amount_of_hay_per_every_second_day
#                 # used_amount_of_hay += amount_of_hay_per_every_second_day
#             else:
#                 food_is_enough = False
#                 break
#         if day % 3 == 0:
#             quantity_cover_per_every_third_day = weight_guinea_pig * 1 / 3
#             if available_cover_kg - quantity_cover_per_every_third_day >= 0:
#                 available_cover_kg -= quantity_cover_per_every_third_day
#                 # used_quantity_cover += quantity_cover_per_every_third_day
#             else:
#                 food_is_enough = False
#                 break
#     else:
#         food_is_enough = False
#         break
# if food_is_enough:
#     print(f"Everything is fine! Puppy is happy! Food: {available_food_kg:.2f}, Hay: {available_hay_kg:.2f}, Cover: {available_cover_kg:.2f}.")
# else:
#     print("Merry must go to the pet store!")
