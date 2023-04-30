number = int(input())
binary_digit = input()

reversed_binary_number = ""

decimal_number = number
while decimal_number > 0:
    remainder = decimal_number % 2
    reversed_binary_number += str(remainder)
    decimal_number //= 2

binary_number = reversed_binary_number[::-1]
count_binary_digit = binary_number.count(binary_digit)

print(count_binary_digit)
# print(f"{number} -> {binary_number}"
#       f"\nWe have {count_binary_digit} {'zeroes' if binary_digit == '0' else 'ones'}.")
