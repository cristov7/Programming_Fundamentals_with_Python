amount_of_experience_to_unlock_tank = float(input())
count_of_battles_to_play = int(input())
total_earned_experiences = 0
unlock_tank = False
needed_count_battles_to_unlock_tank = 0
for battle in range(1, count_of_battles_to_play + 1):
    current_experience = float(input())
    if battle % 3 == 0:
        current_experience *= 1.15
    if battle % 5 == 0:
        current_experience *= 0.90
    if battle % 15 == 0:
        current_experience *= 0.95
    total_earned_experiences += current_experience
    needed_count_battles_to_unlock_tank += 1
    if total_earned_experiences >= amount_of_experience_to_unlock_tank:
        unlock_tank = True
        break
if unlock_tank:
    print(f"Player successfully collected his needed experience for {needed_count_battles_to_unlock_tank} battles.")
else:
    needed_more_experience = abs(amount_of_experience_to_unlock_tank - total_earned_experiences)
    print(f"Player was not able to collect the needed experience, {needed_more_experience:.2f} more needed.")


# def experience_gaining(experience, battles):
#     total_earned_experiences = 0
#     unlock_tank = False
#     needed_count_battles_to_unlock_tank = 0
#     for battle in range(1, count_of_battles_to_play + 1):
#         current_experience = float(input())
#         if battle % 3 == 0:
#             current_experience *= 1.15
#         if battle % 5 == 0:
#             current_experience *= 0.90
#         if battle % 15 == 0:
#             current_experience *= 0.95
#         total_earned_experiences += current_experience
#         needed_count_battles_to_unlock_tank += 1
#         if total_earned_experiences >= amount_of_experience_to_unlock_tank:
#             unlock_tank = True
#             break
#     if unlock_tank:
#         return f"Player successfully collected his needed experience for {needed_count_battles_to_unlock_tank} battles."
#     else:
#         needed_more_experience = abs(amount_of_experience_to_unlock_tank - total_earned_experiences)
#         return f"Player was not able to collect the needed experience, {needed_more_experience:.2f} more needed."
#
#
# amount_of_experience_to_unlock_tank = float(input())
# count_of_battles_to_play = int(input())
# print(experience_gaining(amount_of_experience_to_unlock_tank, count_of_battles_to_play))
