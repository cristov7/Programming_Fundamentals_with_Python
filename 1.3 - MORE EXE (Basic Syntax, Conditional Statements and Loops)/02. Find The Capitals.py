input_string = input()
upper_index_list = []
for index, value in enumerate(input_string):
    if value.isupper():
        upper_index_list.append(index)
    else:
        continue
print(upper_index_list)
