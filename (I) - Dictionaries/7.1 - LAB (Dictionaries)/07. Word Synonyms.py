word_synonyms = {}   # key = word, value = list of synonyms
count_words = int(input())
for word_and_synonym in range(1, count_words + 1):
    word = input()
    synonym = input()
    if word not in word_synonyms.keys():
        word_synonyms[word] = [synonym]
    else:
        word_synonyms[word].append(synonym)
for word, synonyms in word_synonyms.items():
    print(f"{word} - {', '.join(synonyms)}")


# count_words = int(input())
# dictionary = {}
# for word_and_synonym in range(1, count_words + 1):
#     word = input()
#     synonym = input()
#     if word not in dictionary:   # if word not in dictionary:
#         dictionary[word] = [synonym]
#     else:
#         dictionary[word].append(synonym)
# for current_word, current_synonym in dictionary.items():
#     print(f"{current_word} - {', '.join(current_synonym)}")


# number = int(input())
# synonyms = {}
# for _ in range(number):
#     word = input()
#     synonym = input()
#     if word not in synonyms:
#         synonyms[word] = []
#     synonyms[word].append(synonym)
# for current_synonym in synonyms:
#     print(f"{current_synonym} - {', '.join(synonyms[current_synonym])}")
