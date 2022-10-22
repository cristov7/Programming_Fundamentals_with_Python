text = [word for word in input().split()]
filtered_text = [element for element in text if len(element) % 2 == 0]
print("\n".join(filtered_text))


# text = [word for word in input().split()]
# for element in text:
#     if len(element) % 2 == 0:
#         print(element)
