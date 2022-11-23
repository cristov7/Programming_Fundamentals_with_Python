key_list = [int(key) for key in input().split()]
while True:
    command = input()
    if command == "find":
        break
    else:
        text = ""
        index = 0
        for char in command:
            char_ord = ord(char)
            current_value = char_ord - key_list[index]
            text += chr(current_value)
            index += 1
            if index >= len(key_list):
                index = 0
            else:
                continue
        indexes_type_treasure = [index for index, value in enumerate(text) if value == "&"]
        start_index_type = indexes_type_treasure[0]
        end_index_type = indexes_type_treasure[1]
        start_coordinate = 0
        end_coordinate = 0
        for current_index, current_value in enumerate(text):
            if current_value == "<":
                start_coordinate = current_index
            elif current_value == ">":
                end_coordinate = current_index
            else:
                continue
        type_treasure = text[start_index_type + 1: end_index_type]
        treasure_coordinates = text[start_coordinate + 1: end_coordinate]
        print(f"Found {type_treasure} at {treasure_coordinates}")
