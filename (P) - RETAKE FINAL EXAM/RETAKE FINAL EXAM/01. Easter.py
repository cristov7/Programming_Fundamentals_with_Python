word = input()
while True:
    command = input()
    if command == "Easter":
        break
    else:
        command_list = command.split()
        info = command_list[0]
        if info == "Replace":
            current_char = command_list[1]
            new_char = command_list[2]
            word = word.replace(current_char, new_char)
            print(word)
        elif info == "Remove":
            substring = command_list[1]
            word = word.replace(substring, "")
            print(word)
        elif info == "Includes":
            string = command_list[1]
            if string in word:
                print("True")
            else:
                print("False")
        elif info == "Change":
            change_info = command_list[1]
            if change_info == "Upper":
                word = word.upper()
            else:
                word = word.lower()
            print(word)
        elif info == "Reverse":
            start_index = int(command_list[1])
            end_index = int(command_list[2])
            if 0 <= start_index < end_index < len(word):
                filter_word = word[start_index: end_index + 1]
                reverse_word = filter_word[::-1]
                print(reverse_word)
            else:
                continue
