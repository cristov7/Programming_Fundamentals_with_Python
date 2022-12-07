food_preferences = {}
count_dislike_meals = 0
while True:
    command = input()
    if command == "Stop":
        break
    else:
        command_list = command.split("-")
        info = command_list[0]
        if info == "Like":
            guest = command_list[1]
            meal = command_list[2]
            if guest not in food_preferences.keys():
                food_preferences[guest] = [meal]
            else:
                menu_list = food_preferences[guest]
                if meal not in menu_list:
                    food_preferences[guest].append(meal)
                else:
                    continue
        elif info == "Dislike":
            guest = command_list[1]
            meal = command_list[2]
            if guest not in food_preferences.keys():
                print(f"{guest} is not at the party.")
            else:
                menu_list = food_preferences[guest]
                if meal in menu_list:
                    index = menu_list.index(meal)
                    del food_preferences[guest][index]
                    count_dislike_meals += 1
                    print(f"{guest} doesn't like the {meal}.")
                else:
                    print(f"{guest} doesn't have the {meal} in his/her collection.")
for person, menu_list in food_preferences.items():
    print(f"{person}: {', '.join(menu_list)}")
print(f"Unliked meals: {count_dislike_meals}")
