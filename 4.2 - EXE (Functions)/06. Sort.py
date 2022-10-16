# numbers_in_list = list(map(int, input().split(" ")))
# print(sorted(numbers_in_list))


# list_of_numbers = list(map(int, input().split()))
# sorting = sorted(list_of_numbers)
# print(sorting)


def sorted_numbers(numbers: str):
    numbers_as_string_in_list = numbers.split()
    numbers_as_integers_in_list = []
    for element in numbers_as_string_in_list:
        current_element = int(element)
        numbers_as_integers_in_list.append(current_element)
    return sorted(numbers_as_integers_in_list)


numbers_as_string = input()
print(sorted_numbers(numbers_as_string))
