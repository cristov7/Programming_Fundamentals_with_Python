def length_validation(password: str):
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        return False
    return True


def alpha_numeric_validation(password: str):
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True


def digits_validation(password: str):
    digit_counter = 0
    for character in password:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        return False
    return True


enter_password = input()
password_is_not_valid = [length_validation(enter_password),
                         alpha_numeric_validation(enter_password),
                         digits_validation(enter_password)]
if all(password_is_not_valid):   # if all(password_is_not_valid) == True:
    print("Password is valid")


# def password_validation(some_password):
#     validation = []
#     if len(some_password) < 6 or len(some_password) > 10:
#         validation.append("Password must be between 6 and 10 characters")
#     if not some_password.isalnum():
#         validation.append("Password must consist only of letters and digits")
#     digit_counter = 0
#     for character in some_password:
#         if character.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         validation.append("Password must have at least 2 digits")
#     return validation
#
#
# password = input()
# password_is_not_valid = password_validation(password)
# if len(password_is_not_valid) == 0:
#     print("Password is valid")
# else:
#     print("\n".join(password_is_not_valid))


# def password_validation(some_password):
#     pass_is_valid = True
#     if len(some_password) < 6 or len(some_password) > 10:
#         print("Password must be between 6 and 10 characters")
#         pass_is_valid = False
#     if not some_password.isalnum():
#         print("Password must consist only of letters and digits")
#         pass_is_valid = False
#     digit_counter = 0
#     for character in some_password:
#         if character.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         print("Password must have at least 2 digits")
#         pass_is_valid = False
#     return pass_is_valid
#
#
# password = input()
# password_is_valid = password_validation(password)
# if password_is_valid:
#     print("Password is valid")


# def password_validator(password: str):
#     password_is_valid = True
#     length_of_password = len(password)
#     if length_of_password < 6 or length_of_password > 10:
#         password_is_valid = False
#         print("Password must be between 6 and 10 characters")
#     digit_counter = 0
#     for element in password:
#         if 48 <= ord(element) <= 57 or 65 <= ord(element) <= 90 or 97 <= ord(element) <= 122:
#             if 48 <= ord(element) <= 57:
#                 digit_counter += 1
#             else:
#                 continue
#         else:
#             password_is_valid = False
#             print("Password must consist only of letters and digits")
#             break
#     if digit_counter < 2:
#         password_is_valid = False
#         print("Password must have at least 2 digits")
#     return password_is_valid
#
#
# input_password = input()
# true_or_false_password = password_validator(input_password)
# if true_or_false_password:
#     print("Password is valid")
