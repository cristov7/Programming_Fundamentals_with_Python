number = input()
digits_list = []
for digit in number:
    current_digit = int(digit)
    digits_list.append(current_digit)
digits_list.sort(reverse=True)
update_digits_list_as_string = []
for element in digits_list:
    current_element = str(element)
    update_digits_list_as_string.append(current_element)
update_number = ("".join(update_digits_list_as_string))
print(update_number)
