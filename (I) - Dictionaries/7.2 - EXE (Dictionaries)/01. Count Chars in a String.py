chars = input().split()
char_and_counter = {}
for element in chars:
    for char in element:
        if char not in char_and_counter:
            char_and_counter[char] = 1
        else:
            char_and_counter[char] += 1
for char, value in char_and_counter.items():
    print(f"{char} -> {value}")


# text = input().replace(" ", "")
# my_dict = {}
# for symbol in text:
#     count_symbol = text.count(symbol)
#     my_dict[symbol] = count_symbol
# for current_symbol, count in my_dict.items():
#     print(f"{current_symbol} -> {count}")


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
