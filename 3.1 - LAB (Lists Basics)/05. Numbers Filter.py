# my_list =[]
# my_final_list = []
# number = int(input())
# for numbers in range(1, number + 1):
#     current_number = int(input())
#     my_list.append(current_number)
# command = input()
# if command == "even":
#     for even_numbers in my_list:
#         if even_numbers % 2 == 0:
#             my_final_list.append(even_numbers)
# elif command == "odd":
#     for odd_numbers in my_list:
#         if odd_numbers % 2 != 0:
#             my_final_list.append(odd_numbers)
# elif command == "negative":
#     for negative_numbers in my_list:
#         if negative_numbers < 0:
#             my_final_list.append(negative_numbers)
# elif command == "positive":
#     for positive_numbers in my_list:
#         if positive_numbers >= 0:
#             my_final_list.append(positive_numbers)
# print(my_final_list)


number = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"
my_list = []
for numbers in range(1, number + 1):
    current_number = int(input())
    my_list.append(current_number)
command = input()
my_filtered_list = []
for filtered_numbers in my_list:
    filtered_passes = (
            (command == COMMAND_EVEN and filtered_numbers % 2 == 0) or
            (command == COMMAND_ODD and filtered_numbers % 2 != 0) or
            (command == COMMAND_NEGATIVE and filtered_numbers < 0) or
            (command == COMMAND_POSITIVE and filtered_numbers >= 0)
    )
    if filtered_passes:
        my_filtered_list.append(filtered_numbers)
print(my_filtered_list)
