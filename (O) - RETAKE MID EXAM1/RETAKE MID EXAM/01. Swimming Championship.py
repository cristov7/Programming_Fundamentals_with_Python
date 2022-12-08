days_of_the_championship = int(input())
covered_points = int(input())
count_swimmers = int(input())
hotel_room_price_for_swimmer_per_day = float(input())
participation_fee_per_swimmer = float(input())
hotel_expenses_per_day = count_swimmers * hotel_room_price_for_swimmer_per_day
total_hotel_expenses = hotel_expenses_per_day * days_of_the_championship
total_participation_expenses = count_swimmers * participation_fee_per_swimmer
total_expenses = total_participation_expenses + total_hotel_expenses
points_list = []
for day in range(1, days_of_the_championship + 1):
    current_points = float(input())
    if day == 1:
        points_list.append(current_points)
    else:
        index = day - 2
        previous_points = points_list[index]
        bonus_points = previous_points * 0.05
        current_points += bonus_points
        points_list.append(current_points)
total_points = sum(points_list)
cover_expenses_in_percents = 0
championship_was_successful = False
if total_points >= covered_points:
    cover_expenses_in_percents = 25
    championship_was_successful = True
else:
    cover_expenses_in_percents = 10
cover_expenses = total_expenses * (cover_expenses_in_percents / 100)
money_left_to_pay = total_expenses - cover_expenses
print(f"Money left to pay: {money_left_to_pay:.2f} BGN.")
if championship_was_successful:
    print("The championship was successful!")
else:
    print(f"The championship was not successful.")
