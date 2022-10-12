count_rows = int(input())
sum_symbols = 0
for row in range(1, count_rows + 1):
    symbol = input()
    sum_symbols += ord(symbol)
print(f"The sum equals: {sum_symbols}")


# ascii_table_list = []
# number = int(input())
# for letter in range(1, number + 1):
#     current_letter = ord(input())
#     ascii_table_list.append(current_letter)
# print(f"The sum equals: {sum(ascii_table_list)}")
