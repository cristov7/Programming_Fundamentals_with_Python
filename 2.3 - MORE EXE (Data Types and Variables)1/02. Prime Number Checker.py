number = int(input())
is_prime = True
for current_number in range(2, number):
    if number % current_number == 0:
        is_prime = False
        break
    else:
        continue
print(is_prime)


# number = int(input())
# if number >= 0:
#     if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number == 1 and number != 0:
#         if number == 2 or number == 3 or number == 5 or number == 7:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(True)
# else:
#     print(False)
