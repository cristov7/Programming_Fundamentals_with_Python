import re
regex = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
text = input()
destination_list = []
total_points = 0
places_list = re.findall(regex, text)
if places_list:
    for some_tuple in places_list:
        for place in some_tuple:
            if len(place) >= 3:
                destination_list.append(place)
                points = len(place)
                total_points += points
            else:
                continue
    print(f"Destinations: {', '.join(destination_list)}\nTravel Points: {total_points}")
else:
    print(f"Destinations:\nTravel Points: {total_points}")


# import re
# regex = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
# text = input()
# destination_list = []
# total_points = 0
# places_list = re.findall(regex, text)
# for some_tuple in places_list:
#     if len(some_tuple[1]) >= 3:
#         destination_list.append(some_tuple[1])
#         points = len(some_tuple[1])
#         total_points += points
#     else:
#         continue
# print(f"Destinations: {', '.join(destination_list)}\nTravel Points: {total_points}")
