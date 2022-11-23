alphabet = {
    "A": 1, "a": 1, "B": 2, "b": 2, "C": 3, "c": 3, "D": 4, "d": 4, "E": 5, "e": 5,
    "F": 6, "f": 6, "G": 7, "g": 7, "H": 8, "h": 8, "I": 9, "i": 9, "J": 10, "j": 10,
    "K": 11, "k": 11, "L": 12, "l": 12, "M": 13, "m": 13, "N": 14, "n": 14, "O": 15, "o": 15,
    "P": 16, "p": 16, "Q": 17, "q": 17, "R": 18, "r": 18, "S": 19, "s": 19, "T": 20, "t": 20,
    "U": 21, "u": 21, "V": 22, "v": 22, "W": 23, "w": 23, "X": 24, "x": 24, "Y": 25, "y": 25, "Z": 26, "z": 26
}
some_string = input()
first_letter = ""
second_letter = ""
digit = ""
result = 0
for char in some_string:
    if char.isalnum():
        if char.isdigit():
            digit += char
        else:   # elif char.isalpha():
            if char.isupper():
                if first_letter == "":
                    first_letter = char
                else:
                    second_letter = char
                    current_digit = int(digit)
                    if first_letter.isupper():
                        divider = alphabet[first_letter]
                        result += current_digit / divider
                        if second_letter.isupper():
                            subtract = alphabet[second_letter]
                            result -= subtract
                        else:  # elif second_letter.islower():
                            add = alphabet[second_letter]
                            result += add
                    else:   # elif first_letter.islower():
                        multiply = alphabet[first_letter]
                        result += current_digit * multiply
                        if second_letter.isupper():
                            subtract = alphabet[second_letter]
                            result -= subtract
                        else:  # elif second_letter.islower():
                            add = alphabet[second_letter]
                            result += add
                    first_letter = ""
                    second_letter = ""
                    digit = ""
            else:   # elif char.islower():
                if first_letter == "":
                    first_letter = char
                else:
                    second_letter = char
                    current_digit = int(digit)
                    if first_letter.isupper():
                        divider = alphabet[first_letter]
                        result += current_digit / divider
                        if second_letter.isupper():
                            subtract = alphabet[second_letter]
                            result -= subtract
                        else:   # elif second_letter.islower():
                            add = alphabet[second_letter]
                            result += add
                    else:   # elif first_letter.islower():
                        multiply = alphabet[first_letter]
                        result += current_digit * multiply
                        if second_letter.isupper():
                            subtract = alphabet[second_letter]
                            result -= subtract
                        else:  # elif second_letter.islower():
                            add = alphabet[second_letter]
                            result += add
                    first_letter = ""
                    second_letter = ""
                    digit = ""
    else:
        continue
print(f"{result:.2f}")


# def letters_change_numbers(some_string: str):
#     alphabet = {
#         "A": 1, "a": 1, "B": 2, "b": 2, "C": 3, "c": 3, "D": 4, "d": 4, "E": 5, "e": 5,
#         "F": 6, "f": 6, "G": 7, "g": 7, "H": 8, "h": 8, "I": 9, "i": 9, "J": 10, "j": 10,
#         "K": 11, "k": 11, "L": 12, "l": 12, "M": 13, "m": 13, "N": 14, "n": 14, "O": 15, "o": 15,
#         "P": 16, "p": 16, "Q": 17, "q": 17, "R": 18, "r": 18, "S": 19, "s": 19, "T": 20, "t": 20,
#         "U": 21, "u": 21, "V": 22, "v": 22, "W": 23, "w": 23, "X": 24, "x": 24, "Y": 25, "y": 25, "Z": 26, "z": 26
#     }
#     first_letter = ""
#     second_letter = ""
#     digit = ""
#     result = 0
#     for char in some_string:
#         if char.isalnum():
#             if char.isdigit():
#                 digit += char
#             else:  # elif char.isalpha():
#                 if char.isupper():
#                     if first_letter == "":
#                         first_letter = char
#                     else:
#                         second_letter = char
#                         current_digit = int(digit)
#                         if first_letter.isupper():
#                             divider = alphabet[first_letter]
#                             result += current_digit / divider
#                             if second_letter.isupper():
#                                 subtract = alphabet[second_letter]
#                                 result -= subtract
#                             else:  # elif second_letter.islower():
#                                 add = alphabet[second_letter]
#                                 result += add
#                         else:  # elif first_letter.islower():
#                             multiply = alphabet[first_letter]
#                             result += current_digit * multiply
#                             if second_letter.isupper():
#                                 subtract = alphabet[second_letter]
#                                 result -= subtract
#                             else:  # elif second_letter.islower():
#                                 add = alphabet[second_letter]
#                                 result += add
#                         first_letter = ""
#                         second_letter = ""
#                         digit = ""
#                 else:  # elif char.islower():
#                     if first_letter == "":
#                         first_letter = char
#                     else:
#                         second_letter = char
#                         current_digit = int(digit)
#                         if first_letter.isupper():
#                             divider = alphabet[first_letter]
#                             result += current_digit / divider
#                             if second_letter.isupper():
#                                 subtract = alphabet[second_letter]
#                                 result -= subtract
#                             else:  # elif second_letter.islower():
#                                 add = alphabet[second_letter]
#                                 result += add
#                         else:  # elif first_letter.islower():
#                             multiply = alphabet[first_letter]
#                             result += current_digit * multiply
#                             if second_letter.isupper():
#                                 subtract = alphabet[second_letter]
#                                 result -= subtract
#                             else:  # elif second_letter.islower():
#                                 add = alphabet[second_letter]
#                                 result += add
#                         first_letter = ""
#                         second_letter = ""
#                         digit = ""
#         else:
#             continue
#     return result
#
#
# text = input()
# total = letters_change_numbers(text)
# print(f"{total:.2f}")
