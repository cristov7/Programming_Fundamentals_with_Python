sequence_of_numbers_list = list(map(int, input().split()))
final = len(sequence_of_numbers_list) // 2
left_racer_list = sequence_of_numbers_list[:final]
right_racer_list = sequence_of_numbers_list[final + 1:]
right_racer_list.reverse()
left_time = 0
right_time = 0
for l_time in left_racer_list:
    if l_time == 0:
        left_time *= 0.8
    else:
        left_time += l_time
for r_time in right_racer_list:
    if r_time == 0:
        right_time *= 0.8
    else:
        right_time += r_time
winner_race = ""
winning_time = 0
if left_time < right_time:
    winner_race = "left"
    winning_time = left_time
elif right_time < left_time:
    winner_race = "right"
    winning_time = right_time
print(f"The winner is {winner_race} with total time: {winning_time:.1f}")


# times_list = list(map(int, input().split()))
# center = len(times_list) // 2
# left_time = 0
# right_time = 0
# for left in times_list[:center]:
#     if left == 0:
#         left_time *= 0.8
#     else:
#         left_time += left
# for right in reversed(times_list[center+1:]):
#     if right == 0:
#         right_time *= 0.8
#     else:
#         right_time += right
# time = min([left_time, right_time])
# if left_time == time:
#     winner = 'left'
# else:
#     winner = 'right'
# print(f'The winner is {winner} with total time: {time:.1f}')
