morse_alphabet_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
    "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"
}
morse_code = input()
morse_code_words_list = morse_code.split(" | ")
translate_list = []
for morse_word in morse_code_words_list:
    chars_list = morse_word.split()
    letters_list = []
    for char in chars_list:
        letter = morse_alphabet_dict[char]
        letters_list.append(letter)
    word = "".join(letters_list)
    translate_list.append(word)
print(" ".join(translate_list))


# morse_code_alphabet = {
#     "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
#     "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
#
#     "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
#     "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
#     "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
#     "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
# }
# text = input()
# morse_words = text.split(" | ")
# morse_words_list = []
# for morse_symbols in morse_words:
#     current_morse_word = morse_symbols.split()
#     morse_words_list.append(current_morse_word)
# translating_text = []
# for element in morse_words_list:
#     length = len(element)
#     word = ""
#     for index in range(length):
#         for char, value in morse_code_alphabet.items():
#             if element[index] == value:
#                 word += char
#                 break
#             else:
#                 continue
#     upper_word = word.upper()
#     translating_text.append(upper_word)
# print(*translating_text, sep=" ")
