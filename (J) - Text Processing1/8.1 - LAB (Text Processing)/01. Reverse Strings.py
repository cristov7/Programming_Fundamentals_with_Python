while True:
    command = input()
    if command == "end":
        """here we go out of the loop"""
        break
    else:
        word = command
        reversed_word = word[::-1]
        print(f"{word} = {reversed_word}")


# text = input()
# while text != "end":
#     text_reversed = ""
#     for ch in reversed(text):
#         text_reversed += ch
#     print(text + " = " + text_reversed)
#     text = input()


# word_and_reversed_word = {}
# while True:
#     command = input()
#     if command == "end":
#         break
#     else:
#         current_word = command
#         current_reversed_word = current_word[::-1]
#         word_and_reversed_word[current_word] = current_reversed_word
# for word, reversed_word in word_and_reversed_word.items():
#     print(f"{word} = {reversed_word}")


# word_list = []
# while True:
#     command = input()
#     if command == "end":
#         break
#     else:
#         word = command
#         for char in word:
#             word_list.append(char)
#         word_list.reverse()
#         reversed_word = "".join(word_list)
#         print(f"{word} = {reversed_word}")
#         word_list = []
