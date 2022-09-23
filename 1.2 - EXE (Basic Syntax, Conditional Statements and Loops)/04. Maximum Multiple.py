divider_number = int(input())
boundary_number = int(input())
for result in range(boundary_number, divider_number - 1, -1):
    if result % divider_number == 0:
        print(result)
        break


# import sys
# max_result = - sys.maxsize
# divider_number = int(input())
# boundary_number = int(input())
# for result in range(divider_number, boundary_number + 1):
#     if result % divider_number == 0:
#         if result > max_result:
#             max_result = result
# print(max_result)
