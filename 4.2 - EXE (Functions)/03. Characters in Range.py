def collect_characters(first, second):
    characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character))
    return characters


first_character = input()
second_character = input()
result = collect_characters(first_character, second_character)
print(*result)   # (*result, sep=" ") or  (' '.join(result))


# def ascii_translations(start_index, finish_index):
#     for translation in range(start_index, finish_index + 1):
#         current_translation = chr(translation)
#         print(current_translation, end=" ")
#
#
# first_symbol = ord(input()) + 1
# second_symbol = ord(input()) - 1
# ascii_translations(first_symbol, second_symbol)


# def ascii_translations(start_index, finish_index):
#     final_translation = ""
#     for translation in range(start_index, finish_index + 1):
#         current_translation = chr(translation)
#         final_translation += (current_translation + " ")
#     return final_translation
#
#
# first_symbol = ord(input()) + 1
# second_symbol = ord(input()) - 1
# print(ascii_translations(first_symbol, second_symbol))
