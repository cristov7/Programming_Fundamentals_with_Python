resource_quantity = {}
while True:
    command = input()
    if command == "stop":
        break
    else:
        resource = command
        quantity = int(input())
        if resource not in resource_quantity:
            resource_quantity[resource] = quantity
        else:
            resource_quantity[resource] += quantity
for resource, quantity in resource_quantity.items():
    print(f"{resource} -> {quantity}")


# miner_task = {}
# while True:
#     command = input()
#     if command == "stop":
#         break
#     else:
#         current_resource = command
#         current_quantity = int(input())
#         if current_resource not in miner_task:   # if current_resource not in miner_task.keys():
#             miner_task[current_resource] = current_quantity
#         else:
#             miner_task[current_resource] += current_quantity
# for resource, quantity in miner_task.items():
#     print(f"{resource} -> {quantity}")


# resources = {}
# while True:
#     current_resource = input()
#     if current_resource == "stop":
#         break
#     current_quantity = int(input())
#     if current_resource not in resources.keys():
#         resources[current_resource] = 0
#     resources[current_resource] += current_quantity
# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")
