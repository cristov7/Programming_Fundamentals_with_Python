some_string = input()
strings_list = some_string.split()
final_translated_string = ""
for current_string in strings_list:
    length_of_the_string = len(current_string)
    current_translated_string = current_string * length_of_the_string
    final_translated_string += current_translated_string
print(final_translated_string)


# some_strings_list = input().split()
# translated_list = []
# for current_string in some_strings_list:
#     length_of_the_string = len(current_string)
#     current_translated_string = current_string * length_of_the_string
#     translated_list.append(current_translated_string)
# translated_string = "".join(translated_list)
# print(translated_string)

# [print(string * len(string), end="") for string in input().split()]
