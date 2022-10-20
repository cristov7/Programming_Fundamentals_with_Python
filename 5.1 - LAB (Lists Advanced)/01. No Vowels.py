text = input()
vowels = ["a", "o", "u", "e", "i"]
result = [char for char in text if char.lower() not in vowels]
print("".join(result))   # print(*result, sep="")


# text = input()
# vowels = ["a", "o", "u", "e", "i"]
# result = []
# for char in text:
#     if char.lower() not in vowels:
#         result.append(char)
#     else:
#         continue
# print("".join(result))   # print(*result, sep="")


# text = input()
# vowels = ["a", "o", "u", "e", "i"]
# result = ""
# for char in text:
#     if char.lower() not in vowels:
#         result += char
#     else:
#         continue
# print("".join(result))   # print(*result, sep="")


# text = input()
# vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
# no_vowels = ("".join([x for x in text if x not in vowels]))
# print(no_vowels)
