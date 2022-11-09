courses = {}
while True:
    command = input()
    if command == "end":
        for course_name, registered_student in courses.items():
            count_students = len(registered_student)
            print(f"{course_name}: {count_students}")
            for index in range(count_students):
                student_name = registered_student[index]
                print(f"-- {student_name}")
        break
    else:
        command_list = command.split(" : ")
        course_name = command_list[0]
        student_name = command_list[1]
        if course_name not in courses:
            courses[course_name] = [student_name]
        else:
            courses[course_name].append(student_name)


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
