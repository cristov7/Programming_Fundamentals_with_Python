to_remove = input()
word = input()
while to_remove in word:
    word = word.replace(to_remove, "")
print(word)


# first_string = input()
# second_string = input()
# first_string_in_symbol_list = []
# for char in first_string:
#     first_string_in_symbol_list.append(char)
# second_string_in_symbol_list = []
# for symbol in second_string:
#     if symbol in first_string_in_symbol_list:
#         continue
#     else:
#         second_string_in_symbol_list.append(symbol)
# final_word = "".join(second_string_in_symbol_list)
# print(final_word)
