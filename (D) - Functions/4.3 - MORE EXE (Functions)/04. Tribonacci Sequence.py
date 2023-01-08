def tribonacci_calculation_function(some_number: int):
    tribonacci_list = []
    for position in range(1, some_number + 1):
        if len(tribonacci_list) < 3:
            number = sum(tribonacci_list)
            if number == 0:
                number = 1
                tribonacci_list.append(number)
            else:
                tribonacci_list.append(number)
        else:
            last_3_numbers_list = [tribonacci_list[-1], tribonacci_list[-2], tribonacci_list[-3]]
            number = sum(last_3_numbers_list)
            tribonacci_list.append(number)
    return tribonacci_list


start_number = int(input())
numbers_list = tribonacci_calculation_function(start_number)
print(*numbers_list)


# def tribonacci_sequence(number: int):
#     tribonacci_list = []
#     for tribonacci in range(1, number + 1):
#         if tribonacci == 1:
#             current_tribonacci = 1
#             tribonacci_list.append(str(current_tribonacci))
#         elif tribonacci == 2:
#             current_tribonacci = int(tribonacci_list[-1])
#             tribonacci_list.append(str(current_tribonacci))
#         elif tribonacci == 3:
#             before_1_tribonacci = int(tribonacci_list[-1])
#             before_2_tribonacci = int(tribonacci_list[-2])
#             current_tribonacci = before_1_tribonacci + before_2_tribonacci
#             tribonacci_list.append(str(current_tribonacci))
#         else:
#             before_1_tribonacci = int(tribonacci_list[-1])
#             before_2_tribonacci = int(tribonacci_list[-2])
#             before_3_tribonacci = int(tribonacci_list[-3])
#             current_tribonacci = before_1_tribonacci + before_2_tribonacci + before_3_tribonacci
#             tribonacci_list.append(str(current_tribonacci))
#     return (" ".join(tribonacci_list))


# enter_number = int(input())
# print(tribonacci_sequence(enter_number))


# def find_tribonacci(number):
#     t_nums = [1]
#
#     num = 1
#     while len(t_nums) < number:
#
#         if len(t_nums) < 3:
#
#             if len(t_nums) == 1:
#                 if num == t_nums[-1] + 0 + 0:
#                     t_nums.append(num)
#             elif len(t_nums) == 2:
#                 if num == t_nums[-1] + t_nums[-2] + 0:
#                     t_nums.append(num)
#         else:
#             if num == t_nums[-1] + t_nums[-2] + t_nums[-3]:
#                 t_nums.append(num)
#
#         num += 1
#
#     return t_nums
#
#
# def print_tribonacci(l):
#     print(' '.join(map(str, l)))
#
#
# num = int(input())
#
# numlist = find_tribonacci(num)
# print_tribonacci(numlist)
