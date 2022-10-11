number = int(input())
for i in range(1, number + 1, 1):
    print(i * "*")
for j in range(number - 1, 0, -1):
    print(j * "*")


# number = int(input())
# symbol = "*"
# ascending_orders = 0
# for ascending_order in range(1, number + 1):
#     ascending_orders += 1
#     stars = symbol * ascending_orders
#     print(symbol * ascending_orders)
# descending_orders = ascending_orders
# for descending_order in range(number + 1, 1, -1):
#     descending_orders -= 1
#     stars = symbol * descending_orders
#     print(symbol * descending_orders)


# paint = "*"
# number = int(input())
# count_1 = 0
# while count_1 < number:
#     count_1 += 1
#     print(paint * count_1)
# count_2 = number
# while count_2 > 0:
#     count_2 -= 1
#     print(paint * count_2)
