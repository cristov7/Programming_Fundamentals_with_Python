journal = input().split(", ")
while True:
    command = input()
    if command == "Craft!":
        break
    else:
        command_list = command.split(" - ")
        info = command_list[0]
        item = command_list[1]
        if info == "Collect":
            if item in journal:
                continue
            else:
                journal.append(item)
        elif info == "Drop":
            if item in journal:
                journal.remove(item)
            else:
                continue
        elif info == "Combine Items":
            item_list = item.split(":")
            old_item = item_list[0]
            new_item = item_list[1]
            if old_item in journal:
                index_per_old_item = journal.index(old_item)
                journal.insert(index_per_old_item + 1, new_item)
            else:
                continue
        elif info == "Renew":
            if item in journal:
                index_per_item = journal.index(item)
                pop = journal.pop(index_per_item)
                journal.append(pop)
            else:
                continue
print(", ".join(journal))


# def inventory(something):
#     while True:
#         command = input()
#         if command == "Craft!":
#             break
#         else:
#             command_list = command.split(" - ")
#             info = command_list[0]
#             item = command_list[1]
#             if info == "Collect":
#                 if item in something:
#                     continue
#                 else:
#                     something.append(item)
#             elif info == "Drop":
#                 if item in something:
#                     something.remove(item)
#                 else:
#                     continue
#             elif info == "Combine Items":
#                 item_list = item.split(":")
#                 old_item = item_list[0]
#                 new_item = item_list[1]
#                 if old_item in something:
#                     index_per_old_item = something.index(old_item)
#                     something.insert(index_per_old_item + 1, new_item)
#                 else:
#                     continue
#             elif info == "Renew":
#                 if item in something:
#                     index_per_item = something.index(item)
#                     pop = something.pop(index_per_item)
#                     something.append(pop)
#                 else:
#                     continue
#     return ", ".join(something)
#
#
# journal = input().split(", ")
# print(inventory(journal))


# def inventory(items):
#     while True:
#         command_data = input()
#         if command_data == "Craft!":
#             break
#         command, product = command_data.split(" - ")
#         if command == "Collect":
#             if product not in items:
#                 items.append(product)
#         elif command == "Drop":
#             if product in items:
#                 items.remove(product)
#         elif command == "Combine Items":
#             old_item, new_item = product.split(":")
#             if old_item in items:
#                 old_item_index = items.index(old_item)
#                 items.insert(old_item_index + 1, new_item)
#         elif command == "Renew":
#             if product in items:
#                 items.remove(product)
#                 items.append(product)
#     return ", ".join(items)
#
#
# data = input().split(", ")
# print(inventory(data))
