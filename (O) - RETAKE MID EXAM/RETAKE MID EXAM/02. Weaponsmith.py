def parts_of_weapon(some_weapon: str):
    info_per_weapon_list = some_weapon.split("|")
    while True:
        current_command = input()
        if current_command == "Done":
            break
        else:
            command_list = current_command.split()
            info = command_list[0]
            if info == "Add":
                particle = command_list[1]
                index = int(command_list[2])
                if 0 <= index < len(info_per_weapon_list):
                    info_per_weapon_list.insert(index, particle)
                else:
                    continue
            elif info == "Remove":
                index = int(command_list[1])
                if 0 <= index < len(info_per_weapon_list):
                    del info_per_weapon_list[index]
                else:
                    continue
            elif info == "Check":
                command = command_list[1]
                if command == "Even":
                    even_parts_list = [part for index, part in enumerate(info_per_weapon_list) if index % 2 == 0]
                    print(" ".join(even_parts_list))
                elif command == "Odd":
                    odd_parts_list = [part for index, part in enumerate(info_per_weapon_list) if index % 2]
                    print(" ".join(odd_parts_list))
    weapon = "".join(info_per_weapon_list)
    return weapon


info_weapon = input()
ready_weapon = parts_of_weapon(info_weapon)
print(f"You crafted {ready_weapon}!")


# info_per_weapon_list = input().split("|")
# while True:
#     current_command = input()
#     if current_command == "Done":
#         break
#     else:
#         command_list = current_command.split()
#         info = command_list[0]
#         if info == "Add":
#             particle = command_list[1]
#             index = int(command_list[2])
#             if 0 <= index < len(info_per_weapon_list):
#                 info_per_weapon_list.insert(index, particle)
#             else:
#                 continue
#         elif info == "Remove":
#             index = int(command_list[1])
#             if 0 <= index < len(info_per_weapon_list):
#                 del info_per_weapon_list[index]
#             else:
#                 continue
#         elif info == "Check":
#             command = command_list[1]
#             if command == "Even":
#                 even_parts_list = [part for index, part in enumerate(info_per_weapon_list) if index % 2 == 0]
#                 print(" ".join(even_parts_list))
#             elif command == "Odd":
#                 odd_parts_list = [part for index, part in enumerate(info_per_weapon_list) if index % 2]
#                 print(" ".join(odd_parts_list))
# weapon = "".join(info_per_weapon_list)
# print(f"You crafted {weapon}!")
