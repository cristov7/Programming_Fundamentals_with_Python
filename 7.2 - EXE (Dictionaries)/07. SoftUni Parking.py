parking = {}
count_command = int(input())
for command in range(1, count_command + 1):
    info = input().split()
    registration = info[0]
    if registration == "register":
        username = info[1]
        license_plate_number = info[2]
        if username not in parking.keys():  # if username not in parking:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    else:   # elif registration == "unregister":
        username = info[1]
        if username in parking.keys():   # if username not in parking:
            del parking[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")


# parking = {}
# number_of_cars = int(input())
# for car in range(number_of_cars):
#     current_driver = input().split()
#     action = current_driver[0]
#     if action == "register":
#         username = current_driver[1]
#         license_plate_number = current_driver[2]
#         if username in parking.keys():
#             print(f"ERROR: already registered with plate number {license_plate_number}")
#         else:
#             parking[username] = license_plate_number
#             print(f"{username} registered {license_plate_number} successfully")
#     elif action == "unregister":
#         username = current_driver[1]
#         if username not in parking.keys():
#             print(f"ERROR: user {username} not found")
#         else:
#             print(f"{username} unregistered successfully")
#             del parking[username]
# for username, license_plate_number in parking.items():
#     print(f"{username} => {license_plate_number}")
