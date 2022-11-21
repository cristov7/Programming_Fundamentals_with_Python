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
count_unique_symbols = len(set(convert_text))
print(f"Unique symbols used: {count_unique_symbols}")
print(convert_text)
