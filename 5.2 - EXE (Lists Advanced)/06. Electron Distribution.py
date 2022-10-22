count_electrons = int(input())
shell = [0]
index = 1
while count_electrons > 0:
    vacancies = 2 * index ** 2
    if shell[index - 1] < vacancies:
        count_electrons -= 1
        shell[index - 1] += 1
    else:
        count_electrons -= 1
        shell.append(1)
        index += 1
print(shell)


# def electron_distribution(number: int):
#     shell = [0]
#     index = 1
#     while number > 0:
#         vacancies = 2 * index ** 2
#         if shell[index - 1] < vacancies:
#             number -= 1
#             shell[index - 1] += 1
#         else:
#             number -= 1
#             shell.append(1)
#             index += 1
#     return shell
#
#
# count_electrons = int(input())
# print(electron_distribution(count_electrons))
