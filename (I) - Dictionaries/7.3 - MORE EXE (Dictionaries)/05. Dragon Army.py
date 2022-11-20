def check_null_values(dragon_damage, dragon_health, dragon_armor):
    if dragon_damage == "null":
        dragon_damage = 45
    if dragon_health == "null":
        dragon_health = 250
    if dragon_armor == "null":
        dragon_armor = 10
    return dragon_damage, dragon_health, dragon_armor


dragons = {}
number_of_entries = int(input())
for entry in range(number_of_entries):
    type, name, damage, health, armor = input().split()
    damage, health, armor = check_null_values(damage, health, armor)
    if type not in dragons:
        dragons[type] = {"total damage": 0, "total health": 0, "total armor": 0}
    if name not in dragons[type]:
        dragons[type][name] = {}
    else:
        dragons[type]["total damage"] -= dragons[type][name]["damage"]
        dragons[type]["total health"] -= dragons[type][name]["health"]
        dragons[type]["total armor"] -= dragons[type][name]["armor"]
    dragons[type][name]["damage"] = int(damage)
    dragons[type][name]["health"] = int(health)
    dragons[type][name]["armor"] = int(armor)
    dragons[type]["total damage"] += int(damage)
    dragons[type]["total health"] += int(health)
    dragons[type]["total armor"] += int(armor)
statistic_keys = ["total damage", "total health", "total armor"]
for dragon_type, dragon in dragons.items():
    number_of_dragons = len(dragons[dragon_type]) - 3
    average_damage = dragons[dragon_type]["total damage"] / number_of_dragons
    average_health = dragons[dragon_type]["total health"] / number_of_dragons
    average_armor = dragons[dragon_type]["total armor"] / number_of_dragons
    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    sorted_dragons = dict(sorted(dragon.items(), key=lambda x: x[0]))
    for key, value in sorted_dragons.items():
        if key not in statistic_keys:
            print(f"-{key} -> damage: {value['damage']}, health: {value['health']}, armor: {value['armor']}")


# dragon_army = {}
# total_statistic_per_types = {}
# count_dragons = int(input())
# for dragon in range(1, count_dragons + 1):
#     current_dragon = input().split()
#     current_type = current_dragon[0]
#     current_name = current_dragon[1]
#     current_damage = current_dragon[2]
#     if current_damage == "null":
#         current_damage = 45
#     else:
#         current_damage = int(current_dragon[2])
#     current_health = current_dragon[3]
#     if current_health == "null":
#         current_health = 250
#     else:
#         current_health = int(current_dragon[3])
#     current_armor = current_dragon[4]
#     if current_armor == "null":
#         current_armor = 10
#     else:
#         current_armor = int(current_dragon[4])
#     dragon_data = [current_damage, current_health, current_armor]
#     if current_type not in total_statistic_per_types:
#         total_statistic_per_types[current_type] = {}
#         total_statistic_per_types[current_type]["damage"] = current_damage
#         total_statistic_per_types[current_type]["health"] = current_health
#         total_statistic_per_types[current_type]["armor"] = current_armor
#         total_statistic_per_types[current_type]["count"] = 1
#     else:
#         total_statistic_per_types[current_type]["damage"] += current_damage
#         total_statistic_per_types[current_type]["health"] += current_health
#         total_statistic_per_types[current_type]["armor"] += current_armor
#         total_statistic_per_types[current_type]["count"] += 1
#     if current_type not in dragon_army:
#         dragon_army[current_type] = {}
#         dragon_army[current_type][current_name] = dragon_data
#     else:
#         if current_name not in dragon_army[current_type]:
#             dragon_army[current_type][current_name] = dragon_data
#         else:
#             continue
# for dragon_type, dragon_info in dragon_army.items():
#     total_info_type = total_statistic_per_types[dragon_type]
#     total_info_damage = total_info_type["damage"]
#     total_info_health = total_info_type["health"]
#     total_info_armor = total_info_type["armor"]
#     total_info_count = total_info_type["count"]
#     average_damage = total_info_damage / total_info_count
#     average_health = total_info_health / total_info_count
#     average_armor = total_info_armor / total_info_count
#     print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
#     dragon_info_sorted_names = sorted(dragon_info.items(), key=lambda x: x[0])
#     for data in dragon_info_sorted_names:
#         name = data[0]
#         skills = data[1]
#         damage = skills[0]
#         health = skills[1]
#         armor = skills[2]
#         info = f"-{name} -> damage: {damage}, health: {health}, armor: {armor}"
#         print(info)
