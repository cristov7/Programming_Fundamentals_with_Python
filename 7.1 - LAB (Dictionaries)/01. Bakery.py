items = input().split()
bakery = {}
for index in range(0, len(items), 2):   # for index in range(0, len(items) - 1, 2):
    key = items[index]
    value = int(items[index + 1])
    bakery[key] = value
print(bakery)


# items = input().split()
# bakery = {}
# for index in range(0, len(items), 2):
#     bakery[items[index]] = int(items[index + 1])
# print(bakery)


# items = input().split()
# bakery_dictionary = {}
# keys_list = []
# values_list = []
# for index, element in enumerate(items):
#     if index % 2 == 0:
#         keys_list.append(element)
#     else:
#         values_list.append(element)
# for key in keys_list:
#     for value in values_list:
#         bakery_dictionary[key] = int(value)
#         values_list.remove(value)
#         break
# print(bakery_dictionary)
