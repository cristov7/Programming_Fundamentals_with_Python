numbers_list = list(map(int, input().split(", ")))
update_list = [index for index, value in enumerate(numbers_list) if value % 2 == 0]
print(update_list)


# numbers_list = list(map(int, input().split(", ")))
# update_list = list(map(lambda x: x % 2 == 0, numbers_list))
# final_list = [index for index, value in enumerate(update_list) if value]
# print(final_list)


# numbers = list(map(int, input().split(", ")))
# indices = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
# print(indices)
