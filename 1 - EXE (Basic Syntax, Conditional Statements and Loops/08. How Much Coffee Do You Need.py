# count_coffee = 0
# while True:
#     command = input()
#     if command == "END":
#         print(count_coffee)
#         break
#     elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
#         count_coffee += 1
#         if count_coffee > 5:
#             print("You need extra sleep")
#             break
#         else:
#             continue
#     elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
#         count_coffee += 2
#         if count_coffee > 5:
#             print("You need extra sleep")
#             break
#         else:
#             continue
#     else:
#         continue


# count_coffees = 0
# lower_command = ("coding", "dog", "cat", "movie")
# upper_command = ("CODING", "DOG", "CAT", "MOVIE")
# while True:
#     command = input()
#     if command == "END":
#         print(count_coffees)
#         break
#     elif command in lower_command:
#         count_coffees += 1
#         if count_coffees > 5:
#             print("You need extra sleep")
#             break
#         else:
#             continue
#     elif command in upper_command:
#         count_coffees += 2
#         if count_coffees > 5:
#             print("You need extra sleep")
#             break
#         else:
#             continue
#     else:
#         continue


coffee_counter = 0
command = input()
while command != "END":
    if command.upper() == "CODING" \
            or command.upper() == "DOG" \
            or command.upper() == "CAT" \
            or command.upper() == "MOVIE":
        if command.islower():
            coffee_counter += 1
        else: #command.isupper()
            coffee_counter += 2
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)
