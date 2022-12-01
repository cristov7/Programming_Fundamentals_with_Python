import re
text = input()
word = input()
regex = fr"\b{word}\b"
result_list = re.findall(regex, text, re.IGNORECASE)   # re.I
print(len(result_list))


# import re
# text = input()
# word = input()
# regex = fr"(?i)\b{word}\b"
# result_list = re.findall(regex, text, re.IGNORECASE)   # re.I
# print(len(result_list))
