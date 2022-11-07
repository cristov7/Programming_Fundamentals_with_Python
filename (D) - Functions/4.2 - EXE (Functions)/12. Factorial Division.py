def factorial_operation(number: int):
    sum_factorial = number
    for factorial in range(number - 1, 0, - 1):
        sum_factorial *= factorial
    return sum_factorial


first_number = int(input())
second_number = int(input())
factorials = [factorial_operation(first_number), factorial_operation(second_number)]
result = factorials[0] / factorials[1]
print(f"{result:.2f}")


# def factorial(number):
#     for current_number in range(1, number):
#         number *= current_number
#     return number
#
#
# first_number = int(input())
# second_number = int(input())
# first_number_factorial = factorial(first_number)
# second_number_factorial = factorial(second_number)
# final_result = first_number_factorial / second_number_factorial
# print(f"{final_result:.2f}")
