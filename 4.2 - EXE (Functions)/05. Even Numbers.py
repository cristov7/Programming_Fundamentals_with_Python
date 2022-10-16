numbers_in_list = list(map(int, input().split()))   # .split(" ")
even_numbers = filter(lambda x: x % 2 == 0, numbers_in_list)
print(list(even_numbers))


# def even_numbers(numbers: str):
#     numbers_as_string_in_list = numbers.split(" ")  # .split()
#     even_numbers_list = []
#     for number in numbers_as_string_in_list:
#         current_number = int(number)
#         if current_number % 2 == 0:
#             even_numbers_list.append(current_number)
#         else:
#             continue
#     return even_numbers_list
#
#
# numbers_as_string = input()
# print(even_numbers(numbers_as_string))


# numbers_in_list = list(map(int, input().split(" ")))
# even_list = []
# for number in numbers_in_list:
#     if number % 2 == 0:
#         even_list.append(number)
#     else:
#         continue
# print(even_list)


# numbers = list(map(int, input().split()))
# even = list(filter(lambda x: x % 2 == 0, numbers))
# print(even)
