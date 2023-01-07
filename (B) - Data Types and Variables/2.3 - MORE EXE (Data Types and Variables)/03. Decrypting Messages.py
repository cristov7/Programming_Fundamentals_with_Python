key = int(input())
message_list = []
count_rows = int(input())
for row in range(1, count_rows + 1):
    letter = input()
    ord_letter = ord(letter)
    new_ord_letter = ord_letter + key
    new_letter = chr(new_ord_letter)
    message_list.append(new_letter)
print("".join(message_list))


# key = int(input())
# count_rows = int(input())
# for rows in range(1, count_rows + 1):
#     letter = ord(input()) + key
#     update_letter = chr(letter)
#     print(update_letter, end="")


# key = int(input())
# count_rows = int(input())
# for letters in range(1, count_rows + 1):
#     input_letter = input()
#     letter_as_ord = ord(input_letter)
#     update_letter_as_ord = letter_as_ord + key
#     letter_as_chr = chr(update_letter_as_ord)
#     print(letter_as_chr, end="")
