text = input()
digits, letters, others = [], [], []
for symbol in text:
    if symbol.isdigit():
        digits.append(symbol)
    elif symbol.isalpha():
        letters.append(symbol)
    else:   # elif not symbol.isalnum():
        others.append(symbol)
print(*digits, sep="")
print(*letters, sep="")
print(*others, sep="")


# some_string = input()
# digits = ""
# letters = ""
# other_characters = ""
# for char in some_string:
#     if char.isdigit():
#         digits += char
#     elif char.isalpha():
#         letters += char
#     else:   # elif not symbol.isalnum():
#         other_characters += char
# print(digits)
# print(letters)
# print(other_characters)


# some_string = input()
# digits_list = []
# letters_list = []
# other_chars_list = []
# for char in some_string:
#     if char.isdigit():
#         digits_list.append(char)
#     elif char.isalpha():
#         letters_list.append(char)
#     else:   # elif not symbol.isalnum():
#         other_chars_list.append(char)
# final_digits = "".join(digits_list)
# final_letters = "".join(letters_list)
# final_other_chars = "".join(other_chars_list)
# print(final_digits)
# print(final_letters)
# print(final_other_chars)


# def digits_letters_others(some_string: str):
#     digits, letters, others = [], [], []
#     for symbol in text:
#         if symbol.isdigit():
#             digits.append(symbol)
#         elif symbol.isalpha():
#             letters.append(symbol)
#         else:   # elif not symbol.isalnum():
#             others.append(symbol)
#     return f"{''.join(digits)}\n{''.join(letters)}\n{''.join(others)}"
#
#
# text = input()
# print(digits_letters_others(text))
