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
