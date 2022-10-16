def sum_numbers(number_1: int, number_2: int):
    calculation = number_1 + number_2
    return calculation


def subtract(sum_of_number_1_an_number_2: int, number_3: int):
    calculation = sum_of_number_1_an_number_2 - number_3
    return calculation


def add_and_subtract(number_1: int, number_2: int, number_3: int):
    calculation = sum_numbers(number_1, number_2)
    final_calculation = subtract(calculation, number_3)
    return final_calculation


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))


# def sum_numbers(first, second):
#     return first + second
#
#
# def subtract(sum, third):
#     return sum - third
#
#
# def add_and_subtract(first, second, third):
#     sum_of_first_and_second = sum_numbers(first, second)
#     result = subtract(sum_of_first_and_second, third)
#     return result
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# print(add_and_subtract(first_number, second_number, third_number))
