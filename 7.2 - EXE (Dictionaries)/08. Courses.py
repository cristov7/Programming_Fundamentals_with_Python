courses = {}
while True:
    command = input()
    if command == "end":
        break
    else:
        info_list = command.split(" : ")
        course = info_list[0]
        name = info_list[1]
        if course not in courses:
            courses[course] = [name]
        else:
            courses[course].append(name)
for course, name in courses.items():
    registered_students = len(name)
    print(f"{course}: {registered_students}")
    for student in range(registered_students):
        student_name = name[student]
        print(f"-- {student_name}")


# from collections import defaultdict
# course_dict = defaultdict(list)
# while True:
#     command = input()
#     if command == 'end':
#         break
#     course_name, student_name = command.split(' : ')
#     course_dict[course_name].append(student_name)
# for course, students in course_dict.items():
#     print(f"{course}: {len(students)}")
#     print('\n'.join(f"-- {name}" for name in students))
