info_students = {}
while True:
    info = input()
    if info.islower():
        info_list = info.split("_")
        name_of_the_course = " ".join(info_list)
        for course, other_info in info_students.items():
            if course == name_of_the_course:
                for index, person in enumerate(other_info):
                    name = person
                    ID = other_info[index + 1]
                    print(f"{name} - {ID}")
                    other_info.remove(name)
            else:
                continue
        break
    else:
        info_list = info.split(":")
        current_name = info_list[0]
        current_id = info_list[1]
        current_course = info_list[2]
        if current_course not in info_students.keys():
            info_students[current_course] = [current_name, current_id]
        else:
            if current_name == info_students[current_course][0]:
                continue
            else:
                info_students[current_course].extend([current_name, current_id])


# students = {}
# number_of_students = 0
# course = ""
# while True:
#     command = input()
#     if command.islower():   # if command.lower() == command:
#         course = command.replace("_", " ")
#         # command_list = command.split("_")
#         # course = " ".join(command_list)
#         break
#     else:
#         number_of_students += 1
#         current_name, current_id, current_course = command.split(":")
#         # command_list = command.split(":")
#         # current_name = command_list[0]
#         # current_id = command_list[1]
#         # current_course = command_list[2]
#         students[f"Student: {number_of_students}"] = {'course': current_course, 'name': current_name, 'ID': current_id}
# for key, value in students.items():
#     for nested_key, nested_value in value.items():
#         if nested_value == course:
#             name = students[key]['name']
#             ID = students[key]['ID']
#             print(f"{name} - {ID}")
#             # print(f"{students[key]['name']} - {students[key]['ID']}")
#             break
#         else:
#             break


# students = {}
# while True:
#     command = input().split(":")
#     if len(command) == 3:
#         current_name, current_id, current_course = command[0], command[1], command[2]
#         if current_course not in students.keys():   # if course not in students:
#             students[current_course] = []
#             students[current_course].append(f"{current_name} - {current_id}")
#         else:
#             students[current_course].append(f"{current_name} - {current_id}")
#     else:
#         searched_course = command[0].replace("_", " ")
#         for student in students[searched_course]:
#             print(student)
#         break
