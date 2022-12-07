import re
regex = r"\|([A-Z]{4,})\|\:\#([A-Za-z]+\s{1}[A-Za-z]+)\#"
count_bosses = int(input())
for boss in range(1, count_bosses + 1):
    info = input()
    valid_list = re.findall(regex, info)
    if valid_list:
        for boss_info in valid_list:
            boss_name = boss_info[0]
            boss_title = boss_info[1]
            boss_strength = len(boss_name)
            boss_armor = len(boss_title)
            print(f"{boss_name}, The {boss_title}")
            print(f">> Strength: {boss_strength}")
            print(f">> Armor: {boss_armor}")
    else:
        print("Access denied!")
