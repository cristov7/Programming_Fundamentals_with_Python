number = int(input())
position_of_bit = int(input())

reversed_binary_number = ""

decimal_number = number
while decimal_number > 0:
    remainder = decimal_number % 2
    reversed_binary_number += str(remainder)
    decimal_number //= 2

while len(reversed_binary_number) < len(str(number)) * 4:
    reversed_binary_number += "0"

binary_number = reversed_binary_number[::-1]

index = -(position_of_bit + 1)
bit_at_position = binary_number[index]

print(bit_at_position)
# print(f"{binary_number} -> {bit_at_position}")
