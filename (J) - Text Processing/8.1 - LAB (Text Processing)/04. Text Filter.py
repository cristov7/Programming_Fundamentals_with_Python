string_of_banned_words = input().split(", ")
text = input()
for banned_word in string_of_banned_words:
    while banned_word in text:
        length_of_banned_word = len(banned_word)
        text = text.replace(banned_word, length_of_banned_word * "*")
print(text)


# string_of_banned_words = input().split(", ")
# text = input()
# for banned_word in string_of_banned_words:
#     length_of_banned_word = len(banned_word)
#     text = text.replace(banned_word, length_of_banned_word * "*")
# print(text)
