names_in_list = input().split(", ")
result = sorted(names_in_list, key=lambda name: (-len(name), name))
print(result)
