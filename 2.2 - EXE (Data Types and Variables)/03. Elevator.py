count_people = int(input())
max_capacity = int(input())
courses = 0
while True:
    if count_people - max_capacity <= 0:
        courses += 1
        print(courses)
        break
    else:
        courses += 1
        count_people -= max_capacity


# from math import ceil
# count_people = int(input())
# elevator_max_capacity = int(input())
# courses = ceil(count_people / elevator_max_capacity)
# print(courses)


# from math import ceil
# count_people = int(input())
# elevator_max_capacity = int(input())
# courses = 0
# if count_people <= elevator_max_capacity:
#     courses = 1
# else:
#     courses = ceil(count_people / elevator_max_capacity)
# print(courses)


# count_people = int(input())
# elevator_max_capacity = int(input())
# courses = count_people // elevator_max_capacity
# if count_people % elevator_max_capacity == 0:
#     print(courses)
# else:
#     courses += 1
#     print(courses)
