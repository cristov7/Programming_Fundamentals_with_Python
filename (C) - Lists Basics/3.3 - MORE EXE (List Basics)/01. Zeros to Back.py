single_string_list = list(map(int, input().split(", ")))
count_zeros = single_string_list.count(0)
while 0 in single_string_list:
    single_string_list.remove(0)
for zero in range(1, count_zeros + 1):
    single_string_list.append(0)
print(single_string_list)


# numbers_as_string = input()
# numbers_as_string_in_list = numbers_as_string.split(", ")
# numbers_as_integers_in_list = list()
# for element in numbers_as_string_in_list:
#     current_element = int(element)
#     numbers_as_integers_in_list.append(current_element)
# count_zero = numbers_as_integers_in_list.count(0)
# while 0 in numbers_as_integers_in_list:
#     numbers_as_integers_in_list.remove(0)
# counter = 0
# while counter < count_zero:
#     counter += 1
#     numbers_as_integers_in_list.append(0)
# print(numbers_as_integers_in_list)


# num_list = [int(num) for num in input().split(', ')]
# for idx in range(len(num_list)-1, -1, -1):
#     if num_list[idx] == 0:
#         zero = num_list.pop(idx)
#         num_list.append(zero)
# print(num_list)
