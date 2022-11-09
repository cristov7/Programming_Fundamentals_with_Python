students_and_grades = {}
number = int(input())
for student in range(1, number + 1):
    name = input()
    grade = float(input())
    if name not in students_and_grades:
        students_and_grades[name] = [grade]
    else:
        students_and_grades[name].append(grade)
for student, grades in students_and_grades.items():
    count_grades = len(grades)
    sum_grades = sum(grades)
    average_grade = sum_grades / count_grades
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
    else:
        continue


# diary = {}
# number = int(input())
# for student in range(1, number + 1):
#     name = input()
#     grade = float(input())
#     if name not in diary.keys():   # if name not in diary:
#         diary[name] = [grade]
#     else:
#         diary[name].append(grade)
# for name, grades in diary.items():
#     count_grades = len(grades)
#     average_grade = sum(grades) / count_grades
#     if average_grade >= 4.50:
#         print(f"{name} -> {average_grade:.2f}")
#     else:
#         continue


# number_of_students = int(input())
# academy = {}
# for student in range(number_of_students):
#     name = input()
#     grade = float(input())
#     if name not in academy.keys():
#         academy[name] = []
#     academy[name].append(grade)
#
# for student_name, grades in academy.items():
#     average_grade = sum(grades) / len(grades)
#     if average_grade >= 4.50:
#         print(f"{student_name} -> {average_grade:.2f}")
