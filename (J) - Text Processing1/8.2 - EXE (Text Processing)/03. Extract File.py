file_info = input().split("\\")
important_info = file_info[-1]
important_info_list = important_info.split(".")
file_name = important_info_list[0]
file_extension = important_info_list[1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")


# file = input().split(".")
# file_extension = file[-1]
# other_info = file[0]
# length_of_other_info = len(other_info)
# reversed_file_name = ""
# for index in range(-1, -length_of_other_info - 1, -1):
#     current_symbol = other_info[index]
#     if current_symbol == "\\":
#         break
#     else:
#         reversed_file_name += current_symbol
# file_name = reversed_file_name[::-1]
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")


# path_to_file_list = input().split("\\")
# info = path_to_file_list[-1]
# extract_file_list = info.split(".")
# file_name = extract_file_list[0]
# file_extension = extract_file_list[1]
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")
