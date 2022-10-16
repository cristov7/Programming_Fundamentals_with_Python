def the_smallest_number(add_numbers_list):
    return min(add_numbers_list)


numbers_list = list()
for number in range(1, 4, 1):
    current_number = int(input())
    numbers_list.append(current_number)
min_number = the_smallest_number(numbers_list)
print(min_number)


# def the_smallest_number():
#     first_number = int(input())
#     second_number = int(input())
#     third_number = int(input())
#     all_numbers = [first_number, second_number, third_number]
#     min_number = min(all_numbers)
#     return min_number
#
#
# print(the_smallest_number())


# def smallest_number(numbers):
#     return min(numbers)
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# all_numbers = [first_number, second_number, third_number]
# min_number = smallest_number(all_numbers)
# print(min_number)


# numbers_list = []
# for int_num in range(1, 4, 1):
#     current_number = int(input())
#     numbers_list.append(current_number)
# print(min(numbers_list))
