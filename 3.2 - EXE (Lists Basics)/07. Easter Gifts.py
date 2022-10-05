names_of_the_gifts_as_string = input()
names_of_the_gifts_as_string_in_list = names_of_the_gifts_as_string.split()   # .split(" ")
command = input()
while command != "No Money":
    gift_list = command.split()
    if "OutOfStock" in gift_list:
        for index, value in enumerate(names_of_the_gifts_as_string_in_list):
            if value == gift_list[1]:
                names_of_the_gifts_as_string_in_list[index] = "None"
    elif "Required" in gift_list:
        replacing_index = int(gift_list[2])
        if replacing_index >= len(names_of_the_gifts_as_string_in_list) or replacing_index < 0:
            command = input()
            continue
        names_of_the_gifts_as_string_in_list[replacing_index] = gift_list[1]
    elif "JustInCase" in gift_list:
        names_of_the_gifts_as_string_in_list[-1] = gift_list[1]
    command = input()
while "None" in names_of_the_gifts_as_string_in_list:
    for index, value in enumerate(names_of_the_gifts_as_string_in_list):
        if value == "None":
            names_of_the_gifts_as_string_in_list.remove(names_of_the_gifts_as_string_in_list[index])
print(*names_of_the_gifts_as_string_in_list)   # * = " ".join()
