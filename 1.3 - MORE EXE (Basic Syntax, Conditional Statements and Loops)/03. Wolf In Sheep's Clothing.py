animals_in_list = input().split(", ")
animals_in_list.reverse()
if animals_in_list[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    sheep_in_danger = 0
    for index, value in enumerate(animals_in_list):
        if value == "wolf":
            print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")
            break
        else:
            sheep_in_danger += 1
            continue


# animals_in_list = input().split(", ")
# if animals_in_list[-1] == "wolf":
#     print("Please go away and stop eating my sheep")
# else:
#     while True:
#         if animals_in_list[0] == "sheep":
#             animals_in_list.remove("sheep")
#         else:
#             sheep_in_danger = len(animals_in_list) - 1
#             print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")
#             break
