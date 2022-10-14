numbers_as_string_in_list = input().split(" ")   # .split()
numbers_as_integer_in_list = list()
for string_element in numbers_as_string_in_list:
    current_string = int(string_element)
    numbers_as_integer_in_list.append(current_string)
count_numbers_to_remove = int(input())
for numbers_to_remove in range(1, count_numbers_to_remove + 1):
    numbers_as_integer_in_list.remove(min(numbers_as_integer_in_list))
final_list = []
for integer_element in numbers_as_integer_in_list:
    current_integer = str(integer_element)
    final_list.append(current_integer)
print(", ".join(final_list))


# numbers_as_string = input()
# numbers_as_string_in_list = numbers_as_string.split()   # .split(" ")
# count_numbers_to_remove = int(input())
# numbers_as_integers_in_list = []
# for element in numbers_as_string_in_list:
#     current_element = int(element)
#     numbers_as_integers_in_list.append(current_element)
# counter_to_remove = 0
# while True:
#     counter_to_remove += 1
#     if counter_to_remove <= count_numbers_to_remove:
#         numbers_as_integers_in_list.remove(min(numbers_as_integers_in_list))
#     else:
#         break
# update_numbers_as_string_in_list = []
# for element in numbers_as_integers_in_list:
#     current_element = str(element)
#     update_numbers_as_string_in_list.append(current_element)
# print(", ".join(update_numbers_as_string_in_list))
