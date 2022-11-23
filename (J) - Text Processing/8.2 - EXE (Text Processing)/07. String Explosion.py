some_string = input()
power_of_explosion = 0
new_string_list = list()
for index, char in enumerate(some_string):
    if char == ">":
        new_string_list.append(char)
        explosion = int(some_string[index + 1])
        power_of_explosion += explosion
    elif power_of_explosion > 0 and char != ">":
        power_of_explosion -= 1
    else:
        new_string_list.append(char)
new_string = "".join(new_string_list)
print(new_string)


# some_text = input()
# new_text = ""
# strength = 0
# for index in range(len(some_text)):
#     if some_text[index] == ">":
#         new_text += some_text[index]
#         strength += int(some_text[index + 1])
#     elif strength > 0 and some_text[index] != ">":
#         strength -= 1
#     else:
#         new_text += some_text[index]
# print(new_text)


# text = input()
# first_part_of_final_text = ""
# last_part = ""
# first_part_operations = True
# for symbol in text:
#     if first_part_operations:
#         if symbol == ">":
#             last_part += symbol
#             first_part_operations = False
#         else:
#             first_part_of_final_text += symbol
#     else:
#         last_part += symbol
# final_part_of_final_text = ""
# power_of_explosion = 0
# for char in last_part:
#     if char == ">":
#         final_part_of_final_text += char
#     else:
#         if char.isdigit():
#             power_of_explosion += int(char)
#             power_of_explosion -= 1
#         else:
#             if power_of_explosion > 0:
#                 power_of_explosion -= 1
#             else:
#                 final_part_of_final_text += char
# final_text = first_part_of_final_text + final_part_of_final_text
# print(final_text)
