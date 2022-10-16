def loading_bar(number: int):
    percent = number
    count_percents = percent // 10
    count_points = 10 - count_percents
    add_percent = count_percents * "%"
    add_points = count_points * "."
    combination = add_percent + add_points
    if percent == 100:
        return f"{percent}% Complete!\n[{combination}]"
    else:
        return f"{percent}% [{combination}]\nStill loading..."


input_number = int(input())
print(loading_bar(input_number))


# def status(number):
#     if number == 100:
#         return "100% Complete!\n[%%%%%%%%%%]"
#     return f"{number}% [{'%' * (number // 10)}{'.' * (10 - (number // 10))}]\nStill loading..."
#
#
# single_number = int(input())
# print(status(single_number))
