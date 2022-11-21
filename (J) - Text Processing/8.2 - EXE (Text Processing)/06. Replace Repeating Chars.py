text = input()
update_text = ""
last_char = None
for char in text:
    if char == last_char:
        continue
    else:
        last_char = char
        update_text += char
print(update_text)


# text = input()
# update_text_list = []
# last_char = None
# for char in text:
#     if char == last_char:
#         continue
#     else:
#         last_char = char
#         update_text_list.append(char)
# update_text = "".join(update_text_list)
# print(update_text)


# some_text = input()
# final_text = ""
# last_letter = ""
# for current_letter in some_text:
#     if current_letter != last_letter:
#         final_text += current_letter
#         last_letter = current_letter
#     else:
#         continue
# print(final_text)
