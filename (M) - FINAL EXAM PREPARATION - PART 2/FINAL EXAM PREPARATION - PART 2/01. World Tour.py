world_tour = input()
while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {world_tour}")
        break
    else:
        command_list = command.split(":")
        info = command_list[0]
        if info == "Add Stop":
            index = int(command_list[1])
            destination = command_list[2]
            if 0 <= index < len(world_tour):
                left_part = world_tour[:index]
                right_part = world_tour[index:]
                world_tour = left_part + destination + right_part
                print(world_tour)
            else:
                print(world_tour)
        elif info == "Remove Stop":
            start_index = int(command_list[1])
            end_index = int(command_list[2])
            if 0 <= start_index <= end_index < len(world_tour):
                remove_part = world_tour[start_index:end_index + 1]
                world_tour = world_tour.replace(remove_part, "")
                print(world_tour)
            else:
                print(world_tour)
        elif info == "Switch":
            old_destination = command_list[1]
            new_destination = command_list[2]
            if old_destination in world_tour:
                world_tour = world_tour.replace(old_destination, new_destination, 1)
                print(world_tour)
            else:
                print(world_tour)
