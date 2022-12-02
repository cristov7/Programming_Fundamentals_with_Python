heroes_information = {}
count_heroes = int(input())
for hero in range(1, count_heroes + 1):
    hero_info = input().split()
    name = hero_info[0]
    hp = int(hero_info[1])
    mp = int(hero_info[2])
    heroes_information[name] = [hp, mp]
while True:
    command = input()
    if command == "End":
        break
    else:
        command_list = command.split(" - ")
        info = command_list[0]
        if info == "CastSpell":
            hero_name = command_list[1]
            mp_needed = int(command_list[2])
            spell_name = command_list[3]
            mp = heroes_information[hero_name][1]
            current_mp = mp - mp_needed
            if current_mp >= 0:
                heroes_information[hero_name][1] = current_mp
                print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        elif info == "TakeDamage":
            hero_name = command_list[1]
            damage = int(command_list[2])
            attacker = command_list[3]
            hp = heroes_information[hero_name][0]
            current_hp = hp - damage
            if current_hp > 0:
                heroes_information[hero_name][0] = current_hp
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_information[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")
        elif info == "Recharge":
            hero_name = command_list[1]
            amount = int(command_list[2])
            mp = heroes_information[hero_name][1]
            max_mp = 200
            current_mp = mp + amount
            amount_recovered = 0
            if current_mp > max_mp:
                current_mp = 200
                amount_recovered = current_mp - mp
                heroes_information[hero_name][1] = current_mp
            else:
                amount_recovered = amount
                heroes_information[hero_name][1] = current_mp
            print(f"{hero_name} recharged for {amount_recovered} MP!")
        elif info == "Heal":
            hero_name = command_list[1]
            amount = int(command_list[2])
            hp = heroes_information[hero_name][0]
            max_hp = 100
            current_hp = hp + amount
            amount_recovered = 0
            if current_hp > max_hp:
                current_hp = 100
                amount_recovered = current_hp - hp
                heroes_information[hero_name][0] = current_hp
            else:
                amount_recovered = amount
                heroes_information[hero_name][0] = current_hp
            print(f"{hero_name} healed for {amount_recovered} HP!")
for current_hero, hp_mp_list in heroes_information.items():
    hp = hp_mp_list[0]
    mp = hp_mp_list[1]
    print(current_hero)
    print(f"  HP: {hp}")
    print(f"  MP: {mp}")
