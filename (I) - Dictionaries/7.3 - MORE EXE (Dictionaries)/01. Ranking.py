contest_and_password_for_contest = {}
while True:
    command = input()
    if command == "end of contests":
        break
    else:
        command_list = command.split(":")
        contest = command_list[0]
        password_for_contest = command_list[1]
        contest_and_password_for_contest[contest] = password_for_contest
ranking = {}
while True:
    command = input()
    if command == "end of submissions":
        break
    else:
        command_list = command.split("=>")
        contest = command_list[0]
        password = command_list[1]
        username = command_list[2]
        points = int(command_list[3])
        if contest in contest_and_password_for_contest:
            if password == contest_and_password_for_contest[contest]:
                if username not in ranking:
                    ranking[username] = {}
                    ranking[username][contest] = points
                else:
                    if contest not in ranking[username]:
                        ranking[username][contest] = points
                    else:
                        if points > ranking[username][contest]:
                            ranking[username][contest] = points
                        else:
                            continue
            else:
                continue
        else:
            continue
info_students = {}
for name, info in ranking.items():
    for language, points in info.items():
        if name not in info_students:
            info_students[name] = points
        else:
            info_students[name] += points
best_candidate = ""
best_points = 0
for candidate, total_points in info_students.items():
    if total_points > best_points:
        best_candidate = candidate
        best_points = total_points
    else:
        continue
print(f"Best candidate is {best_candidate} with total {best_points} points.")
print("Ranking:")
sorted_ranking_names_list = sorted(ranking.keys())
for name in sorted_ranking_names_list:
    for current_student, current_info in ranking.items():
        if name == current_student:
            print(name)
            languages_and_points_list = []
            for current_language, current_points in current_info.items():
                languages_and_points_list.append(f"{current_points}-{current_language}")
            languages_and_points_list.sort(reverse=True)
            for element in languages_and_points_list:
                current_element = element.split("-")
                language = current_element[1]
                points = current_element[0]
                print(f"#  {language} -> {points}")
        else:
            continue
