first_char = input()
second_char = input()
first_char_value = ord(first_char)
second_char_value = ord(second_char)
text = input()
text_values = [ord(char) for char in text]
sum_values = 0
for value in text_values:
    if first_char_value < value < second_char_value:
        sum_values += value
    else:
        continue
print(sum_values)
