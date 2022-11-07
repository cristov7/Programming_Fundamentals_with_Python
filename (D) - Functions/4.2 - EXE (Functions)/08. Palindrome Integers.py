def palindrome_integers(numbers: str):
    numbers_as_string_in_list = numbers.split(", ")
    for element in numbers_as_string_in_list:
        palindrome = element[::-1]
        if element == palindrome:
            print(True)
        else:
            print(False)


numbers_as_string = input()
palindrome_integers(numbers_as_string)


# list_of_numbers_as_string = list(input().split(', '))
# for element in list_of_numbers_as_string:
#     palindrome = element[::-1]
#     if palindrome == element:
#         print(True)
#     else:
#         print(False)
