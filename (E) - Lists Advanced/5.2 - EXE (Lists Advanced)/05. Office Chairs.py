count_rooms = int(input())
total_count_chairs = 0
total_count_visitors = 0
game_on = True
for number_of_room in range(1, count_rooms + 1):
    chairs_and_visitors_info = input()
    info_list = chairs_and_visitors_info.split()
    count_chairs = len(info_list[0])
    count_visitors = int(info_list[1])
    total_count_chairs += count_chairs
    total_count_visitors += count_visitors
    if count_chairs < count_visitors:
        needed_chairs_in_room = abs(count_chairs - count_visitors)
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")
        game_on = False
    else:
        continue
if game_on:
    total_free_chairs = abs(total_count_chairs - total_count_visitors)
    print(f"Game On, {total_free_chairs} free chairs left")


# def check_the_rooms(number: int):
#     total_count_free_chairs = 0
#     total_count_needed_chairs = 0
#     for room in range(1, number + 1):
#         chairs, visitors = input().split()
#         diff = len(chairs) - int(visitors)
#         if diff > 0:
#             total_count_free_chairs += diff
#         elif diff == 0:
#             continue
#         else:
#             total_count_needed_chairs += abs(diff)
#             print(f"{abs(diff)} more chairs needed in room {room}")
#     return total_count_free_chairs, total_count_needed_chairs
#
#
# number_of_rooms = int(input())
# free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
# if free_chairs >= needed_chairs:
#     print(f"Game On, {free_chairs} free chairs left")
