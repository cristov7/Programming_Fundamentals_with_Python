text = input().replace(" ", "")
my_dict = {}
for symbol in text:
    count_symbol = text.count(symbol)
    my_dict[symbol] = count_symbol
for current_symbol, count in my_dict.items():
    print(f"{current_symbol} -> {count}")


# current_input = input().split()
# symbols = ''.join(current_input)
# letters = {}
# for symbol in symbols:
#     if symbol not in letters.keys():
#         letters[symbol] = 0
#     letters[symbol] += 1
# for char, occurrences in letters.items():
#     print(f"{char} -> {occurrences}")


# text = "".join(input().split(" "))
# my_dict = {}
# for symbol in text:
#     count_symbol = text.count(symbol)
#     my_dict[symbol] = count_symbol
# for current_symbol, current_count in my_dict.items():
#     print(f"{current_symbol} -> {current_count}")
