strings_list = input().split()
first_string = strings_list[0]
second_string = strings_list[1]
total_sum = 0
if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(first_string) < len(second_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else:
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)


# two_strings = input().split()
# first_string = two_strings[0]
# second_string = two_strings[1]
# length_of_first_string = len(first_string)
# length_of_second_string = len(second_string)
# ascii_values_per_first_string = []
# ascii_values_per_second_string = []
# for char in first_string:
#     current_char = ord(char)
#     ascii_values_per_first_string.append(current_char)
# for char in second_string:
#     current_char = ord(char)
#     ascii_values_per_second_string.append(current_char)
# total_sum = 0
# if length_of_first_string > length_of_second_string:
#     for index in range(length_of_second_string):
#         total_sum += ascii_values_per_first_string[index] * ascii_values_per_second_string[index]
#     for index in range(length_of_second_string, length_of_first_string):
#         total_sum += ascii_values_per_first_string[index]
# elif length_of_first_string < length_of_second_string:
#     for index in range(length_of_first_string):
#         total_sum += ascii_values_per_first_string[index] * ascii_values_per_second_string[index]
#     for index in range(length_of_first_string, length_of_second_string):
#         total_sum += ascii_values_per_second_string[index]
# else:   # elif length_of_first_string == length_of_second_string:
#     for index in range(length_of_first_string):   # for index in range(length_of_second_string):
#         total_sum += ascii_values_per_first_string[index] * ascii_values_per_second_string[index]
# print(total_sum)


# two_strings = input().split()
# first_string = two_strings[0]
# second_string = two_strings[1]
# total_sum = 0
# if len(first_string) > len(second_string):
#     for index in range(len(second_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
#     for index in range(len(second_string), len(first_string)):
#         total_sum += ord(first_string[index])
# elif len(first_string) < len(second_string):
#     for index in range(len(first_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
#     for index in range(len(first_string), len(second_string)):
#         total_sum += ord(second_string[index])
# else:   # elif len(first_string) == len(second_string):
#     for index in range(len(first_string)):   # for index in range(len(second_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
# print(total_sum)
