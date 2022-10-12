animals_in_list = input().split(", ")
if animals_in_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    while True:
        if animals_in_list[0] == "sheep":
            animals_in_list.remove("sheep")
        else:
            sheep_in_danger = len(animals_in_list) - 1
            print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")
            break
