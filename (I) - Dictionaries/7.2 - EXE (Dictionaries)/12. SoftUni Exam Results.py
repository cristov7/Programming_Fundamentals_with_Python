exam_results = {}
submissions = {}
banned_people = []
while True:
    command = input()
    if command == "exam finished":
        break
    else:
        command_list = command.split("-")
        if len(command_list) == 3:
            name = command_list[0]
            language = command_list[1]
            points = int(command_list[2])
            if language not in exam_results:
                submissions[language] = 1
                exam_results[language] = {}
                exam_results[language][name] = points
            else:
                submissions[language] += 1
                if name in exam_results[language]:
                    max_points = exam_results[language][name]
                    if points <= max_points:
                        continue
                    else:
                        exam_results[language][name] = points
                else:
                    exam_results[language][name] = points
        else:   # len(command_list) == 2:
            banned_name = command_list[0]
            banned_people.append(banned_name)
            for current_language, info in exam_results.items():
                if banned_name in info:
                    exam_results[current_language][banned_name] = "banned"
                else:
                    continue
print("Results:")
for programming_language, information in exam_results.items():
    for current_name, current_points in information.items():
        if current_name in banned_people:
            continue
        else:
            print(f"{current_name} | {current_points}")
print("Submissions:")
for current_programming_language, current_submissions in submissions.items():
    print(f"{current_programming_language} - {current_submissions}")


# exam_results = {}
# submissions = {}
# while True:
#     command = input()
#     if command == "exam finished":
#         print("Results:")
#         for programming_language, programming_information in exam_results.items():
#             for current_name, current_points in programming_information.items():
#                 if current_points == "banned":
#                     continue
#                 else:
#                     print(f"{current_name} | {current_points}")
#         print("Submissions:")
#         for every_language, every_person in submissions.items():
#             count_people = len(every_person)
#             print(f"{every_language} - {count_people}")
#         break
#     else:
#         command_list = command.split("-")
#         username = command_list[0]
#         info = command_list[1]
#         if info == "banned":
#             for current_language, current_information in exam_results.items():
#                 for name in current_information:
#                     if name == username:
#                         exam_results[current_language][username] = "banned"
#                         break
#                     else:
#                         continue
#         else:
#             language = info
#             if language not in submissions:
#                 submissions[language] = [username]
#             else:
#                 submissions[language].append(username)
#             points = int(command_list[2])
#             if language not in exam_results:
#                 exam_results[language] = {}
#                 exam_results[language][username] = points
#             else:
#                 if username not in exam_results[language]:
#                     exam_results[language][username] = points
#                 else:
#                     if points > exam_results[language][username]:
#                         exam_results[language][username] = points
#                     else:
#                         continue
