max_capacity = 255
water_in_reservoir = 0
count_times = int(input())
for current_time in range(1, count_times + 1):
    liters_water = int(input())
    if liters_water + water_in_reservoir <= max_capacity:
        water_in_reservoir += liters_water
    else:
        print("Insufficient capacity!")
print(water_in_reservoir)


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
