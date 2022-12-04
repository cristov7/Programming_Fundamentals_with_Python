import re
regex = r"\|([A-Z]{4,})\|\:\#([A-Za-z]+\s{1}[A-Za-z]+)\#"
count_bosses = int(input())
for boss in range(1, count_bosses + 1):
    command = input()
    valid_list = re.findall(regex, command)
    if valid_list:
        for boss_info in valid_list:
            boss_name = boss_info[0]
            title = boss_info[1]
            strength = len(boss_name)
            armor = len(title)
            print(f"{boss_name}, The {title}")
            print(f">> Strength: {strength}")
            print(f">> Armor: {armor}")
    else:
        print("Access denied!")
