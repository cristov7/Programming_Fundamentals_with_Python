list_of_characters = input().split(", ")
ascii_info = {}
for character in list_of_characters:
    ascii_value = ord(character)
    ascii_info[character] = int(ascii_value)
print(ascii_info)


# chars_list = input().split(", ")
# dictionary = {element: ord(element) for element in chars_list}
# print(dictionary)
