number = int(input())
for string in range(1, number + 1):
    current_string = input()
    """substring -> slicing"""
    name_start_index = current_string.index("@") + 1
    name_end_index = current_string.index("|")
    name = current_string[name_start_index: name_end_index]
    age_start_index = current_string.index("#") + 1
    age_end_index = current_string.index("*")
    age = int(current_string[age_start_index: age_end_index])
    print(f"{name} is {age} years old.")
