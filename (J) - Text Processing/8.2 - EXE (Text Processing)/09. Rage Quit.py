data = input().upper()
convert_text = ""
part_of_convert_text = ""
number = ""
for index in range(len(data)):
    if not data[index].isdigit():
        part_of_convert_text += data[index]
    else:
        number += data[index]
        if index + 1 < len(data):
            if data[index + 1].isdigit():
                continue
            else:
                total_number = int(number)
                convert_text += part_of_convert_text * total_number
                part_of_convert_text = ""
                number = ""
        else:
            total_number = int(number)
            convert_text += part_of_convert_text * total_number
            part_of_convert_text = ""
            number = ""
unique_symbols = set(convert_text)
count_unique_symbols = len(unique_symbols)
print(f"Unique symbols used: {count_unique_symbols}")
print(convert_text)


# def rage_quiz(information):
#     info = information.upper()
#     convert_text = ""
#     part_of_convert_text = ""
#     number = ""
#     for index in range(len(info)):
#         if not info[index].isdigit():
#             part_of_convert_text += info[index]
#         else:
#             number += info[index]
#             if index + 1 < len(info):
#                 if info[index + 1].isdigit():
#                     continue
#                 else:
#                     total_number = int(number)
#                     convert_text += part_of_convert_text * total_number
#                     part_of_convert_text = ""
#                     number = ""
#             else:
#                 total_number = int(number)
#                 convert_text += part_of_convert_text * total_number
#                 part_of_convert_text = ""
#                 number = ""
#     unique_symbols = set(convert_text)
#     count_unique_symbols = len(unique_symbols)
#     return f"Unique symbols used: {count_unique_symbols}\n{convert_text}"
# 
# 
# data = input().upper()
# result = rage_quiz(data)
# print(result)
