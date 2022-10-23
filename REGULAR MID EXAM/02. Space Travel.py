travel_route_to_titan = input().split("||")
the_starting_amount_of_fuel = int(input())
the_starting_amount_of_ammunition = int(input())
for element in range(len(travel_route_to_titan)):
    info = travel_route_to_titan[element].split()
    command = info[0]
    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    else:
        if command == "Travel":
            light_years = int(info[1])
            the_starting_amount_of_fuel -= light_years
            if the_starting_amount_of_fuel >= 0:
                print(f"The spaceship travelled {light_years} light-years.")
            else:
                print("Mission failed.")
                break
        elif command == "Enemy":
            enemy_armour = int(info[1])
            if the_starting_amount_of_ammunition >= enemy_armour:
                the_starting_amount_of_ammunition -= enemy_armour
                print(f"An enemy with {enemy_armour} armour is defeated.")
            else:
                the_starting_amount_of_fuel -= enemy_armour * 2
                if the_starting_amount_of_fuel >= 0:
                    print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
                else:
                    print("Mission failed.")
                    break
        elif command == "Repair":
            number_of_ammunition_and_fuel_added = int(info[1])
            fuel_added = number_of_ammunition_and_fuel_added
            ammunition_added = number_of_ammunition_and_fuel_added * 2
            the_starting_amount_of_fuel += ammunition_added
            the_starting_amount_of_ammunition += fuel_added
            print(f"Ammunitions added: {ammunition_added}.")
            print(f"Fuel added: {fuel_added}.")


# def space_travel(travel_route_to_titan, the_starting_amount_of_fuel, the_starting_amount_of_ammunition):
#     for element in range(len(travel_route_to_titan)):
#         info = travel_route_to_titan[element].split()
#         command = info[0]
#         if command == "Titan":
#             print("You have reached Titan, all passengers are safe.")
#             break
#         else:
#             if command == "Travel":
#                 light_years = int(info[1])
#                 the_starting_amount_of_fuel -= light_years
#                 if the_starting_amount_of_fuel >= 0:
#                     print(f"The spaceship travelled {light_years} light-years.")
#                 else:
#                     print("Mission failed.")
#                     break
#             elif command == "Enemy":
#                 enemy_armour = int(info[1])
#                 if the_starting_amount_of_ammunition >= enemy_armour:
#                     the_starting_amount_of_ammunition -= enemy_armour
#                     print(f"An enemy with {enemy_armour} armour is defeated.")
#                 else:
#                     the_starting_amount_of_fuel -= enemy_armour * 2
#                     if the_starting_amount_of_fuel >= 0:
#                         print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
#                     else:
#                         print("Mission failed.")
#                         break
#             elif command == "Repair":
#                 number_of_ammunition_and_fuel_added = int(info[1])
#                 fuel_added = number_of_ammunition_and_fuel_added
#                 ammunition_added = number_of_ammunition_and_fuel_added * 2
#                 the_starting_amount_of_fuel += ammunition_added
#                 the_starting_amount_of_ammunition += fuel_added
#                 print(f"Ammunitions added: {ammunition_added}.")
#                 print(f"Fuel added: {fuel_added}.")
#
#
# route_to_titan = input().split("||")
# amount_of_fuel = int(input())
# amount_of_ammunition = int(input())
# space_travel(route_to_titan, amount_of_fuel, amount_of_ammunition)
