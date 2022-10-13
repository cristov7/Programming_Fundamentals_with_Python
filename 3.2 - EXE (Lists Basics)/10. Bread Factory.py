events = input().split("|")
total_coins = 100
total_energy = 100
factory_is_open = True
for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value = int(event_items[1])
    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            factory_is_open = False
            break
if factory_is_open:  # if factory_is_open == True:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")


# events_per_day = input()   # "{event/ingredient}-{number}"
# even_list = events_per_day.split("|")
# closed_bakery = False
# total_energy = 100
# total_coins = 100
# event_type_list = []
# event_value_list = []
# for even in even_list:
#     current_event = even.split("-")
#     event_type = current_event[0]
#     event_value = int(current_event[1])
#     event_type_list.append(event_type)
#     event_value_list.append(event_value)
# for index, element in enumerate(event_type_list):
#     if closed_bakery:   # if closed_bakery == True:
#         break
#     else:
#         if index < len(event_type_list):
#             if element == "rest":
#                 if total_energy + event_value_list[index] > 100:
#                     print("You gained 0 energy.")
#                     print(f"Current energy: {total_energy}.")
#                 else:
#                     total_energy += event_value_list[index]
#                     print(f"You gained {event_value_list[index]} energy.")
#                     print(f"Current energy: {total_energy}.")
#             elif element == "order":
#                 if total_energy - 30 >= 0:
#                     total_coins += event_value_list[index]
#                     print(f"You earned {event_value_list[index]} coins.")
#                     total_energy -= 30
#                 else:
#                     total_energy += 50
#                     print("You had to rest!")
#             else:
#                 if total_coins - event_value_list[index] >= 0:
#                     total_coins -= event_value_list[index]
#                     print(f"You bought {event_type_list[index]}.")
#                 else:
#                     print(f"Closed! Cannot afford {event_type_list[index]}.")
#                     closed_bakery = True
#         else:
#             break
# if not closed_bakery:
#     print("Day completed!")
#     print(f"Coins: {total_coins}")
#     print(f"Energy: {total_energy}")
