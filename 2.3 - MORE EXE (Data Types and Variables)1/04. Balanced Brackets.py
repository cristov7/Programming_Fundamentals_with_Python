number_of_lines = int(input())
is_open = False
is_close = False
counter = 0
for line in range(number_of_lines):
    text = input()
    if "(" and ")" not in text:
        counter += 1
    for char in text:
        if char == "(":
            if not is_open and not is_close:
                is_open = True
            else:
                is_open = False
        elif char == ")":
            is_close = True
        if is_open and is_close:
            is_open = False
            is_close = False
if not is_close and not is_open and number_of_lines != counter:
    print("BALANCED")
else:
    print("UNBALANCED")


# balanced_or_unbalanced = ""
# symbol_list = []
# number = int(input())
# for rows in range(1, number + 1):
#     symbol = input()
#     if symbol == "(":
#         symbol_list.append(symbol)
#         balanced_or_unbalanced = "UNBALANCED"
#     elif symbol == ")":
#         symbol_list.append(symbol)
#         if "(" in symbol_list:
#             symbol_list.remove("(")
#             symbol_list.remove(")")
#             balanced_or_unbalanced = "BALANCED"
#         else:
#             balanced_or_unbalanced = "UNBALANCED"
#             break
#     else:
#         continue
# print(balanced_or_unbalanced)
