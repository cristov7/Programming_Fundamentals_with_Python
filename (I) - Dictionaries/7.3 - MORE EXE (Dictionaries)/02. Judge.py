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

    
# users = {}
# contests = {}
# input_line = input().split(" -> ")
# while input_line[0] != "no more time":
#     username, contest, points = input_line[0], input_line[1], int(input_line[2])
#     if contest not in contests:
#         contests[contest] = {username: 0}
#     if username not in contests[contest]:
#         contests[contest][username] = 0
#     else:
#         if points < contests[contest][username]:
#             points = contests[contest][username]
#     contests[contest][username] = points
#     contests[contest][username] = points
#     if username not in users:
#         users[username] = {"total_points": 0, contest: 0}
#     if contest not in users[username]:
#         users[username][contest] = 0
#     else:
#         users[username]["total_points"] -= users[username][contest]
#         if points < users[username][contest]:
#             points = users[username][contest]
#     users[username]["total_points"] += points
#     users[username][contest] = points
#     input_line = input().split(" -> ")
# for contest in contests:
#     print(f"{contest}: {len(contests[contest])} participants")
#     sorted_participants = sorted(contests[contest].items(), key=lambda x: (-x[1], x[0]))
#     sorted_contest = dict(sorted_participants)
#     counter = 0
#     for participant, points in sorted_contest.items():
#         counter += 1
#         print(f"{counter}. {participant} <::> {points}")
# new_keys = []
# new_values = []
# for key, value in users.items():
#     new_keys.append(key)
#     new_values.append(value["total_points"])
# user_scores = dict(zip(new_keys, new_values))
# sorted_scores = dict(sorted(user_scores.items(), key=lambda k: (-k[1], k[0])))
# print("Individual standings:")
# counter = 0
# for key, value in sorted_scores.items():
#     counter += 1
#     print(f"{counter}. {key} -> {value}")
