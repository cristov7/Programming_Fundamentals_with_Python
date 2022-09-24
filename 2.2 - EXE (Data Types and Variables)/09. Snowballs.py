best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0
best_snowball_value = 0
snowball_quality = 0
count_snowballs = int(input())
for snowball in range(1, count_snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_value = int(input())
    snowball_quality = (snowball_weight / snowball_time) ** snowball_value
    if snowball_quality > best_snowball_quality:
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time
        best_snowball_quality = int(snowball_quality)
        best_snowball_value = snowball_value
    else:
        continue
print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball_quality} ({best_snowball_value})")
