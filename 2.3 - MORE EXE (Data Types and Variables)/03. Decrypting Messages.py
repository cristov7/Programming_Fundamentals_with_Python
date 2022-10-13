# key = int(input())
# count_rows = int(input())
# for rows in range(1, count_rows + 1):
#     letter = ord(input()) + key
#     update_letter = chr(letter)
#     print(update_letter, end="")


key = int(input())
count_rows = int(input())
for letters in range(1, count_rows + 1):
    input_letter = input()
    letter_as_ord = ord(input_letter)
    update_letter_as_ord = letter_as_ord + key
    letter_as_chr = chr(update_letter_as_ord)
    print(letter_as_chr, end="")
