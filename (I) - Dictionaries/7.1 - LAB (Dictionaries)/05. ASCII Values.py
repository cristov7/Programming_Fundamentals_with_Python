chars_list = input().split(", ")
dictionary = {element: ord(element) for element in chars_list}
print(dictionary)
