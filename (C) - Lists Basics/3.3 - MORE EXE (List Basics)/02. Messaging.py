numbers_as_string_in_list = input().split(" ")   # .split()
message_as_string = input()
length_of_message_as_string = len(message_as_string)
index_per_message = []
for number_as_string in numbers_as_string_in_list:
    length_of_element = len(number_as_string)
    if length_of_element == 1:
        number = int(number_as_string)
        index_per_message.append(number)
    else:
        sum_number = 0
        for index in range(length_of_element):
            number = int(number_as_string[index])
            sum_number += number
        index_per_message.append(sum_number)
counter = 0
for index, value in enumerate(index_per_message):
    if value + counter >= length_of_message_as_string:
        result = value + counter - length_of_message_as_string
        current_symbol = message_as_string[result]
        print(current_symbol, end="")
        counter += 1
    else:
        current_symbol = message_as_string[value + counter]
        print(current_symbol, end="")
        counter += 1
