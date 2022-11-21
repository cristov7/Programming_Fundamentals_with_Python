text = input()
encrypted_text = ""
for char in text:
    ord_char = ord(char)
    new_ord_char = ord_char + 3
    new_char = chr(new_ord_char)
    encrypted_text += new_char
print(encrypted_text)


# text = input()
# encrypted_text = []
# for char in text:
#     new_char = ord(char) + 3
#     encrypted_text.append(chr(new_char))
# print("".join(encrypted_text))
