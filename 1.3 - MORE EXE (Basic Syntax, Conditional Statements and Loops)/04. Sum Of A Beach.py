input_string = input().lower()
list_of_letters = []
for char in input_string:
    list_of_letters.append(char)
counter = 0
while True:
    if "s" in list_of_letters and "a" in list_of_letters and "n" in list_of_letters and "d" in list_of_letters:
        counter += 1
        list_of_letters.remove("s")
        list_of_letters.remove("a")
        list_of_letters.remove("n")
        list_of_letters.remove("d")
    elif "w" in list_of_letters and "a" in list_of_letters and "t" in list_of_letters and "e" in list_of_letters and "r" in list_of_letters:
        counter += 1
        list_of_letters.remove("w")
        list_of_letters.remove("a")
        list_of_letters.remove("t")
        list_of_letters.remove("e")
        list_of_letters.remove("r")
    elif "f" in list_of_letters and "i" in list_of_letters and "s" in list_of_letters and "h" in list_of_letters:
        counter += 1
        list_of_letters.remove("f")
        list_of_letters.remove("i")
        list_of_letters.remove("s")
        list_of_letters.remove("h")
    elif "s" in list_of_letters and "u" in list_of_letters and "n" in list_of_letters:
        counter += 1
        list_of_letters.remove("s")
        list_of_letters.remove("u")
        list_of_letters.remove("n")
    else:
        print(counter)
        break
