import re
some_string = input()
regex = r"\b_([A-Za-z0-9]+)\b"
result_list = re.findall(regex, some_string)
print(",".join(result_list))   # print(*result_list, sep=",")


# import re
# some_string = input()
# regex = r"\b_[A-Za-z0-9]+\b"
# result_list = re.findall(regex, some_string)
# convert_result_list = [result[1:] for result in result_list]
# print(",".join(convert_result_list))   # print(*convert_result_list, sep=",")


# some_string = input().split()
# result_list = []
# for element in some_string:
#     first_char = element[0]
#     other_chars = element[1:]
#     if first_char == "_" and other_chars.isalpha():
#         result_list.append(other_chars)
#     else:
#         continue
# print(",".join(result_list))


# import re
# some_string = input()
# result_list = list()
# split_regex_list = re.split("\s", some_string)
# for element in split_regex_list:
#     first_char = element[0]
#     other_chars = element[1:]
#     if first_char == "_" and other_chars.isalpha():
#         result_list.append(other_chars)
#     else:
#         continue
# print(",".join(result_list))
