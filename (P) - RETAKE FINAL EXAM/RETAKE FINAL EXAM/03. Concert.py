concert = {}
while True:
    command = input()
    if command == "Start!":
        break
    else:
        command_list = command.split("; ")
        info = command_list[0]
        if info == "Add":
            band_name = command_list[1]
            members = command_list[2]
            list_of_members = members.split(", ")
            unique_list_of_members = []
            for member in list_of_members:
                if member not in unique_list_of_members:
                    unique_list_of_members.append(member)
                else:
                    continue
            if band_name not in concert.keys():
                concert[band_name] = {}
                concert[band_name]["members"] = unique_list_of_members
            else:
                if "members" not in concert[band_name]:
                    concert[band_name]["members"] = unique_list_of_members
                else:
                    current_unique_list_of_members = concert[band_name]["members"]
                    for member in unique_list_of_members:
                        if member not in current_unique_list_of_members:
                            current_unique_list_of_members.append(member)
                        else:
                            continue
                    concert[band_name]["members"] = current_unique_list_of_members
        elif info == "Play":
            band_name = command_list[1]
            play_time = int(command_list[2])
            if band_name not in concert.keys():
                concert[band_name] = {}
                concert[band_name]["time"] = play_time
            else:
                if "time" not in concert[band_name]:
                    concert[band_name]["time"] = play_time
                else:
                    concert[band_name]["time"] += play_time
total_time = 0
for band_name, more_info in concert.items():
    if "members" in more_info and "time" in more_info:
        total_time += concert[band_name]["time"]
    else:
        continue
print(f"Total time: {total_time}")
for band_name, more_info in concert.items():
    if "members" in more_info and "time" in more_info:
        play_time = concert[band_name]["time"]
        print(f"{band_name} -> {play_time}")
    else:
        continue
for band_name, more_info in concert.items():
    if "members" in more_info and "time" in more_info:
        print(band_name)
        members_list = more_info["members"]
        for member in members_list:
            print(f"=> {member}")
        break
    else:
        continue
