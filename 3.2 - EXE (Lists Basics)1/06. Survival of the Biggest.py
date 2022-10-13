numbers_as_string = input()
numbers_as_string_in_list = numbers_as_string.split()   # .split(" ")
count_numbers_to_remove = int(input())
numbers_as_integers_in_list = []
for element in numbers_as_string_in_list:
    current_element = int(element)
    numbers_as_integers_in_list.append(current_element)
counter_to_remove = 0
while True:
    counter_to_remove += 1
    if counter_to_remove <= count_numbers_to_remove:
        numbers_as_integers_in_list.remove(min(numbers_as_integers_in_list))
    else:
        break
update_numbers_as_string_in_list = []
for element in numbers_as_integers_in_list:
    current_element = str(element)
    update_numbers_as_string_in_list.append(current_element)
print(", ".join(update_numbers_as_string_in_list))
