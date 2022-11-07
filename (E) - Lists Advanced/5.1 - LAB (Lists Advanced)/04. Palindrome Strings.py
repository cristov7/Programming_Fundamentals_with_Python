words_separated_by_space = input()
palindrome_word = input()
words_in_list = words_separated_by_space.split(" ")   # .split()
palindrome_list = [palindrome for palindrome in words_in_list if palindrome == palindrome[::-1]]
counter_palindrome_word_in_palindrome_list = palindrome_list.count(palindrome_word)
print(palindrome_list)
print(f"Found palindrome {counter_palindrome_word_in_palindrome_list} times")


# def palindrome_strings(word: str):
#     if word == word[::-1]:
#         return word
#
#
# text = input().split()
# palindrome = input()
# palindrome_list = [element for element in text if palindrome_strings(element)]
# palindrome_counter = palindrome_list.count(palindrome)
# print(palindrome_list)
# print(f"Found palindrome {palindrome_counter} times")
