numbers_list = list(map(int, input().split()))
while True:
    command = input()
    if command == "End":
        break
    else:
        command_list = command.split()
        info = command_list[0]
        if info == "Shoot":
            index = int(command_list[1])
            power = int(command_list[2])
            if 0 <= index <= len(numbers_list) - 1:
                numbers_list[index] -= power
                if numbers_list[index] <= 0:
                    pop = numbers_list.pop(index)
                else:
                    continue
            else:
                continue
        elif info == "Add":
            index = int(command_list[1])
            value = int(command_list[2])
            if 0 <= index <= len(numbers_list) - 1:
                numbers_list.insert(index, value)
            else:
                print("Invalid placement!")
                continue
        elif info == "Strike":
            index = int(command_list[1])
            radius = int(command_list[2])
            if 0 <= index - radius <= len(numbers_list) - 1 and 0 <= index + radius <= len(numbers_list) - 1:
                values_to_remove = []
                for idx, value in enumerate(numbers_list):
                    if index - radius <= idx <= index + radius:
                        values_to_remove.append(value)
                    else:
                        continue
                for element in values_to_remove:
                    if element in numbers_list:
                        numbers_list.remove(element)
                    else:
                        continue
            else:
                print("Strike missed!")
                continue
numbers_list_as_strings = list(map(str, numbers_list))
print("|".join(numbers_list_as_strings))


# def shoot_func(index, power, targets):
#     if 0 <= index < len(targets):
#         if targets[index] - power <= 0:
#             targets.pop(index)
#         else:
#             targets[index] -= power
#     return targets
# 
# 
# def add_func(index, value, targets):
#     if 0 <= index < len(targets):
#         targets.insert(index, value)
#     else:
#         print("Invalid placement!")
#     return targets
# 
# 
# def strike_func(index, radius, targets):
#     validator_index = index - radius >= 0 and index + radius < len(targets)
#     if validator_index:
#         start_target_index = index - radius
#         final_target_index = index + radius
#         targets = [targets[i] for i in range(len(targets)) if i < start_target_index or i > final_target_index]
#     else:
#         print("Strike missed!")
#     return targets
# 
# 
# def moving_target(targets):
#     while True:
#         command = input()
#         if command == "End":
#             break
#         current_command, first_element, second_element = command.split()
#         if current_command == "Shoot":
#             targets = shoot_func(int(first_element), int(second_element), targets)
#         elif current_command == "Add":
#             targets = add_func(int(first_element), int(second_element), targets)
#         elif current_command == "Strike":
#             targets = strike_func(int(first_element), int(second_element), targets)
#     result = "|".join([str(num) for num in targets])
#     print(result)
# 
# 
# data = list(map(int, input().split()))
# moving_target(data)
