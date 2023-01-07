numbers = [int(integer) for integer in input().split()]
command = input().split()
while command[0] != "end":
    even_numbers = [even for even in numbers if even % 2 == 0]
    odd_numbers = [odd for odd in numbers if odd % 2 != 0]
    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print(f'Invalid index')
    elif command[0] == "max":
        if command[1] == "even" and even_numbers:
            print((len(numbers) - numbers[::-1].index(max(even_numbers)) - 1))
        elif command[1] == "odd" and odd_numbers:
            print((len(numbers) - numbers[::-1].index(max(odd_numbers)) - 1))
        else:
            print('No matches')
    elif command[0] == "min":
        if command[1] == "even" and even_numbers:
            print((len(numbers) - numbers[::-1].index(min(even_numbers)) - 1))
        elif command[1] == "odd" and odd_numbers:
            print((len(numbers) - numbers[::-1].index(min(odd_numbers)) - 1))
        else:
            print('No matches')
    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even_numbers[0:int(command[1])])
            else:
                print(odd_numbers[0:int(command[1])])
        else:
            print(f"Invalid count")
    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even_numbers[-int(command[1]):])
            else:
                print(odd_numbers[-int(command[1]):])
        else:
            print(f"Invalid count")
    command = input().split()
print(numbers)


# numbers_List = list(map(int, input().split()))
# while True:
#     command = input()
#     if command == "end":
#         break
#     else:
#         command_list = command.split()
#         info = command_list[0]
#         if info == "exchange":
#             index = int(command_list[1])
#             if 0 <= index < len(numbers_List):
#                 end_part_list = numbers_List[:index + 1]
#                 first_part_list = numbers_List[index + 1:]
#                 numbers_List = first_part_list + end_part_list
#             else:
#                 print("Invalid index")
#         elif info == "max":
#             more_info = command_list[1]
#             if more_info == "even":
#                 if len(numbers_List) > 1:
#                     max_number = ""
#                     max_index = ""
#                     for index, number in enumerate(numbers_List):
#                         if number % 2 == 0:
#                             if max_number == "":
#                                 max_number = number
#                                 max_index = index
#                             elif number >= max_number:
#                                 max_number = number
#                                 max_index = index
#                         else:
#                             continue
#                     if max_index == "":
#                         print("No matches")
#                     else:
#                         print(max_index)
#                 else:
#                     print("No matches")
#             elif more_info == "odd":
#                 if len(numbers_List) > 0:
#                     max_number = ""
#                     max_index = ""
#                     for index, number in enumerate(numbers_List):
#                         if number % 2:
#                             if max_number == "":
#                                 max_number = number
#                                 max_index = index
#                             elif number >= max_number:
#                                 max_number = number
#                                 max_index = index
#                         else:
#                             continue
#                     if max_index == "":
#                         print("No matches")
#                     else:
#                         print(max_index)
#                 else:
#                     print("No matches")
#         elif info == "min":
#             more_info = command_list[1]
#             if more_info == "even":
#                 if len(numbers_List) > 1:
#                     min_number = ""
#                     max_index = ""
#                     for index, number in enumerate(numbers_List):
#                         if number % 2 == 0:
#                             if min_number == "":
#                                 min_number = number
#                                 max_index = index
#                             elif number <= min_number:
#                                 min_number = number
#                                 max_index = index
#                         else:
#                             continue
#                     if max_index == "":
#                         print("No matches")
#                     else:
#                         print(max_index)
#                 else:
#                     print("No matches")
#             elif more_info == "odd":
#                 if len(numbers_List) > 0:
#                     min_number = ""
#                     max_index = ""
#                     for index, number in enumerate(numbers_List):
#                         if number % 2:
#                             if min_number == "":
#                                 min_number = number
#                                 max_index = index
#                             elif number <= min_number:
#                                 min_number = number
#                                 max_index = index
#                         else:
#                             continue
#                     if max_index == "":
#                         print("No matches")
#                     else:
#                         print(max_index)
#                 else:
#                     print("No matches")

#         elif info == "first":
#             count = int(command_list[1])
#             more_info = command_list[2]
#             if more_info == "even":
#                 if count > len(numbers_List):
#                     print("Invalid count")
#                 else:
#                     even_list = [number for number in numbers_List if number % 2 == 0]
#                     if len(even_list) >= count:
#                         first_count_even_list = []
#                         for number in even_list:
#                             first_count_even_list.append(number)
#                             if len(first_count_even_list) == count:
#                                 break
#                             else:
#                                 continue
#                         print(first_count_even_list)
#                     else:
#                         print(even_list)

#             elif more_info == "odd":
#                 if count > len(numbers_List):
#                     print("Invalid count")
#                 else:
#                     odd_list = [number for number in numbers_List if number % 2]
#                     if len(odd_list) >= count:
#                         first_count_odd_list = []
#                         for number in odd_list:
#                             first_count_odd_list.append(number)
#                             if len(first_count_odd_list) == count:
#                                 break
#                             else:
#                                 continue
#                         print(first_count_odd_list)
#                     else:
#                         print(odd_list)

#         elif info == "last":
#             count = int(command_list[1])
#             more_info = command_list[2]
#             if more_info == "even":
#                 if count > len(numbers_List):
#                     print("Invalid count")
#                 else:
#                     even_list = [number for number in numbers_List if number % 2 == 0]
#                     if len(even_list) == 0:
#                         print("[]")
#                     else:
#                         start_index = count * (-1)
#                         last_count_even_list = even_list[start_index:]
#                         print(last_count_even_list)

#             elif more_info == "odd":
#                 if count > len(numbers_List):
#                     print("Invalid count")
#                 else:
#                     odd_list = [number for number in numbers_List if number % 2]
#                     if len(odd_list) == 0:
#                         print("[]")
#                     else:
#                         start_index = count * (-1)
#                         last_count_odd_list = odd_list[start_index:]
#                         print(last_count_odd_list)
# print(numbers_List)
