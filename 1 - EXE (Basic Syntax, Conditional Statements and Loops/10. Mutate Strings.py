first_string = input()
second_string = input()
number_of_symbols = len(first_string)
not_to_printed_string = first_string
for index in range(number_of_symbols):
    left_part = second_string[0:index + 1]
    right_part = first_string[index + 1: number_of_symbols]
    current_string = left_part + right_part
    if current_string == not_to_printed_string:
        continue
    else:
        print(current_string)
        not_to_printed_string = current_string
