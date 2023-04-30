number = int(input())

reversed_binary_number = ""

decimal_number = number
while decimal_number > 0:
    remainder = decimal_number % 2
    reversed_binary_number += str(remainder)
    decimal_number //= 2

binary_number = reversed_binary_number[::-1]
bit_at_first_position = binary_number[-2]

print(bit_at_first_position)
# print(f"{binary_number}  {bit_at_first_position}")
