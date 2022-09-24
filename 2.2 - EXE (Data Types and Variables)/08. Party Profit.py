people_in_group = int(input())
days = int(input())
earn_coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        people_in_group -= 2
    if day % 15 == 0:
        people_in_group += 5
    if day % 3 == 0:
        earn_coins -= 3 * people_in_group
    if day % 5 == 0:
        earn_coins += 20 * people_in_group
        # if day % 3 == 0:
        #     earn_coins -= 2 * people_in_group
    if day % 5 == 0 and day % 3 == 0:
        earn_coins -= 2 * people_in_group
    earn_coins += 50
    earn_coins -= 2 * people_in_group
average_coins_per_person = earn_coins // people_in_group
print(f"{people_in_group} companions received {average_coins_per_person} coins each.")
