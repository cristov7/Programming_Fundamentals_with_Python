n = int(input())
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")


# n = int(input())
# counter = 0
# for count_numbers in range(1, n + 1):
#     current_number = int(input())
#     counter += 1
#     if current_number % 2 == 0:
#         if counter == n:
#             print("All numbers are even.")
#             break
#     else:
#         print(f"{current_number} is odd!")
#         break
