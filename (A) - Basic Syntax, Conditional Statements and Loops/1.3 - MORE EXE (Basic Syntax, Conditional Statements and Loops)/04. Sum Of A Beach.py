single_string = input().lower()
beach_list = ["sand", "water", "fish", "sun"]
total = 0
for element in beach_list:
    result = single_string.count(element)
    total += result
print(total)


# input_string = input().lower()
# counter_sand = input_string.count("sand")
# counter_water = input_string.count("water")
# counter_fish = input_string.count("fish")
# counter_sun = input_string.count("sun")
# how_many_times = counter_sand + counter_water + counter_fish + counter_sun
# print(how_many_times)


# input_string = input().lower()
# list_of_letters = []
# for char in input_string:
#     list_of_letters.append(char)
# counter = 0
# while True:
#     if "s" in list_of_letters and "a" in list_of_letters and "n" in list_of_letters and "d" in list_of_letters:
#         counter += 1
#         list_of_letters.remove("s")
#         list_of_letters.remove("a")
#         list_of_letters.remove("n")
#         list_of_letters.remove("d")
#     elif "w" in list_of_letters and "a" in list_of_letters and "t" in list_of_letters and "e" in list_of_letters and "r" in list_of_letters:
#         counter += 1
#         list_of_letters.remove("w")
#         list_of_letters.remove("a")
#         list_of_letters.remove("t")
#         list_of_letters.remove("e")
#         list_of_letters.remove("r")
#     elif "f" in list_of_letters and "i" in list_of_letters and "s" in list_of_letters and "h" in list_of_letters:
#         counter += 1
#         list_of_letters.remove("f")
#         list_of_letters.remove("i")
#         list_of_letters.remove("s")
#         list_of_letters.remove("h")
#     elif "s" in list_of_letters and "u" in list_of_letters and "n" in list_of_letters:
#         counter += 1
#         list_of_letters.remove("s")
#         list_of_letters.remove("u")
#         list_of_letters.remove("n")
#     else:
#         print(counter)
#         break
