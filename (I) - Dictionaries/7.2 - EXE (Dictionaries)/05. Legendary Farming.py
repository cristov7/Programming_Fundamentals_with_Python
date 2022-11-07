items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
obtained = False
while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    current_items = input().split()
for material, quantity in items.items():
    print(f"{material}: {quantity}")


# items = {"shards": 0, "fragments": 0, "motes": 0}
# legendary_item_points = 250
# legendary_farming = False
# while True:
#     if legendary_farming:   # if legendary_farming == True:
#         break
#     else:
#         current_items = input().split()
#         available_items = {}
#         for index in range(0, len(current_items), 2):
#             name_of_item = current_items[index + 1]
#             quantity_of_item = int(current_items[index])
#             if name_of_item not in available_items:   # if name_of_item not in available_items.keys():
#                 available_items[name_of_item] = quantity_of_item
#             else:
#                 available_items[name_of_item] += quantity_of_item
#         for item, quantity in available_items.items():
#             if item.lower() == "shards":
#                 items["shards"] += quantity
#                 if items["shards"] >= legendary_item_points:
#                     items["shards"] -= legendary_item_points
#                     legendary_item_name = "Shadowmourne"
#                     print(f"{legendary_item_name} obtained!")
#                     legendary_farming = True
#                     break
#                 else:
#                     continue
#             elif item.lower() == "fragments":
#                 items["fragments"] += quantity
#                 if items["fragments"] >= legendary_item_points:
#                     items["fragments"] -= legendary_item_points
#                     legendary_item_name = "Valanyr"
#                     print(f"{legendary_item_name} obtained!")
#                     legendary_farming = True
#                     break
#                 else:
#                     continue
#             elif item.lower() == "motes":
#                 items["motes"] += quantity
#                 if items["motes"] >= legendary_item_points:
#                     items["motes"] -= legendary_item_points
#                     legendary_item_name = "Dragonwrath"
#                     print(f"{legendary_item_name} obtained!")
#                     legendary_farming = True
#                     break
#                 else:
#                     continue
#             else:
#                 if item not in items:   # if item not in items.keys():
#                     items[item] = quantity
#                 else:
#                     items[item] += quantity
# for item, quantity in items.items():
#     print(f"{item}: {quantity}")
