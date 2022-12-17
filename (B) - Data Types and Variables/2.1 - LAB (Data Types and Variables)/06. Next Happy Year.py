year = int(input())
current_year = year
while True:
    current_year += 1
    current_year_as_string = str(current_year)
    digits_list = [digit for digit in current_year_as_string]
    unique_digits_list = list(set(digits_list))
    length_digits_list = len(digits_list)
    length_unique_digits_list = len(unique_digits_list)
    if length_digits_list == length_unique_digits_list:
        print(current_year)
        break
    else:
        continue


# year = int(input())
# happy_year_condition = False
# while not happy_year_condition:
#     year += 1
#     set_year = set()
#     for i in range(len(str(year))):
#         set_year.add(str(year)[i])
#     happy_year_condition = len(set_year) == len(str(year))
# print(year)


# year = int(input())
# new_year = year
# happy_year = False
# while not happy_year:
#     new_year += 1
#     for i in range(len(str(new_year))):
#         for k in range(len(str(new_year))):
#             if str(new_year)[i] != str(new_year)[k] and i != k:
#                 happy_year = True
#                 continue
#             elif str(new_year)[i] == str(new_year)[k] and i != k:
#                 happy_year = False
#                 break
#         if not happy_year:
#             break
#         else:
#             continue
# print(new_year)
