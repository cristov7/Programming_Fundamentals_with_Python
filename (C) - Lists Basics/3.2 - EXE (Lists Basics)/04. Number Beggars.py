items_list = list(map(int, input().split(", ")))
beggars_list = [0 for beggar in range(int(input()))]
if len(items_list) == len(beggars_list):
    for index in range(len(items_list)):
        beggars_list[index] += items_list[index]
elif len(items_list) < len(beggars_list):
    for index, item in enumerate(items_list):
        beggars_list[index] += item
elif len(items_list) > len(beggars_list):
    for index_beggar, current_beggar in enumerate(beggars_list):
        for index_item in range(index_beggar, len(items_list), len(beggars_list)):
            beggars_list[index_beggar] += items_list[index_item]
print(beggars_list)


# numbers_as_string = input()
# count_beggars = int(input())
# numbers_as_string_in_list = numbers_as_string.split(", ")
# numbers_as_integer_in_list = list()
# for element in numbers_as_string_in_list:
#     current_element = int(element)
#     numbers_as_integer_in_list.append(current_element)
# sum_per_beggar_in_list = []
# for beggar in range(count_beggars):
#     index = beggar
#     sum_per_beggar = 0
#     for takes in range(len(numbers_as_integer_in_list)):
#         if index < len(numbers_as_integer_in_list):
#             current_take = numbers_as_integer_in_list[index]
#             sum_per_beggar += current_take
#             index += count_beggars
#         else:
#             break
#     sum_per_beggar_in_list.append(sum_per_beggar)
# print(sum_per_beggar_in_list)


# takes_as_strings = input()
# count_beggars = int(input())
# takes_as_strings_in_list = takes_as_strings.split(", ")
# takes_as_integers_in_list = []
# for takes in takes_as_strings_in_list:
#     current_take = int(takes)
#     takes_as_integers_in_list.append(current_take)
# final_takes_per_every_beggar_in_list = []
# starting_index_per_takes = 0
# while starting_index_per_takes < count_beggars:
#     takes_per_current_beggar = 0
#     for current_takes in range(starting_index_per_takes, len(takes_as_integers_in_list), count_beggars):
#         takes_per_current_beggar += takes_as_integers_in_list[current_takes]
#     final_takes_per_every_beggar_in_list.append(takes_per_current_beggar)
#     starting_index_per_takes += 1
# print(final_takes_per_every_beggar_in_list)
