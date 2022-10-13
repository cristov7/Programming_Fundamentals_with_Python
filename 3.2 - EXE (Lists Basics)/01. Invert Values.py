numbers_as_string = input()
numbers_as_string_in_list = numbers_as_string.split(" ")
invert_values_list = []
for element in numbers_as_string_in_list:
    current_element = int(element) * (-1)
    invert_values_list.append(current_element)
print(invert_values_list)


# numbers_in_string = input()
# my_numbers_list = numbers_in_string.split(" ")   # my_numbers_list = numbers_in_string.split()
# my_opposite_list = []
# for element in my_numbers_list:
#     current_element = -int(element)
#     my_opposite_list.append(current_element)
# print(my_opposite_list)


# string_of_numbers = input()
# my_list = string_of_numbers.split()
# my_opposite_numbers_list = []
# for element in my_list:
#     current_element = int(element) * (-1)   # current_element = -int(element)
#     my_opposite_numbers_list.append(current_element)
# print(my_opposite_numbers_list)


# string_of_numbers = input().split()
# my_opposite_numbers_list = []
# for element in string_of_numbers:
#     my_opposite_numbers_list.append(-int(element))
# print(my_opposite_numbers_list)
