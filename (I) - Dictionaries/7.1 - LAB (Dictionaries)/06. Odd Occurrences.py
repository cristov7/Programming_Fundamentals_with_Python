words = [word.lower() for word in input().split()]
word_and_counter = {}
for word in words:
    if word not in word_and_counter.keys():
        count_word = words.count(word)
        word_and_counter[word] = count_word
    else:
        continue
for word, number in word_and_counter.items():
    if number % 2:
        print(f"{word}", end=" ")
    else:
        continue


# words_list = [element.lower() for element in input().split()]
# dictionary = {}
# for word in words_list:
#     count_word = words_list.count(word)
#     if count_word % 2:
#         dictionary[word] = f" {count_word} times"
#     else:
#         continue
# for key in dictionary:   # for key in dictionary.keys():
#     print(key, end=" ")


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
