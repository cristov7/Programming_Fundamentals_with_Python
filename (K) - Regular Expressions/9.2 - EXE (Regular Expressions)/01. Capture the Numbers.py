import re
regex = r"\d+"
while True:
    command = input()
    if command == "":
        break
    else:
        numbers_list = re.findall(regex, command)
        # if len(numbers_list) == 0:
        #     continue
        # else:
        #     [print(number, end=" ") for number in numbers_list]
        [print(number, end=" ") for number in numbers_list]


# import re
# regex = r"\d+"
# while True:
#     command = input()
#     if command == "":
#         break
#     else:
#         numbers_list = re.findall(regex, command)
#         if numbers_list:
#             print(*numbers_list, end=" ")
#         else:
#             continue


# import re
# regex = r"\d+"
# line = input()
# while line:
#     numbers_list = re.findall(regex, line)
#     if numbers_list:
#         print(*numbers_list, end=" ")
#         line = input()
#     else:
#         line = input()
