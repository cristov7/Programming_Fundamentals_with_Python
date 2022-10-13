# grade = float(input())
#
#
# def data_grades(grade: float):
#     if 2.00 <= grade <= 2.99:
#         print("Fail")
#     elif 3.00 <= grade <= 3.49:
#         print("Poor")
#     elif 3.50 <= grade <= 4.49:
#         print("Good")
#     elif 4.50 <= grade <= 5.49:
#         print("Very Good")
#     elif 5.50 <= grade <= 6.00:
#         print("Excellent")
#
#
# data_grades(grade)


def data_grades(grade: float):
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif 3.00 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    elif 5.50 <= grade <= 6.00:
        return "Excellent"


input_grade = float(input())
print(data_grades(input_grade))
