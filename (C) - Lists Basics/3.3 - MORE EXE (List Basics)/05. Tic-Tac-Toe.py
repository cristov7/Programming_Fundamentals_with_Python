line_1 = list(map(int, input().split()))
line_2 = list(map(int, input().split()))
line_3 = list(map(int, input().split()))
if (line_1[0] == 1 and line_1[1] == 1 and line_1[2] == 1)\
        or (line_2[0] == 1 and line_2[1] == 1 and line_2[2] == 1)\
        or (line_3[0] == 1 and line_3[1] == 1 and line_3[2] == 1)\
        or (line_1[0] == 1 and line_2[0] == 1 and line_3[0] == 1)\
        or (line_1[1] == 1 and line_2[1] == 1 and line_3[1] == 1)\
        or (line_1[2] == 1 and line_2[2] == 1 and line_3[2] == 1)\
        or (line_1[0] == 1 and line_2[1] == 1 and line_3[2] == 1)\
        or (line_1[2] == 1 and line_2[1] == 1 and line_3[0] == 1):
    print("First player won")
elif (line_1[0] == 2 and line_1[1] == 2 and line_1[2] == 2) \
        or (line_2[0] == 2 and line_2[1] == 2 and line_2[2] == 2) \
        or (line_3[0] == 2 and line_3[1] == 2 and line_3[2] == 2) \
        or (line_1[0] == 2 and line_2[0] == 2 and line_3[0] == 2) \
        or (line_1[1] == 2 and line_2[1] == 2 and line_3[1] == 2) \
        or (line_1[2] == 2 and line_2[2] == 2 and line_3[2] == 2) \
        or (line_1[0] == 2 and line_2[1] == 2 and line_3[2] == 2) \
        or (line_1[2] == 2 and line_2[1] == 2 and line_3[0] == 2):
    print("Second player won")
else:
    print("Draw!")


# row1 = [int(num) for num in input().split()]
# row2 = [int(num) for num in input().split()]
# row3 = [int(num) for num in input().split()]
# winner = ''
# if row1[0] == row1[1] == row1[2] == 1 or \
#         row2[0] == row2[1] == row2[2] == 1 or \
#         row3[0] == row3[1] == row3[2] == 1 or \
#         row1[0] == row2[0] == row3[0] == 1 or \
#         row1[1] == row2[1] == row3[1] == 1 or \
#         row1[2] == row2[2] == row3[2] == 1 or \
#         row1[0] == row2[1] == row3[2] == 1 or \
#         row1[2] == row2[1] == row3[0] == 1:
#     winner = 'First player'
# elif row1[0] == row1[1] == row1[2] == 2 or \
#         row2[0] == row2[1] == row2[2] == 2 or \
#         row3[0] == row3[1] == row3[2] == 2 or \
#         row1[0] == row2[0] == row3[0] == 2 or \
#         row1[1] == row2[1] == row3[1] == 2 or \
#         row1[2] == row2[2] == row3[2] == 2 or \
#         row1[0] == row2[1] == row3[2] == 2 or \
#         row1[2] == row2[1] == row3[0] == 2:
#     winner = 'Second player'
# if winner:
#     print(f'{winner} won')
# else:
#     print('Draw!')
