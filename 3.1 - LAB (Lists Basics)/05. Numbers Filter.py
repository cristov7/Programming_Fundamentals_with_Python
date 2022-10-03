some_list = []
printed_list = []
number = int(input())
for integer_numbers in range(1, number + 1):
    current_int_number = int(input())
    some_list.append(current_int_number)
command = input()
if command == "even":
    for element in some_list:
        if element % 2 == 0:
            printed_list.append(element)
        else:
            continue
elif command == "odd":
    for element in some_list:
        if element % 2 != 0:
            printed_list.append(element)
        else:
            continue
elif command == "negative":
    for element in some_list:
        if element < 0:
            printed_list.append(element)
        else:
            continue
elif command == "positive":
    for element in some_list:
        if element >= 0:
            printed_list.append(element)
        else:
            continue
print(printed_list)


# number = int(input())
# COMMAND_EVEN = "even"
# COMMAND_ODD = "odd"
# COMMAND_NEGATIVE = "negative"
# COMMAND_POSITIVE = "positive"
# my_list = []
# for numbers in range(1, number + 1):
#     current_number = int(input())
#     my_list.append(current_number)
# command = input()
# my_filtered_list = []
# for filtered_numbers in my_list:
#     filtered_passes = (
#             (command == COMMAND_EVEN and filtered_numbers % 2 == 0) or
#             (command == COMMAND_ODD and filtered_numbers % 2 != 0) or
#             (command == COMMAND_NEGATIVE and filtered_numbers < 0) or
#             (command == COMMAND_POSITIVE and filtered_numbers >= 0)
#     )
#     if filtered_passes:
#         my_filtered_list.append(filtered_numbers)
# print(my_filtered_list)
