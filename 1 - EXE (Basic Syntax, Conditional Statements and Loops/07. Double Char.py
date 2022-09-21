while True:
    current_string = input()
    if current_string == "End":
        break
    elif current_string == "SoftUni":
        continue
    else:
        translated_string = ""
        for symbol in current_string:
            double_symbol = 2 * symbol
            translated_string += double_symbol
        print(translated_string)
