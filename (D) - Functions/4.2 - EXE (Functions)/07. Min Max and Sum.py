# numbers_in_list = list(map(int, input().split(" ")))
# print(f"The minimum number is {min(numbers_in_list)}")
# print(f"The maximum number is {max(numbers_in_list)}")
# print(f"The sum number is: {sum(numbers_in_list)}")


def min_max_and_sum(numbers: str):
    numbers_as_string_in_list = numbers.split(" ")
    numbers_as_integers_in_list = []
    for element in numbers_as_string_in_list:
        current_element = int(element)
        numbers_as_integers_in_list.append(current_element)
    min_num_in_list = min(numbers_as_integers_in_list)
    max_num_in_list = max(numbers_as_integers_in_list)
    sum_nums_in_list = sum(numbers_as_integers_in_list)
    return min_num_in_list, max_num_in_list, sum_nums_in_list


numbers_as_string = input()
min_number, max_number, sum_numbers = min_max_and_sum(numbers_as_string)
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
