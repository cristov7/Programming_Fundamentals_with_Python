# list_positives = []
# list_negatives = []
# count_of_positives = 0
# sum_of_negatives = 0
# number = int(input())
# for numbers in range(1, number + 1):
#     current_number = int(input())
#     if current_number >= 0:
#         count_of_positives += 1
#         list_positives.append(current_number)
#     else:
#         sum_of_negatives += current_number
#         list_negatives.append(current_number)
# print(list_positives)
# print(list_negatives)
# print(f"Count of positives: {count_of_positives}")
# print(f"Sum of negatives: {sum_of_negatives}")


list_positives = []
list_negatives = []
number = int(input())
for numbers in range(1, number + 1):
    current_number = int(input())
    if current_number >= 0:
        list_positives.append(current_number)
    else:
        list_negatives.append(current_number)
print(list_positives)
print(list_negatives)
print(f"Count of positives: {len(list_positives)}")
print(f"Sum of negatives: {sum(list_negatives)}")
