words_list = [element.lower() for element in input().split()]
dictionary = {}
for word in words_list:
    count_word = words_list.count(word)
    if count_word % 2:
        dictionary[word] = f" {count_word} times"
    else:
        continue
for key in dictionary:   # for key in dictionary.keys():
    print(key, end=" ")


# words = input().split()
# dictionary = {}
# for word in words:
#     word_lower = word.lower()
#     if word_lower not in dictionary:
#         dictionary[word_lower] = 0
#     dictionary[word_lower] += 1
# for key, value in dictionary.items():
#     if value % 2:
#         print(key, end=" ")
