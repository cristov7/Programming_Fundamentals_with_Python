def odd_and_even_sum(number: str):
    length_of_number = len(number)
    even_numbers_list = []
    odd_numbers_list = []
    for index in range(length_of_number):
        current_number = int(number[index])
        if current_number % 2 == 0:
            even_numbers_list.append(current_number)
        else:
            odd_numbers_list.append(current_number)
    return f"Odd sum = {sum(odd_numbers_list)}, Even sum = {sum(even_numbers_list)}"


numbers_as_string = input()
print(odd_and_even_sum(numbers_as_string))


# numbers_as_string = input()
# length_of_number_as_string = len(numbers_as_string)
# even_numbers_list = []
# odd_numbers_list = []
# for index in range(length_of_number_as_string):
#     current_number = int(numbers_as_string[index])
#     if current_number % 2 == 0:
#         even_numbers_list.append(current_number)
#     else:
#         odd_numbers_list.append(current_number)
# print(f"Odd sum = {sum(odd_numbers_list)}, Even sum = {sum(even_numbers_list)}")


# def even_and_odd_numbers(number: str):
#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0
#     for digit in number:
#         if int(digit) % 2 == 0:  # digit is even
#             sum_of_even_digits += int(digit)
#         else:  # digit is odd
#             sum_of_odd_digits += int(digit)
#     return sum_of_odd_digits, sum_of_even_digits
#
#
# number_as_string = input()
# sum_odd, sum_even = even_and_odd_numbers(number_as_string)
# print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")
