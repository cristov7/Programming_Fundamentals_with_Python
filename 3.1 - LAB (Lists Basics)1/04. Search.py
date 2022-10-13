# number = int(input())
# secret_word = input()
# my_list = []
# for words in range(1, number + 1):
#     word = input()
#     my_list.append(word)
# print(my_list)
# for index in range(len(my_list)-1, -1, -1):
#     element = my_list[index]
#     if secret_word not in element:
#         my_list.remove(element)
#     else:
#         continue
# print(my_list)


number = int(input())
secret_word = input()
my_first_list = []
my_second_list = []
for words in range(1, number + 1):
    word = input()
    my_first_list.append(word)
    if secret_word not in word:
        continue
    else:   # secret_word in word
        my_second_list.append(word)
print(my_first_list)
print(my_second_list)


# my_list = []
# number = int(input())
# word = input()
# for random_strings in range(1, number + 1):
#     some_string = input()
#     my_list.append(some_string)
# print(my_list)
# my_second_list = my_list.copy()
# for element in my_second_list:
#     if word in element:
#         continue
#     else:
#         my_second_list.remove(element)
# print(my_second_list)
