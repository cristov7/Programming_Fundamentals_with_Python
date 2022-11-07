phonebook = {}
while True:
    info = input()
    if info.isdigit():
        number = int(info)
        for information in range(1, number + 1):
            name = input()
            if name in phonebook:   # if name in phonebook.keys():
                number = phonebook[name]
                print(f"{name} -> {number}")
            else:
                print(f"Contact {name} does not exist.")
        break
    else:
        current_name, current_number = info.split("-")
        phonebook[current_name] = current_number
        # info_list = info.split("-")
        # current_name = info_list[0]
        # current_number = info_list[1]
        # if current_name not in phonebook:
        #     phonebook[current_name] = current_number
        # else:
        #     phonebook[current_name] = current_number


# phonebook = {}
# while True:
#     entry = input()
#     if "-" not in entry:
#         break
#     name, phone = entry.split("-")
#     phonebook[name] = phone
# for check in range(int(entry)):
#     searched_name = input()
#     if searched_name in phonebook.keys():
#         print(f"{searched_name} -> {phonebook[searched_name]}")
#     else:
#         print(f"Contact {searched_name} does not exist.")
