numbers_list = [int(number) for number in input().split(", ")]
positive_list = [str(number) for number in numbers_list if number >= 0]
negative_list = [str(number) for number in numbers_list if number < 0]
even_list = [str(number) for number in numbers_list if number % 2 == 0]
odd_list = [str(number) for number in numbers_list if number % 2]
print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")


# def positive_number(numbers):
#     return [str(current_number) for current_number in numbers if int(current_number) >= 0]
#
#
# def negative_number(numbers):
#     return [str(current_number) for current_number in numbers if int(current_number) < 0]
#
#
# def even_number(numbers):
#     return [str(current_number) for current_number in numbers if int(current_number) % 2 == 0]
#
#
# def odd_number(numbers):
#     return [str(current_number) for current_number in numbers if int(current_number) % 2]
#
#
# numbers_list = [number for number in input().split(", ")]
# print(f"Positive: {', '.join(positive_number(numbers_list))}")
# print(f"Negative: {', '.join(negative_number(numbers_list))}")
# print(f"Even: {', '.join(even_number(numbers_list))}")
# print(f"Odd: {', '.join(odd_number(numbers_list))}")
