import re
regex = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"
all_full_names = input()
filtered_names_list = re.findall(regex, all_full_names)
print(*filtered_names_list, sep=" ")


# full_names_list = input().split(", ")
# for name_and_family_name in full_names_list:
#     name = ""
#     white_space = 0
#     family_name = ""
#     for char in name_and_family_name:
#         if char == " ":
#             white_space += 1
#         elif white_space == 0 and char.isalpha():
#             name += char
#         elif white_space == 1 and char.isalpha():
#             family_name += char
#         else:
#             break
#     if len(name) >= 2 and len(family_name) >= 2:
#         first_letter_in_name = name[0]
#         first_letter_in_family_name = family_name[0]
#         if first_letter_in_name.isupper() and first_letter_in_family_name.isupper():
#             rest_letters_in_name = name[1:]
#             rest_letters_in_family_name = family_name[1:]
#             if rest_letters_in_name.islower() and rest_letters_in_family_name.islower():
#                 print(name_and_family_name, end=" ")
#             else:
#                 continue
#         else:
#             continue
#     else:
#         continue
