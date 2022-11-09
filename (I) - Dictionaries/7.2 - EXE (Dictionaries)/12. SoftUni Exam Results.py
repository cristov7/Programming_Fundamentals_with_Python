exam_results = {}
submissions = {}
while True:
    command = input()
    if command == "exam finished":
        print("Results:")
        for programming_language, programming_information in exam_results.items():
            for current_name, current_points in programming_information.items():
                if current_points == "banned":
                    continue
                else:
                    print(f"{current_name} | {current_points}")
        print("Submissions:")
        for every_language, every_person in submissions.items():
            count_people = len(every_person)
            print(f"{every_language} - {count_people}")
        break
    else:
        command_list = command.split("-")
        username = command_list[0]
        info = command_list[1]
        if info == "banned":
            for current_language, current_information in exam_results.items():
                for name in current_information:
                    if name == username:
                        exam_results[current_language][username] = "banned"
                        break
                    else:
                        continue
        else:
            language = info
            if language not in submissions:
                submissions[language] = [username]
            else:
                submissions[language].append(username)
            points = int(command_list[2])
            if language not in exam_results:
                exam_results[language] = {}
                exam_results[language][username] = points
            else:
                if username not in exam_results[language]:
                    exam_results[language][username] = points
                else:
                    if points > exam_results[language][username]:
                        exam_results[language][username] = points
                    else:
                        continue


# from collections import defaultdict
# submissions = defaultdict(int)
# students = {}
# while True:
#     command = input()
#     if command == 'exam finished':
#         break
#     input_data = command.split('-')
#     name = input_data[0]
#     language = input_data[1]
#     if language == 'banned':
#         for course, student_names in students.items():
#             if name in student_names.keys():
#                 students[course].pop(name)
#     else:
#         submissions[language] += 1
#         points = int(input_data[2])
#         if language not in students.keys():
#             students[language] = {}
#         if name not in students[language]:
#             students[language][name] = 0
#         if students[language][name] < points:
#             students[language][name] = points
# print('Results:')
# for course, users in students.items():
#     for name, score in users.items():
#         print(f"{name} | {score}")
# print('Submissions:')
# print('\n'.join(f'{language} - {count}' for language, count in submissions.items()))
