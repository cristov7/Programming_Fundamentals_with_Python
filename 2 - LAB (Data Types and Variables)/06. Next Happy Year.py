year = int(input())
happy_year_condition = False
while not happy_year_condition:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])
    happy_year_condition = len(set_year) == len(str(year))
print(year)


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
