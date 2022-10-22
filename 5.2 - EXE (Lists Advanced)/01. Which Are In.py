first_string_in_list = input().split(", ")
second_string_in_list = input().split(", ")
substrings_list = []
for current_element in first_string_in_list:
    for element in second_string_in_list:
        if current_element in element:
            substrings_list.append(current_element)
            break
        else:
            continue
print(substrings_list)


# first_string_in_list = input().split(", ")
# second_string_in_list = input().split(", ")
# substrings_list = []
# for current_element in first_string_in_list:
#     for element in second_string_in_list:
#         if current_element in element and not current_element in substrings_list:
#             substrings_list.append(current_element)
#         else:
#             continue
# print(substrings_list)


# first_string_in_list = input().split(", ")
# second_string_in_list = input().split(", ")
# substrings_list = [current_element for current_element in first_string_in_list
#                    if any(current_element in element for element in second_string_in_list)]
# print(substrings_list)
