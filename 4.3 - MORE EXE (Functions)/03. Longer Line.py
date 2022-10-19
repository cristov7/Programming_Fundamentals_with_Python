from math import floor


def longer_line(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float):
    length_first_line = (((abs(x1) + abs(x2)) ** 2) + ((abs(y1) + abs(y2)) ** 2)) ** 0.5
    length_second_line = (((abs(x3) + abs(x4)) ** 2) + ((abs(y3) + abs(y4)) ** 2)) ** 0.5
    if length_first_line >= length_second_line:
        diff_from_x1_to_zero = abs(x1)
        diff_from_y1_to_zero = abs(y1)
        diff_from_x2_to_zero = abs(x2)
        diff_from_y2_to_zero = abs(y2)
        if diff_from_x1_to_zero + diff_from_y1_to_zero <= diff_from_x2_to_zero + diff_from_y2_to_zero:
            return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    else:
        diff_from_x3_to_zero = abs(x3)
        diff_from_y3_to_zero = abs(y3)
        diff_from_x4_to_zero = abs(x4)
        diff_from_y4_to_zero = abs(y4)
        if diff_from_x3_to_zero + diff_from_y3_to_zero <= diff_from_x4_to_zero + diff_from_y4_to_zero:
            return f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"
        return f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})"


first_point_x1 = float(input())
first_point_y1 = float(input())
second_point_x2 = float(input())
second_point_y2 = float(input())
third_point_x3 = float(input())
third_point_y3 = float(input())
fourth_point_x4 = float(input())
fourth_point_y4 = float(input())
print(longer_line(first_point_x1, first_point_y1, second_point_x2, second_point_y2,
                  third_point_x3, third_point_y3, fourth_point_x4, fourth_point_y4))


# def calc_line_len(l):
#     a = sum([abs(l[0]), abs(l[2])])
#     b = sum([abs(l[1]), abs(l[3])])
#     return (a**2 + b**2)**0.5
#
#
# def comp_line_len(l1, l2, l1_len, l2_len):
#     if l1_len >= l2_len:
#         return l1
#     return l2
#
#
# def format_center(l):
#     if sum([abs(l[0]), abs(l[1])]) <= sum([abs(l[2]), abs(l[3])]):
#         return f'({int(l[0])}, {int(l[1])})({int(l[2])}, {int(l[3])})'
#     return f'({int(l[2])}, {int(l[3])})({int(l[0])}, {int(l[1])})'
#
#
# l1 = [float(input()) for _ in range(4)]
# l2 = [float(input()) for _ in range(4)]
# l1_len = calc_line_len(l1)
# l2_len = calc_line_len(l2)
# longer_line = comp_line_len(l1, l2, l1_len, l2_len)
# print(format_center(longer_line))
