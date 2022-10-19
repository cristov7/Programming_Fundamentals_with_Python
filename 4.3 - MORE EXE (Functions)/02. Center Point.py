from math import floor


def center_point(x1: float, y1: float, x2: float, y2: float):
    diff_from_x1_to_zero = abs(x1)
    diff_from_y1_to_zero = abs(y1)
    diff_from_x2_to_zero = abs(x2)
    diff_from_y2_to_zero = abs(y2)
    if diff_from_x1_to_zero <= diff_from_x2_to_zero and diff_from_y1_to_zero <= diff_from_y2_to_zero:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


first_point_x1 = float(input())
first_point_y1 = float(input())
second_point_x2 = float(input())
second_point_y2 = float(input())
print(center_point(first_point_x1, first_point_y1, second_point_x2, second_point_y2))
