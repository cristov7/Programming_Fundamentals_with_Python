number_of_lines = int(input())
calculating = ""
info = True
for line in range(1, number_of_lines + 1):
    random_string = input()
    if random_string == "(" and calculating == "":
        calculating += random_string
    elif random_string == "(" and calculating != "":
        info = False
        break
    elif random_string == ")" and calculating == "(":
        calculating = ""
    elif random_string == ")" and calculating == "":
        info = False
        break
    else:
        continue
if info:
    print("BALANCED")
else:
    print("UNBALANCED")


# number_of_lines = int(input())
# is_open = False
# is_close = False
# counter = 0
# for line in range(number_of_lines):
#     text = input()
#     if "(" and ")" not in text:
#         counter += 1
#     for char in text:
#         if char == "(":
#             if not is_open and not is_close:
#                 is_open = True
#             else:
#                 is_open = False
#         elif char == ")":
#             is_close = True
#         if is_open and is_close:
#             is_open = False
#             is_close = False
# if not is_close and not is_open and number_of_lines != counter:
#     print("BALANCED")
# else:
#     print("UNBALANCED")

