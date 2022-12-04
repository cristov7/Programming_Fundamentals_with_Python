deciphered_magic = input()
while True:
    command = input()
    if command == "Abracadabra":
        break
    elif command == "Abjuration":
        deciphered_magic = deciphered_magic.upper()
        print(deciphered_magic)
    elif command == "Necromancy":
        deciphered_magic = deciphered_magic.lower()
        print(deciphered_magic)
    else:
        command_list = command.split()
        info = command_list[0]
        if info == "Illusion":
            index = int(command_list[1])
            letter = command_list[2]
            if 0 <= index < len(deciphered_magic):
                first_part = deciphered_magic[:index]
                last_part = deciphered_magic[index + 1:]
                deciphered_magic = first_part + letter + last_part
                print("Done!")
            else:
                print("The spell was too weak.")
        elif info == "Divination":
            first_substring = command_list[1]
            second_substring = command_list[2]
            if first_substring in deciphered_magic:
                while first_substring in deciphered_magic:
                    deciphered_magic = deciphered_magic.replace(first_substring, second_substring)
                print(deciphered_magic)
            else:
                continue
        elif info == "Alteration":
            substring = command_list[1]
            if substring in deciphered_magic:
                while substring in deciphered_magic:
                    deciphered_magic = deciphered_magic.replace(substring, "")
                print(deciphered_magic)
            else:
                print("The spell did not work!")
        else:
            print("The spell did not work!")
