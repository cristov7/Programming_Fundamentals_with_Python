legendary_farming = {"shards": 0, "fragments": 0, "motes": 0}
points_legendary_item = 250
obtained = False
while True:
    if obtained:
        break
    else:
        items_list = input().split()
        quantity = None
        for item in items_list:
            if item.isdigit():
                quantity = int(item)
            else:
                material = item.lower()
                if material not in legendary_farming:
                    legendary_farming[material] = quantity
                else:
                    legendary_farming[material] += quantity
                if legendary_farming["shards"] >= points_legendary_item:
                    name_legendary_item = "Shadowmourne"
                    print(f"{name_legendary_item} obtained!")
                    legendary_farming["shards"] -= points_legendary_item
                    obtained = True
                    break
                elif legendary_farming["fragments"] >= points_legendary_item:
                    name_legendary_item = "Valanyr"
                    print(f"{name_legendary_item} obtained!")
                    legendary_farming["fragments"] -= points_legendary_item
                    obtained = True
                    break
                elif legendary_farming["motes"] >= points_legendary_item:
                    name_legendary_item = "Dragonwrath"
                    print(f"{name_legendary_item} obtained!")
                    legendary_farming["motes"] -= points_legendary_item
                    obtained = True
                    break
for material, quantity in legendary_farming.items():
    print(f"{material}: {quantity}")


# items = {"shards": 0, "fragments": 0, "motes": 0}
# current_items = input().split()
# obtained = False
# while not obtained:
#     for index in range(0, len(current_items), 2):
#         value = int(current_items[index])
#         key = current_items[index + 1].lower()
#         if key not in items.keys():
#             items[key] = 0
#         items[key] += value
#         if items["shards"] >= 250:
#             print("Shadowmourne obtained!")
#             items["shards"] -= 250
#             obtained = True
#         elif items["fragments"] >= 250:
#             print("Valanyr obtained!")
#             items["fragments"] -= 250
#             obtained = True
#         elif items["motes"] >= 250:
#             print("Dragonwrath obtained!")
#             items["motes"] -= 250
#             obtained = True
#         if obtained:
#             break
#     if obtained:
#         break
#     current_items = input().split()
# for material, quantity in items.items():
#     print(f"{material}: {quantity}")
