numbers_list = [int(number) for number in input().split(", ")]
check_list = list()
for number_of_group in range(1, 11):
    check_list.clear()
    if len(numbers_list) != 0:
        for number in numbers_list:
            if number <= (number_of_group * 10):
                check_list.append(number)
            else:
                continue
        for added_number in check_list:
            numbers_list.remove(added_number)
        print(f"Group of {number_of_group * 10}'s: {check_list}")


# numbers_list = list(map(int, input().split(", ")))
# group_of_10 = [number for number in numbers_list if 0 <= number <= 10]
# group_of_20 = [number for number in numbers_list if 10 <= number <= 20]
# group_of_30 = [number for number in numbers_list if 20 <= number <= 30]
# group_of_40 = [number for number in numbers_list if 30 <= number <= 40]
# group_of_50 = [number for number in numbers_list if 40 <= number <= 50]
# print(f"Group of 10's: {group_of_10}")
# print(f"Group of 20's: {group_of_20}")
# print(f"Group of 30's: {group_of_30}")
# print(f"Group of 40's: {group_of_40}")
# print(f"Group of 50's: {group_of_50}")


# def group_of_10(number):
#     return [current_number for current_number in number if 0 <= current_number <= 10]
#
#
# def group_of_20(number):
#     return [current_number for current_number in number if 10 <= current_number <= 20]
#
#
# def group_of_30(number):
#     return [current_number for current_number in number if 20 <= current_number <= 30]
#
#
# def group_of_40(number):
#     return [current_number for current_number in number if 30 <= current_number <= 40]
#
#
# def group_of_50(number):
#     return [current_number for current_number in number if 40 <= current_number <= 50]
#
#
# numbers_list = list(map(int, input().split(", ")))
# print(f"Group of 10's: {group_of_10(numbers_list)}")
# print(f"Group of 20's: {group_of_20(numbers_list)}")
# print(f"Group of 30's: {group_of_30(numbers_list)}")
# print(f"Group of 40's: {group_of_40(numbers_list)}")
# print(f"Group of 50's: {group_of_50(numbers_list)}")
