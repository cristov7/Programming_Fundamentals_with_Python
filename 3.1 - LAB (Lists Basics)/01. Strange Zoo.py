# tail = input()
# body = input()
# head = input()
# my_list = [head, body, tail]
# print(my_list)


# tail = input()
# body = input()
# head = input()
# my_list = [tail, body, head]
# my_list[0], my_list[2] = my_list[2], my_list[0]
# print(my_list)


my_list = []
for _ in range(3):
    data = input()
    my_list.append(data)
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)
