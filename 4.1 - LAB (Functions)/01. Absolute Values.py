numbers_as_string = input()
numbers_as_string_in_list = numbers_as_string.split()   # .split(" ")
numbers_as_float_in_list = []
for element in numbers_as_string_in_list:
    current_element = float(element)
    numbers_as_float_in_list.append(current_element)
absolute_numbers_as_float_in_list = []
for number in numbers_as_float_in_list:
    current_absolute_number = abs(number)
    absolute_numbers_as_float_in_list.append(current_absolute_number)
print(absolute_numbers_as_float_in_list)


# numbers = input().split()
# abs_numbers = []
# for num in numbers:
#     abs_numbers.append(abs(float(num)))
# print(abs_numbers)


# numbers = list(map(float, input().split()))
# result = [abs(num) for num in numbers]
# print(result)
