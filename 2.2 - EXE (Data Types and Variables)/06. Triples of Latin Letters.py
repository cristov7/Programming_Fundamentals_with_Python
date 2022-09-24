# count_symbols = int(input())
# for first_symbol in range(count_symbols):
#     for second_symbol in range(count_symbols):
#         for third_symbol in range(count_symbols):
#             print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")


count_symbols = int(input())
start_symbol = 97
final_symbol = 97 + (count_symbols - 1)
for first_symbol in range(start_symbol, final_symbol + 1):
    for second_symbol in range(start_symbol, final_symbol + 1):
        for third_symbol in range(start_symbol, final_symbol + 1):
            print(chr(first_symbol), end="")
            print(chr(second_symbol), end="")
            print(chr(third_symbol))
