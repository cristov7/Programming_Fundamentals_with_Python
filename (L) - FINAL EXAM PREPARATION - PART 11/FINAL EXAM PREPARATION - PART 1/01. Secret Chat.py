concealed_message = input()
while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {concealed_message}")
        break
    else:
        command_list = command.split(":|:")
        info = command_list[0]
        if info == "InsertSpace":
            index = int(command_list[1])
            left_part = concealed_message[:index]
            middle_part = " "
            right_part = concealed_message[index:]
            concealed_message = left_part + middle_part + right_part
        elif info == "Reverse":
            substring = command_list[1]
            if substring in concealed_message:
                concealed_message = concealed_message.replace(substring, "", 1)
                reverse_substring = substring[::-1]
                concealed_message += reverse_substring
            else:
                print("error")
                continue
        elif info == "ChangeAll":
            substring = command_list[1]
            replacement = command_list[2]
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
