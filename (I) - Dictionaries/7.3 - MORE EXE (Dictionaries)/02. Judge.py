judge = {}
while True:
    command = input()
    if command == "no more time":
        break
    else:
        command_list = command.split(" -> ")
        username = command_list[0]
        contest = command_list[1]
        points = int(command_list[2])
        if contest not in judge:
            judge[contest] = {}
            judge[contest][username] = points
        else:
            if username not in judge[contest]:
                judge[contest][username] = points
            else:
                if points > judge[contest][username]:
                    judge[contest][username] = points
                else:
                    continue
for programming_language, more_information in judge.items():
    count_students = len(more_information)
    print(f"{programming_language}: {count_students} participants")
    more_information_sorted_usernames = sorted(more_information.items(), key=lambda x: x[0])
    more_information_sorted_points = sorted(more_information_sorted_usernames, key=lambda x: x[1], reverse=True)
    number_of_position = 0
    for current_username, current_points in more_information_sorted_points:
        number_of_position += 1
        print(f"{number_of_position}. {current_username} <::> {current_points}")
print("Individual standings:")
individual_standings = {}
for information in judge.values():
    for username_info, points_info in information.items():
        if username_info not in individual_standings:
            individual_standings[username_info] = points_info
        else:
            individual_standings[username_info] += points_info
position = 0
individual_standings_sorted_names = sorted(individual_standings.items(), key=lambda x: x[0])
individual_standings_sorted_points = sorted(individual_standings_sorted_names, key=lambda x: x[1], reverse=True)
for person_name, person_points in individual_standings_sorted_points:
    position += 1
    print(f"{position}. {person_name} -> {person_points}")
