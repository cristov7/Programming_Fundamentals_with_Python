dwarfs = {}
input_line = input()
while input_line != "Once upon a time":
    dwarf_info = input_line.split(" <:> ")
    dwarf_name, dwarf_hat_color, dwarf_physics = dwarf_info[0], dwarf_info[1], int(dwarf_info[2])
    if dwarf_hat_color not in dwarfs:
        dwarfs[dwarf_hat_color] = {}
    else:
        if dwarf_name not in dwarfs[dwarf_hat_color]:
            dwarfs[dwarf_hat_color][dwarf_name] = 0
        else:
            if dwarf_physics < dwarfs[dwarf_hat_color][dwarf_name]:
                dwarf_physics = dwarfs[dwarf_hat_color][dwarf_name]
    dwarfs[dwarf_hat_color][dwarf_name] = dwarf_physics
    input_line = input()
dwarfs_dict = {}
for hat_color, members in dwarfs.items():
    hat_length = len(members)
    for dwarf, physics in members.items():
        dwarf_name_color = f"{dwarf}|{hat_color}"
        dwarfs_dict[dwarf_name_color] = {"name": dwarf, "physics": physics, "members": hat_length, "hat_color": hat_color}
for item in sorted(dwarfs_dict, key=lambda k: (dwarfs_dict[k]['physics'], dwarfs_dict[k]['members']), reverse=True):
    current_dwarf = dwarfs_dict[item]
    print(f"({current_dwarf['hat_color']}) {current_dwarf['name']} <-> {current_dwarf['physics']}")


# snow_white_dwarfs = {}
# while True:
#     command = input()
#     if command == "Once upon a time":
#         break
#     else:
#         command_list = command.split(" <:> ")
#         dwarf_name = command_list[0]
#         dwarf_hat_color = command_list[1]
#         dwarf_physics = int(command_list[2])
#         dwarf = f"({dwarf_hat_color}) {dwarf_name}"
#         if dwarf not in snow_white_dwarfs:
#             snow_white_dwarfs[dwarf] = dwarf_physics
#         else:
#             if dwarf_physics > snow_white_dwarfs[dwarf]:
#                 snow_white_dwarfs[dwarf] = dwarf_physics
#             else:
#                 continue
# info_sorted_names = sorted(snow_white_dwarfs.items(), key=lambda x: x[0])
# info_sorted_physics = sorted(info_sorted_names, key=lambda x: x[1], reverse=True)
# for current_dwarf, current_physics in info_sorted_physics:
#     print(f"{current_dwarf} <-> {current_physics}")
