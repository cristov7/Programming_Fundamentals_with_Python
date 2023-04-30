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
binary_number_list = list(binary_number)

index = -(position_of_bit + 1)
binary_number_list[index] = "0"

new_decimal_number = 0
for power, digit in enumerate(binary_number_list[::-1]):
    new_decimal_number += int(digit) * 2 ** power

print(new_decimal_number)
# print(f"{binary_number} -> {''.join(binary_number_list)}")
