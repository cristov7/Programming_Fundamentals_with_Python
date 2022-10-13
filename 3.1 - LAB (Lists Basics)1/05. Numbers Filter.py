lst_numbers = list()
count_number = int(input())
for number in range(1, count_number + 1):
    current_number = int(input())
    lst_numbers.append(current_number)
command = input()
lst_update = []
if command == "even":   # 0 се счита за положително и четно
    for element in lst_numbers:
        if element % 2 == 0:
            lst_update.append(element)
        else:
            continue
elif command == "odd":
    for element in lst_numbers:
        if element % 2 != 0:
            lst_update.append(element)
        else:
            continue
elif command == "negative":
    for element in lst_numbers:
        if element < 0:
            lst_update.append(element)
        else:
            continue
elif command == "positive":   # 0 се счита за положително и четно
    for element in lst_numbers:
        if element >= 0:
            lst_update.append(element)
        else:
            continue
print(lst_update)


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
