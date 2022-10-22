sequence_of_integers = list(map(int, input().split()))
length_target = len(sequence_of_integers)
count_of_shot_targets = 0
while True:
    command = input()
    if command == "End":
        break
    else:
        index = int(command)
        if 0 <= index <= (length_target - 1):
            value = sequence_of_integers[index]
            if value == -1:
                continue
            else:
                sequence_of_integers[index] = -1
                count_of_shot_targets += 1
                for idx, target in enumerate(sequence_of_integers):
                    if target > value and target != -1:
                        sequence_of_integers[idx] -= value
                    elif target <= value and target != -1:
                        sequence_of_integers[idx] += value
        else:
            continue
shot_targets_list = [str(element) for element in sequence_of_integers]
print(f"Shot targets: {count_of_shot_targets} -> {' '.join(shot_targets_list)}")


# def shoot_for_the_win(numbers):
#     length_target = len(numbers)
#     count_of_shot_targets = 0
#     while True:
#         command = input()
#         if command == "End":
#             break
#         else:
#             index = int(command)
#             if 0 <= index <= (length_target - 1):
#                 value = numbers[index]
#                 if value == -1:
#                     continue
#                 else:
#                     numbers[index] = -1
#                     count_of_shot_targets += 1
#                     for idx, target in enumerate(numbers):
#                         if target > value and target != -1:
#                             numbers[idx] -= value
#                         elif target <= value and target != -1:
#                             numbers[idx] += value
#             else:
#                 continue
#     shot_targets_list = [str(element) for element in numbers]
#     return f"Shot targets: {count_of_shot_targets} -> {' '.join(shot_targets_list)}"
#
#
# sequence_of_integers = list(map(int, input().split()))
# print(shoot_for_the_win(sequence_of_integers))


# def reduce_values(targets_sequence, index):
#     special_value = targets_sequence[index]
#     targets_sequence[index] = -1
#
#     for i in range(len(targets_sequence)):
#         if targets_sequence[i] == -1:
#             continue
#         if special_value < targets_sequence[i]:
#             targets_sequence[i] -= special_value
#         else:
#             targets_sequence[i] += special_value
#     return targets_sequence
#
#
# def shoot_for_the_win(target_sequence):
#     count_of_shot_targets = 0
#     while True:
#         command = input()
#         if command == "End":
#             break
#         index = int(command)
#         if 0 <= index < len(target_sequence) and target_sequence[index] != -1:
#             count_of_shot_targets += 1
#             reduce_values(target_sequence, index)
#     convert_target_values_to_string = [str(num) for num in target_sequence]
#     return f"Shot targets: {count_of_shot_targets} -> {' '.join(convert_target_values_to_string)}"
#
#
# data = list(map(int, input().split()))
# print(shoot_for_the_win(data))
