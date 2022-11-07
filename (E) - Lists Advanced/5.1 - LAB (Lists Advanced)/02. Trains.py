count_wagons = int(input())
wagon = [0 for current_wagon in range(count_wagons)]
while True:
    command = input()
    if command == "End":
        print(wagon)
        break
    else:
        command_list = command.split(" ")
        current_command = command_list[0]
        if current_command == "add":
            people_to_add = int(command_list[1])
            wagon[-1] += people_to_add
        elif current_command == "insert":
            index_per_wagon = int(command_list[1])
            people_to_insert = int(command_list[2])
            wagon[index_per_wagon] += people_to_insert
        elif current_command == "leave":
            index_per_wagon = int(command_list[1])
            people_to_leave = int(command_list[2])
            wagon[index_per_wagon] -= people_to_leave


# count_wagons = int(input())
# wagon = [0 for current_wagon in range(count_wagons)]
# while True:
#     command = input()
#     if command == "End":
#         print(wagon)
#         break
#     else:
#         command_list = command.split(" ")
#         if command_list[0] == "add":
#             wagon[-1] += int(command_list[1])
#         elif command_list[0] == "insert":
#             wagon[int(command_list[1])] += int(command_list[2])
#         elif command_list[0] == "leave":
#             wagon[int(command_list[1])] -= int(command_list[2])


# count_wagon = int(input())
# train = []
# for wagon in range(1, count_wagon + 1):
#     train.append(0)
# while True:
#     command = input()
#     if command == "End":
#         break
#     else:
#         command_list = command.split(" ")
#         if command_list[0] == "add":
#             train[-1] += int(command_list[1])
#         elif command_list[0] == "insert":
#             train[int(command_list[1])] += int(command_list[2])
#         elif command_list[0] == "leave":
#             train[int(command_list[1])] -= int(command_list[2])
# print(train)


# number = int(input())
# wagon = [0] * number
# while True:
#     command = input()
#     if command == "End":
#         break
#     split_command = command.split(" ")
#     current_command = split_command[0]
#     if current_command == "add":
#         people_to_add = int(split_command[1])
#         wagon[-1] += people_to_add
#     elif current_command == "insert":
#         index = int(split_command[1])
#         people_to_insert = int(split_command[2])
#         wagon[index] += people_to_insert
#     elif current_command == "leave":
#         index = int(split_command[1])
#         people_to_leave = int(split_command[2])
#         wagon[index] -= people_to_leave
# print(wagon)
