from collections import defaultdict
submissions = defaultdict(int)
students = {}
while True:
    command = input()
    if command == 'exam finished':
        break
    input_data = command.split('-')
    name = input_data[0]
    language = input_data[1]
    if language == 'banned':
        for course, student_names in students.items():
            if name in student_names.keys():
                students[course].pop(name)
    else:
        submissions[language] += 1
        points = int(input_data[2])
        if language not in students.keys():
            students[language] = {}
        if name not in students[language]:
            students[language][name] = 0
        if students[language][name] < points:
            students[language][name] = points
print('Results:')
for course, users in students.items():
    for name, score in users.items():
        print(f"{name} | {score}")
print('Submissions:')
print('\n'.join(f'{language} - {count}' for language, count in submissions.items()))


# exam_results = {}
# submissions = []
# while True:
#     command = input()
#     if command == "exam finished":
#         break
#     else:
#         command_list = command.split("-")
#         username = command_list[0]
#         status = command_list[1]
#         if status == "banned":
#             del exam_results[username]
#         else:
#             language = status
#             points = command_list[2]
#             submissions.append(language)
#             if username not in exam_results:   # if username not in exam_results.keys():
#                 exam_results[username] = {}
#                 exam_results[username][language] = points
#             else:
#                 if language in exam_results[username].keys():
#                     last_points = exam_results[username][language]
#                     if points > last_points:
#                         exam_results[username][language] = points
#                     else:
#                         continue
#                 else:
#                     exam_results[username][language] = points
# print("Results:")
# for username, info in exam_results.items():
#     for language in info:   # for points in info.keys():
#         points = info[language]
#         print(f"{username} | {points}")
# print("Submissions:")
# for language in submissions:
#     current_language = language
#     count_submissions_language = submissions.count(current_language)
#     print(f"{current_language} - {count_submissions_language}")
#     for count_removes in range(1, count_submissions_language + 1):
#         submissions.remove(current_language)
