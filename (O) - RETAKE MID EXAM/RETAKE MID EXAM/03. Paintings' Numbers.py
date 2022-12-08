collection_of_numbers_list = input().split()
while True:
    command = input()
    if command == "END":
        break
    else:
        command_list = command.split()
        info = command_list[0]
        if info == "Change":
            painting_number = command_list[1]
            new_number = command_list[2]
            if painting_number in collection_of_numbers_list:
                index_per_painting_number = collection_of_numbers_list.index(painting_number)
                collection_of_numbers_list[index_per_painting_number] = new_number
            else:
                continue
        elif info == "Hide":
            painting_number = command_list[1]
            if painting_number in collection_of_numbers_list:
                collection_of_numbers_list.remove(painting_number)
            else:
                continue
        elif info == "Switch":
            first_painting_number = command_list[1]
            second_painting_number = command_list[2]
            if first_painting_number in collection_of_numbers_list and \
                    second_painting_number in collection_of_numbers_list:
                first_index = collection_of_numbers_list.index(first_painting_number)
                second_index = collection_of_numbers_list.index(second_painting_number)
                collection_of_numbers_list[first_index], collection_of_numbers_list[second_index] = \
                    collection_of_numbers_list[second_index], collection_of_numbers_list[first_index]
            else:
                continue
        elif info == "Insert":
            index = int(command_list[1]) + 1
            painting_number = command_list[2]
            if 0 <= index < len(collection_of_numbers_list):
                collection_of_numbers_list.insert(index, painting_number)
            else:
                continue
        elif info == "Reverse":
            collection_of_numbers_list.reverse()
numbers_as_string = " ".join(collection_of_numbers_list)
print(numbers_as_string)
