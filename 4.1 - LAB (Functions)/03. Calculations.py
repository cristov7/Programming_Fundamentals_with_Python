operator = input()
first_number = int(input())
second_number = int(input())


def calculation(choice, number_1, number_2):
    if choice == "multiply":
        return number_1 * number_2
    elif choice == "divide":
        return number_1 // number_2
    elif choice == "add":
        return number_1 + number_2
    elif choice == "subtract":
        return number_1 - number_2


print(calculation(operator, first_number, second_number))


# operator = input()
# first_number = int(input())
# second_number = int(input())
#
#
# def result(operator, first_number, second_number):
#     if operator == "multiply":
#         return first_number * second_number
#     elif operator == "divide":
#         return first_number // second_number
#     elif operator == "add":
#         return first_number + second_number
#     elif operator == "subtract":
#         return first_number - second_number
#
#
# print(result(operator, first_number, second_number))


# def calculation(first_number, second_number, operator):
#     result = None
#     if operator == "multiply":
#         result = first_number * second_number
#     elif operator == "divide":
#         result = int(first_number / second_number)
#     elif operator == "add":
#         result = first_number + second_number
#     elif operator == "subtract":
#         result = first_number - second_number
#     print(result)
# 
# 
# input_operator = input()
# input_first_number = int(input())
# input_second_number = int(input())
# calculation(input_first_number, input_second_number, input_operator)
