def no_redundant_symbols(name):
    if " " in name:
        return False
    else:
        return True


def can_contain(name):
    for char in name:
        if char.isalnum() or char == "-" or char == "_":
            continue
        else:
            return False
    return True


def length(name):
    if 3 <= len(name) <= 16:
        return True
    else:
        return False


def valid_username(name):
    if length(name) and can_contain(name) and no_redundant_symbols(name):
        return True
    else:
        return False


usernames_list = input().split(", ")
for username in usernames_list:
    if valid_username(username):
        print(username)
    else:
        continue


# usernames_list = input().split(", ")
# for username in usernames_list:
#     if 3 <= len(username) <= 16:
#         if username.isalnum() or "-" in username or "_" in username:
#             print(username)
#         else:
#             continue
#     else:
#         continue


# usernames_list = input().split(", ")
# invalid_symbol = False
# for username in usernames_list:
#     if 3 <= len(username) <= 16:
#         for symbol in username:
#             if symbol.isalnum() or symbol == "-" or symbol == "_":
#                 continue
#             else:
#                 invalid_symbol = True
#                 break
#         if invalid_symbol:
#             invalid_symbol = False
#             continue
#         else:
#             print(username)
#     else:
#         continue
