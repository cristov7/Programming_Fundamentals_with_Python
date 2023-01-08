def multiplication_function(some_list: list):
    result = 0
    for index, number in enumerate(some_list):
        if index == 0:
            result = number
        else:
            multiply = result * number
            result = multiply
    if result > 0:
        return "positive"
    elif result < 0:
        return "negative"
    else:
        return "zero"


numbers_list = [int(input()) for number in range(3)]
calculation = multiplication_function(numbers_list)
print(calculation)


# def multiplication_sign(number_1: int, number_2: int, number_3: int):
#     numbers_list = [number_1, number_2, number_3]
#     counter_minus = 0
#     for number in numbers_list:
#         if number == 0:
#             return "zero"
#         else:
#             if number < 0:
#                 counter_minus += 1
#             else:
#                 continue
#     if counter_minus % 2 == 0:
#         return "positive"
#     else:
#         return "negative"
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# print(multiplication_sign(first_number, second_number, third_number))
