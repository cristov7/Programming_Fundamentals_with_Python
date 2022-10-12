reservoir_max_liters = 255
reservoir_in_liters = 0
number = int(input())
for water_liters in range(1, number + 1):
    liters = int(input())
    if reservoir_max_liters >= liters:
        reservoir_max_liters -= liters
        reservoir_in_liters += liters
    else:
        print("Insufficient capacity!")
else:
    print(reservoir_in_liters)


# max_capacity = 255
# water_in_reservoir = 0
# count_times = int(input())
# for current_time in range(1, count_times + 1):
#     liters_water = int(input())
#     if liters_water + water_in_reservoir <= max_capacity:
#         water_in_reservoir += liters_water
#     else:
#         print("Insufficient capacity!")
# print(water_in_reservoir)


# count_times = int(input())
# max_capacity = 255
# water_in_reservoir = 0
# for current_time in range(1, count_times + 1):
#     liters_water = int(input())
#     if max_capacity - liters_water < 0:
#         print("Insufficient capacity!")
#         continue
#     else:
#         max_capacity -= liters_water
#         water_in_reservoir += liters_water
# print(water_in_reservoir)
