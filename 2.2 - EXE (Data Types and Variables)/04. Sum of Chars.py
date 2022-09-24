count_rows = int(input())
sum_symbols = 0
for row in range(1, count_rows + 1):
    symbol = input()
    sum_symbols += ord(symbol)
print(f"The sum equals: {sum_symbols}")
