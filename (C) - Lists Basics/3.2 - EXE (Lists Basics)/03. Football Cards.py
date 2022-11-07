team_A_list = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_B_list = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
game_was_terminated = False
input_red_cards_as_string = input()
red_cards_in_list = input_red_cards_as_string.split(" ")   # .split()
for red_card in red_cards_in_list:
    if red_card in team_A_list:
        team_A_list.remove(red_card)
        if len(team_A_list) < 7:
            game_was_terminated = True
            break
        else:
            continue
    elif red_card in team_B_list:
        team_B_list.remove(red_card)
        if len(team_B_list) < 7:
            game_was_terminated = True
            break
        else:
            continue
    else:
        continue
if game_was_terminated:   # if game_was_terminated == True:
    print(f"Team A - {len(team_A_list)}; Team B - {len(team_B_list)}")
    print("Game was terminated")
else:   # game_was_terminated == False:
    print(f"Team A - {len(team_A_list)}; Team B - {len(team_B_list)}")


# team_A_players = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_B_players = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
# red_cards_for_players = input().split()
# game_was_stopped = False
# for player in red_cards_for_players:
#     if player in team_A_players:
#         team_A_players.remove(player)
#     elif player in team_B_players:
#         team_B_players.remove(player)
#     if len(team_A_players) < 7 or len(team_B_players) < 7:
#         game_was_stopped = True
#         break
# print(f"Team A - {len(team_A_players)}; Team B - {len(team_B_players)}")
# if game_was_stopped:   # if game_was_stopped == True:
#     print("Game was terminated")


# team_A_players_list = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_B_players_list = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
# red_cards_in_string = input()
# red_cards_list = red_cards_in_string.split(" ")   # red_cards_list = red_cards_in_string.split()
# for player in red_cards_list:
#     if player in team_A_players_list:
#         team_A_players_list.remove(player)
#         if len(team_A_players_list) < 7:
#             print(f"Team A - {len(team_A_players_list)}; Team B - {len(team_B_players_list)}")
#             print("Game was terminated")
#             break
#         else:
#             continue
#     elif player in team_B_players_list:
#         team_B_players_list.remove(player)
#         if len(team_B_players_list) < 7:
#             print(f"Team A - {len(team_A_players_list)}; Team B - {len(team_B_players_list)}")
#             print("Game was terminated")
#             break
#         else:
#             continue
#     else:
#         continue
# else:
#     print(f"Team A - {len(team_A_players_list)}; Team B - {len(team_B_players_list)}")


# team_A_players = ["A-" + str(s) for s in range(1, 12)]
# team_B_players = ["B-" + str(s) for s in range(1, 12)]

