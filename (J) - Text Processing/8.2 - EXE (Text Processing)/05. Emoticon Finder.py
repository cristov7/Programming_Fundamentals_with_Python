text = input()
for index, value in enumerate(text):
    if value == ":":
        emoticon = value + text[index + 1]
        print(emoticon)
    else:
        continue


# text = input()
# for index in range(len(text)):
#     if text[index] == ":":   # if single_string[index] == ":" and index +1 <= len(text):
#         print(f":{text[index + 1]}")
#     else:
#         continue
