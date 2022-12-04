import re
regex = r"(\#{1}|\|{1})([A-Z a-z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
text = input()
kcal_per_day = 2000
result_list = re.findall(regex, text)
food = []
total_kcal = 0
if result_list:
    for result in result_list:
        item_name = result[1]
        expiration_date = result[2]
        calories = int(result[3])
        food.append([item_name, expiration_date, calories])
        total_kcal += calories
    if total_kcal > 0:
        enough_food_for_days = total_kcal // kcal_per_day   # int(total_kcal / kcal_per_day)
        print(f"You have food to last you for: {enough_food_for_days} days!")
    else:
        print("You have food to last you for: 0 days!")
    for info in food:
        item = info[0]
        date = info[1]
        kcal = info[2]
        print(f"Item: {item}, Best before: {date}, Nutrition: {kcal}")
else:
    print("You have food to last you for: 0 days!")


# import re
# regex = r"(\#{1}|\|{1})([A-Z a-z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
# text = input()
# result_list = re.findall(regex, text)
# print_result = ""
# total_kcal = 0
# for info in result_list:
#     print_result += f"Item: {info[1]}, Best before: {info[2]}, Nutrition: {info[3]}\n"
#     total_kcal += int(info[3])
# kcal_per_day = 2000
# enough_food_for_days = int(total_kcal / kcal_per_day)
# print(f"You have food to last you for: {enough_food_for_days} days!")
# print(print_result)
