phonebook = {}
while True:
    info = input()
    if info.isdigit():
        number = int(info)
        for people in range(1, number + 1):
            contact = input()
            if contact in phonebook:
                phone_number = phonebook[contact]
                print(f"{contact} -> {phone_number}")
            else:
                print(f"Contact {contact} does not exist.")
        break
    else:
        name_and_phone_number = info.split("-")
        name = name_and_phone_number[0]
        phone_number = name_and_phone_number[1]
        if name not in phonebook:
            phonebook[name] = phone_number
        else:
            phonebook[name] = phone_number


# phonebook = {}
# while True:
#     info = input()
#     if info.isdigit():
#         number = int(info)
#         for information in range(1, number + 1):
#             name = input()
#             if name in phonebook:   # if name in phonebook.keys():
#                 number = phonebook[name]
#                 print(f"{name} -> {number}")
#             else:
#                 print(f"Contact {name} does not exist.")
#         break
#     else:
#         current_name, current_number = info.split("-")
#         phonebook[current_name] = current_number
#         # info_list = info.split("-")
#         # current_name = info_list[0]
#         # current_number = info_list[1]
#         # if current_name not in phonebook:
#         #     phonebook[current_name] = current_number
#         # else:
#         #     phonebook[current_name] = current_number


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
