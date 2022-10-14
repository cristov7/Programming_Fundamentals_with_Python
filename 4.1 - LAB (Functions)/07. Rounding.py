numbers_as_string = input()
numbers_as_string_in_list = numbers_as_string.split()   # .split(" ")
numbers_as_float_in_list = []
for element in numbers_as_string_in_list:
    current_element = float(element)
    numbers_as_float_in_list.append(current_element)
round_numbers_as_float_in_list = []
for number in numbers_as_float_in_list:
    current_number = round(number)
    round_numbers_as_float_in_list.append(current_number)
print(round_numbers_as_float_in_list)


# numbers_as_string_in_list = input().split(" ")   # .split()
# round_numbers_in_list = []
# for element in numbers_as_string_in_list:
#     current_element = float(element)
#     round_number = round(current_element)
#     round_numbers_in_list.append(round_number)
# print(round_numbers_in_list)


# result = list(map(lambda x: round(float(x)), input().split(" ")))
# print(result)


# input_numbers = list(map(float, input().split()))
# print([round(number) for number in input_numbers])
