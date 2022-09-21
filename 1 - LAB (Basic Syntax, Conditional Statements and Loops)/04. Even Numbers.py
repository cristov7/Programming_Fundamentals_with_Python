number = int(input())
for numbers in range(number):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
        break
    else:
        continue
else:
    print("All numbers are even.")


# number = int(input())
# counter = 0
# for count_numbers in range(1, number + 1):
#     current_number = int(input())
#     counter += 1
#     if current_number % 2 == 0:
#         if counter == number:
#             print("All numbers are even.")
#             break
#         else:
#             continue
#     else:
#         print(f"{current_number} is odd!")
#         break
